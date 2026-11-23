import tkinter as tk

def calculaIVA():
  basenumero = base.get()
  basenumero = float(basenumero)
  iva = basenumero*0.21
  resultado.config(text=iva)

ventana = tk.Tk()

base = tk.Entry(ventana)
base.pack(padx=20,pady=20)

boton_calcula = tk.Button(ventana,text="Calcula!",command=calculaIVA)
boton_calcula.pack(padx=20,pady=20)

resultado = tk.Label(ventana,text="resultado")
resultado.pack(padx=20,pady=20)

ventana.mainloop()