import mysql.connector	# Conectar a MySQL
from flask import Flask	# Crear una web

aplicacion = Flask(__name__)

connection = mysql.connector.connect(
        host='localhost',
        user='tiendaonlinetame',
        password='TAME123$',
        database='tiendaonlinetame'
    )

# Creo un cursor para poder pedir cosas
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
  print(producto)

cursor.close()
connection.close()