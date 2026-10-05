import tkinter as tk

ventana = tk.Tk()

insertar = tk.Frame(ventana)
insertar.grid(row=0,column=0)
leer = tk.Frame(ventana)
leer.grid(row=0,column=1)

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)
tk.Label(leer,text="Leer").pack(padx=20,pady=20)


ventana.mainloop()