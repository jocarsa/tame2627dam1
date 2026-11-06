
import mysql.connector  # Conectar a MySQL
from flask import Flask  # Crear una web

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():
    connection = mysql.connector.connect(
        host='localhost',
        user='tiendaonlinetame',
        password='TAME123$',
        database='tiendaonlinetame'
    )

    # Creo un cursor para poder pedir cosas
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM productos;")
    productos = cursor.fetchall()

    cadena = """
    <!doctype html>
    <html>
        <head>
        </head>
        <body>
    """

    for producto in productos:
        cadena += """
            <article>
                <h3>""" + producto['nombre'] + """</h3>
            </article>
        """

    cursor.close()
    connection.close()

    cadena += """
        </body>
    </html>
    """

    return cadena


if __name__ == "__main__":
    aplicacion.run()
