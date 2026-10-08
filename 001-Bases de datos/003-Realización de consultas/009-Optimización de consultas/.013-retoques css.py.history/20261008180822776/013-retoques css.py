
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
      body{background:grey;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:500px;}
      p{text-align:justify;font-size:11px;}
      .imagen{width:100%;height:200px;background:grey;border-radius:10px;
      background:url(https://media.licdn.com/dms/image/v2/D4D22AQHCNtw3Cp9Dyw/feedshare-shrink_800/feedshare-shrink_800/0/1710619757165?e=2147483647&v=beta&t=PU6PGO8fh-PhOx2V8ALEBeq5n1i5ooypcs76mQf7JHw);
      background-size:cover;background-position:center center;}
      section{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
    <p>Soy José Vicente Carratalá, docente, programador y desarrollador de software, con más de 25 años de experiencia en el ámbito de la informática y la formación tecnológica. Me apasionan la programación, la inteligencia artificial, las bases de datos y el desarrollo de aplicaciones web.
<br>
<br>A lo largo de mi trayectoria he combinado la enseñanza con la creación de proyectos tecnológicos propios, buscando siempre soluciones prácticas, innovadoras y accesibles. Me considero una persona curiosa, autodidacta y creativa, con una filosofía clara: aprender haciendo, experimentar constantemente y compartir el conocimiento.</p>
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
          	<div class='imagen'></div>
          	<h4>"""+entrada[1]+"""</h4>
            <time>"""+str(entrada[2])+"""</time>
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
