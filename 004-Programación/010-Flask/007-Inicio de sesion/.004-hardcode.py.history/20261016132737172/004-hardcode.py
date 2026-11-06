from flask import Flask,request

aplicacion = Flask(__name__)

usuario = "jocarsa"
contrasena = "jocarsa"
pasas = "no"

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
  if request.form['usuario'] == usuario and request.form['contrasena'] == contrasena:
    pasas = "si"
  else:
    pasas = "no"
    
  return """
  Me han enviado:<br>
  Usuario: """+request.form['usuario']+"""<br>
  Contraseña: """+request.form['contrasena']+"""<br>
  Pasas a la aplicación?: """+pasas+"""
  """

@aplicacion.route("/escritorio")
def escritorio():
  return "Yo soy el escritorio"

if __name__ == "__main__": 
  aplicacion.run()
