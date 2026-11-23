import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='blogdamtame2627',
        password='TAME123$',
        database='blogdamtame2627'
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM articulos;")
articulos = cursor.fetchall()
for articulo in articulos:
  print(articulo)
  
cursor.close()
connection.close()