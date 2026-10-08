from flask import Flask 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return "Hola soy la página de inicio"

if __name__ == "__main__": 
  aplicacion.run()

