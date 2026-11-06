import mysql.connector	# Conectar a MySQL
from flask import Flask	# Crear una web

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  connection = mysql.connector.connect(
          host='localhost',
          user='tiendaonlinetame',
          password='TAME123$',
          database='tiendaonlinetame'
      )

  # Creo un cursor para poder pedir cosas
  cursor = connection.cursor(dictionary=True)

  cursor.execute("SELECT * FROM productos;")
  productos = cursor.fetchall()
	cadena = ""
  for producto in productos:
    caden += str(producto)

  cursor.close()
  connection.close()
  return 
  
if __name__ == "__main__":
    aplicacion.run()