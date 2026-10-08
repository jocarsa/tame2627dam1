sudo mysql -u root -p

CREATE DATABASE blog2627;

USE blog2627;

CREATE TABLE entradas(
	id INT PRIMARY KEY AUTO INCREMENT,
  titulo VARCHAR(100),
  fecha DATE,
  contenido TEXT
);