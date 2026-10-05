import mysql.connector

# Conectamos con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='programacion2627',
    password='TAME123$',
    database='programacion2627'
)		

cursor = connection.cursor()

print("Programa de gestión de alumnos v0.1")
while True:
  print("Escoge una opcion:")
  print("1.-Insertar un nuevo registro")
  print("2.-Leer registros")
  opcion = input("Selecciona tu opcion: ")
  if opcion == "1":
    print("Insertamos un registro")
    nombre = input("Dime el nombre del nuevo alumno: ")
    apellidos = input("Dime los apellidos del nuevo alumno: ")
    email = input("Dime el email del nuevo alumno: ")
    cursor.execute("""
      INSERT INTO alumnos 
      VALUES(NULL,'"""+nombre+"""','"""+apellidos+"""','"""+email+"""')
      """)	# en este momento programacion se une con bbdd
    connection.commit()
  elif opcion == "2":
    print("Listamos los registros")
    cursor.execute("SELECT * FROM alumnos")	# en este momento programacion se une con bbdd
    filas = cursor.fetchall()						# quiero todos los registros
    # Devuelvo las filas
    for fila in filas:
      print(fila)
    
cursor.close()
connection.close()