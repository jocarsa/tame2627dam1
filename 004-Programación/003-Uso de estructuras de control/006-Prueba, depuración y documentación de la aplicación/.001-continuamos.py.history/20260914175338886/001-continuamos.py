# Saludo
print("Programa agenda v0.1")
print("por Jose Vicente Carratala")

nombre = ""
# Bucle infinito
while True:
  print("Escoge una opción:")
  print("1.-Leer registros")
  print("2.-Insertar registros")
  print("3.-Actualizar registros")
  print("4.-Eliminar registros")
  opcion = input("Escoge una opción: ")
  # Tratamiento de las opciones
  if opcion == "1":
    print("Te voy a listar los registros")
    print(nombre)
  elif opcion == "2":
    print("Vamos a insertar un registro")
    nombre = input("Dime que nombre quieres introducir:")
  elif opcion == "3":
    print("Vamos a actualizar un registro")
    nombre = input("Dime que nombre pongo:")
  elif opcion == "4":
    print("Vamos a eliminar un registro")