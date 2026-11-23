# Importo la libreria de MySQL
import mysql.connector

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)		

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Ejecuto una petición sobre el cursor
cursor.execute("SELECT * FROM entradas")

# Dame todas las filas
entradas = cursor.fetchall()	

# Devuelveme todas las entradas
for entrada in entradas:
  print(entrada)

cursor.close()
connection.close()