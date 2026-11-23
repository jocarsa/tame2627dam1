from flask import Flask 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return "Hola soy la página de inicioa"

if __name__ == "__main__": 
  aplicacion.run()

