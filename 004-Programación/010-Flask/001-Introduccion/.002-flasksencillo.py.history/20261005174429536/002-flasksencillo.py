from flask import Flask # Voy a crear HTML desde Python

aplicacion = Flask(__name__) # Este es el archivo principal del ejercicio

@aplicacion.route("/")
def inicio():
  return "Hola mundo en HTML desde Flask"