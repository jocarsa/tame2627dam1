import tkinter as tk

ventana = tk.Tk()

area = tk.Text(ventana)
area.pack(padx=20,pady=20)

area.config(text="Hola que tal")

ventana.mainloop()