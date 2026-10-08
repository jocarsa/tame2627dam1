from flask import Flask 

aplicacion = Flask(__name__) 


productos = [
    {
        "nombre": "Zapatillas Running Pro",
        "precio": 79.99,
        "descripcion": "Zapatillas ligeras para correr."
    },
    {
        "nombre": "Balón de fútbol",
        "precio": 24.95,
        "descripcion": "Balón de fútbol de tamaño reglamentario."
    },
    {
        "nombre": "Raqueta de tenis",
        "precio": 89.50,
        "descripcion": "Raqueta ligera de fibra de carbono."
    },
    {
        "nombre": "Balón de baloncesto",
        "precio": 29.99,
        "descripcion": "Balón resistente para pistas interiores y exteriores."
    },
    {
        "nombre": "Mancuernas de 5 kg",
        "precio": 34.90,
        "descripcion": "Juego de dos mancuernas para entrenamiento."
    },
    {
        "nombre": "Esterilla de yoga",
        "precio": 19.95,
        "descripcion": "Esterilla antideslizante para yoga y pilates."
    },
    {
        "nombre": "Bicicleta de montaña",
        "precio": 459.99,
        "descripcion": "Bicicleta de montaña con 21 velocidades."
    },
    {
        "nombre": "Guantes de boxeo",
        "precio": 49.90,
        "descripcion": "Guantes acolchados para entrenamiento de boxeo."
    },
    {
        "nombre": "Cuerda para saltar",
        "precio": 12.50,
        "descripcion": "Cuerda ajustable para ejercicios cardiovasculares."
    },
    {
        "nombre": "Camiseta deportiva",
        "precio": 22.95,
        "descripcion": "Camiseta transpirable de secado rápido."
    },
    {
        "nombre": "Pantalón de running",
        "precio": 27.99,
        "descripcion": "Pantalón corto ligero para corredores."
    },
    {
        "nombre": "Botella deportiva",
        "precio": 14.95,
        "descripcion": "Botella reutilizable de 750 ml."
    },
    {
        "nombre": "Mochila de senderismo",
        "precio": 59.90,
        "descripcion": "Mochila de 30 litros con múltiples compartimentos."
    },
    {
        "nombre": "Casco de ciclismo",
        "precio": 44.50,
        "descripcion": "Casco ligero con ventilación y ajuste regulable."
    },
    {
        "nombre": "Gafas de natación",
        "precio": 18.99,
        "descripcion": "Gafas impermeables con protección antivaho."
    },
    {
        "nombre": "Aletas de natación",
        "precio": 32.95,
        "descripcion": "Aletas flexibles para entrenamiento en piscina."
    },
    {
        "nombre": "Balón de voleibol",
        "precio": 26.50,
        "descripcion": "Balón oficial para voleibol recreativo."
    },
    {
        "nombre": "Patines en línea",
        "precio": 89.99,
        "descripcion": "Patines ajustables con ruedas de poliuretano."
    },
    {
        "nombre": "Banda elástica",
        "precio": 9.95,
        "descripcion": "Banda de resistencia para ejercicios musculares."
    },
    {
        "nombre": "Reloj deportivo",
        "precio": 119.90,
        "descripcion": "Reloj con GPS y monitorización de actividad física."
    }
]


@aplicacion.route("/")
def inicio():
  principio = """
  <!-- Aqui empieza la parte de arriba -->
<!doctype html>
<html lang="es">
  <head>
    <title>Tienda de deportes de Bernat</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;}
      header,main,footer{padding:20px;background:white;width:800px;margin:auto;
      text-align:center;}
    </style>
  </head>
  <body>
    <header>
      <h1>Tienda de deportes</h1>
      <h2>de Jose Vicente Carratala</h2>
    </header>
    <main>
      <h2>Catálogo de productos</h2>
      <section>
<!-- Aqui acaba la parte de arriba -->
  """
  medio = ""
  for producto in productos:
    medio += """
    	<article>
      	<h4>"""+producto['nombre']+"""</h4>
        <p>"""+producto['descripcion']+"""</p>
        <button>🛒 """+str(producto['precio'])+""" €</button>
      </article>
      """
  final += """
  <!-- Aqui empieza la parte de bajo -->        
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
<!-- Aqui acaba la parte de bajo --> 
  """
  return principio+medio+final

if __name__ == "__main__": 
  aplicacion.run()