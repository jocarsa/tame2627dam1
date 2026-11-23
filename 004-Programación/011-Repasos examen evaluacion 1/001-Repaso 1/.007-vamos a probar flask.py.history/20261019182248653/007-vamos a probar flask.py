from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  
if __name__ == "__main__":
  aplicacion.run()