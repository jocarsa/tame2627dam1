from flask import Flask 

aplicacion = Flask(__name__) 

productos = [{},{},{},{}]

@aplicacion.route("/")
def inicio():
  salida = ""
  for producto in productos:
    salida += '<article><h4>'+producto+'</h4></article>'
  return salida

if __name__ == "__main__": 
  aplicacion.run()