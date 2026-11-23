import tkinter as tk
from tkinter import messagebox
import os

ARCHIVO = "agenda.csv"


# ============================================
# FUNCIONES
# ============================================

def guardar():
    nombre_texto = nombre.get().strip()
    apellidos_texto = apellidos.get().strip()
    email_texto = email.get().strip()

    if nombre_texto == "":
        messagebox.showwarning(
            "Faltan datos",
            "Debes introducir al menos el nombre."
        )
        nombre.focus()
        return

    archivo = open(ARCHIVO, "a")
    texto = nombre_texto + "," + apellidos_texto + "," + email_texto + "\n"
    archivo.write(texto)
    archivo.close()

    estado.config(text="✓ Contacto guardado correctamente")

    limpiar()
    leer_contactos()


def leer_contactos():
    area.config(state="normal")
    area.delete("1.0", tk.END)

    if not os.path.exists(ARCHIVO):
        area.insert(tk.END, "\n   Todavía no hay contactos guardados.")
        area.config(state="disabled")
        contador.config(text="0 contactos")
        return

    archivo = open(ARCHIVO, "r")
    lineas = archivo.readlines()
    archivo.close()

    numero = 0

    for linea in lineas:
        linea = linea.strip()

        if linea == "":
            continue

        datos = linea.split(",")

        if len(datos) >= 3:
            numero += 1

            area.insert(tk.END, "  👤  " + datos[0] + " " + datos[1] + "\n")
            area.insert(tk.END, "      " + datos[2] + "\n")
            area.insert(tk.END, "      " + "─" * 42 + "\n\n")

    contador.config(
        text=str(numero) + (" contacto" if numero == 1 else " contactos")
    )

    area.config(state="disabled")


def limpiar():
    nombre.delete(0, tk.END)
    apellidos.delete(0, tk.END)
    email.delete(0, tk.END)
    nombre.focus()


# ============================================
# VENTANA
# ============================================

ventana = tk.Tk()
ventana.title("Agenda de contactos")
ventana.geometry("900x600")
ventana.minsize(800, 500)
ventana.configure(bg="#18181b")

# Las dos columnas crecerán con la ventana
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=2)
ventana.rowconfigure(1, weight=1)


# ============================================
# CABECERA
# ============================================

cabecera = tk.Frame(
    ventana,
    bg="#2563eb",
    height=80
)
cabecera.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="ew"
)

cabecera.grid_propagate(False)

tk.Label(
    cabecera,
    text="AGENDA",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#2563eb"
).pack(
    side="left",
    padx=30,
    pady=20
)

tk.Label(
    cabecera,
    text="Gestión de contactos",
    font=("Arial", 11),
    fg="#dbeafe",
    bg="#2563eb"
).pack(
    side="left"
)


# ============================================
# PANEL IZQUIERDO - INSERTAR
# ============================================

insertar = tk.Frame(
    ventana,
    bg="#27272a"
)
insertar.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=(20, 10),
    pady=20
)

tk.Label(
    insertar,
    text="Nuevo contacto",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#27272a"
).pack(
    anchor="w",
    padx=25,
    pady=(25, 5)
)

tk.Label(
    insertar,
    text="Introduce los datos del contacto",
    font=("Arial", 10),
    fg="#a1a1aa",
    bg="#27272a"
).pack(
    anchor="w",
    padx=25,
    pady=(0, 25)
)


# NOMBRE

tk.Label(
    insertar,
    text="Nombre",
    font=("Arial", 10, "bold"),
    fg="#d4d4d8",
    bg="#27272a"
).pack(
    anchor="w",
    padx=25
)

nombre = tk.Entry(
    insertar,
    font=("Arial", 12),
    bg="#3f3f46",
    fg="white",
    insertbackground="white",
    relief="flat"
)
nombre.pack(
    fill="x",
    padx=25,
    pady=(5, 18),
    ipady=8
)


# APELLIDOS

tk.Label(
    insertar,
    text="Apellidos",
    font=("Arial", 10, "bold"),
    fg="#d4d4d8",
    bg="#27272a"
).pack(
    anchor="w",
    padx=25
)

apellidos = tk.Entry(
    insertar,
    font=("Arial", 12),
    bg="#3f3f46",
    fg="white",
    insertbackground="white",
    relief="flat"
)
apellidos.pack(
    fill="x",
    padx=25,
    pady=(5, 18),
    ipady=8
)


# EMAIL

tk.Label(
    insertar,
    text="Email",
    font=("Arial", 10, "bold"),
    fg="#d4d4d8",
    bg="#27272a"
).pack(
    anchor="w",
    padx=25
)

email = tk.Entry(
    insertar,
    font=("Arial", 12),
    bg="#3f3f46",
    fg="white",
    insertbackground="white",
    relief="flat"
)
email.pack(
    fill="x",
    padx=25,
    pady=(5, 25),
    ipady=8
)


# BOTÓN GUARDAR

boton = tk.Button(
    insertar,
    text="＋  Guardar contacto",
    command=guardar,
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
boton.pack(
    fill="x",
    padx=25,
    ipady=10
)


# BOTÓN LIMPIAR

boton_limpiar = tk.Button(
    insertar,
    text="Limpiar formulario",
    command=limpiar,
    font=("Arial", 10),
    bg="#3f3f46",
    fg="#d4d4d8",
    activebackground="#52525b",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)
boton_limpiar.pack(
    fill="x",
    padx=25,
    pady=10,
    ipady=7
)


# ============================================
# PANEL DERECHO - CONTACTOS
# ============================================

leer = tk.Frame(
    ventana,
    bg="#27272a"
)
leer.grid(
    row=1,
    column=1,
    sticky="nsew",
    padx=(10, 20),
    pady=20
)

leer.rowconfigure(2, weight=1)
leer.columnconfigure(0, weight=1)

tk.Label(
    leer,
    text="Mis contactos",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#27272a"
).grid(
    row=0,
    column=0,
    sticky="w",
    padx=25,
    pady=(25, 0)
)

contador = tk.Label(
    leer,
    text="0 contactos",
    font=("Arial", 10),
    fg="#60a5fa",
    bg="#27272a"
)
contador.grid(
    row=1,
    column=0,
    sticky="w",
    padx=25,
    pady=(5, 15)
)


# ============================================
# TEXT + SCROLL
# ============================================

contenedor_texto = tk.Frame(
    leer,
    bg="#27272a"
)
contenedor_texto.grid(
    row=2,
    column=0,
    sticky="nsew",
    padx=25,
    pady=(0, 25)
)

contenedor_texto.rowconfigure(0, weight=1)
contenedor_texto.columnconfigure(0, weight=1)

scroll = tk.Scrollbar(contenedor_texto)
scroll.grid(
    row=0,
    column=1,
    sticky="ns"
)

area = tk.Text(
    contenedor_texto,
    font=("Arial", 11),
    bg="#18181b",
    fg="#e4e4e7",
    insertbackground="white",
    relief="flat",
    padx=10,
    pady=10,
    yscrollcommand=scroll.set,
    wrap="word"
)

area.grid(
    row=0,
    column=0,
    sticky="nsew"
)

scroll.config(command=area.yview)


# ============================================
# BARRA DE ESTADO
# ============================================

estado = tk.Label(
    ventana,
    text="Agenda preparada",
    font=("Arial", 9),
    fg="#a1a1aa",
    bg="#18181b",
    anchor="w"
)

estado.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=20,
    pady=(0, 10)
)


# ============================================
# ATAJOS
# ============================================

ventana.bind(
    "<Return>",
    lambda evento: guardar()
)

ventana.bind(
    "<Escape>",
    lambda evento: limpiar()
)


# ============================================
# INICIO
# ============================================

leer_contactos()
nombre.focus()

ventana.mainloop()