import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Insertar").grid(row=0,column=0)

tk.Label(ventana, text="Leer").grid(row=0,column=1)


ventana.mainloop()