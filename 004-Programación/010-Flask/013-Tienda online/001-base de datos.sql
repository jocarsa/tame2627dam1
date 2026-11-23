sudo mysql -u root -p

CREATE DATABASE tiendaonlinedamtame2627;

USE tiendaonlinedamtame2627;

CREATE TABLE productos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion VARCHAR(100),
  precio DECIMAL(6,2)
);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Balón de fútbol Adidas', 'Balón de fútbol tamaño 5', 29.99),
('Balón de baloncesto Nike', 'Balón de baloncesto de cuero sintético', 34.50),
('Raqueta de tenis Wilson', 'Raqueta de tenis para principiantes', 89.99),
('Zapatillas running Asics', 'Zapatillas ligeras para correr', 119.95),
('Mancuernas 5 kg', 'Juego de dos mancuernas de 5 kg', 39.99),
('Esterilla de yoga', 'Esterilla antideslizante de 6 mm', 19.95),
('Bicicleta de montaña', 'Bicicleta MTB de 21 velocidades', 499.00),
('Casco de ciclismo', 'Casco ligero con ventilación', 45.90),
('Guantes de boxeo', 'Guantes de entrenamiento de 12 oz', 49.99),
('Cuerda para saltar', 'Comba ajustable para entrenamiento', 12.50),
('Gafas de natación', 'Gafas con protección antivaho', 18.95),
('Aletas de natación', 'Aletas cortas para entrenamiento', 32.00),
('Mochila deportiva', 'Mochila de 30 litros impermeable', 44.95),
('Balón de voleibol', 'Balón oficial de voleibol', 27.99),
('Patines en línea', 'Patines ajustables con ruedas de 80 mm', 129.00),
('Tabla de skate', 'Monopatín de madera de arce', 79.95),
('Banda elástica', 'Banda de resistencia para ejercicios', 14.99),
('Pesa rusa 12 kg', 'Kettlebell de hierro fundido', 54.90),
('Red de bádminton', 'Red portátil con soportes', 39.50),
('Reloj deportivo', 'Reloj con cronómetro y pulsómetro', 159.99);


SELECT * FROM productos;

CREATE USER 'tiendaonlinedamtame2627'@'localhost' IDENTIFIED BY 'TAME123$';

GRANT USAGE ON *.* TO 'tiendaonlinedamtame2627'@'localhost';

ALTER USER 'tiendaonlinedamtame2627'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;


GRANT ALL PRIVILEGES ON tiendaonlinedamtame2627.* 
TO 'tiendaonlinedamtame2627'@'localhost';

FLUSH PRIVILEGES;

EXIT;