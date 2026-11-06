import os
from decimal import Decimal
from flask import Flask, render_template, request, jsonify, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "TAME123$"

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="tiendaonlinedamtame2627", password="TAME123$",
        database="tiendaonlinedamtame2627")

def producto_dict(row):
    row['precio'] = float(row['precio'])
    return row

@app.get('/')
@app.get('/articulos')
def catalogo():
    db = conectar()
    cur = db.cursor(dictionary=True)
    q = request.args.get('q', '').strip()[:100]
    categoria = request.args.get('categoria', '').strip()[:80]
    orden = request.args.get('orden', 'recientes')
    ordenes = {'recientes': 'id DESC', 'precio_asc': 'precio ASC',
               'precio_desc': 'precio DESC', 'nombre': 'nombre ASC'}
    sql = 'SELECT id,nombre,descripcion,categoria,imagen,precio,stock,destacado FROM productos WHERE activo=1'
    params = []
    if q:
        sql += ' AND (nombre LIKE %s OR descripcion LIKE %s)'
        params += [f'%{q}%', f'%{q}%']
    if categoria:
        sql += ' AND categoria=%s'
        params.append(categoria)
    sql += ' ORDER BY ' + ordenes.get(orden, ordenes['recientes'])
    cur.execute(sql, params)
    productos = [producto_dict(x) for x in cur.fetchall()]
    cur.execute('SELECT DISTINCT categoria FROM productos WHERE activo=1 ORDER BY categoria')
    categorias = [x['categoria'] for x in cur.fetchall()]
    cur.close(); db.close()
    return render_template('tienda.html', productos=productos, categorias=categorias,
                           q=q, categoria=categoria, orden=orden)

@app.post('/api/pedidos')
def crear_pedido():
    datos = request.get_json(silent=True) or {}
    cliente = datos.get('cliente') or {}
    items = datos.get('items') or []
    nombre = str(cliente.get('nombre', '')).strip()[:120]
    email = str(cliente.get('email', '')).strip()[:190]
    direccion = str(cliente.get('direccion', '')).strip()[:255]
    if not nombre or '@' not in email or not direccion or not isinstance(items, list) or not items or len(items) > 100:
        return jsonify(error='Datos del pedido incompletos'), 400
    cantidades = {}
    try:
        for item in items:
            pid, cantidad = int(item['id']), int(item['cantidad'])
            if pid <= 0 or not 1 <= cantidad <= 100:
                raise ValueError()
            cantidades[pid] = cantidades.get(pid, 0) + cantidad
            if cantidades[pid] > 100:
                raise ValueError()
    except (TypeError, ValueError, KeyError):
        return jsonify(error='Artículos no válidos'), 400
    db = conectar()
    cur = db.cursor(dictionary=True)
    try:
        db.start_transaction()
        ids = sorted(cantidades)
        placeholders = ','.join(['%s'] * len(ids))
        cur.execute(f'SELECT id,nombre,precio,stock FROM productos WHERE activo=1 AND id IN ({placeholders}) FOR UPDATE', ids)
        encontrados = {p['id']: p for p in cur.fetchall()}
        if len(encontrados) != len(ids) or any(encontrados[i]['stock'] < cantidades[i] for i in ids):
            db.rollback()
            return jsonify(error='Uno o más artículos no tienen stock suficiente'), 409
        total = sum((encontrados[i]['precio'] * cantidades[i] for i in ids), Decimal('0.00'))
        cur.execute('INSERT INTO pedidos (cliente_nombre,cliente_email,cliente_direccion,total) VALUES (%s,%s,%s,%s)',
                    (nombre, email, direccion, total))
        pedido_id = cur.lastrowid
        for i in ids:
            p = encontrados[i]
            cantidad = cantidades[i]
            cur.execute('INSERT INTO pedido_lineas (pedido_id,producto_id,nombre_producto,cantidad,precio_unitario,subtotal) VALUES (%s,%s,%s,%s,%s,%s)',
                        (pedido_id, i, p['nombre'], cantidad, p['precio'], p['precio'] * cantidad))
            cur.execute('UPDATE productos SET stock=stock-%s WHERE id=%s', (cantidad, i))
        db.commit()
        return jsonify(ok=True, pedido_id=pedido_id, total=float(total)), 201
    except Exception:
        db.rollback()
        app.logger.exception('Error guardando pedido')
        return jsonify(error='No se pudo guardar el pedido'), 500
    finally:
        cur.close(); db.close()

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG') == '1')
