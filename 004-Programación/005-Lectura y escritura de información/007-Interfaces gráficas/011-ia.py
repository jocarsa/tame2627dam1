import tkinter as tk

# -----------------------------------
# Funciones
# -----------------------------------

def calculaIVA():
    try:
        basenumero = float(base.get().replace(",", "."))

        porcentaje = iva_seleccionado.get()
        iva = basenumero * porcentaje / 100
        total = basenumero + iva

        resultado_iva.config(
            text=f"{iva:.2f} €"
        )

        resultado_total.config(
            text=f"{total:.2f} €"
        )

        mensaje.config(
            text=f"IVA aplicado: {porcentaje}%",
            fg="#888888"
        )

    except ValueError:
        mensaje.config(
            text="⚠ Introduce un número válido",
            fg="#ff5c5c"
        )


def limpiar():
    base.delete(0, tk.END)
    resultado_iva.config(text="0.00 €")
    resultado_total.config(text="0.00 €")
    mensaje.config(text="Introduce una base imponible")
    base.focus()


# -----------------------------------
# Ventana
# -----------------------------------

ventana = tk.Tk()
ventana.title("Calculadora de IVA")
ventana.geometry("480x650")
ventana.resizable(False, False)
ventana.configure(bg="#111827")


# -----------------------------------
# Título
# -----------------------------------

titulo = tk.Label(
    ventana,
    text="CALCULADORA IVA",
    font=("Arial", 24, "bold"),
    bg="#111827",
    fg="white"
)

titulo.pack(pady=(35, 5))


subtitulo = tk.Label(
    ventana,
    text="Calcula impuestos de forma rápida",
    font=("Arial", 11),
    bg="#111827",
    fg="#9ca3af"
)

subtitulo.pack(pady=(0, 25))


# -----------------------------------
# Tarjeta principal
# -----------------------------------

tarjeta = tk.Frame(
    ventana,
    bg="#1f2937",
    padx=30,
    pady=25
)

tarjeta.pack(
    padx=35,
    fill="x"
)


# -----------------------------------
# Base imponible
# -----------------------------------

etiqueta_base = tk.Label(
    tarjeta,
    text="BASE IMPONIBLE",
    font=("Arial", 10, "bold"),
    bg="#1f2937",
    fg="#9ca3af"
)

etiqueta_base.pack(anchor="w")


base = tk.Entry(
    tarjeta,
    font=("Arial", 24),
    justify="right",
    bg="#111827",
    fg="white",
    insertbackground="white",
    relief="flat"
)

base.pack(
    fill="x",
    ipady=12,
    pady=(8, 20)
)


# -----------------------------------
# Selector IVA
# -----------------------------------

etiqueta_iva = tk.Label(
    tarjeta,
    text="TIPO DE IVA",
    font=("Arial", 10, "bold"),
    bg="#1f2937",
    fg="#9ca3af"
)

etiqueta_iva.pack(anchor="w")


iva_seleccionado = tk.IntVar(value=21)

tipos = tk.Frame(
    tarjeta,
    bg="#1f2937"
)

tipos.pack(
    fill="x",
    pady=(10, 20)
)


for porcentaje in [4, 10, 21]:

    boton = tk.Radiobutton(
        tipos,
        text=f"{porcentaje}%",
        variable=iva_seleccionado,
        value=porcentaje,
        indicatoron=False,
        font=("Arial", 12, "bold"),
        bg="#374151",
        fg="white",
        selectcolor="#2563eb",
        activebackground="#2563eb",
        activeforeground="white",
        relief="flat",
        padx=15,
        pady=8
    )

    boton.pack(
        side="left",
        expand=True,
        fill="x",
        padx=4
    )


# -----------------------------------
# Botón calcular
# -----------------------------------

boton_calcula = tk.Button(
    tarjeta,
    text="CALCULAR IVA",
    command=calculaIVA,
    font=("Arial", 13, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

boton_calcula.pack(
    fill="x",
    ipady=10,
    pady=(5, 20)
)


# -----------------------------------
# Resultados
# -----------------------------------

texto_iva = tk.Label(
    tarjeta,
    text="IVA",
    font=("Arial", 10),
    bg="#1f2937",
    fg="#9ca3af"
)

texto_iva.pack(anchor="w")


resultado_iva = tk.Label(
    tarjeta,
    text="0.00 €",
    font=("Arial", 20, "bold"),
    bg="#1f2937",
    fg="#60a5fa"
)

resultado_iva.pack(anchor="e")


separador = tk.Frame(
    tarjeta,
    bg="#374151",
    height=1
)

separador.pack(
    fill="x",
    pady=15
)


texto_total = tk.Label(
    tarjeta,
    text="TOTAL CON IVA",
    font=("Arial", 10, "bold"),
    bg="#1f2937",
    fg="#9ca3af"
)

texto_total.pack(anchor="w")


resultado_total = tk.Label(
    tarjeta,
    text="0.00 €",
    font=("Arial", 30, "bold"),
    bg="#1f2937",
    fg="#34d399"
)

resultado_total.pack(anchor="e")


# -----------------------------------
# Mensajes
# -----------------------------------

mensaje = tk.Label(
    ventana,
    text="Introduce una base imponible",
    font=("Arial", 10),
    bg="#111827",
    fg="#888888"
)

mensaje.pack(pady=18)


# -----------------------------------
# Limpiar
# -----------------------------------

boton_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    command=limpiar,
    font=("Arial", 10),
    bg="#111827",
    fg="#9ca3af",
    activebackground="#111827",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

boton_limpiar.pack()


# Permite calcular pulsando ENTER
ventana.bind("<Return>", lambda event: calculaIVA())

# Foco inicial
base.focus()

ventana.mainloop()