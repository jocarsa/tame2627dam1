import tkinter as tk

ventana = tk.Tk()

base = tk.Entry(ventana)
base.pack(padx=20,pady=20)

boton_calcula = tk.Button(ventana)
boton_calcula.pack(padx=20,pady=20)

ventana.mainloop()