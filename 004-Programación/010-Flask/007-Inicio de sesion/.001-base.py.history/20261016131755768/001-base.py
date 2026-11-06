from flask import Flask 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return "Yo soy el inicio"

@aplicacion.route("/login")
def iniciar_sesion():
  return "Yo soy el login"



if __name__ == "__main__": 
  aplicacion.run()
