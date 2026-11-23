sudo mysql -u root -p

CREATE DATABASE logintame;
USE logintame;

CREATE DATABASE usuarios(
	if INT PRIMARY KEY AUTO_INCREMENT,
  usuario VARCHAR(100),
  contrasena VARCHAR(100)
);

INSERT INTO usuarios VALUES(
	NULL,
  'jocarsa',
  'jocarsatame'
);