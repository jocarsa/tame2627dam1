from flask import Flask

aplicacion = Flask(__name__)

contador = 0

@aplicacion.route("/")
def inicio():
  contador = contador + 1
  return "ahora el contador dice: "+str(contador)
 
if __name__ == "__main__": 
  aplicacion.run()