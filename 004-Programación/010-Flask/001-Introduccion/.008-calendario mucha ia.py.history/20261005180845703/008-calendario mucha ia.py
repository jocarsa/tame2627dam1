from flask import Flask
import calendar

aplicacion = Flask(__name__)

@aplicacion.route("/")
def inicio():

    anio = 2026

    meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    cadena = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Calendario anual</title>

        <style>

            *{
                box-sizing:border-box;
            }

            body{
                margin:0;
                padding:40px;
                font-family:Arial, sans-serif;
                background:#f3f4f6;
            }

            h1{
                text-align:center;
                font-size:40px;
                margin-bottom:40px;
                color:#333;
            }

            .calendario{
                max-width:1400px;
                margin:auto;

                display:grid;
                grid-template-columns:repeat(3, 1fr);
                gap:25px;
            }

            .mes{
                background:white;
                padding:20px;
                border-radius:12px;

                box-shadow:
                    0px 5px 15px rgba(0,0,0,0.1);
            }

            .mes h2{
                text-align:center;
                margin-top:0;
                margin-bottom:15px;
                color:#333;
            }

            .semana,
            .dias{
                display:grid;
                grid-template-columns:repeat(7, 1fr);
                gap:4px;
            }

            .semana div{
                text-align:center;
                font-size:12px;
                font-weight:bold;
                color:#888;
                padding:5px;
            }

            .dia{
                aspect-ratio:1;
                display:flex;
                justify-content:center;
                align-items:center;

                border-radius:6px;
                font-size:13px;

                background:#f5f5f5;

                cursor:pointer;
                transition:0.2s;
            }

            .dia:hover{
                background:#333;
                color:white;
                transform:scale(1.1);
            }

            .vacio{
                aspect-ratio:1;
            }

            .fin-semana{
                background:#fff0f0;
                color:#c44;
            }


            @media(max-width:1000px){

                .calendario{
                    grid-template-columns:repeat(2,1fr);
                }

            }


            @media(max-width:600px){

                body{
                    padding:15px;
                }

                .calendario{
                    grid-template-columns:1fr;
                }

            }

        </style>
    </head>

    <body>

        <h1>Calendario """ + str(anio) + """</h1>

        <div class="calendario">
    """

    # Recorremos los 12 meses
    for numero_mes in range(1, 13):

        cadena += """
        <div class="mes">

            <h2>""" + meses[numero_mes - 1] + """</h2>

            <div class="semana">
                <div>L</div>
                <div>M</div>
                <div>X</div>
                <div>J</div>
                <div>V</div>
                <div>S</div>
                <div>D</div>
            </div>

            <div class="dias">
        """

        # Obtenemos las semanas del mes.
        # Cada semana contiene 7 números.
        # El 0 significa que ese día pertenece
        # al mes anterior o posterior.

        semanas = calendar.monthcalendar(anio, numero_mes)

        for semana in semanas:

            for posicion, dia in enumerate(semana):

                if dia == 0:

                    cadena += """
                    <div class="vacio"></div>
                    """

                else:

                    # sábado = 5
                    # domingo = 6

                    if posicion >= 5:
                        clase = "dia fin-semana"
                    else:
                        clase = "dia"

                    cadena += (
                        '<div class="' + clase + '">'
                        + str(dia) +
                        '</div>'
                    )

        cadena += """
            </div>

        </div>
        """

    cadena += """
        </div>

    </body>
    </html>
    """

    return cadena


if __name__ == "__main__":
    aplicacion.run(debug=True)