import mysql.connector

# Conectamos con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='programacion2627',
    password='TAME123$',
    database='programacion2627'
)		

print("Programa de gestión de alumnos v0.1")
while True:
  print("Escoge una opcion:")
  print("1.-Insertar un nuevo registro")
  print("2.-Leer registros")
  opcion = input("Selecciona tu opcion: ")
  if opcion == "1":
    print("Insertamos un registro")
    nombre = input("Dime el nombre del nuevo alumno")
    apellidos = input("Dime los apellidos del nuevo alumno")
    email = input("Dime el email del nuevo alumno")
    
  elif opcion == "2":
    print("Listamos los registros")