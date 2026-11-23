from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():

    cadena = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Calendario</title>

        <style>
            *{
                box-sizing:border-box;
            }

            body{
                margin:0;
                background:#f3f4f6;
                font-family:Arial, sans-serif;
                display:flex;
                justify-content:center;
                padding:50px;
            }

            .calendario{
                width:700px;
                background:white;
                border-radius:15px;
                padding:25px;
                box-shadow:0px 10px 30px rgba(0,0,0,0.15);
            }

            h1{
                margin:0 0 25px 0;
                text-align:center;
                color:#333;
            }

            .semana{
                display:grid;
                grid-template-columns:repeat(7,1fr);
                margin-bottom:10px;
            }

            .semana div{
                text-align:center;
                font-weight:bold;
                color:#777;
                padding:10px;
            }

            .dias{
                display:grid;
                grid-template-columns:repeat(7,1fr);
                gap:8px;
            }

            .dia{
                height:80px;
                border:1px solid #ddd;
                border-radius:8px;
                padding:10px;
                font-size:18px;
                cursor:pointer;
                transition:0.2s;
                background:#fafafa;
            }

            .dia:hover{
                background:#333;
                color:white;
                transform:translateY(-3px);
                box-shadow:0px 5px 10px rgba(0,0,0,0.2);
            }

            .fin-semana{
                background:#fff3f3;
            }
        </style>
    </head>

    <body>

        <div class="calendario">

            <h1>Octubre 2026</h1>

            <div class="semana">
                <div>Lun</div>
                <div>Mar</div>
                <div>Mié</div>
                <div>Jue</div>
                <div>Vie</div>
                <div>Sáb</div>
                <div>Dom</div>
            </div>

            <div class="dias">
    """

    # Octubre de 2026 empieza en jueves.
    # Dejamos tres huecos: lunes, martes y miércoles.
    for i in range(3):
        cadena += "<div></div>"

    for dia in range(1, 32):

        posicion = (dia + 2) % 7

        if posicion == 5 or posicion == 6:
            clase = "dia fin-semana"
        else:
            clase = "dia"

        cadena += '<div class="' + clase + '">' + str(dia) + '</div>'

    cadena += """
            </div>

        </div>

    </body>
    </html>
    """

    return cadena


if __name__ == "__main__":
    aplicacion.run(debug=True)