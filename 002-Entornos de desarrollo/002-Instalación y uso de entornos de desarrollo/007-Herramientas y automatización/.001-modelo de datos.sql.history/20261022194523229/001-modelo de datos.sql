Contacto
-nombre
-apellidos
-móvil
-email
-empresa
-cateogoría
-ciudad

sudo mysql -u root -p

CREATE DATABASE javaagenda;

USE javaagenda;

CREATE TABLE contacto(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  movil VARCHAR(100),
  email VARCHAR(100),
  empresa VARCHAR(100),
  categoria VARCHAR(100),
  ciudad VARCHAR(100)
);