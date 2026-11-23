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
def inicio():
  
  
  
if __name__ == "__main__": 
  aplicacion.run()