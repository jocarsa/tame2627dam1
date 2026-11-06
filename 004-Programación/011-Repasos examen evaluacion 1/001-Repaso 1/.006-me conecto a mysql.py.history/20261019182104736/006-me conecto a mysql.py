import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='tiendaexamen',
        password='TAME123$',
        database='tiendaexamen'
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM productos;")
entradas = cursor.fetchall()
cursor.close()
connection.close()