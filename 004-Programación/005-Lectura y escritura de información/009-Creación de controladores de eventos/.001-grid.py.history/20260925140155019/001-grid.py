import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Insertar").grid(row=0,col=0)

tk.Label(ventana, text="Leer").grid(row=0,col=1)


ventana.mainloop()