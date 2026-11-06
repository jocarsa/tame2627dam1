import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='tiendaexamen',
        password='TAME123$',
        database='tiendaexamen'
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
  print(producto)
  
cursor.close()
connection.close()