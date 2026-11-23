import tkinter as tk

def guardar():
  archivo = open("agenda.csv",'a')
  texto = nombre.get()+","+apellidos.get()+","+email.get()+"\n"
  archivo.write(texto)
  archivo.close()
  
ventana = tk.Tk()

insertar = tk.Frame(ventana)
insertar.grid(row=0,column=0)
leer = tk.Frame(ventana)
leer.grid(row=0,column=1)

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)

tk.Label(insertar, text="Nombre").pack()
nombre = tk.Entry(insertar)
nombre.pack(padx=20, pady=10)

tk.Label(insertar, text="Apellidos").pack()
apellidos = tk.Entry(insertar)
apellidos.pack(padx=20, pady=10)

tk.Label(insertar, text="Email").pack()
email = tk.Entry(insertar)
email.pack(padx=20, pady=10)

boton = tk.Button(insertar, text="Guardar contacto")
boton.pack(padx=20, pady=20)

tk.Label(leer,text="Leer").pack(padx=20,pady=20)

area = tk.Text(leer)
area.pack(padx=20,pady=20)


ventana.mainloop()