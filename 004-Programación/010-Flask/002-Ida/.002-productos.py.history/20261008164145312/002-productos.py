from flask import Flask 

aplicacion = Flask(__name__) 

productos = ['manzana','pera','platano','fresas']

@aplicacion.route("/")
def inicio():
  return "Hola desde Python, esto te lo da Python"

if __name__ == "__main__": 
  aplicacion.run()