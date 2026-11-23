from flask import Flask 

aplicacion = Flask(__name__) 

@aplicacion.route("/guardar")
def guardar():
  return "ok yo te voy a guardar el formulario"
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