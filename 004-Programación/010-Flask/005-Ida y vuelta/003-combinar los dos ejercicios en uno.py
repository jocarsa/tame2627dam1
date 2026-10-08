
# Importo la libreria para pintar webs
from flask import Flask, request
from markupsafe import escape

# Importo la libreria para conectarme a MySQL
import mysql.connector

# Creo una aplicación web
aplicacion = Flask(__name__)


# Pinto el blog
@aplicacion.route("/")
def inicio():

    # Me conecto a la base de datos
    connection = mysql.connector.connect(
        host='localhost',
        user='blog2627',
        password='Blog2627$',
        database='blog2627'
    )

    # Creo un cursor
    cursor = connection.cursor()

    # Obtengo todas las entradas
    cursor.execute("SELECT * FROM entradas ORDER BY fecha DESC;")
    entradas = cursor.fetchall()

    cursor.close()
    connection.close()

    # Creo la cabecera del blog
    salida = """
    <!doctype html>
    <html lang="es">
      <head>
        <title>El blog de Jose Vicente</title>
        <meta charset="utf-8">
        <style>
          body{background:grey;font-family:Arial;}
          header,main,footer{
            background:white;
            padding:20px;
            margin:20px auto;
            width:800px;
          }
          article{
            border-bottom:1px solid grey;
            padding:20px 0;
          }
        </style>
      </head>
      <body>
        <header>
          <h1>El blog de Jose Vicente</h1>
          <a href="/admin">Administrar blog</a>
        </header>
        <main>
    """

    # Pinto cada entrada del blog
    for entrada in entradas:
        salida += """
          <article>
            <h2>""" + str(escape(entrada[1])) + """</h2>
            <small>""" + str(escape(entrada[2])) + """</small>
            <p>""" + str(escape(entrada[3])) + """</p>
          </article>
        """

    # Cierro el documento HTML
    salida += """
        </main>
        <footer>
          El blog de Jose Vicente
        </footer>
      </body>
    </html>
    """

    return salida


# Pinto el formulario de administración
@aplicacion.route("/admin")
def admin():
    return """
    <!doctype html>
    <html lang="es">
      <head>
        <title>Administración del blog</title>
        <meta charset="utf-8">
        <style>
          body{background:grey;font-family:Arial;}
          form{
            width:400px;
            background:white;
            padding:20px;
            margin:40px auto;
            display:flex;
            flex-direction:column;
            gap:20px;
          }
        </style>
      </head>
      <body>
        <form action="/guardar" method="POST">
          <h1>Nueva entrada</h1>

          <label>Introduce el título de la noticia</label>
          <input type="text" name="titulo" required>

          <label>Introduce la fecha de la noticia</label>
          <input type="date" name="fecha" required>

          <label>Introduce el texto de la noticia</label>
          <textarea name="texto" required></textarea>

          <input type="submit" value="Guardar entrada">

          <a href="/">Volver al blog</a>
        </form>
      </body>
    </html>
    """


# Recojo el contenido del formulario
@aplicacion.route("/guardar", methods=["POST"])
def guardar():

    # Me conecto a la base de datos
    connection = mysql.connector.connect(
        host='localhost',
        user='blog2627',
        password='Blog2627$',
        database='blog2627'
    )

    # Creo un cursor
    cursor = connection.cursor()

    # Inserto la nueva entrada
    cursor.execute("""
        INSERT INTO entradas (titulo, fecha, contenido)
        VALUES (%s, %s, %s);
    """, (
        request.form["titulo"],
        request.form["fecha"],
        request.form["texto"]
    ))

    connection.commit()

    cursor.close()
    connection.close()

    print("el titulo es", request.form["titulo"])
    print("la fecha es", request.form["fecha"])
    print("el texto es", request.form["texto"])

    return """
    <!doctype html>
    <html lang="es">
      <head>
        <title>Entrada guardada</title>
        <meta charset="utf-8">
      </head>
      <body>
        <h1>Entrada guardada correctamente</h1>
        <p>La noticia se ha insertado en MySQL.</p>

        <a href="/admin">Volver al formulario</a>
        <br>
        <a href="/">Ver el blog</a>
      </body>
    </html>
    """


if __name__ == "__main__":
    aplicacion.run()
