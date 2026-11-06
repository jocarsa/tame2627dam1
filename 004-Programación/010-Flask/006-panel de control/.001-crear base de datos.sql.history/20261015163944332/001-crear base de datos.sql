sudo mysql -u root -p

CREATE DATABASE tiendaonlinetame;

USE tiendaonlinetame;

CREATE TABLE productos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion TEXT,
  imagen VARCHAR(100)
);