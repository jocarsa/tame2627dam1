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

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return "Esto marcha"
cursor = connection.cursor()
cursor.execute("SELECT * FROM noticias;")
noticias = cursor.fetchall()

for noticia in noticias:
  print(noticia)
  
if __name__ == "__main__":
  aplicacion.run()
  
cursor.close()
connection.close()