from flask import Flask,render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return render_template("blog.html")

@aplicacion.route("/articulos")
def articulos():
  return render_template("articulos.json")

if __name__ == "__main__": 
  aplicacion.run()

