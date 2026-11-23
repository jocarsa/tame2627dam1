# Primero importo el conector
import mysql.connector
# Importo la librería que me permite hacer web
from flask import Flask, render_template,jsonify

# Me conecto a la base de datos
connection = mysql.connector.connect(
  host='localhost',
  user='tiendaonlinedamtame2627',
  password='TAME123$',
  database='tiendaonlinedamtame2627'
)

# Siempre creo un cursor porque es el que transporta los datos
cursor = connection.cursor(dictionary = True)

# Creo una aplicación web
aplicacion = Flask(__name__)

# Creo una ruta solo para servir los datos
@aplicacion.route("/datos")
def datos():
  	# Ejecuto lo que le quiero pedir a la base de datos
    cursor.execute("SELECT * FROM productos;")

    # Dame todos los productos
    productos = cursor.fetchall()
    # Vomito todo el json
    return jsonify(productos)
    
# Ahora creo una ruta para definir qué va a ver la gente
@aplicacion.route("/")
def articulos():
    # Llamo a la plantilla y le paso los productos para que los pinte
    return render_template("tienda.html")
  
# Vamos a ver cómo insertamos el pedido
@aplicacion.route("/insertarpedido")
def insertarpedido():
  	cursor.execute("INSERT INTO pedidos VALUES(NULL,'2026-10-29','100');")
		connection.commit()
    # De momento digo hola
    return "ok insertado"


# Arranco la web porque si no, no se ve
if __name__ == "__main__":
    aplicacion.run()
# Es buena costumbre cerrar los recursos
cursor.close()
connection.close()