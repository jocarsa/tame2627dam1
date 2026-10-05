sudo mysql -u root -p

CREATE DATABASE centrodeformacion2627;

USE centrodeformacion2627;

CREATE TABLE alumnos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);

CREATE TABLE asignaturas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  horas INT,
  codigo VARCHAR(100)
);

CREATE TABLE matriculas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  fecha DATE,
  alumnos_id INT,
  asignaturas_id INT
);