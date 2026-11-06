from flask import Flask,render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  return render_template("blog.html")

if __name__ == "__main__": 
  aplicacion.run()

