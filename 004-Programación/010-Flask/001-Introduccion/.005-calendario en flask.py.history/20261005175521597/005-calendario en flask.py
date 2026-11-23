from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  
  