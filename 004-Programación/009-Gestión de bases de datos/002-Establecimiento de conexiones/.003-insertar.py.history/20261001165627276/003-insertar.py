import mysql.connector

# Conectamos con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='programacion2627',
    password='TAME123$',
    database='programacion2627'
)		

# Creo un cursor que es el que transporta la información
cursor = connection.cursor()

nombre = input("Introduce un nuevo nombre: ")
# Le pido algo a la base de datos
cursor.execute("SELECT * FROM alumnos")	# en este momento programacion se une con bbdd

cursor.close()
connection.close()