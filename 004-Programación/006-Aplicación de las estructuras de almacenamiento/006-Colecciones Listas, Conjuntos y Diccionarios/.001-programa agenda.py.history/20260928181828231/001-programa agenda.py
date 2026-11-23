agenda = []

print("Programa agenda v0.1")
while True:
  print("Escoge una opcion")
  print("1.-Introducir un nuevo registro")
  print("2.-Listado de registros")
  opcion = input("Elige una opcion: ")
  if opcion == "1":
  	nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    diccionario = {"nombre":nombre,"apellidos":apellidos,"email":email}
    agenda.append(diccionario)
	elif opcion == "2":
  