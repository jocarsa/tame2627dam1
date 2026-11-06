from flask import Flask 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return "Yo soy el inicio"

@aplicacion.route("/login")
def iniciar_sesion():
  return "Yo soy el login"

@aplicacion.route("/escritorio")
def escritorio():
  return "Yo soy el escritorio"




if __name__ == "__main__": 
  aplicacion.run()
