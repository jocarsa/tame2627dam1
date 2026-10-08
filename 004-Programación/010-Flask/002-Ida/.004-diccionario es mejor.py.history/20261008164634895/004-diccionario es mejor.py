from flask import Flask 

aplicacion = Flask(__name__) 

productos = [{
	"nombre":"zapatillas",
  "precio":"45.45",
  "descripcion":"Estas son unas zapatillas muy bonitas"
},{},{},{}]

@aplicacion.route("/")
def inicio():
  salida = ""
  for producto in productos:
    salida += '<article><h4>'+producto+'</h4></article>'
  return salida

if __name__ == "__main__": 
  aplicacion.run()