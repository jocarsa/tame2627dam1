sudo mysql -u root -p

CREATE DATABASE tiendazapatillas;

USE tiendazapatillas;

CREATE TABLE productos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion VARCHAR(255),
  precio DECIMAL(4,2)
);