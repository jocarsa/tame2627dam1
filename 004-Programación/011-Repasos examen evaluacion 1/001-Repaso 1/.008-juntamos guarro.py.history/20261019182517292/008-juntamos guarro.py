from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='tiendaexamen',
        password='TAME123$',
        database='tiendaexamen'
    )
cursor = connection.cursor()

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  cursor.execute("SELECT * FROM productos;")
  productos = cursor.fetchall()
	cadena = ""
  for producto in productos:
   	cadena += str(producto)
  return cadena
  
if __name__ == "__main__":
  aplicacion.run()
  
cursor.close()
connection.close()