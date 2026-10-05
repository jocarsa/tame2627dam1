from flask import Flask				# Importo la libreria de pintar en la web
import mysql.connector				# E importo la libreria de conectar a MySQL

# Conectamos con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='tiendazapatillas',
    password='TiendaZapatillas123$',
    database='tiendazapatillas'
)		

# Creo un cursor que es el que transporta la información
cursor = connection.cursor()

aplicacion = Flask(__name__)	# Creo una aplicación

@aplicacion.route("/")
def inicio():	# Cada vez que alguien pida la pagina principal del servidor
  cadena = ""
  # Le pido algo a la base de datos
	cursor.execute("SELECT * FROM productos")	# en este momento programacion se une con bbdd
	filas = cursor.fetchall()						# quiero todos los registros
  # Devuelvo las filas
  for fila in filas:
    cadena += fila
  return cadena
  
  
if __name__ == "__main__": 
  aplicacion.run()
  
cursor.close()
connection.close()