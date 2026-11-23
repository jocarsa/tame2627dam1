import tkinter as tk

ventana = tk.Tk()

area = tk.Text(ventana)
area.pack(padx=20, pady=20)

area.insert("1.0", "Hola que tal")

ventana.mainloop()