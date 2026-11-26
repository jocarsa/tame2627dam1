import os

origen = "027-Refactorizar"
destino = "compilado.md"

lenguajes = {
    ".py": "python",
    ".php": "php",
    ".html": "html",
    ".css": "css",
    ".js": "javascript",
    ".ts": "typescript",
    ".json": "json",
    ".sql": "sql",
    ".xml": "xml",
    ".md": "markdown",
    ".sh": "bash",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".txt": "text",
    ".yaml": "yaml",
    ".yml": "yaml"
}

archivos = []


def generar_arbol(carpeta, prefijo=""):
    resultado = ""

    elementos = sorted(
        [
            e for e in os.listdir(carpeta)
            if ".history" not in e
        ],
        key=lambda e: (
            not os.path.isdir(os.path.join(carpeta, e)),
            e.lower()
        )
    )

    for i, elemento in enumerate(elementos):
        ruta = os.path.join(carpeta, elemento)
        ultimo = i == len(elementos) - 1

        conector = "└── " if ultimo else "├── "

        resultado += prefijo + conector + elemento + "\n"

        if os.path.isdir(ruta) and not os.path.islink(ruta):
            nuevo_prefijo = prefijo + (
                "    " if ultimo else "│   "
            )

            resultado += generar_arbol(ruta, nuevo_prefijo)

        elif os.path.isfile(ruta):
            archivos.append(ruta)

    return resultado


with open(destino, "w", encoding="utf-8") as markdown:

    markdown.write("# Documentación del proyecto\n\n")

    # Árbol de carpetas y archivos

    markdown.write("## Estructura del proyecto\n\n")
    markdown.write("```text\n")
    markdown.write(origen + "/\n")
    markdown.write(generar_arbol(origen))
    markdown.write("```\n\n")

    # Contenido de los archivos

    markdown.write("## Código fuente\n\n")

    for archivo in archivos:

        ruta_relativa = os.path.relpath(archivo, origen)
        extension = os.path.splitext(archivo)[1].lower()
        lenguaje = lenguajes.get(extension, "text")

        try:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read()

            # Evitar archivos binarios
            if "\x00" in contenido:
                continue

            # Evitar conflictos con fences existentes
            fence = "```"

            while fence in contenido:
                fence += "`"

            markdown.write(f"### {ruta_relativa}\n\n")
            markdown.write(f"{fence}{lenguaje}\n")
            markdown.write(contenido)

            if not contenido.endswith("\n"):
                markdown.write("\n")

            markdown.write(f"{fence}\n\n")

            print("Procesado:", ruta_relativa)

        except (UnicodeDecodeError, OSError):
            print("Omitido:", ruta_relativa)

print("Archivo generado:", destino)