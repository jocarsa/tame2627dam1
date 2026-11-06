
from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector

aplicacion = Flask(__name__)
aplicacion.secret_key = "clave-secreta-cambiar-en-produccion"

usuario = "jocarsa"
contrasena = "jocarsa"

@aplicacion.route("/")
def inicio():
    if session.get("usuario"):
        return redirect(url_for("escritorio"))
    return render_template("login.html")


@aplicacion.route("/login", methods=["POST"])
def iniciar_sesion():
    usuario_recibido = request.form.get("usuario", "")
    contrasena_recibida = request.form.get("contrasena", "")

    """if usuario_recibido == usuario and contrasena_recibida == contrasena:
        session["usuario"] = usuario_recibido
        pasas = "si"
    else:
        pasas = "no""""
    connection = mysql.connector.connect(
        host='localhost',
        user='logintame',
        password='TAME123$',
        database='logintame'
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE usuario = '"+usuario_recibido+"' AND contrasena == '"+contrasena_recibida+"';")
    usuario = cursor.fetchall()
		pasas = 'no'
    for producto in productos:
        cadena += str(producto)
    

    return render_template(
        "procesar_login.html",
        pasas=pasas,
        usuario=usuario_recibido
    )


@aplicacion.route("/escritorio")
def escritorio():
    if not session.get("usuario"):
        return redirect(url_for("inicio"))

    return render_template(
        "escritorio.html",
        usuario=session["usuario"]
    )


@aplicacion.route("/logout")
def cerrar_sesion():
    session.clear()
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    aplicacion.run(debug=True)
