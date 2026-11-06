sudo mysql -u root -p

CREATE DATABASE periodicodam2627;

USE periodicodam2627;

CREATE TABLE noticias(
	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(100),
  fecha DATE,
  texto TEXT,
  autor VARCHAR(100)
);