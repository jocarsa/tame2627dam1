# Windows: pip install mysql-connector-python
# Linux: pip3 install mysql-connector-python --break-system-packages

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

# Le pido algo a la base de datos
cursor.execute("SELECT * FROM alumnos")	# en este momento programacion se une con bbdd

filas = cursor.fetchall()						# quiero todos los registros

# Devuelvo las filas
for fila in filas:
  print(fila)

cursor.close()
connection.close()