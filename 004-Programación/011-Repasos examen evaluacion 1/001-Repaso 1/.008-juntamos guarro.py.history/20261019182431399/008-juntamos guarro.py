from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='tiendaexamen',
        password='TAME123$',
        database='tiendaexamen'
    )

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return "Esto marcha"
  
if __name__ == "__main__":
  aplicacion.run()