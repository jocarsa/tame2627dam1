# Primero importo las librerías
import mysql.connector
from flask import Flask
# Me conecto a la base de datos
connection = mysql.connector.connect(
        host='localhost',
        user='periodicodam2627',
        password='TAME123$',
        database='periodicodam2627'
    )
# Creo una aplicación web
aplicacion = Flask(__name__)
# Defino la ruta principal
@aplicacion.route("/")
def inicio(): 
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM noticias;")
  noticias = cursor.fetchall()
  return "Esto marcha"

# arranco el servidor  
if __name__ == "__main__":
  aplicacion.run()
  
cursor.close()
connection.close()