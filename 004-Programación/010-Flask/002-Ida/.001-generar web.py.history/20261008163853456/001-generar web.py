from flask import Flask 

aplicacion = Flask(__name__) 

@aplicacion.route("/")
def inicio():
  return "Hola mundo en HTML desde Flask con Python"

if __name__ == "__main__": 
  aplicacion.run()