# Importo la libreria de MySQL
import mysql.connector

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='programacion2627',
    password='TAME123$',
    database='programacion2627'
)		

cursor = connection.cursor()

cursor.execute("SELECT * FROM alumnos")

filas = cursor.fetchall()	

for fila in filas:
  print(fila)

cursor.close()
connection.close()