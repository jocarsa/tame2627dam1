from flask import Flask 

aplicacion = Flask(__name__)

@aplicacion.route("/proyectos")
def proyectos():
  return """
  	<a href="/sobremi">Sobre mi</a>
    <a href="/contacto">Contacto</a>
    <a href="/proyectos">Proyectos</a>
  	<p>Hola soy la página de proyectos</p>
    """

@aplicacion.route("/contacto")
def contacto():
  return """
  	<a href="/sobremi">Sobre mi</a>
    <a href="/contacto">Contacto</a>
    <a href="/proyectos">Proyectos</a>
  	<p>Hola soy la página de contacto</p>
    """

@aplicacion.route("/sobremi")
def sobremi():
  return """
  	<a href="/sobremi">Sobre mi</a>
    <a href="/contacto">Contacto</a>
    <a href="/proyectos">Proyectos</a>
  	<p>Hola soy la página de sobre mi</p>
    """

@aplicacion.route("/")
def inicio():
  return """
  	<a href="/sobremi">Sobre mi</a>
    <a href="/contacto">Contacto</a>
    <a href="/proyectos">Proyectos</a>
  	<p>Hola soy la página de inicio</p>
    """

if __name__ == "__main__": 
  aplicacion.run()

