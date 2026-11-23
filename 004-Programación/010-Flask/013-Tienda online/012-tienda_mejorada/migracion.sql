-- Ejecutar sobre la base de datos de la tienda, tras realizar una copia de seguridad.
ALTER TABLE productos
 ADD COLUMN categoria VARCHAR(80) NOT NULL DEFAULT 'Deporte' AFTER descripcion,
 ADD COLUMN imagen VARCHAR(500) NULL AFTER categoria,
 ADD COLUMN stock INT UNSIGNED NOT NULL DEFAULT 20 AFTER precio,
 ADD COLUMN destacado TINYINT(1) NOT NULL DEFAULT 0 AFTER stock,
 ADD COLUMN activo TINYINT(1) NOT NULL DEFAULT 1 AFTER destacado;

CREATE TABLE IF NOT EXISTS pedidos (
 id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
 cliente_nombre VARCHAR(120) NOT NULL,
 cliente_email VARCHAR(190) NOT NULL,
 cliente_direccion VARCHAR(255) NOT NULL,
 total DECIMAL(10,2) NOT NULL,
 estado VARCHAR(30) NOT NULL DEFAULT 'pendiente',
 creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS pedido_lineas (
 id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
 pedido_id BIGINT UNSIGNED NOT NULL,
 producto_id INT NOT NULL,
 nombre_producto VARCHAR(120) NOT NULL,
 cantidad INT UNSIGNED NOT NULL,
 precio_unitario DECIMAL(10,2) NOT NULL,
 subtotal DECIMAL(10,2) NOT NULL,
 CONSTRAINT fk_lineas_pedido FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
 INDEX idx_producto (producto_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

UPDATE productos SET categoria = CASE
 WHEN LOWER(nombre) REGEXP 'bal[oó]n|pelota|raqueta|porter[ií]a' THEN 'Deportes de equipo'
 WHEN LOWER(nombre) REGEXP 'mancuerna|pesa|esterilla|fitness|yoga|comba' THEN 'Fitness'
 WHEN LOWER(nombre) REGEXP 'zapatilla|running|correr' THEN 'Running'
 WHEN LOWER(nombre) REGEXP 'bicicleta|casco|ciclismo' THEN 'Ciclismo'
 ELSE 'Accesorios' END;
