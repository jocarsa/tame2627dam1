# SPORTLAB — tienda deportiva Flask + MySQL

## Instalación

1. Haz copia de seguridad de tu base de datos.
2. Selecciona la base de datos de la tienda y ejecuta `migracion.sql` **una sola vez**. Parte de la tabla existente `productos(id,nombre,descripcion,precio)`.
3. Instala dependencias: `pip install -r requirements.txt`.
4. Configura las variables de entorno:

```bash
export DB_HOST=localhost
export DB_NAME=tiendaonlinedamtame2627
export DB_USER=tu_usuario_mysql
export DB_PASSWORD='tu_clave_mysql'
export FLASK_SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_hex(32))')"
python3 app.py
```

5. Visita `http://127.0.0.1:5000/articulos`.

## Alcance

El catálogo, búsqueda, filtros y carrito son funcionales. El carrito se guarda en `localStorage`; los pedidos se registran en MySQL con control de stock transaccional. **No hay pasarela de pago ni envío automático de correos.** El checkout registra solicitudes de pedido sin cobrar. Para uso público en producción faltan protección antiabuso, HTTPS, política de privacidad, gestión de pedidos, autenticación administrativa, pagos y logística.

Las imágenes se pueden configurar mediante el campo `productos.imagen` (URL de imagen). Si está vacío, se muestra una composición gráfica.

La migración no debe ejecutarse dos veces porque `ALTER TABLE` añadiría columnas duplicadas.
