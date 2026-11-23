from flask import Flask		# Importo la libreria de pintar en la web
import mysql.connector		# E importo la libreria de conectar a MySQL

aplicacion = Flask(__name__)	# Creo una aplicación

@aplicacion.route("/")
def inicio():
  
  
  
if __name__ == "__main__": 
  aplicacion.run()