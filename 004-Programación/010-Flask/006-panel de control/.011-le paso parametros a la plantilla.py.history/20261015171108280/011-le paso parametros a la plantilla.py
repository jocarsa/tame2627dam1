from flask import Flask,render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
  nombre = "La tienda de Jose Vicente desde Python"
	return render_template(
    "tienda.html",
  	enviotienda = tienda
  )

if __name__ == "__main__":
    aplicacion.run()