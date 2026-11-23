# Primero importo las librerías
import mysql.connector
from flask import Flask,render_template
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
  cursor = connection.cursor(dictionary=True) # IMPORTANTE!!!!!!!!
  cursor.execute("SELECT * FROM noticias;")
  noticias = cursor.fetchall()
  return render_template("portada.html",noticias = noticias)

@aplicacion.route("/nuevoarticulo")
def nuevoarticulo():  
  return render_template("nuevoarticulo.html") 

@aplicacion.route("/procesa")
def procesa():  
  cursor = connection.cursor(dictionary=True) # IMPORTANTE!!!!!!!!
  cursor.execute("SELECT * FROM noticias;")
  return render_template("procesa.html") 

# arranco el servidor  
if __name__ == "__main__":
  aplicacion.run()
# cierro la conexión
cursor.close()
connection.close()