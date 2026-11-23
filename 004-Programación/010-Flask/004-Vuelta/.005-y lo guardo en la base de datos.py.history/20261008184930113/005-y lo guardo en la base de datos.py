# Importo la libreria para pintar webs
from flask import Flask, request
# Importo la libreria para conectarme a MySQL
import mysql.connector

# Creo una aplicación web
aplicacion = Flask(__name__) 

# Recojo el contenido del formulario
@aplicacion.route("/guardar", methods=["POST"])
def guardar():
  # Me conecto a la base de datos con el usuario que acabo de crear
  connection = mysql.connector.connect(
      host='localhost',
      user='blog2627',
      password='Blog2627$',
      database='blog2627'
  )		
  # Creo un cursor para poder pedir cosas
  cursor = connection.cursor()
  # Ejecuto una petición sobre el cursor
  cursor.execute("SELECT * FROM entradas;")
  conexion.commit()
  cursor.close()
	connection.close()
 
  print("el titulo es",request.form["titulo"])
  print("la fecha es",request.form["fecha"])
  print("el texto es",request.form["texto"])
  return "ok yo te voy a guardar el formulario"

# Pinto el formulario
@aplicacion.route("/")
def inicio():
  return """
  	<!doctype html>
    <html lang="es">
      <head>
        <title>Formulario</title>
        <meta charset="utf-8">
        <style>
          body{background:grey;}
          form{width:400px;background:white;padding:20px;margin:auto;
          display:flex;flex-direction:column;gap:20px;}
        </style>
      </head>
      <body>
        <form action="/guardar" method="POST">
          <label>Introduce el título de la noticia</label>
          <input type="text" name="titulo">
          <label>Introduce la fecha de la noticia</label>
          <input type="date" name="fecha">
          <label>Introduce el texto de la noticia</label>
          <textarea name="texto"></textarea>
          <input type="submit">
        </form>
      </body>
    </html>
  """

if __name__ == "__main__": 
  aplicacion.run()