import tkinter as tk

ventana = tk.Tk()

nombre = tk.Entry(ventana)
nombre.pack(padx=20,pady=20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx=20,pady=20)

email = tk.Entry(ventana)
email.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Guardar contacto")
boton.pack(padx=20,pady=20)

ventana.mainloop()