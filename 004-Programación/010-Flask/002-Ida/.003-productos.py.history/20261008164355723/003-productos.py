from flask import Flask 

aplicacion = Flask(__name__) 

productos = ['manzana','pera','platano','fresas']

@aplicacion.route("/")
def inicio():
  salida = ""
  for producto in productos:
    cadena += '<article><h4>'+producto+'</h4></article>'
  return productos

if __name__ == "__main__": 
  aplicacion.run()