import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='tienda2627',
    password='TAME123$',
    database='tienda2627'
)		
cursor = connection.cursor()

cursor.execute("SELECT * FROM alumnos")	

filas = cursor.fetchall()

for fila in filas:
  print(fila)

cursor.close()
connection.close()