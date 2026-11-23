sudo mysql -u root -p

CREATE DATABASE tienda2627;

USE tienda2627;

CREATE TABLE pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATE,
  cliente VARCHAR(100),
  importe DECIMAL(9,2)
);