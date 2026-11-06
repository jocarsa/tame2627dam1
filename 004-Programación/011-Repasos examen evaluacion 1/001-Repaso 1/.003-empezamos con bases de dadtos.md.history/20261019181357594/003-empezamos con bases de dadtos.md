sudo mysql -u root -p
CREATE DATABASE tiendaexamen;
USE tiendaexamen;

CREATE TABLE productos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion TEXT,
  precio DECIMAL(6,2)
);