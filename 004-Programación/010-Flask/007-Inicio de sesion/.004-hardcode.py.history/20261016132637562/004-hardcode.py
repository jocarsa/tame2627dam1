from flask import Flask,request

aplicacion = Flask(__name__)

usuario = "jocarsa"
contrasena = "jocarsa"

@aplicacion.route("/")
def inicio():
  return """
  <form method="POST" action="/login">
  	<input type="text" name="usuario">
    <input type="password" name="contrasena">
    <input type="submit">
  </form>
  """

@aplicacion.route("/login",methods=['POST'])
def iniciar_sesion():
  return """
  Me han enviado:<br>
  Usuario: """+request.form['usuario']+"""<br>
  Contraseña: """+request.form['contrasena']+"""<br>
  """

@aplicacion.route("/escritorio")
def escritorio():
  return "Yo soy el escritorio"

if __name__ == "__main__": 
  aplicacion.run()
