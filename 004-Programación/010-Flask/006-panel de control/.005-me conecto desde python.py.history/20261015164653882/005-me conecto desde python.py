import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='tiendaonlinetame',
        password='TAME123$',
        database='tiendaonlinetame'
    )

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

cursor.execute("SELECT * FROM productos;")
entradas = cursor.fetchall()

cursor.close()
connection.close()