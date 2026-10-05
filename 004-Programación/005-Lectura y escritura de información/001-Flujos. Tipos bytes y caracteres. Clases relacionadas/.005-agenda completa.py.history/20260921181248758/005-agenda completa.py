print("SuperAgenda v0.2 por Jose Vicente Carratala")
while True:
  print("Selecciona una opcion")
  print("1.-Introduce un registro")
  print("2.-Selecciona los registros")
  opcion = input("Escoge una opción: ")
  if opcion == "1":
    archivo = open("agenda.txt",'a')
    nombre = input("Ahora introduce el nuevo nombre: ")
    archivo.write(nombre)
    archivo.close()
  elif opcion == "2":