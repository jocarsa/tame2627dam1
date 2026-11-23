from flask import Flask,render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return render_template("blog.html")

@aplicacion.route("/articulos")
def articulos():
  # Ahora me conecto a la base de datos y te doy los articulos
  
  

if __name__ == "__main__": 
  aplicacion.run()

