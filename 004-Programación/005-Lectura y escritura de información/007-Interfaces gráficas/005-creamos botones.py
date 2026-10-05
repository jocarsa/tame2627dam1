import tkinter as tk

raiz = tk.Tk()

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola, mundo!", font=("Arial", 24))  # Aumentar el tamaño del texto
etiqueta.pack()

boton = tk.Button(raiz,text="Pulsame si te atreves")
boton.pack()

raiz.mainloop()  # no te salgas del bucle