from flask import Flask
import mysql.connector

# Conectamos con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='tiendazapatillas',
    password='TiendaZapatillas123$',
    database='tiendazapatillas'
)

# Creo un cursor que es el que transporta la información
cursor = connection.cursor()

aplicacion = Flask(__name__)


@aplicacion.route("/")
def inicio():

    cadena = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tienda de zapatillas</title>

        <style>
            *{
                box-sizing:border-box;
            }

            body{
                margin:0;
                font-family:Arial, sans-serif;
                background:#f5f5f5;
            }

            header{
                background:#222;
                color:white;
                padding:30px;
                text-align:center;
            }

            header h1{
                margin:0;
            }

            main{
                max-width:1200px;
                margin:auto;
                padding:30px;
            }

            .productos{
                display:grid;
                grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));
                gap:20px;
            }

            .producto{
                background:white;
                padding:25px;
                border-radius:10px;
                box-shadow:0px 3px 10px rgba(0,0,0,0.1);
                transition:0.3s;
            }

            .producto:hover{
                transform:translateY(-5px);
                box-shadow:0px 8px 20px rgba(0,0,0,0.15);
            }

            .producto h2{
                margin-top:0;
                color:#222;
            }

            .descripcion{
                color:#666;
                min-height:60px;
                line-height:1.5;
            }

            .precio{
                font-size:24px;
                font-weight:bold;
                color:#16833b;
                margin-top:20px;
            }

            .id{
                font-size:11px;
                color:#aaa;
            }

            button{
                width:100%;
                border:0;
                padding:12px;
                margin-top:15px;
                background:#222;
                color:white;
                border-radius:5px;
                cursor:pointer;
            }

            button:hover{
                background:#444;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>Tienda de zapatillas</h1>
            <p>Nuestros productos</p>
        </header>

        <main>
            <div class="productos">
    """

    # Le pido los productos a la base de datos
    cursor.execute("SELECT * FROM productos")
    filas = cursor.fetchall()

    # Creo una tarjeta por cada producto
    for fila in filas:

        cadena += """
            <div class="producto">
                <div class="id">Producto #""" + str(fila[0]) + """</div>

                <h2>""" + str(fila[1]) + """</h2>

                <div class="descripcion">
                    """ + str(fila[2]) + """
                </div>

                <div class="precio">
                    """ + str(fila[3]) + """ €
                </div>

                <button>Ver producto</button>
            </div>
        """

    cadena += """
            </div>
        </main>

    </body>
    </html>
    """

    return cadena


if __name__ == "__main__":
    aplicacion.run()