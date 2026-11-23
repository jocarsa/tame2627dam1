DROP DATABASE IF EXISTS tienda_practicas;

CREATE DATABASE tienda_practicas
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE tienda_practicas;


-- ============================================
-- CLIENTES
-- ============================================

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    ciudad VARCHAR(80),
    provincia VARCHAR(80),
    pais VARCHAR(80) DEFAULT 'España',
    fecha_nacimiento DATE,
    fecha_registro DATE NOT NULL,
    activo BOOLEAN DEFAULT TRUE
);


-- ============================================
-- CATEGORIAS
-- ============================================

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);


-- ============================================
-- PROVEEDORES
-- ============================================

CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(150),
    ciudad VARCHAR(80),
    pais VARCHAR(80)
);


-- ============================================
-- PRODUCTOS
-- ============================================

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    coste DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    categoria_id INT,
    proveedor_id INT,
    fecha_alta DATE,
    activo BOOLEAN DEFAULT TRUE,

    FOREIGN KEY (categoria_id)
        REFERENCES categorias(id),

    FOREIGN KEY (proveedor_id)
        REFERENCES proveedores(id)
);


-- ============================================
-- EMPLEADOS
-- ============================================

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    puesto VARCHAR(80),
    salario DECIMAL(10,2),
    departamento VARCHAR(80),
    ciudad VARCHAR(80),
    fecha_contratacion DATE,
    jefe_id INT,

    FOREIGN KEY (jefe_id)
        REFERENCES empleados(id)
);


-- ============================================
-- PEDIDOS
-- ============================================

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    empleado_id INT,
    fecha DATE NOT NULL,
    estado VARCHAR(30),
    metodo_pago VARCHAR(30),
    gastos_envio DECIMAL(10,2) DEFAULT 0,
    descuento DECIMAL(10,2) DEFAULT 0,

    FOREIGN KEY (cliente_id)
        REFERENCES clientes(id),

    FOREIGN KEY (empleado_id)
        REFERENCES empleados(id)
);


-- ============================================
-- DETALLES DE LOS PEDIDOS
-- ============================================

CREATE TABLE detalles_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    descuento DECIMAL(5,2) DEFAULT 0,

    FOREIGN KEY (pedido_id)
        REFERENCES pedidos(id),

    FOREIGN KEY (producto_id)
        REFERENCES productos(id)
);


-- ============================================
-- ALMACENES
-- ============================================

CREATE TABLE almacenes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(80),
    capacidad INT
);


-- ============================================
-- INVENTARIO
-- ============================================

CREATE TABLE inventario (
    almacen_id INT,
    producto_id INT,
    cantidad INT DEFAULT 0,

    PRIMARY KEY (almacen_id, producto_id),

    FOREIGN KEY (almacen_id)
        REFERENCES almacenes(id),

    FOREIGN KEY (producto_id)
        REFERENCES productos(id)
);


-- ============================================
-- VALORACIONES
-- ============================================

CREATE TABLE valoraciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    producto_id INT NOT NULL,
    puntuacion INT,
    comentario VARCHAR(500),
    fecha DATE,

    FOREIGN KEY (cliente_id)
        REFERENCES clientes(id),

    FOREIGN KEY (producto_id)
        REFERENCES productos(id)
);


-- ============================================
-- INDICES PARA PRACTICAR OPTIMIZACION
-- ============================================

CREATE INDEX idx_clientes_ciudad
ON clientes(ciudad);

CREATE INDEX idx_clientes_provincia
ON clientes(provincia);

CREATE INDEX idx_productos_precio
ON productos(precio);

CREATE INDEX idx_productos_categoria
ON productos(categoria_id);

CREATE INDEX idx_pedidos_fecha
ON pedidos(fecha);

CREATE INDEX idx_pedidos_cliente
ON pedidos(cliente_id);

CREATE INDEX idx_detalles_producto
ON detalles_pedido(producto_id);