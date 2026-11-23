import tkinter as tk

ventana = tk.Tk()

tk.Pane(ventana, text="Insertar").grid(row=0,column=0)

tk.Pane(ventana, text="Leer").grid(row=0,column=1)


ventana.mainloop()