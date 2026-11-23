
PRAGMA foreign_keys = ON;

-- ============================================
-- ELIMINAR TABLAS ANTERIORES
-- ============================================

DROP TABLE IF EXISTS movimientos_inventario;
DROP TABLE IF EXISTS pagos;
DROP TABLE IF EXISTS facturas;
DROP TABLE IF EXISTS detalles_pedido;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS inventario;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS proveedores;
DROP TABLE IF EXISTS almacenes;
DROP TABLE IF EXISTS empleados;
DROP TABLE IF EXISTS clientes;

-- ============================================
-- 1. CLIENTES
-- ============================================

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT UNIQUE,
    telefono TEXT,
    direccion TEXT,
    ciudad TEXT,
    provincia TEXT,
    codigo_postal TEXT,
    fecha_registro TEXT,
    activo INTEGER DEFAULT 1
);

INSERT INTO clientes
(nombre, apellidos, email, telefono, ciudad, provincia, fecha_registro)
VALUES
('Juan', 'García López', 'juan@gmail.com', '600111222', 'Valencia', 'Valencia', '2025-01-15'),
('María', 'Martínez Ruiz', 'maria@gmail.com', '600222333', 'Madrid', 'Madrid', '2025-02-10'),
('Pedro', 'Sánchez Pérez', 'pedro@gmail.com', '600333444', 'Barcelona', 'Barcelona', '2025-03-05'),
('Ana', 'Fernández Gil', 'ana@gmail.com', '600444555', 'Sevilla', 'Sevilla', '2025-04-12'),
('Luis', 'Rodríguez Díaz', 'luis@gmail.com', '600555666', 'Alicante', 'Alicante', '2025-05-20'),
('Carmen', 'López Torres', 'carmen@gmail.com', '600666777', 'Valencia', 'Valencia', '2025-06-18'),
('David', 'Moreno Castro', 'david@gmail.com', '600777888', 'Murcia', 'Murcia', '2025-07-22'),
('Laura', 'Jiménez Romero', 'laura@gmail.com', '600888999', 'Madrid', 'Madrid', '2025-08-30');

-- ============================================
-- 2. EMPLEADOS
-- ============================================

CREATE TABLE empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT UNIQUE,
    telefono TEXT,
    puesto TEXT,
    departamento TEXT,
    salario REAL,
    fecha_contratacion TEXT,
    activo INTEGER DEFAULT 1
);

INSERT INTO empleados
(nombre, apellidos, email, puesto, departamento, salario, fecha_contratacion)
VALUES
('Carlos', 'Pérez', 'carlos@empresa.com', 'Director', 'Dirección', 3500, '2020-01-10'),
('Elena', 'Gómez', 'elena@empresa.com', 'Comercial', 'Ventas', 1800, '2021-03-15'),
('Miguel', 'Ruiz', 'miguel@empresa.com', 'Comercial', 'Ventas', 1900, '2022-06-01'),
('Sofía', 'Navarro', 'sofia@empresa.com', 'Administrativa', 'Administración', 1700, '2023-02-20'),
('Javier', 'Torres', 'javier@empresa.com', 'Almacenero', 'Logística', 1600, '2023-09-12'),
('Lucía', 'Serrano', 'lucia@empresa.com', 'Contable', 'Finanzas', 2100, '2022-11-05');

-- ============================================
-- 3. PROVEEDORES
-- ============================================

CREATE TABLE proveedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cif TEXT UNIQUE,
    contacto TEXT,
    email TEXT,
    telefono TEXT,
    direccion TEXT,
    ciudad TEXT,
    pais TEXT DEFAULT 'España'
);

INSERT INTO proveedores
(nombre, cif, contacto, email, ciudad)
VALUES
('Tecnología Global SL', 'B12345678', 'Roberto Díaz', 'ventas@tecnoglobal.es', 'Madrid'),
('Distribuciones Levante', 'B23456789', 'Isabel Pérez', 'info@levante.es', 'Valencia'),
('Informática Europa', 'B34567890', 'Antonio López', 'pedidos@informaticaeuropa.es', 'Barcelona'),
('Oficina Total', 'B45678901', 'Marta Gil', 'ventas@oficinatotal.es', 'Sevilla'),
('Componentes Express', 'B56789012', 'Daniel Ruiz', 'info@componentes.es', 'Alicante');

-- ============================================
-- 4. CATEGORÍAS
-- ============================================

CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    categoria_padre_id INTEGER,
    FOREIGN KEY (categoria_padre_id)
        REFERENCES categorias(id)
);

INSERT INTO categorias (nombre, descripcion, categoria_padre_id)
VALUES
('Informática', 'Productos informáticos', NULL),
('Ordenadores', 'Equipos de sobremesa y portátiles', 1),
('Periféricos', 'Accesorios informáticos', 1),
('Componentes', 'Componentes internos', 1),
('Oficina', 'Material de oficina', NULL),
('Mobiliario', 'Muebles de oficina', 5),
('Papelería', 'Material de papelería', 5),
('Monitores', 'Pantallas y monitores', 3);

-- ============================================
-- 5. PRODUCTOS
-- ============================================

CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    coste REAL,
    iva REAL DEFAULT 21,
    categoria_id INTEGER,
    proveedor_id INTEGER,
    fecha_alta TEXT,
    activo INTEGER DEFAULT 1,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id),
    FOREIGN KEY (proveedor_id) REFERENCES proveedores(id)
);

INSERT INTO productos
(codigo, nombre, precio, coste, categoria_id, proveedor_id, fecha_alta)
VALUES
('P001', 'Portátil Lenovo ThinkPad', 899.99, 650, 2, 1, '2025-01-10'),
('P002', 'Portátil ASUS VivoBook', 749.99, 520, 2, 1, '2025-01-12'),
('P003', 'Ratón Logitech MX Master', 89.90, 55, 3, 2, '2025-01-15'),
('P004', 'Teclado mecánico Corsair', 129.99, 85, 3, 2, '2025-01-18'),
('P005', 'Monitor Samsung 27 pulgadas', 249.99, 175, 8, 3, '2025-02-01'),
('P006', 'Monitor LG 24 pulgadas', 159.99, 110, 8, 3, '2025-02-05'),
('P007', 'Disco SSD Samsung 1TB', 99.99, 65, 4, 5, '2025-02-10'),
('P008', 'Memoria RAM Kingston 16GB', 59.99, 35, 4, 5, '2025-02-12'),
('P009', 'Procesador AMD Ryzen 7', 329.99, 245, 4, 5, '2025-02-15'),
('P010', 'Silla ergonómica', 199.99, 120, 6, 4, '2025-03-01'),
('P011', 'Mesa de oficina', 299.99, 180, 6, 4, '2025-03-05'),
('P012', 'Pack 500 folios A4', 6.99, 3.50, 7, 4, '2025-03-10'),
('P013', 'Bolígrafos azules pack 20', 8.99, 4.20, 7, 4, '2025-03-12'),
('P014', 'Impresora HP LaserJet', 189.99, 130, 3, 3, '2025-03-15'),
('P015', 'Webcam Logitech HD', 69.99, 42, 3, 2, '2025-03-20');

-- ============================================
-- 6. ALMACENES
-- ============================================

CREATE TABLE almacenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT,
    ciudad TEXT,
    responsable_id INTEGER,
    FOREIGN KEY (responsable_id) REFERENCES empleados(id)
);

INSERT INTO almacenes (nombre, direccion, ciudad, responsable_id)
VALUES
('Almacén Central', 'Calle Industria 10', 'Valencia', 5),
('Almacén Madrid', 'Avenida Europa 25', 'Madrid', 5),
('Almacén Barcelona', 'Calle Comercio 8', 'Barcelona', 5);

-- ============================================
-- 7. INVENTARIO
-- ============================================

CREATE TABLE inventario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    almacen_id INTEGER NOT NULL,
    cantidad INTEGER DEFAULT 0,
    stock_minimo INTEGER DEFAULT 5,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (almacen_id) REFERENCES almacenes(id),
    UNIQUE(producto_id, almacen_id)
);

INSERT INTO inventario
(producto_id, almacen_id, cantidad, stock_minimo)
VALUES
(1, 1, 15, 3),
(2, 1, 20, 5),
(3, 1, 50, 10),
(4, 1, 35, 8),
(5, 1, 18, 5),
(6, 1, 25, 5),
(7, 1, 40, 10),
(8, 1, 60, 10),
(9, 1, 12, 3),
(10, 1, 10, 3),
(11, 1, 8, 2),
(12, 1, 200, 30),
(13, 1, 150, 20),
(14, 1, 14, 4),
(15, 1, 30, 5),
(1, 2, 8, 3),
(3, 2, 25, 5),
(5, 2, 12, 3),
(7, 2, 20, 5),
(10, 2, 6, 2),
(2, 3, 10, 3),
(4, 3, 15, 5),
(6, 3, 9, 3),
(8, 3, 25, 5);

-- ============================================
-- 8. PEDIDOS
-- ============================================

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    empleado_id INTEGER,
    fecha TEXT NOT NULL,
    estado TEXT DEFAULT 'pendiente',
    direccion_envio TEXT,
    gastos_envio REAL DEFAULT 0,
    observaciones TEXT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)
);

INSERT INTO pedidos
(cliente_id, empleado_id, fecha, estado, gastos_envio)
VALUES
(1, 2, '2025-09-01', 'entregado', 5.99),
(2, 3, '2025-09-03', 'entregado', 0),
(3, 2, '2025-09-05', 'entregado', 5.99),
(1, 3, '2025-09-10', 'entregado', 0),
(4, 2, '2025-09-12', 'enviado', 5.99),
(5, 3, '2025-09-15', 'entregado', 0),
(6, 2, '2025-09-18', 'pendiente', 5.99),
(7, 3, '2025-09-20', 'entregado', 0),
(8, 2, '2025-09-22', 'enviado', 5.99),
(2, 3, '2025-10-01', 'entregado', 0),
(3, 2, '2025-10-05', 'pendiente', 5.99),
(5, 3, '2025-10-10', 'entregado', 0),
(1, 2, '2025-10-15', 'entregado', 5.99),
(4, 3, '2025-10-20', 'cancelado', 0),
(6, 2, '2025-11-01', 'pendiente', 5.99);

-- ============================================
-- 9. DETALLES DE PEDIDO
-- ============================================

CREATE TABLE detalles_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    descuento REAL DEFAULT 0,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

INSERT INTO detalles_pedido
(pedido_id, producto_id, cantidad, precio_unitario, descuento)
VALUES
(1, 1, 1, 899.99, 0),
(1, 3, 1, 89.90, 10),
(2, 5, 2, 249.99, 0),
(2, 4, 1, 129.99, 0),
(3, 7, 2, 99.99, 0),
(3, 8, 2, 59.99, 0),
(4, 2, 1, 749.99, 5),
(4, 15, 1, 69.99, 0),
(5, 10, 2, 199.99, 0),
(5, 11, 1, 299.99, 0),
(6, 9, 1, 329.99, 0),
(6, 8, 2, 59.99, 0),
(7, 12, 10, 6.99, 0),
(7, 13, 5, 8.99, 0),
(8, 14, 1, 189.99, 0),
(8, 12, 5, 6.99, 0),
(9, 1, 1, 899.99, 10),
(9, 5, 1, 249.99, 0),
(10, 3, 2, 89.90, 0),
(10, 4, 2, 129.99, 5),
(11, 7, 3, 99.99, 0),
(12, 2, 1, 749.99, 0),
(12, 6, 2, 159.99, 0),
(13, 9, 1, 329.99, 0),
(13, 8, 4, 59.99, 0),
(14, 10, 1, 199.99, 0),
(15, 11, 2, 299.99, 0),
(15, 12, 20, 6.99, 0);

-- ============================================
-- 10. FACTURAS
-- ============================================

CREATE TABLE facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT UNIQUE NOT NULL,
    pedido_id INTEGER UNIQUE NOT NULL,
    fecha_emision TEXT NOT NULL,
    fecha_vencimiento TEXT,
    base_imponible REAL NOT NULL,
    iva REAL NOT NULL,
    total REAL NOT NULL,
    estado TEXT DEFAULT 'pendiente',
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
);

INSERT INTO facturas
(numero, pedido_id, fecha_emision, fecha_vencimiento,
 base_imponible, iva, total, estado)
SELECT
    'FAC-2025-' || printf('%04d', p.id),
    p.id,
    p.fecha,
    date(p.fecha, '+30 days'),
    ROUND(
        SUM(d.cantidad * d.precio_unitario *
            (1 - d.descuento / 100.0)) + p.gastos_envio, 2
    ),
    ROUND(
        (SUM(d.cantidad * d.precio_unitario *
            (1 - d.descuento / 100.0)) + p.gastos_envio) * 0.21, 2
    ),
    ROUND(
        (SUM(d.cantidad * d.precio_unitario *
            (1 - d.descuento / 100.0)) + p.gastos_envio) * 1.21, 2
    ),
    CASE
        WHEN p.estado = 'entregado' THEN 'pagada'
        ELSE 'pendiente'
    END
FROM pedidos p
JOIN detalles_pedido d ON d.pedido_id = p.id
WHERE p.estado <> 'cancelado'
GROUP BY p.id;

-- ============================================
-- 11. PAGOS
-- ============================================

CREATE TABLE pagos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    factura_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    importe REAL NOT NULL,
    metodo TEXT NOT NULL,
    referencia TEXT,
    FOREIGN KEY (factura_id) REFERENCES facturas(id)
);

INSERT INTO pagos
(factura_id, fecha, importe, metodo, referencia)
SELECT
    id,
    date(fecha_emision, '+2 days'),
    total,
    CASE
        WHEN id % 3 = 0 THEN 'transferencia'
        WHEN id % 3 = 1 THEN 'tarjeta'
        ELSE 'bizum'
    END,
    'PAGO-' || printf('%05d', id)
FROM facturas
WHERE estado = 'pagada';

-- ============================================
-- 12. MOVIMIENTOS DE INVENTARIO
-- ============================================

CREATE TABLE movimientos_inventario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_id INTEGER NOT NULL,
    almacen_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    tipo TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    motivo TEXT,
    empleado_id INTEGER,
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (almacen_id) REFERENCES almacenes(id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id)
);

INSERT INTO movimientos_inventario
(producto_id, almacen_id, fecha, tipo, cantidad, motivo, empleado_id)
VALUES
(1, 1, '2025-08-01', 'entrada', 20, 'Compra proveedor', 5),
(2, 1, '2025-08-02', 'entrada', 25, 'Compra proveedor', 5),
(3, 1, '2025-08-03', 'entrada', 60, 'Compra proveedor', 5),
(5, 1, '2025-08-05', 'entrada', 30, 'Compra proveedor', 5),
(7, 1, '2025-08-10', 'entrada', 50, 'Compra proveedor', 5),
(1, 1, '2025-09-01', 'salida', 1, 'Pedido 1', 5),
(3, 1, '2025-09-01', 'salida', 1, 'Pedido 1', 5),
(5, 1, '2025-09-03', 'salida', 2, 'Pedido 2', 5),
(7, 1, '2025-09-05', 'salida', 2, 'Pedido 3', 5),
(2, 1, '2025-09-10', 'salida', 1, 'Pedido 4', 5),
(3, 1, '2025-09-15', 'entrada', 20, 'Reposición', 5),
(5, 1, '2025-09-20', 'entrada', 10, 'Reposición', 5),
(7, 1, '2025-10-01', 'entrada', 15, 'Reposición', 5);

-- ============================================
-- ÍNDICES
-- ============================================

CREATE INDEX idx_pedidos_cliente ON pedidos(cliente_id);
CREATE INDEX idx_pedidos_fecha ON pedidos(fecha);
CREATE INDEX idx_detalles_pedido ON detalles_pedido(pedido_id);
CREATE INDEX idx_detalles_producto ON detalles_pedido(producto_id);
CREATE INDEX idx_productos_categoria ON productos(categoria_id);
CREATE INDEX idx_productos_proveedor ON productos(proveedor_id);
CREATE INDEX idx_facturas_fecha ON facturas(fecha_emision);
CREATE INDEX idx_pagos_factura ON pagos(factura_id);
CREATE INDEX idx_inventario_producto ON inventario(producto_id);

-- ============================================
-- COMPROBACIÓN
-- ============================================

SELECT 'clientes' AS tabla, COUNT(*) AS registros FROM clientes
UNION ALL
SELECT 'empleados', COUNT(*) FROM empleados
UNION ALL
SELECT 'proveedores', COUNT(*) FROM proveedores
UNION ALL
SELECT 'categorias', COUNT(*) FROM categorias
UNION ALL
SELECT 'productos', COUNT(*) FROM productos
UNION ALL
SELECT 'almacenes', COUNT(*) FROM almacenes
UNION ALL
SELECT 'inventario', COUNT(*) FROM inventario
UNION ALL
SELECT 'pedidos', COUNT(*) FROM pedidos
UNION ALL
SELECT 'detalles_pedido', COUNT(*) FROM detalles_pedido
UNION ALL
SELECT 'facturas', COUNT(*) FROM facturas
UNION ALL
SELECT 'pagos', COUNT(*) FROM pagos
UNION ALL
SELECT 'movimientos_inventario', COUNT(*) FROM movimientos_inventario;
