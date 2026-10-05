sudo mysql -u root -p

CREATE DATABASE programacion2627;

USE programacion2627;

CREATE TABLE alumnos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);

DESCRIBE alumnos;