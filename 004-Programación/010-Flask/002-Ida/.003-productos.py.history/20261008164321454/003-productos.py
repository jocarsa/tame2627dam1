from flask import Flask 

aplicacion = Flask(__name__) 

productos = ['manzana','pera','platano','fresas']

@aplicacion.route("/")
def inicio():
  salida = ""
  for producto in productos:
    
  return productos

if __name__ == "__main__": 
  aplicacion.run()