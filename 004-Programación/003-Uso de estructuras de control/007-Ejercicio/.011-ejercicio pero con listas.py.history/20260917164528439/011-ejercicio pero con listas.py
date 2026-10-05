from funciones import *
  
muestraMensajeBienvenida()
clientes = []
while True:
  muestraMenu()
  opcion = input("Introduce tu opción:")
  if opcion == "1":
    listarRegistros(clientes)
  elif opcion == "2":
    crearRegistro(clientes,registro)
  elif opcion == "3":
    actualizarRegistro(clientes,registro)
  elif opcion == "4":
    eliminarRegistro(clientes,registro)
