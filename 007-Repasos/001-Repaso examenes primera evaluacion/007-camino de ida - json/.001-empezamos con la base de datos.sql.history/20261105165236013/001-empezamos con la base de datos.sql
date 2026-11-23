sudo mysql -u root -p

CREATE DATABASE blogexamen2627;
USE blogexamen2627;

CREATE TABLE noticias(
	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(100),
  fecha DATE,
  contenido TEXT
);

