import os
from datetime import date
import mysql.connector
from flask import Flask, render_template, request, jsonify

aplicacion = Flask(__name__)

def conectar():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'blogexamen2627'),
        password=os.getenv('DB_PASSWORD', 'TAME123$'),
        database=os.getenv('DB_NAME', 'blogexamen2627')
    )

@aplicacion.route('/')
def inicio():
    return render_template('inicio.html')

@aplicacion.route('/datos')
def datos():
    conexion = conectar()
    try:
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute('SELECT id, titulo, fecha, contenido FROM noticias ORDER BY fecha DESC, id DESC')
            noticias = cursor.fetchall()
            for noticia in noticias:
                if noticia['fecha'] is not None:
                    noticia['fecha'] = noticia['fecha'].isoformat()
            return jsonify(noticias)
        finally:
            cursor.close()
    finally:
        conexion.close()

@aplicacion.route('/recibe', methods=['POST'])
def recibe():
    titulo = request.form.get('titulo', '').strip()
    fecha = request.form.get('fecha', '').strip()
    contenido = request.form.get('contenido', '').strip()
    if not titulo or not fecha or not contenido or len(titulo) > 100:
        return jsonify(error='Completa todos los campos (título máximo 100 caracteres).'), 400
    try:
        date.fromisoformat(fecha)
    except ValueError:
        return jsonify(error='La fecha no es válida.'), 400
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute('INSERT INTO noticias (titulo, fecha, contenido) VALUES (%s, %s, %s)', (titulo, fecha, contenido))
            conexion.commit()
            return jsonify(ok=True, id=cursor.lastrowid), 201
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
    finally:
        conexion.close()

if __name__ == '__main__':
    aplicacion.run(debug=True)
