from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  cadena = "<style>div{width:50px;height:50px;border:1px grey;float:left}</style>"
  for dia in range(1,31):
    cadena += "<div>"+str(dia)+"</div>"
  return cadena

if __name__ == "__main__": 
  aplicacion.run()