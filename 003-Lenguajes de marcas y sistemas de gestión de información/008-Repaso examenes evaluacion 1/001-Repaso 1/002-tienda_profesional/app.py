from flask import Flask, render_template, request
import mysql.connector

aplicacion = Flask(__name__)

def conectar():
    return mysql.connector.connect(host='localhost', user='tiendaexamen', password='TAME123$', database='tiendaexamen')

@aplicacion.route('/')
def inicio():
    conexion = conectar()
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute('SELECT * FROM productos ORDER BY id DESC')
        productos = cursor.fetchall()
        cursor.close()
    finally:
        conexion.close()
    return render_template('front.html', productos=productos)

@aplicacion.route('/admin')
def admin():
    return render_template('admin.html')

@aplicacion.route('/insertar', methods=['POST'])
def insertar():
    nombre = request.form.get('nombre', '').strip()
    descripcion = request.form.get('descripcion', '').strip()
    precio = request.form.get('precio', '').strip()
    if not nombre or not descripcion or not precio:
        return render_template('ok.html', correcto=False, mensaje='Completa todos los campos.'), 400
    try:
        from decimal import Decimal, InvalidOperation
        importe = Decimal(precio)
        if not importe.is_finite() or importe < 0 or importe > Decimal('9999.99'):
            raise InvalidOperation
    except (InvalidOperation, ValueError):
        return render_template('ok.html', correcto=False, mensaje='Introduce un precio válido entre 0 y 9999,99 €.'), 400
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)', (nombre, descripcion, importe))
        conexion.commit()
        cursor.close()
    finally:
        conexion.close()
    return render_template('ok.html', correcto=True, mensaje=f'«{nombre}» se ha añadido correctamente al catálogo.')

if __name__ == '__main__':
    aplicacion.run(debug=True)
