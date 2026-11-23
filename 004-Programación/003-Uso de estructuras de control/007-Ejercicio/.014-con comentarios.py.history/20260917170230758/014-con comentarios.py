from funciones import *
  
muestraMensajeBienvenida()
clientes = []
while True:
  muestraMenu()
  opcion = input("Introduce tu opción:")
  print("-"*30)
  if opcion == "1":
    # Cuando listo los clientes solo necesito los clientes
    listarRegistros(clientes)
  elif opcion == "2":
    # Al insertar necesito dos datos, clientes, y nuevo cliente
    # Pero no tengo los datos del nuevo cliente: se los pregunto al usuario
    nuevocliente = input("Introduce un nuevo cliente: ")
    clientes = crearRegistro(clientes,nuevocliente) # Le paso dos parametros
  elif opcion == "3":
    indice = int(input("Introduce el indice a modificar: "))
    valor = input("Introduce el valor a insertar")
   	clientes =  actualizarRegistro(clientes,indice,valor)
  elif opcion == "4":
    indice = int(input("Introduce el indice a eliminar"))
    clientes = eliminarRegistro(clientes,indice)
  print("-"*30)
  
  
  
  
  