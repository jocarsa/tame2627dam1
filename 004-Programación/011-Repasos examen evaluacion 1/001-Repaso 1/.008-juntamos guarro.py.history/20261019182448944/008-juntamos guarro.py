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

  for producto in productos:
    print(producto)
  return "Esto marcha"
  
if __name__ == "__main__":
  aplicacion.run()