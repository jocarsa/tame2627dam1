from funciones import *
  
muestraMensajeBienvenida()
nombre = ""
while True:
  muestraMenu()
  opcion = input("Introduce tu opción:")
  if opcion == "1":
    listarRegistros(nombre)
