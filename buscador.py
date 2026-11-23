#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Interactive recursive text search (no CLI args) with optional find & replace.

Features:
- Prompts user for search string + options + mode (find / replace).
- Walks all subdirectories from the script directory.
- Searches inside "text-like" files (extension allowlist + binary sniff).
- Prints matches with file + line numbers + context.
- Replace mode:
  - Prompts for replacement text
  - Previews changes (before/after)
  - Confirms before writing (all / per-file)
- Provides numbered console actions to open file/folder (and optional editor shortcuts).

Works on Linux/macOS/Windows.
"""

from __future__ import annotations

import os
import sys
import fnmatch
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple


# ----------------------------
# Config (edit if you want)
# ----------------------------

DEFAULT_TEXT_EXTS = {
    ".txt", ".md", ".rst", ".csv", ".tsv", ".log", ".json", ".yaml", ".yml",
    ".xml", ".html", ".htm", ".css", ".scss", ".sass", ".less",
    ".js", ".ts", ".jsx", ".tsx",
    ".py", ".pyi", ".java", ".c", ".h", ".cpp", ".hpp", ".cs", ".go", ".rs",
    ".php", ".phtml", ".rb", ".pl", ".sh", ".bash", ".zsh", ".ps1", ".bat",
    ".ini", ".cfg", ".conf", ".toml", ".properties",
    ".sql",
}

SKIP_DIR_NAMES = {
    ".git", ".hg", ".svn",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    "node_modules", "dist", "build", ".next", ".venv", "venv",
    ".idea", ".vscode",
}

MAX_FILE_SIZE = 15 * 1024 * 1024  # 15 MB
BINARY_SNIFF_BYTES = 4096
MAX_MATCHES_TO_DISPLAY = 2000

# Replace preview limits (to keep console usable)
MAX_FILES_TO_PREVIEW = 50
MAX_CHANGES_PER_FILE_TO_PREVIEW = 30


@dataclass
class Hit:
    file_path: Path
    line_no: int
    line_text: str


@dataclass
class Action:
    label: str
    kind: str  # "open_file" | "open_folder" | "open_in_editor"
    target: Path
    extra: Optional[str] = None  # e.g., editor command prefix joined by "|"


@dataclass
class ReplacePlan:
    file_path: Path
    encoding_used: str
    original_text: str
    new_text: str
    changes_count: int
    changed_lines_preview: List[Tuple[int, str, str]]  # (line_no, before, after)


def script_root() -> Path:
    return Path(__file__).resolve().parent


def is_probably_binary(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            chunk = f.read(BINARY_SNIFF_BYTES)
        if b"\x00" in chunk:
            return True
        weird = 0
        for b in chunk:
            if b in (9, 10, 13):  # \t \n \r
                continue
            if 32 <= b <= 126:
                continue
            if b >= 128:  # allow UTF-8 bytes
                continue
            weird += 1
        return weird > max(10, len(chunk) // 10)
    except Exception:
        return True


def should_skip_dir(dirname: str) -> bool:
    return dirname in SKIP_DIR_NAMES


def parse_exts_input(s: str) -> Optional[set]:
    """
    User may enter:
    - empty -> None (use default)
    - "default" -> None
    - ".py,.js,.html" -> set of exts
    - "py,js,html" -> also accepted
    - "*" -> special marker meaning "try all text-like (binary sniff only)"
    """
    s = s.strip()
    if not s or s.lower() == "default":
        return None
    if s == "*":
        return {"*"}
    parts = [p.strip() for p in s.replace(";", ",").split(",") if p.strip()]
    exts = set()
    for p in parts:
        if not p.startswith("."):
            p = "." + p
        exts.add(p.lower())
    return exts if exts else None


def parse_globs_input(s: str) -> Optional[List[str]]:
    s = s.strip()
    if not s:
        return None
    parts = [p.strip() for p in s.replace(";", ",").split(",") if p.strip()]
    return parts or None


def match_file(path: Path, exts: set, globs: Optional[List[str]]) -> bool:
    if globs:
        name = path.name
        if not any(fnmatch.fnmatch(name, g) for g in globs):
            return False

    if exts == {"*"}:
        return True  # rely on binary sniff only

    if path.suffix.lower() in exts:
        return True

    if path.suffix == "" and path.name.lower() in {"dockerfile", "makefile", "readme", "license"}:
        return True

    return False


def iter_candidate_files(root: Path, exts: set, globs: Optional[List[str]]) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not should_skip_dir(d)]
        for fn in filenames:
            p = Path(dirpath) / fn
            try:
                if not p.is_file():
                    continue
                if p.stat().st_size > MAX_FILE_SIZE:
                    continue
                if match_file(p, exts, globs):
                    yield p
            except Exception:
                continue


def read_text_best_effort(path: Path) -> Tuple[Optional[str], Optional[str]]:
    """
    Returns (text, encoding_used) or (None, None) if unreadable.
    """
    try:
        return path.read_text(encoding="utf-8", errors="replace"), "utf-8"
    except Exception:
        try:
            return path.read_text(encoding="latin-1", errors="replace"), "latin-1"
        except Exception:
            return None, None


def find_hits_in_text(text: str, needle: str, case_sensitive: bool) -> List[Tuple[int, str]]:
    hits: List[Tuple[int, str]] = []
    needle_cmp = needle if case_sensitive else needle.lower()

    for i, line in enumerate(text.splitlines(), start=1):
        hay = line if case_sensitive else line.lower()
        if needle_cmp in hay:
            hits.append((i, line.rstrip("\n")))
    return hits


def search_in_file(path: Path, needle: str, case_sensitive: bool) -> List[Hit]:
    if is_probably_binary(path):
        return []

    text, _enc = read_text_best_effort(path)
    if text is None:
        return []

    hits = []
    for ln, line in find_hits_in_text(text, needle, case_sensitive):
        hits.append(Hit(path, ln, line))
    return hits


def build_replace_plan(
    path: Path,
    needle: str,
    replacement: str,
    case_sensitive: bool,
) -> Optional[ReplacePlan]:
    if is_probably_binary(path):
        return None

    text, enc = read_text_best_effort(path)
    if text is None or enc is None:
        return None

    if not case_sensitive:
        # For simple substring replace without regex, Python doesn't support case-insensitive replace directly.
        # We do a conservative approach:
        # - Replace occurrences by scanning lines and rebuilding (case-insensitive match).
        # This preserves original casing of non-matching parts, but replaces matched substrings exactly.
        lower_needle = needle.lower()
        if not needle:
            return None

        lines = text.splitlines(keepends=True)
        new_lines: List[str] = []
        changes = 0
        changed_lines_preview: List[Tuple[int, str, str]] = []

        for idx, line in enumerate(lines, start=1):
            low = line.lower()
            if lower_needle not in low:
                new_lines.append(line)
                continue

            out = []
            start = 0
            while True:
                pos = low.find(lower_needle, start)
                if pos == -1:
                    out.append(line[start:])
                    break
                out.append(line[start:pos])
                out.append(replacement)
                start = pos + len(needle)
                changes += 1
            new_line = "".join(out)
            new_lines.append(new_line)

            if len(changed_lines_preview) < MAX_CHANGES_PER_FILE_TO_PREVIEW:
                before = line.rstrip("\n\r")
                after = new_line.rstrip("\n\r")
                changed_lines_preview.append((idx, before, after))

        new_text = "".join(new_lines)
    else:
        changes = text.count(needle)
        if changes == 0:
            return None

        # Preview: compute changed line samples
        changed_lines_preview = []
        for ln, before in find_hits_in_text(text, needle, True):
            if len(changed_lines_preview) >= MAX_CHANGES_PER_FILE_TO_PREVIEW:
                break
            after = before.replace(needle, replacement)
            changed_lines_preview.append((ln, before, after))

        new_text = text.replace(needle, replacement)

    if new_text == text:
        return None

    return ReplacePlan(
        file_path=path,
        encoding_used=enc,
        original_text=text,
        new_text=new_text,
        changes_count=changes,
        changed_lines_preview=changed_lines_preview,
    )


def write_text_best_effort(path: Path, text: str, encoding: str) -> bool:
    try:
        # Write back using the encoding we used to read (utf-8 or latin-1)
        path.write_text(text, encoding=encoding, errors="replace")
        return True
    except Exception:
        return False


def detect_editors() -> List[Tuple[str, List[str]]]:
    candidates: List[Tuple[str, List[str]]] = []

    def exists(cmd: str) -> bool:
        from shutil import which
        return which(cmd) is not None

    if exists("code"):
        candidates.append(("VS Code", ["code", "-g"]))
    if exists("subl"):
        candidates.append(("Sublime Text", ["subl"]))
    if sys.platform.startswith("win") and exists("notepad++"):
        candidates.append(("Notepad++", ["notepad++"]))

    return candidates


def open_path_default(path: Path) -> None:
    if sys.platform.startswith("win"):
        os.startfile(str(path))  # type: ignore[attr-defined]
    elif sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=False)
    else:
        subprocess.run(["xdg-open", str(path)], check=False)


def open_in_editor(editor_cmd: List[str], file_path: Path, line_no: Optional[int]) -> None:
    cmd = editor_cmd[:]
    if cmd and cmd[0] == "code" and line_no is not None:
        cmd.append(f"{file_path}:{line_no}")
    else:
        cmd.append(str(file_path))
    subprocess.run(cmd, check=False)


def build_actions(hits: List[Hit]) -> List[Action]:
    actions: List[Action] = []

    seen_files = set()
    unique_files: List[Path] = []
    for h in hits:
        if h.file_path not in seen_files:
            seen_files.add(h.file_path)
            unique_files.append(h.file_path)

    editors = detect_editors()

    max_files_for_actions = min(len(unique_files), 50)
    for fp in unique_files[:max_files_for_actions]:
        actions.append(Action(label=f"Open file: {fp}", kind="open_file", target=fp))
        actions.append(Action(label=f"Open folder: {fp.parent}", kind="open_folder", target=fp.parent))
        for ed_label, ed_cmd in editors:
            actions.append(Action(label=f"Open in {ed_label}: {fp}", kind="open_in_editor", target=fp, extra="|".join(ed_cmd)))

    return actions


def prompt_bool(label: str, default: bool) -> bool:
    suffix = "Y/n" if default else "y/N"
    while True:
        s = input(f"{label} ({suffix}): ").strip().lower()
        if not s:
            return default
        if s in {"y", "yes", "s", "si"}:
            return True
        if s in {"n", "no"}:
            return False
        print("Please type y or n.")


def prompt_choice(label: str, choices: List[str], default: str) -> str:
    """
    choices: list of allowed lowercase tokens (e.g., ["find", "replace"])
    default must be one of them.
    """
    choices_disp = "/".join(choices)
    while True:
        s = input(f"{label} ({choices_disp}) [default: {default}]: ").strip().lower()
        if not s:
            return default
        if s in choices:
            return s
        print(f"Please type one of: {choices_disp}")


def print_find_results(hits: List[Hit], files_scanned: int) -> None:
    print("-" * 72)
    print(f"Files scanned: {files_scanned}")
    print(f"Matches found: {len(hits)}")
    if len(hits) >= MAX_MATCHES_TO_DISPLAY:
        print(f"(Stopped after {MAX_MATCHES_TO_DISPLAY} matches to keep output manageable.)")
    print("-" * 72)

    if not hits:
        return

    current_file: Optional[Path] = None
    for h in hits:
        if current_file != h.file_path:
            current_file = h.file_path
            print(f"\n📄 {current_file}")
        preview = h.line_text.strip()
        if len(preview) > 220:
            preview = preview[:220] + "…"
        print(f"  {h.line_no:>6}: {preview}")


def preview_replace_plans(plans: List[ReplacePlan]) -> None:
    print("\n" + "-" * 72)
    total_changes = sum(p.changes_count for p in plans)
    print(f"Replace preview: {len(plans)} file(s) would change, {total_changes} replacement(s) total.")
    print("-" * 72)

    for idx, p in enumerate(plans[:MAX_FILES_TO_PREVIEW], start=1):
        print(f"\n[{idx}] 📄 {p.file_path}  ({p.changes_count} replacement(s))")
        if not p.changed_lines_preview:
            print("  (No line preview available.)")
            continue
        for ln, before, after in p.changed_lines_preview:
            b = before.strip()
            a = after.strip()
            if len(b) > 220:
                b = b[:220] + "…"
            if len(a) > 220:
                a = a[:220] + "…"
            if b == a:
                continue
            print(f"  {ln:>6}: - {b}")
            print(f"         + {a}")

        if p.changes_count > MAX_CHANGES_PER_FILE_TO_PREVIEW:
            print(f"  (Preview capped at {MAX_CHANGES_PER_FILE_TO_PREVIEW} changed lines.)")

    if len(plans) > MAX_FILES_TO_PREVIEW:
        print(f"\n(Preview capped at {MAX_FILES_TO_PREVIEW} files.)")


def apply_replace_plans(plans: List[ReplacePlan]) -> Tuple[int, int]:
    """
    Returns (files_written, files_failed)
    """
    ok = 0
    fail = 0
    for p in plans:
        success = write_text_best_effort(p.file_path, p.new_text, p.encoding_used)
        if success:
            ok += 1
        else:
            fail += 1
    return ok, fail


def main() -> None:
    root = script_root()
    print("=" * 72)
    print("Recursive Text Search (interactive, no CLI)")
    print(f"Root: {root}")
    print("=" * 72)

    mode = prompt_choice("Mode", ["find", "replace"], default="find")

    needle = input("Search string: ").strip()
    if not needle:
        print("No search string given. Exiting.")
        return

    replacement = ""
    if mode == "replace":
        replacement = input("Replacement string: ")

    case_sensitive = prompt_bool("Case sensitive?", default=False)

    exts_input = input(
        "File extensions to search (comma-separated, e.g. .py,.js) "
        "[Enter for default | type * for any (binary-sniff only)]: "
    )
    exts = parse_exts_input(exts_input) or set(DEFAULT_TEXT_EXTS)

    globs_input = input("Optional filename globs (e.g. *.py,*.md) [Enter for none]: ")
    globs = parse_globs_input(globs_input)

    print("\nScanning...\n")

    files_scanned = 0

    if mode == "find":
        hits: List[Hit] = []
        for path in iter_candidate_files(root, exts, globs):
            files_scanned += 1
            file_hits = search_in_file(path, needle, case_sensitive)
            if file_hits:
                hits.extend(file_hits)
                if len(hits) >= MAX_MATCHES_TO_DISPLAY:
                    break

        print_find_results(hits, files_scanned)

        if not hits:
            return

        actions = build_actions(hits)
        if actions:
            print("\n" + "=" * 72)
            print("Actions (type a number, or press Enter to quit)")
            print("=" * 72)
            for idx, a in enumerate(actions, start=1):
                print(f"[{idx:>3}] {a.label}")

            while True:
                choice = input("\nAction #: ").strip()
                if not choice:
                    break
                if not choice.isdigit():
                    print("Please enter a number.")
                    continue
                i = int(choice)
                if not (1 <= i <= len(actions)):
                    print("Out of range.")
                    continue

                a = actions[i - 1]
                try:
                    if a.kind in {"open_file", "open_folder"}:
                        open_path_default(a.target)
                    elif a.kind == "open_in_editor":
                        ed_cmd = (a.extra or "").split("|")
                        line = next((h.line_no for h in hits if h.file_path == a.target), None)
                        open_in_editor(ed_cmd, a.target, line)
                    else:
                        print("Unknown action.")
                except Exception as e:
                    print(f"Failed: {e}")

        print("\nDone.")
        return

    # -----------------
    # Replace mode
    # -----------------
    plans: List[ReplacePlan] = []
    hits_for_actions: List[Hit] = []

    for path in iter_candidate_files(root, exts, globs):
        files_scanned += 1

        plan = build_replace_plan(path, needle, replacement, case_sensitive)
        if not plan:
            continue

        plans.append(plan)

        # Build a minimal hits list for actions (line numbers from preview)
        for ln, before, _after in plan.changed_lines_preview[:10]:
            hits_for_actions.append(Hit(path, ln, before))

        # Safety: avoid insane runs
        total_changes = sum(p.changes_count for p in plans)
        if total_changes >= MAX_MATCHES_TO_DISPLAY:
            break

    print("-" * 72)
    print(f"Files scanned: {files_scanned}")
    print(f"Files that would change: {len(plans)}")
    print(f"Total replacements: {sum(p.changes_count for p in plans)}")
    if sum(p.changes_count for p in plans) >= MAX_MATCHES_TO_DISPLAY:
        print(f"(Stopped after ~{MAX_MATCHES_TO_DISPLAY} replacements to keep output manageable.)")
    print("-" * 72)

    if not plans:
        return

    preview_replace_plans(plans)

    # Confirmation workflow
    print("\n" + "=" * 72)
    print("Apply changes?")
    print("=" * 72)
    print("Type:")
    print("  a  -> apply ALL files")
    print("  p  -> apply PER FILE (you choose y/n per file)")
    print("  n  -> do NOT apply (quit)")
    print("  q  -> quit")
    while True:
        ans = input("Choice [a/p/n/q]: ").strip().lower()
        if ans in {"a", "p", "n", "q", ""}:
            break
        print("Please type a, p, n, or q.")

    if ans in {"n", "q", ""}:
        print("No changes applied.")
        return

    if ans == "a":
        ok, fail = apply_replace_plans(plans)
        print(f"\nApplied. Files written: {ok}, failed: {fail}")
    else:
        ok = 0
        fail = 0
        for p in plans:
            resp = input(f"Apply changes to {p.file_path}? (y/N): ").strip().lower()
            if resp not in {"y", "yes", "s", "si"}:
                continue
            success = write_text_best_effort(p.file_path, p.new_text, p.encoding_used)
            if success:
                ok += 1
            else:
                fail += 1
        print(f"\nApplied (per file). Files written: {ok}, failed: {fail}")

    # Actions after replace (open changed files quickly)
    actions = build_actions(hits_for_actions)
    if actions:
        print("\n" + "=" * 72)
        print("Actions (type a number, or press Enter to quit)")
        print("=" * 72)
        for idx, a in enumerate(actions, start=1):
            print(f"[{idx:>3}] {a.label}")

        while True:
            choice = input("\nAction #: ").strip()
            if not choice:
                break
            if not choice.isdigit():
                print("Please enter a number.")
                continue
            i = int(choice)
            if not (1 <= i <= len(actions)):
                print("Out of range.")
                continue

            a = actions[i - 1]
            try:
                if a.kind in {"open_file", "open_folder"}:
                    open_path_default(a.target)
                elif a.kind == "open_in_editor":
                    ed_cmd = (a.extra or "").split("|")
                    line = next((h.line_no for h in hits_for_actions if h.file_path == a.target), None)
                    open_in_editor(ed_cmd, a.target, line)
                else:
                    print("Unknown action.")
            except Exception as e:
                print(f"Failed: {e}")

    print("\nDone.")


if __name__ == "__main__":
    main()

