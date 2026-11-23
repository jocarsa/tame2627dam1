# Importo la libreria de MySQL
import mysql.connector

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)		

cursor = connection.cursor()

cursor.execute("SELECT * FROM alumnos")

filas = cursor.fetchall()	

for fila in filas:
  print(fila)

cursor.close()
connection.close()