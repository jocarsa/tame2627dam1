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
	cadena = """
  <!doctype html>
  <html>
  	<head>
    </head>
    <body>
    <header>
    	<h1>La tienda de Jose Vicente</h1>
    </header>
    <main>
  """
	for producto in productos:
		cadena += """
    	<article>
      	<h3>"""+cadena[1]+"""</h3>
        <p>"""+cadena[2]+"""</p>
        <p>"""+cadena[3]+""" €</p>
      </article>
    """
	return cadena
  
if __name__ == "__main__":
  aplicacion.run()
  
cursor.close()
connection.close()