
from flask import Flask, render_template

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
    nombre = "La tienda de Jose Vicente desde Python"
    piedepagina = "(c) 2026 Jose Vicente Carratala desde Python"
    productos = [
    	'producto1',
      'producto2',
      'producto3',
      'producto4',
      'producto5',
      'producto6'
    ]

    return render_template(
        "tienda.html",
        enviotienda=nombre,
        enviopiedepagina=piedepagina,
     		enviolista = productos
    )


if __name__ == "__main__":
    aplicacion.run()
