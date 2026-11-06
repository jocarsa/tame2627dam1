from flask import Flask 

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return """
  <form method="POST" action="/login">
  	<input type="text" name="usuario>
    <input type="password" name="contrasena">
    <input type="submit">
  </form>
  """

@aplicacion.route("/login")
def iniciar_sesion():
  return "Yo soy el login"

@aplicacion.route("/escritorio")
def escritorio():
  return "Yo soy el escritorio"

if __name__ == "__main__": 
  aplicacion.run()
