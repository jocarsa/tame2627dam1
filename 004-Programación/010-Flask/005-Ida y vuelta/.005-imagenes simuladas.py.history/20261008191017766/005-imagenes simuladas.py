
from flask import Flask, request
from markupsafe import escape
import mysql.connector

aplicacion = Flask(__name__)


# Estilos compartidos por toda la aplicación
estilos = """
<style>
  * {
    box-sizing: border-box;
  }

  :root {
    --primario: #6366f1;
    --primario-oscuro: #4f46e5;
    --fondo: #f4f6fb;
    --blanco: #ffffff;
    --texto: #1e293b;
    --secundario: #64748b;
    --borde: #e2e8f0;
    --sombra: 0 10px 35px rgba(15,23,42,0.06);
  }

  body {
    margin: 0;
    background: var(--fondo);
    color: var(--texto);
    font-family: 'Segoe UI', Arial, sans-serif;
    line-height: 1.7;
  }

  a {
    color: var(--primario);
    text-decoration: none;
    transition: 0.2s;
  }

  a:hover {
    color: var(--primario-oscuro);
  }

  header {
    background: white;
    border-bottom: 1px solid var(--borde);
    position: sticky;
    top: 0;
    z-index: 100;
  }

  .navegacion {
    max-width: 1100px;
    margin: auto;
    padding: 18px 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
  }

  .logo {
    font-size: 23px;
    font-weight: 800;
    letter-spacing: -1px;
    color: var(--texto);
  }

  .logo span {
    color: var(--primario);
  }

  .boton {
    display: inline-block;
    background: var(--primario);
    color: white;
    padding: 12px 24px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: 0.25s;
  }

  .boton:hover {
    background: var(--primario-oscuro);
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(99,102,241,0.2);
  }

  .boton-secundario {
    background: #eef2ff;
    color: var(--primario);
  }

  .boton-secundario:hover {
    background: #e0e7ff;
    color: var(--primario-oscuro);
  }

  .contenedor {
    max-width: 1100px;
    margin: auto;
    padding: 45px 25px;
  }

  .hero {
    background: linear-gradient(135deg,#312e81,#6366f1);
    color: white;
    padding: 75px 35px;
    text-align: center;
    border-radius: 22px;
    margin-bottom: 45px;
    position: relative;
    overflow: hidden;
  }

  .hero::after {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    background: rgba(255,255,255,0.07);
    border-radius: 50%;
    right: -100px;
    top: -150px;
  }

  .hero h1 {
    font-size: clamp(32px,5vw,52px);
    letter-spacing: -2px;
    line-height: 1.2;
    margin: 0 0 15px;
  }

  .hero p {
    opacity: 0.85;
    font-size: 17px;
    margin: 0;
  }

  .titulo-seccion {
    font-size: 25px;
    letter-spacing: -0.7px;
    margin-bottom: 25px;
  }

  .grid-entradas {
    display: grid;
    grid-template-columns: repeat(2,minmax(0,1fr));
    gap: 25px;
  }

  article {
    background: white;
    border: 1px solid var(--borde);
    border-radius: 18px;
    padding: 30px;
    box-shadow: var(--sombra);
    transition: 0.3s;
    min-width: 0;
    overflow-wrap: anywhere;
  }

  article:hover {
    transform: translateY(-5px);
    box-shadow: 0 18px 45px rgba(15,23,42,0.1);
    border-color: #c7d2fe;
  }

  .etiqueta {
    display: inline-block;
    background: #eef2ff;
    color: var(--primario);
    padding: 5px 12px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 15px;
  }

  article h2 {
    font-size: 23px;
    line-height: 1.35;
    letter-spacing: -0.6px;
    margin: 0 0 12px;
  }

  .fecha {
    display: block;
    color: var(--secundario);
    font-size: 13px;
    margin-bottom: 18px;
  }

  .contenido {
    color: #475569;
    font-size: 15px;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }

  .panel {
    max-width: 650px;
    margin: 20px auto 60px;
    background: white;
    border: 1px solid var(--borde);
    border-radius: 20px;
    padding: 40px;
    box-shadow: var(--sombra);
  }

  .panel h1 {
    margin: 0 0 8px;
    font-size: 30px;
    letter-spacing: -1px;
  }

  .panel .descripcion {
    color: var(--secundario);
    margin: 0 0 35px;
    font-size: 14px;
  }

  .campo {
    margin-bottom: 24px;
  }

  label {
    display: block;
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 9px;
  }

  input[type="text"],
  input[type="date"],
  textarea {
    display: block;
    width: 100%;
    padding: 14px 16px;
    border: 1px solid var(--borde);
    border-radius: 10px;
    background: #f8fafc;
    font: inherit;
    font-size: 15px;
    color: var(--texto);
    outline: none;
    transition: 0.2s;
  }

  input:focus,
  textarea:focus {
    border-color: var(--primario);
    background: white;
    box-shadow: 0 0 0 4px rgba(99,102,241,0.1);
  }

  textarea {
    min-height: 220px;
    resize: vertical;
  }

  .acciones {
    display: flex;
    gap: 12px;
    align-items: center;
    flex-wrap: wrap;
  }

  .mensaje-exito {
    text-align: center;
    padding: 20px 0;
  }

  .icono-exito {
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background: #dcfce7;
    color: #16a34a;
    font-size: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 25px;
  }

  .mensaje-exito p {
    color: var(--secundario);
    margin-bottom: 30px;
  }

  .vacio {
    grid-column: 1 / -1;
    background: white;
    border: 1px dashed var(--borde);
    padding: 60px 25px;
    border-radius: 18px;
    text-align: center;
    color: var(--secundario);
  }

  footer {
    text-align: center;
    padding: 35px 20px;
    border-top: 1px solid var(--borde);
    color: var(--secundario);
    font-size: 13px;
  }
	.imagenarticulo{
  	width:100%;
    height:300px;
    border-radius:10px;
  }
  @media(max-width:700px) {
    .grid-entradas {
      grid-template-columns: 1fr;
    }

    .contenedor {
      padding: 25px 16px;
    }

    .hero {
      padding: 55px 22px;
      margin-bottom: 30px;
    }

    .panel {
      padding: 26px 20px;
    }

    .navegacion {
      padding: 15px 16px;
    }

    .logo {
      font-size: 19px;
    }

    article {
      padding: 24px;
    }
  }
</style>
"""


# Cabecera compartida
def cabecera(titulo):
    return """
    <!doctype html>
    <html lang="es">
    <head>
      <meta charset="utf-8">
      <meta name="viewport"
            content="width=device-width,initial-scale=1">
      <title>""" + titulo + """</title>
      """ + estilos + """
    </head>
    <body>
      <header>
        <nav class="navegacion">
          <a href="/" class="logo">jocarsa<span>.</span>blog</a>
          <a href="/admin" class="boton">+ Nueva entrada</a>
        </nav>
      </header>
    """


# Página principal del blog
@aplicacion.route("/")
def inicio():

    connection = mysql.connector.connect(
        host='localhost',
        user='blog2627',
        password='Blog2627$',
        database='blog2627'
    )

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM entradas ORDER BY fecha DESC;"
    )
    entradas = cursor.fetchall()

    cursor.close()
    connection.close()

    salida = cabecera("El blog de Jose Vicente")

    salida += """
      <main class="contenedor">
        <section class="hero">
          <h1>Ideas, código y tecnología.</h1>
          <p>
            Un espacio para compartir conocimientos,
            experiencias y proyectos.
          </p>
        </section>

        <h2 class="titulo-seccion">Últimas publicaciones</h2>

        <section class="grid-entradas">
    """

    for entrada in entradas:
        titulo = str(escape(entrada[1]))
        fecha = str(escape(entrada[2]))
        contenido = str(escape(entrada[3]))

        salida += """
          <article>
          	<div class='imagenarticulo'></div>
            <span class="etiqueta">Publicación</span>
            <h2>""" + titulo + """</h2>
            <time class="fecha">""" + fecha + """</time>
            <div class="contenido">""" + contenido + """</div>
          </article>
        """

    if len(entradas) == 0:
        salida += """
          <div class="vacio">
            <h2>Todavía no hay publicaciones</h2>
            <p>Comienza creando tu primera entrada.</p>
            <a href="/admin" class="boton">
              Crear entrada
            </a>
          </div>
        """

    salida += """
        </section>
      </main>

      <footer>
        © 2026 jocarsa.blog · Tecnología y aprendizaje
      </footer>
    </body>
    </html>
    """

    return salida


# Formulario de administración
@aplicacion.route("/admin")
def admin():

    salida = cabecera("Nueva entrada")

    salida += """
      <main class="contenedor">
        <section class="panel">

          <h1>Crear nueva entrada</h1>
          <p class="descripcion">
            Comparte una nueva publicación con tus lectores.
          </p>

          <form action="/guardar" method="POST">

            <div class="campo">
              <label for="titulo">Título de la publicación</label>
              <input
                type="text"
                id="titulo"
                name="titulo"
                placeholder="Escribe un título interesante..."
                maxlength="100"
                required>
            </div>

            <div class="campo">
              <label for="fecha">Fecha de publicación</label>
              <input
                type="date"
                id="fecha"
                name="fecha"
                required>
            </div>

            <div class="campo">
              <label for="texto">Contenido de la publicación</label>
              <textarea
                id="texto"
                name="texto"
                placeholder="Empieza a escribir tu noticia..."
                required></textarea>
            </div>

            <div class="acciones">
              <button type="submit" class="boton">
                Publicar entrada
              </button>

              <a href="/" class="boton boton-secundario">
                Cancelar
              </a>
            </div>

          </form>
        </section>
      </main>

      <footer>
        © 2026 jocarsa.blog · Panel de administración
      </footer>

      <script>
        document.getElementById("fecha").value =
          new Date().toLocaleDateString("en-CA");
      </script>
    </body>
    </html>
    """

    return salida


# Guardar la entrada en MySQL
@aplicacion.route("/guardar", methods=["POST"])
def guardar():

    connection = mysql.connector.connect(
        host='localhost',
        user='blog2627',
        password='Blog2627$',
        database='blog2627'
    )

    cursor = connection.cursor()

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

    salida = cabecera("Entrada publicada")

    salida += """
      <main class="contenedor">
        <section class="panel mensaje-exito">

          <div class="icono-exito">✓</div>

          <h1>¡Entrada publicada!</h1>

          <p>
            Tu nueva publicación se ha guardado
            correctamente en la base de datos.
          </p>

          <div class="acciones"
               style="justify-content:center">

            <a href="/admin" class="boton">
              Crear otra entrada
            </a>

            <a href="/" class="boton boton-secundario">
              Ver el blog
            </a>

          </div>
        </section>
      </main>
    </body>
    </html>
    """

    return salida


if __name__ == "__main__":
    aplicacion.run()
