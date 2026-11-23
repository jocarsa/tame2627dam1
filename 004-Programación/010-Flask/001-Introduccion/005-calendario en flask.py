from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  cadena = ""
  for dia in range(1,31):
    cadena += "<div>"+str(dia)+"</div>"
  return cadena

if __name__ == "__main__": 
  aplicacion.run()