from funciones import *
  
muestraMensajeBienvenida()
clientes = []
while True:
  muestraMenu()
  opcion = input("Introduce tu opción:")
  if opcion == "1":
    listarRegistros(nombre)
