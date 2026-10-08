from flask import Flask 

aplicacion = Flask(__name__)

navegacion = """
	<nav>
  	<a href="/sobremi">Sobre mi</a>
    <a href="/contacto">Contacto</a>
    <a href="/proyectos">Proyectos</a>
  </nav>
"""
@aplicacion.route("/proyectos")
def proyectos():
  return navegacion+"""	
  	<p>Hola soy la página de proyectos</p>
    """

@aplicacion.route("/contacto")
def contacto():
  return navegacion+"""	
  	<p>Hola soy la página de contacto</p>
    """

@aplicacion.route("/sobremi")
def sobremi():
  return navegacion+"""	
  	<p>Hola soy la página de sobre mi</p>
    """

@aplicacion.route("/")
def inicio():
  return navegacion+"""	
  	<p>Hola soy la página de inicio</p>
    """

if __name__ == "__main__": 
  aplicacion.run()

