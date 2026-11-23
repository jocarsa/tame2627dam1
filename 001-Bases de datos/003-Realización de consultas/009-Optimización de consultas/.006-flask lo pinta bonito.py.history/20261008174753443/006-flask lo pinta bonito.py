
# Importo la libreria de MySQL
import mysql.connector

# Importo la libreria de Flask para presentar cosas en la web
from flask import Flask

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Creo una aplicación web
aplicacion = Flask(__name__)

# Defino que es lo que pasa en el punto de inicio
@aplicacion.route("/")
def inicio():
    salida = ""

    # Ejecuto una petición sobre el cursor
    cursor.execute("SELECT * FROM entradas;")

    # Dame todas las filas
    entradas = cursor.fetchall()

    # Devuelveme todas las entradas
    for entrada in entradas:
        salida += str(entrada) + "<br>"

    return salida

# Arranco la aplicación web
if __name__ == "__main__":
    aplicacion.run(debug=True)
