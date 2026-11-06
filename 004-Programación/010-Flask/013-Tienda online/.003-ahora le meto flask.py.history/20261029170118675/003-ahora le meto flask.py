# Primero importo el conector
import mysql.connector
# Importo la librería que me permite hacer web
from flask import Flask,render_template

# Me conecto a la base de datos con los datos que hemos creado
connection = mysql.connector.connect(
        host='localhost',
        user='tiendaonlinedamtame2627',
        password='TAME123$',
        database='tiendaonlinedamtame2627'
    )
# Creo una aplicación web
aplicacion = Flask(__name__)
# Ahora creo una ruta para definir que es lo que va a ver la gente cuando entre a root
@aplicacion.route("/articulos")
def articulos():
  # Siempre creo un cursor porque es el que transporta los datos
	cursor = connection.cursor()

  # Ejecuto lo que le quiero pedir a la base de datos
  cursor.execute("SELECT * FROM productos;")

  # Dame todos los 
  productos = cursor.fetchall()
  return render_template("tienda.html",productos=productos)

# Arranco la web porque si no, no se ve
if __name__ == "__main__": 
  aplicacion.run()

# Es buena costumbre cerrar los recursos
cursor.close()
connection.close()