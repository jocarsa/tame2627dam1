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

if connection.is_connected():
    print("Connected to MySQL database")

cursor = connection.cursor()

cursor.execute("SELECT * FROM alumnos")

fila = cursor.fetchone()

while fila is not None:
    print(fila)
    fila = cursor.fetchone()

cursor.close()
connection.close()