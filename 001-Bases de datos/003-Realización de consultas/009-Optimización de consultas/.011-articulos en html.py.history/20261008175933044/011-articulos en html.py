
# Importo la libreria de MySQL
import mysql.connector

# Importo la libreria de Flask para presentar cosas en la web
from flask import Flask

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Creo una aplicación web
aplicacion = Flask(__name__)

# Defino que es lo que pasa en el punto de inicio
@aplicacion.route("/")
def inicio():

    cabeza = """
    <!-- Inicio del trozo de cabeza -->
<!doctype html>
<html lang="es">
  <head>
    <title>El blog de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;}
      header,main,footer{background:white;padding:20px;margin:auto;width:800px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
      <section>
<!-- Final del trozo de cabeza -->
    """

    cuerpo = ""

    # Ejecuto una petición sobre el cursor
    cursor.execute("SELECT * FROM entradas;")

    # Dame todas las filas
    entradas = cursor.fetchall()

    # Devuelveme todas las entradas
    for entrada in entradas:
        cuerpo += """
        	<article>
          	<h4>"""+entrada[1]+"""</h4>
            <time>"""+entrada[2]+"""</time>
            <p>"""+entrada[3]+"""</p>
          </article>
        """

    piedepagina = """
    <!-- Inicio del trozo de pie de pagina -->
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
<!-- Final del trozo de pie de pagina -->
    """

    return cabeza + cuerpo + piedepagina


# Arranco la aplicación web
if __name__ == "__main__":
    aplicacion.run(debug=True)
