import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='tiendaexamen',
        password='TAME123$',
        database='tiendaexamen'
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM entradas ORDER BY fecha DESC;")
entradas = cursor.fetchall()
cursor.close()
connection.close()