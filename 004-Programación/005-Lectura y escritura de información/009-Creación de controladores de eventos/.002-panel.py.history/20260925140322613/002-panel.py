import tkinter as tk

ventana = tk.Tk()

tk.Frame(ventana, text="Insertar").grid(row=0,column=0)

tk.Frame(ventana, text="Leer").grid(row=0,column=1)


ventana.mainloop()