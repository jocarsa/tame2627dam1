'''
	Super programa agenda v0.3
  Jose Vicente Carratalá
  
  contacto
  -nombre
  -apellidos
  -email
  -telefono
'''
print("Programa agenda")
print("v0.3 Jose Vicente Carratala")
print("Gestiona tu propia agenda")

while True:
  print("Selecciona una opcion")
  print("1.-Insertar un registro")
  print("2.-Listar registros")
  opcion = input("Elige una opción: ")
  if opcion == "1":
  	nombre = input("Dime el nombre del nuevo registro: ")
	elif opcion == "2":