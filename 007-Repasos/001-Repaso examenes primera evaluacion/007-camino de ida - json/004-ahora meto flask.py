import mysql.connector												# Impporto conector
from flask import Flask,render_template				# Le pongo flask para web

aplicacion = Flask(__name__)									# Creo una aplicación web

connection = mysql.connector.connect(
        host='localhost',
        user='blogexamen2627',
        password='TAME123$',
        database='blogexamen2627'
    )																					# Me conecto a la base de datos
cursor = connection.cursor(dictionary=True)		# Creo un cursor para hacer peticiones + diccionario

@aplicacion.route("/")												# Defino la ruta de inicio
def inicio(): 																# Defino la función de inicio
  return render_template("inicio.html")				# Renderizo un template

cursor.execute("SELECT * FROM noticias;")			# Selecciono todo de noticias
noticias = cursor.fetchall()									# Lo meto todo en un array

for noticia in noticias:											# Para cada una de las noticias
  print(noticia)															# Imprimo la noticia
  
 
if __name__ == "__main__":										# Si estoy en el archivo principal
  aplicacion.run()														# arranco el servidor 
  
cursor.close()																# Cierro el cursor
connection.close()														# Cierro la conexión