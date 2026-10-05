import tkinter as tk

ventana = tk.Tk()

def guardar():
  archivo = open("agenda.csv",'a')

tk.Label(ventana, text="Nombre").pack()
nombre = tk.Entry(ventana)
nombre.pack(padx=20, pady=10)

tk.Label(ventana, text="Apellidos").pack()
apellidos = tk.Entry(ventana)
apellidos.pack(padx=20, pady=10)

tk.Label(ventana, text="Email").pack()
email = tk.Entry(ventana)
email.pack(padx=20, pady=10)

boton = tk.Button(ventana, text="Guardar contacto")
boton.pack(padx=20, pady=20)

ventana.mainloop()