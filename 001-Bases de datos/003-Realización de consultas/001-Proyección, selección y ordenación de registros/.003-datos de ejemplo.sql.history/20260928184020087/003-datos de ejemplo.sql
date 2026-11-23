USE tienda_practicas;


-- ============================================
-- CATEGORIAS
-- ============================================

INSERT INTO categorias (nombre, descripcion) VALUES
('Ordenadores', 'Ordenadores de sobremesa y portátiles'),
('Monitores', 'Monitores y pantallas'),
('Periféricos', 'Teclados, ratones y accesorios'),
('Componentes', 'Componentes internos de ordenador'),
('Almacenamiento', 'Discos duros, SSD y memorias'),
('Redes', 'Equipamiento de red'),
('Impresión', 'Impresoras y consumibles'),
('Audio', 'Auriculares, altavoces y micrófonos'),
('Telefonía', 'Smartphones y accesorios'),
('Tablets', 'Tablets y accesorios'),
('Gaming', 'Productos para videojuegos'),
('Oficina', 'Equipamiento de oficina');


-- ============================================
-- PROVEEDORES
-- ============================================

INSERT INTO proveedores
(nombre, contacto, telefono, email, ciudad, pais)
VALUES
('TechDistribuciones', 'Laura Gómez', '961000001', 'ventas@techdist.es', 'Valencia', 'España'),
('IberHardware', 'Carlos Ruiz', '911000002', 'info@iberhardware.es', 'Madrid', 'España'),
('Mediterránea Digital', 'Ana Torres', '965000003', 'ventas@medigital.es', 'Alicante', 'España'),
('EuroComponents', 'Pierre Martin', '331000004', 'sales@eurocomponents.fr', 'Paris', 'Francia'),
('GermanTech', 'Hans Müller', '491000005', 'info@germantech.de', 'Berlin', 'Alemania'),
('Asia Electronics', 'Li Wei', '861000006', 'sales@asiaelectronics.cn', 'Shenzhen', 'China'),
('Levante Informática', 'Marta López', '963000007', 'pedidos@levanteinfo.es', 'Valencia', 'España'),
('Barcelona Components', 'Jordi Serra', '931000008', 'ventas@bcncomponents.es', 'Barcelona', 'España'),
('Digital Norte', 'Iker Alonso', '944000009', 'info@digitalnorte.es', 'Bilbao', 'España'),
('Tech Portugal', 'Joao Silva', '351000010', 'sales@techportugal.pt', 'Lisboa', 'Portugal');


-- ============================================
-- CLIENTES
-- ============================================

INSERT INTO clientes
(nombre, apellidos, email, telefono, ciudad, provincia, pais, fecha_nacimiento, fecha_registro, activo)
VALUES
('Ana','García López','ana.garcia@email.com','600100001','Valencia','Valencia','España','1985-03-12','2023-01-15',1),
('Carlos','Martínez Ruiz','carlos.martinez@email.com','600100002','Madrid','Madrid','España','1979-07-23','2023-02-18',1),
('Laura','Sánchez Pérez','laura.sanchez@email.com','600100003','Valencia','Valencia','España','1992-11-05','2023-03-20',1),
('David','López Gómez','david.lopez@email.com','600100004','Alicante','Alicante','España','1988-04-17','2023-04-11',1),
('Marta','Fernández Gil','marta.fernandez@email.com','600100005','Barcelona','Barcelona','España','1995-01-30','2023-05-03',1),
('Javier','Ruiz Torres','javier.ruiz@email.com','600100006','Madrid','Madrid','España','1982-09-14','2023-06-16',1),
('Elena','Navarro Díaz','elena.navarro@email.com','600100007','Sevilla','Sevilla','España','1990-06-22','2023-07-09',1),
('Pablo','Romero Vidal','pablo.romero@email.com','600100008','Valencia','Valencia','España','1987-12-01','2023-08-13',1),
('Lucía','Moreno Cano','lucia.moreno@email.com','600100009','Castellón','Castellón','España','1998-08-19','2023-09-01',1),
('Sergio','Ortiz Ramos','sergio.ortiz@email.com','600100010','Murcia','Murcia','España','1983-05-25','2023-10-14',1),

('Andrea','Molina Serra','andrea.molina@email.com','600100011','Valencia','Valencia','España','1991-02-11','2023-11-03',1),
('Miguel','Castro León','miguel.castro@email.com','600100012','Madrid','Madrid','España','1977-10-09','2023-12-12',1),
('Sara','Vega Pastor','sara.vega@email.com','600100013','Alicante','Alicante','España','1996-07-07','2024-01-09',1),
('Raúl','Santos Mora','raul.santos@email.com','600100014','Barcelona','Barcelona','España','1984-03-28','2024-01-19',1),
('Cristina','Iglesias Soto','cristina.iglesias@email.com','600100015','Valencia','Valencia','España','1989-09-15','2024-02-03',1),
('Alberto','Crespo Marín','alberto.crespo@email.com','600100016','Zaragoza','Zaragoza','España','1981-11-21','2024-02-18',1),
('Patricia','Reyes Calvo','patricia.reyes@email.com','600100017','Madrid','Madrid','España','1993-04-04','2024-03-07',1),
('Rubén','Herrero Peña','ruben.herrero@email.com','600100018','Bilbao','Vizcaya','España','1986-06-16','2024-03-28',1),
('Natalia','Blasco Ferrer','natalia.blasco@email.com','600100019','Valencia','Valencia','España','1997-01-23','2024-04-05',1),
('Óscar','Domingo Soler','oscar.domingo@email.com','600100020','Castellón','Castellón','España','1975-08-31','2024-04-17',1),

('Beatriz','Campos Lara','beatriz.campos@email.com','600100021','Madrid','Madrid','España','1988-02-14','2024-05-02',1),
('Alejandro','Nieto Sanz','alejandro.nieto@email.com','600100022','Valencia','Valencia','España','1994-05-19','2024-05-20',1),
('Silvia','Pardo Roca','silvia.pardo@email.com','600100023','Alicante','Alicante','España','1980-12-03','2024-06-11',1),
('Iván','Fuentes Gil','ivan.fuentes@email.com','600100024','Murcia','Murcia','España','1999-03-15','2024-06-26',1),
('Noelia','Marcos Vidal','noelia.marcos@email.com','600100025','Valencia','Valencia','España','1992-10-27','2024-07-01',1),
('Adrián','Ramos Puig','adrian.ramos@email.com','600100026','Barcelona','Barcelona','España','1987-07-13','2024-07-17',1),
('Eva','Caballero León','eva.caballero@email.com','600100027','Madrid','Madrid','España','1995-06-29','2024-08-04',1),
('Víctor','Serrano Cano','victor.serrano@email.com','600100028','Valencia','Valencia','España','1983-01-18','2024-08-25',1),
('Isabel','Pascual Mora','isabel.pascual@email.com','600100029','Sevilla','Sevilla','España','1978-09-08','2024-09-10',1),
('Daniel','Giménez Pastor','daniel.gimenez@email.com','600100030','Alicante','Alicante','España','2000-04-21','2024-09-30',1),

('Marina','Torres Rico','marina.torres@email.com','600100031','Valencia','Valencia','España','1991-11-17','2024-10-15',1),
('Hugo','Vázquez Peña','hugo.vazquez@email.com','600100032','Madrid','Madrid','España','1985-05-06','2024-11-02',1),
('Alicia','Méndez Soto','alicia.mendez@email.com','600100033','Barcelona','Barcelona','España','1996-03-03','2024-11-21',1),
('Mario','Pastor Gil','mario.pastor@email.com','600100034','Valencia','Valencia','España','1989-08-26','2024-12-05',1),
('Teresa','Cano Ruiz','teresa.cano@email.com','600100035','Castellón','Castellón','España','1976-02-09','2024-12-20',1),
('Gonzalo','Soler Martí','gonzalo.soler@email.com','600100036','Madrid','Madrid','España','1993-12-12','2025-01-08',1),
('Lorena','Martín Vera','lorena.martin@email.com','600100037','Valencia','Valencia','España','1998-07-30','2025-01-25',1),
('Marcos','Gil Santos','marcos.gil@email.com','600100038','Alicante','Alicante','España','1984-10-20','2025-02-14',1),
('Clara','Vidal Sanz','clara.vidal@email.com','600100039','Valencia','Valencia','España','1990-01-05','2025-03-01',1),
('Jorge','Peña Serra','jorge.pena@email.com','600100040','Barcelona','Barcelona','España','1982-06-24','2025-03-19',1),

('Rocío','Lara Ferrer','rocio.lara@email.com','600100041','Sevilla','Sevilla','España','1997-04-16','2025-04-04',1),
('Fernando','Calvo Roca','fernando.calvo@email.com','600100042','Madrid','Madrid','España','1974-11-10','2025-04-22',1),
('Nuria','Sanz León','nuria.sanz@email.com','600100043','Valencia','Valencia','España','1988-09-02','2025-05-07',1),
('Álvaro','Puig Mora','alvaro.puig@email.com','600100044','Murcia','Murcia','España','1995-02-28','2025-05-25',1),
('Sonia','León Pastor','sonia.leon@email.com','600100045','Alicante','Alicante','España','1981-07-17','2025-06-09',1),
('Guillermo','Mora Gil','guillermo.mora@email.com','600100046','Valencia','Valencia','España','1992-05-11','2025-06-28',1),
('Irene','Pastor Cano','irene.pastor@email.com','600100047','Madrid','Madrid','España','1999-10-04','2025-07-13',1),
('Eduardo','Gil Vidal','eduardo.gil@email.com','600100048','Barcelona','Barcelona','España','1986-03-09','2025-08-01',1),
('Carmen','Vidal Torres','carmen.vidal@email.com','600100049','Valencia','Valencia','España','1979-12-27','2025-08-18',0),
('Roberto','Torres Ruiz','roberto.torres@email.com','600100050','Alicante','Alicante','España','1983-08-08','2025-09-05',0);


-- ============================================
-- PRODUCTOS
-- ============================================

INSERT INTO productos
(nombre, descripcion, precio, coste, stock, categoria_id, proveedor_id, fecha_alta, activo)
VALUES
('Portátil Basic 15','Portátil 15 pulgadas',599.99,410.00,34,1,1,'2023-01-10',1),
('Portátil Pro 14','Portátil profesional',1099.99,790.00,18,1,2,'2023-02-15',1),
('Portátil Gaming X','Portátil gaming RTX',1599.99,1180.00,9,1,5,'2023-03-11',1),
('PC Oficina i5','Ordenador oficina',649.99,440.00,27,1,7,'2023-04-01',1),
('PC Gaming RTX','Ordenador gaming',1899.99,1390.00,7,1,5,'2023-04-19',1),

('Monitor 22 FullHD','Monitor 22 pulgadas',129.99,78.00,65,2,3,'2023-01-20',1),
('Monitor 24 IPS','Monitor IPS 24 pulgadas',179.99,110.00,48,2,3,'2023-02-12',1),
('Monitor 27 QHD','Monitor QHD',299.99,190.00,31,2,4,'2023-03-21',1),
('Monitor 32 4K','Monitor UHD 4K',499.99,320.00,16,2,4,'2023-05-10',1),
('Monitor Gaming 165Hz','Monitor alta frecuencia',349.99,230.00,24,2,5,'2023-06-17',1),

('Teclado básico','Teclado USB',19.99,7.00,150,3,6,'2023-01-05',1),
('Teclado mecánico','Teclado mecánico RGB',89.99,45.00,72,3,6,'2023-02-07',1),
('Ratón óptico','Ratón USB',14.99,5.00,200,3,6,'2023-01-07',1),
('Ratón Gaming','Ratón gaming RGB',59.99,27.00,95,3,6,'2023-03-08',1),
('Webcam FullHD','Webcam 1080p',69.99,32.00,54,3,8,'2023-04-14',1),

('Intel Core i5','Procesador Intel',219.99,175.00,35,4,2,'2023-02-01',1),
('Intel Core i7','Procesador Intel',389.99,310.00,21,4,2,'2023-02-01',1),
('AMD Ryzen 5','Procesador AMD',199.99,150.00,40,4,4,'2023-02-20',1),
('AMD Ryzen 7','Procesador AMD',369.99,285.00,25,4,4,'2023-02-20',1),
('Memoria RAM 16GB','DDR4 16GB',69.99,38.00,110,4,6,'2023-03-02',1),
('Memoria RAM 32GB','DDR5 32GB',139.99,82.00,68,4,6,'2023-03-02',1),
('RTX 4060','Tarjeta gráfica',399.99,330.00,17,4,5,'2023-05-15',1),
('RTX 4070','Tarjeta gráfica',649.99,540.00,11,4,5,'2023-05-15',1),

('SSD 500GB','SSD SATA',49.99,29.00,140,5,6,'2023-01-12',1),
('SSD 1TB','SSD NVMe',89.99,52.00,125,5,6,'2023-02-11',1),
('SSD 2TB','SSD NVMe',169.99,105.00,63,5,6,'2023-03-19',1),
('HDD 2TB','Disco duro mecánico',74.99,45.00,80,5,8,'2023-01-24',1),
('HDD 4TB','Disco duro mecánico',119.99,73.00,45,5,8,'2023-04-02',1),

('Router WiFi 6','Router inalámbrico',129.99,74.00,38,6,9,'2023-02-13',1),
('Switch 8 puertos','Switch Gigabit',39.99,20.00,57,6,9,'2023-03-10',1),
('Switch 24 puertos','Switch profesional',179.99,105.00,19,6,9,'2023-04-15',1),
('Adaptador WiFi USB','Adaptador inalámbrico',24.99,11.00,96,6,6,'2023-05-21',1),

('Impresora Láser','Impresora láser monocromo',199.99,130.00,23,7,3,'2023-03-18',1),
('Impresora Color','Impresora multifunción',159.99,99.00,31,7,3,'2023-04-22',1),
('Tóner Negro','Tóner impresora',59.99,27.00,85,7,3,'2023-05-01',1),

('Auriculares Basic','Auriculares estéreo',29.99,12.00,130,8,6,'2023-01-14',1),
('Auriculares Gaming','Auriculares gaming',89.99,41.00,74,8,5,'2023-03-16',1),
('Micrófono USB','Micrófono condensador',99.99,49.00,42,8,8,'2023-04-13',1),
('Altavoces 2.1','Sistema altavoces',79.99,37.00,36,8,8,'2023-05-18',1),

('Smartphone Basic','Smartphone gama entrada',199.99,130.00,58,9,6,'2023-02-08',1),
('Smartphone Pro','Smartphone gama alta',899.99,650.00,22,9,6,'2023-03-09',1),
('Smartphone Ultra','Smartphone premium',1199.99,880.00,13,9,6,'2023-06-01',1),

('Tablet 10','Tablet 10 pulgadas',249.99,160.00,47,10,6,'2023-02-27',1),
('Tablet Pro','Tablet profesional',649.99,440.00,25,10,6,'2023-05-08',1),

('Mando Gaming','Mando inalámbrico',59.99,31.00,81,11,5,'2023-03-23',1),
('Volante Gaming','Volante con pedales',249.99,160.00,18,11,5,'2023-05-25',1),
('Silla Gaming','Silla ergonómica',229.99,125.00,14,11,7,'2023-06-19',1),

('Silla Oficina','Silla ergonómica oficina',189.99,100.00,29,12,7,'2023-04-03',1),
('Mesa Oficina','Mesa de trabajo',249.99,135.00,17,12,7,'2023-04-03',1),
('Lámpara LED','Lámpara escritorio',34.99,14.00,67,12,7,'2023-05-11',1);


-- ============================================
-- EMPLEADOS
-- Primero insertamos responsables
-- ============================================

INSERT INTO empleados
(nombre, apellidos, puesto, salario, departamento, ciudad, fecha_contratacion, jefe_id)
VALUES
('Antonio','García Mora','Director',5200,'Dirección','Valencia','2015-01-10',NULL),
('María','López Ruiz','Responsable Ventas',3200,'Ventas','Valencia','2017-03-15',1),
('Joaquín','Martínez Gil','Responsable Logística',3100,'Logística','Valencia','2018-05-22',1),
('Sandra','Pérez Cano','Responsable Administración',3300,'Administración','Madrid','2016-09-14',1);


INSERT INTO empleados
(nombre, apellidos, puesto, salario, departamento, ciudad, fecha_contratacion, jefe_id)
VALUES
('Luis','Torres Vidal','Comercial',2100,'Ventas','Valencia','2019-02-11',2),
('Nerea','Sanz Pérez','Comercial',2200,'Ventas','Madrid','2020-04-16',2),
('Andrés','Ruiz León','Comercial',2050,'Ventas','Alicante','2021-01-20',2),
('Paula','Gil Mora','Comercial',2300,'Ventas','Barcelona','2018-07-09',2),
('Ramón','Vega Cano','Almacén',1900,'Logística','Valencia','2020-11-12',3),
('Julia','Soler Rico','Almacén',1850,'Logística','Valencia','2022-02-14',3),
('Emilio','Pastor Serra','Transportista',1950,'Logística','Madrid','2019-08-21',3),
('Carla','Navarro Gil','Administrativa',2000,'Administración','Madrid','2021-06-07',4);


-- ============================================
-- ALMACENES
-- ============================================

INSERT INTO almacenes (nombre, ciudad, capacidad) VALUES
('Almacén Central Valencia','Valencia',50000),
('Almacén Madrid','Madrid',35000),
('Almacén Barcelona','Barcelona',30000),
('Almacén Alicante','Alicante',20000),
('Almacén Sevilla','Sevilla',18000);


-- ============================================
-- INVENTARIO
-- ============================================

INSERT INTO inventario (almacen_id, producto_id, cantidad)
SELECT
    1,
    id,
    FLOOR(10 + RAND() * 100)
FROM productos;

INSERT INTO inventario (almacen_id, producto_id, cantidad)
SELECT
    2,
    id,
    FLOOR(5 + RAND() * 70)
FROM productos;

INSERT INTO inventario (almacen_id, producto_id, cantidad)
SELECT
    3,
    id,
    FLOOR(5 + RAND() * 60)
FROM productos;

INSERT INTO inventario (almacen_id, producto_id, cantidad)
SELECT
    4,
    id,
    FLOOR(2 + RAND() * 40)
FROM productos;

INSERT INTO inventario (almacen_id, producto_id, cantidad)
SELECT
    5,
    id,
    FLOOR(2 + RAND() * 30)
FROM productos;


-- ============================================
-- PEDIDOS
-- ============================================

INSERT INTO pedidos
(cliente_id, empleado_id, fecha, estado, metodo_pago, gastos_envio, descuento)
VALUES
(1,5,'2024-01-05','Entregado','Tarjeta',4.99,0),
(2,6,'2024-01-08','Entregado','PayPal',0,10),
(3,5,'2024-01-12','Entregado','Tarjeta',4.99,0),
(4,7,'2024-01-20','Cancelado','Transferencia',0,0),
(5,8,'2024-02-02','Entregado','Tarjeta',0,20),
(6,6,'2024-02-14','Entregado','PayPal',4.99,0),
(7,5,'2024-02-21','Entregado','Tarjeta',0,5),
(8,7,'2024-03-01','Entregado','Transferencia',7.99,0),
(9,5,'2024-03-10','Entregado','Tarjeta',4.99,0),
(10,6,'2024-03-19','Devuelto','PayPal',0,0),

(11,8,'2024-04-02','Entregado','Tarjeta',0,15),
(12,6,'2024-04-11','Entregado','Transferencia',4.99,0),
(13,7,'2024-04-25','Entregado','Tarjeta',0,0),
(14,8,'2024-05-03','Entregado','PayPal',7.99,10),
(15,5,'2024-05-17','Entregado','Tarjeta',0,0),
(16,6,'2024-05-29','Cancelado','Transferencia',4.99,0),
(17,5,'2024-06-04','Entregado','Tarjeta',0,20),
(18,7,'2024-06-18','Entregado','PayPal',4.99,0),
(19,8,'2024-06-30','Entregado','Tarjeta',0,0),
(20,6,'2024-07-07','Entregado','Transferencia',7.99,0),

(21,5,'2024-07-18','Entregado','Tarjeta',0,5),
(22,7,'2024-08-02','Entregado','PayPal',4.99,0),
(23,8,'2024-08-15','Devuelto','Tarjeta',0,0),
(24,5,'2024-08-29','Entregado','Transferencia',4.99,10),
(25,6,'2024-09-05','Entregado','Tarjeta',0,0),
(26,7,'2024-09-17','Entregado','PayPal',7.99,0),
(27,8,'2024-10-01','Entregado','Tarjeta',0,25),
(28,5,'2024-10-14','Entregado','Transferencia',4.99,0),
(29,6,'2024-10-28','Entregado','Tarjeta',0,0),
(30,7,'2024-11-09','Cancelado','PayPal',0,0),

(31,8,'2024-11-21','Entregado','Tarjeta',4.99,0),
(32,5,'2024-12-03','Entregado','Transferencia',0,15),
(33,6,'2024-12-15','Entregado','Tarjeta',7.99,0),
(34,7,'2024-12-28','Entregado','PayPal',0,0),

(1,5,'2025-01-07','Entregado','Tarjeta',0,10),
(3,6,'2025-01-19','Entregado','PayPal',4.99,0),
(5,8,'2025-02-02','Entregado','Tarjeta',0,0),
(8,7,'2025-02-16','Entregado','Transferencia',7.99,0),
(11,5,'2025-03-01','Entregado','Tarjeta',0,5),
(15,6,'2025-03-18','Entregado','PayPal',4.99,0),

(19,8,'2025-04-04','Entregado','Tarjeta',0,20),
(22,5,'2025-04-21','Entregado','Transferencia',0,0),
(25,7,'2025-05-05','Entregado','Tarjeta',4.99,0),
(28,6,'2025-05-19','Devuelto','PayPal',0,0),
(31,8,'2025-06-03','Entregado','Tarjeta',7.99,10),
(35,5,'2025-06-22','Entregado','Transferencia',0,0),
(38,7,'2025-07-08','Entregado','Tarjeta',4.99,0),
(40,6,'2025-07-25','Entregado','PayPal',0,15),
(43,8,'2025-08-12','Entregado','Tarjeta',0,0),
(46,5,'2025-09-01','Pendiente','Transferencia',4.99,0),

(2,6,'2025-09-10','Entregado','Tarjeta',0,0),
(4,7,'2025-09-15','Entregado','PayPal',4.99,10),
(6,8,'2025-09-20','Pendiente','Tarjeta',0,0),
(9,5,'2025-09-25','Procesando','Transferencia',7.99,0);


-- ============================================
-- DETALLES DE PEDIDOS
-- ============================================

INSERT INTO detalles_pedido
(pedido_id, producto_id, cantidad, precio_unitario, descuento)
VALUES
(1,1,1,599.99,0),
(1,11,1,19.99,0),
(1,13,1,14.99,0),

(2,7,2,179.99,0),
(2,14,1,59.99,5),

(3,25,1,89.99,0),
(3,20,2,69.99,0),

(4,3,1,1599.99,0),

(5,41,1,899.99,5),
(5,36,1,29.99,0),

(6,16,1,219.99,0),
(6,20,2,69.99,0),

(7,29,1,129.99,0),
(7,32,2,24.99,0),

(8,33,1,199.99,0),
(8,35,2,59.99,0),

(9,12,1,89.99,0),
(9,14,1,59.99,0),

(10,43,1,249.99,0),

(11,22,1,399.99,0),
(11,17,1,389.99,0),

(12,6,2,129.99,0),
(12,15,1,69.99,0),

(13,24,2,49.99,0),
(13,25,1,89.99,0),

(14,37,1,89.99,0),
(14,38,1,99.99,0),

(15,2,1,1099.99,0),

(16,42,1,1199.99,0),

(17,8,2,299.99,5),
(17,12,2,89.99,0),

(18,45,2,59.99,0),
(18,46,1,249.99,0),

(19,48,1,189.99,0),
(19,49,1,249.99,0),

(20,21,1,139.99,0),
(20,25,2,89.99,0),

(21,4,1,649.99,0),
(21,11,2,19.99,0),

(22,9,1,499.99,0),

(23,40,1,199.99,0),
(23,36,2,29.99,0),

(24,30,2,39.99,0),
(24,29,1,129.99,0),

(25,18,1,199.99,0),
(25,20,2,69.99,0),

(26,34,1,159.99,0),
(26,35,2,59.99,0),

(27,3,1,1599.99,5),
(27,14,1,59.99,0),

(28,44,1,649.99,0),
(28,38,1,99.99,0),

(29,26,2,169.99,0),

(30,47,1,229.99,0),

(31,5,1,1899.99,0),
(31,10,1,349.99,0),

(32,31,1,179.99,0),
(32,30,2,39.99,0),

(33,23,1,649.99,0),
(33,21,1,139.99,0),

(34,39,1,79.99,0),
(34,37,1,89.99,0),

(35,1,1,599.99,0),
(35,15,1,69.99,0),

(36,25,2,89.99,0),
(36,20,1,69.99,0),

(37,41,1,899.99,0),

(38,46,1,249.99,0),
(38,45,2,59.99,0),

(39,7,2,179.99,0),
(39,11,2,19.99,0),

(40,17,1,389.99,0),
(40,22,1,399.99,0),

(41,43,2,249.99,0),

(42,33,1,199.99,0),
(42,35,1,59.99,0),

(43,2,1,1099.99,0),
(43,12,1,89.99,0),

(44,29,1,129.99,0),
(44,30,1,39.99,0),

(45,8,1,299.99,0),
(45,14,2,59.99,0),

(46,48,1,189.99,0),
(46,50,2,34.99,0),

(47,24,3,49.99,0),

(48,42,1,1199.99,0),
(48,36,1,29.99,0),

(49,10,1,349.99,0),
(49,37,1,89.99,0),

(50,4,1,649.99,0),
(50,6,1,129.99,0),

(51,19,1,369.99,0),
(51,21,1,139.99,0),

(52,27,2,74.99,0),

(53,44,1,649.99,0),
(53,38,1,99.99,0),

(54,5,1,1899.99,0),
(54,12,1,89.99,0);


-- ============================================
-- VALORACIONES
-- ============================================

INSERT INTO valoraciones
(cliente_id, producto_id, puntuacion, comentario, fecha)
VALUES
(1,1,5,'Muy buen portátil','2024-01-20'),
(2,7,4,'Buena calidad de imagen','2024-01-25'),
(3,25,5,'SSD muy rápido','2024-02-02'),
(5,41,4,'Buen teléfono','2024-02-19'),
(6,16,5,'Excelente procesador','2024-03-01'),
(7,29,4,'Buena cobertura WiFi','2024-03-12'),
(8,33,3,'Correcta pero algo ruidosa','2024-03-20'),
(9,12,5,'Excelente teclado','2024-04-01'),
(11,22,5,'Muy buen rendimiento','2024-04-18'),
(12,6,4,'Buena relación calidad precio','2024-05-01'),
(13,24,5,'Muy rápido','2024-05-15'),
(14,37,4,'Cómodos','2024-06-02'),
(15,2,5,'Perfecto para trabajar','2024-06-09'),
(17,8,4,'Buena resolución','2024-07-01'),
(18,46,5,'Muy divertido','2024-07-13'),
(19,48,4,'Silla cómoda','2024-07-21'),
(21,4,4,'Buen ordenador de oficina','2024-08-02'),
(22,9,5,'Excelente monitor','2024-08-19'),
(24,29,4,'Funciona perfectamente','2024-09-14'),
(25,18,5,'Gran procesador','2024-09-22'),
(27,3,5,'Potentísimo','2024-10-20'),
(28,44,4,'Buena tablet','2024-11-01'),
(29,26,5,'Muy buena capacidad','2024-11-17'),
(31,5,5,'Una bestia','2024-12-03'),
(32,31,4,'Buen switch','2024-12-20'),
(33,23,5,'Excelente gráfica','2025-01-08'),
(34,39,3,'Sonido correcto','2025-01-12'),
(1,15,4,'Webcam correcta','2025-01-25'),
(3,20,5,'RAM perfecta','2025-02-03'),
(5,41,5,'Sigue funcionando genial','2025-02-21'),
(8,46,4,'Buen volante','2025-03-02'),
(11,7,4,'Buen monitor','2025-03-21'),
(15,22,5,'Excelente GPU','2025-04-01'),
(19,43,4,'Tablet recomendable','2025-04-17'),
(22,33,4,'Impresora rápida','2025-05-02'),
(25,2,5,'Portátil excelente','2025-05-25'),
(31,8,5,'Muy buena imagen','2025-06-14'),
(35,48,4,'Cómoda para trabajar','2025-07-02'),
(38,24,5,'Buen SSD','2025-07-29'),
(40,42,4,'Teléfono excelente','2025-08-11');