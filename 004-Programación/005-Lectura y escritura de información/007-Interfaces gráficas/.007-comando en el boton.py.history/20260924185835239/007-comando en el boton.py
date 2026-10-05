import tkinter as tk

raiz = tk.Tk()

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola, mundo!", font=("Arial", 24))  # Aumentar el tamaño del texto
etiqueta.pack(padx=20,pady=20)

boton = tk.Button(raiz,text="Pulsame si te atreves",command=pulsaBoton)
boton.pack(padx=20,pady=20)

raiz.mainloop()  # no te salgas del bucle