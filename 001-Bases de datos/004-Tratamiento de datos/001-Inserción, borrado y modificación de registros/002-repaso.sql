sudo mysql -u root p

CREATE DATABASE crud;
USE crud;

CREATE TABLE alumnos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);