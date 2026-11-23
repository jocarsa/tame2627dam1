sudo mysql -u root -p

CREATE DATABASE tiendaonlinedamtame2627;

USE tiendaonlinedamtame2627;

CREATE TABLE productos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion VARCHAR(100),
  precio DECIMAL(6,2)
);

