import os
from datetime import date
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import mysql.connector

aplicacion = Flask(__name__)
aplicacion.secret_key = os.getenv('FLASK_SECRET_KEY', 'cambiar-esta-clave-en-produccion')

def conexion():
    return mysql.connector.connect(host=os.getenv('DB_HOST','localhost'), user=os.getenv('DB_USER','blogdamtame2627'), password=os.getenv('DB_PASSWORD','TAME123$'), database=os.getenv('DB_NAME','blogdamtame2627'))

def consultar(sql, parametros=()):
    db = conexion()
    try:
        cursor = db.cursor(dictionary=True)
        try:
            cursor.execute(sql, parametros)
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        db.close()

@aplicacion.route('/')
def inicio():
    return render_template('blog.html')

@aplicacion.route('/articulos')
def articulos():
    return jsonify(consultar('SELECT id,titulo,fecha,contenido FROM articulos ORDER BY fecha DESC,id DESC'))

@aplicacion.route('/listado')
def listado():
    registros = consultar('SELECT id,titulo,fecha,contenido FROM articulos ORDER BY fecha DESC,id DESC')
    return render_template('tabla.html', articulos=registros, total=len(registros))

@aplicacion.route('/nuevo')
def nuevo():
    return render_template('formulario.html', hoy=date.today().isoformat())

@aplicacion.route('/inserta', methods=['POST'])
def inserta():
    titulo = request.form.get('titulo','').strip()
    fecha = request.form.get('fecha','').strip()
    contenido = request.form.get('contenido','').strip()
    if not titulo or not fecha or not contenido or len(titulo)>100:
        flash('Completa correctamente todos los campos (título máximo 100 caracteres).','error')
        return redirect(url_for('nuevo'))
    db = conexion()
    try:
        cursor = db.cursor()
        try:
            cursor.execute('INSERT INTO articulos (titulo,fecha,contenido) VALUES (%s,%s,%s)',(titulo,fecha,contenido))
            db.commit()
        finally:
            cursor.close()
    finally:
        db.close()
    flash('Artículo publicado correctamente.','success')
    return redirect(url_for('listado'))

if __name__ == '__main__':
    aplicacion.run(debug=os.getenv('FLASK_DEBUG') == '1')
