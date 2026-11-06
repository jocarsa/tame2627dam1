# Primero importo el conector
import mysql.connector

# Me conecto a la base de datos con los datos que hemos creado
connection = mysql.connector.connect(
        host='localhost',
        user='tiendaonlinedamtame2627',
        password='TAME123$',
        database='tiendaonlinedamtame2627'
    )
cursor = connection.cursor()
cursor.execute("SELECT * FROM articulos;")
articulos = cursor.fetchall()
for articulo in articulos:
  print(articulo)
  
cursor.close()
connection.close()