import os
import hmac
import secrets
from functools import wraps
from decimal import Decimal
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, abort
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


# Administración: configurar ADMIN_PASSWORD y FLASK_SECRET_KEY como variables de entorno.
ESTADOS = ('pendiente', 'preparando', 'enviado', 'entregado', 'cancelado')

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('admin_autenticado'):
            return redirect(url_for('admin_login'))
        return fn(*args, **kwargs)
    return wrapper

def verificar_csrf():
    token = session.get('admin_csrf', '')
    if not token or not hmac.compare_digest(token, request.form.get('csrf', '')):
        abort(400, 'Token de formulario inválido')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if session.get('admin_autenticado'):
        return redirect(url_for('admin'))
    error = None
    if request.method == 'POST':
        clave = os.environ.get('ADMIN_PASSWORD', '')
        if clave and hmac.compare_digest(request.form.get('password', ''), clave):
            session.clear()
            session['admin_autenticado'] = True
            session['admin_csrf'] = secrets.token_urlsafe(32)
            return redirect(url_for('admin'))
        error = 'Contraseña incorrecta o ADMIN_PASSWORD no configurada'
    return render_template('admin_login.html', error=error)

@app.post('/admin/logout')
@admin_required
def admin_logout():
    verificar_csrf()
    session.clear()
    return redirect(url_for('admin_login'))

@app.get('/admin')
@admin_required
def admin():
    vista = request.args.get('vista', 'pedidos')
    if vista not in ('pedidos', 'clientes'):
        vista = 'pedidos'
    q = request.args.get('q', '').strip()[:100]
    estado = request.args.get('estado', '').strip()
    if estado not in ESTADOS:
        estado = ''
    db = conectar()
    cur = db.cursor(dictionary=True)
    try:
        cur.execute("SELECT COUNT(*) pedidos, COALESCE(SUM(CASE WHEN estado <> 'cancelado' THEN total ELSE 0 END),0) ventas, SUM(estado='pendiente') pendientes, COUNT(DISTINCT LOWER(cliente_email)) clientes FROM pedidos")
        kpis = cur.fetchone()
        cur.execute('SELECT COUNT(*) productos, COALESCE(SUM(stock),0) unidades FROM productos WHERE activo=1')
        kpis.update(cur.fetchone())
        pedidos, clientes = [], []
        if vista == 'pedidos':
            sql = 'SELECT id,cliente_nombre,cliente_email,cliente_direccion,total,estado,creado_en,fecha FROM pedidos WHERE 1=1'
            args = []
            if q:
                sql += ' AND (cliente_nombre LIKE %s OR cliente_email LIKE %s OR CAST(id AS CHAR) LIKE %s)'
                args.extend([f'%{q}%']*3)
            if estado:
                sql += ' AND estado=%s'
                args.append(estado)
            sql += ' ORDER BY id DESC LIMIT 200'
            cur.execute(sql, args)
            pedidos = cur.fetchall()
            if pedidos:
                ids = [p['id'] for p in pedidos]
                cur.execute('SELECT pedido_id, nombre_producto, cantidad, precio_unitario, subtotal FROM pedido_lineas WHERE pedido_id IN (' + ','.join(['%s']*len(ids)) + ') ORDER BY id', ids)
                lineas = {}
                for linea in cur.fetchall():
                    lineas.setdefault(linea['pedido_id'], []).append(linea)
                for pedido in pedidos:
                    pedido['lineas'] = lineas.get(pedido['id'], [])
        else:
            sql = "SELECT LOWER(cliente_email) email, MAX(cliente_nombre) nombre, COUNT(*) pedidos, SUM(CASE WHEN estado <> 'cancelado' THEN total ELSE 0 END) gastado, MAX(creado_en) ultima_compra FROM pedidos WHERE cliente_email IS NOT NULL AND cliente_email <> ''"
            args = []
            if q:
                sql += ' AND (cliente_nombre LIKE %s OR cliente_email LIKE %s)'
                args.extend([f'%{q}%']*2)
            sql += ' GROUP BY LOWER(cliente_email) ORDER BY ultima_compra DESC LIMIT 200'
            cur.execute(sql, args)
            clientes = cur.fetchall()
        return render_template('admin.html', vista=vista, q=q, estado=estado,
                               estados=ESTADOS, kpis=kpis, pedidos=pedidos, clientes=clientes,
                               csrf=session['admin_csrf'])
    finally:
        cur.close()
        db.close()

@app.post('/admin/pedidos/<int:pedido_id>/estado')
@admin_required
def admin_cambiar_estado(pedido_id):
    verificar_csrf()
    estado = request.form.get('estado', '')
    if estado not in ESTADOS:
        abort(400, 'Estado no válido')
    db = conectar()
    cur = db.cursor()
    try:
        cur.execute('UPDATE pedidos SET estado=%s WHERE id=%s', (estado, pedido_id))
        db.commit()
        if cur.rowcount == 0:
            abort(404)
    except Exception:
        db.rollback()
        raise
    finally:
        cur.close()
        db.close()
    return redirect(url_for('admin', vista='pedidos'))

@app.get('/admin/clientes/<path:email>')
@admin_required
def admin_cliente(email):
    db = conectar()
    cur = db.cursor(dictionary=True)
    try:
        cur.execute('SELECT id,cliente_nombre,cliente_email,cliente_direccion,total,estado,creado_en FROM pedidos WHERE LOWER(cliente_email)=LOWER(%s) ORDER BY id DESC', (email,))
        pedidos = cur.fetchall()
        if not pedidos:
            abort(404)
        return render_template('admin_cliente.html', pedidos=pedidos, email=email, csrf=session['admin_csrf'])
    finally:
        cur.close()
        db.close()

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG') == '1')
