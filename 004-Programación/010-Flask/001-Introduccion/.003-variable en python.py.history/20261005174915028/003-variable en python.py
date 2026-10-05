from flask import Flask # Voy a crear HTML desde Python

aplicacion = Flask(__name__) # Este es el archivo principal del ejercicio

edad = 48

@aplicacion.route("/")
def inicio():
  return "Hola mundo y tu edad es de: "+edad+" años"

if __name__ == "__main__": # si es cierto que estoy en el archivo principal
  aplicacion.run()

