from flask import Flask 

aplicacion = Flask(__name__)

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

