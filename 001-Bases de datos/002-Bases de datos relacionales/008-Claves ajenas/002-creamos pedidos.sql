SHOW TABLES;

CREATE TABLE pedidos(
	fecha DATE,
  numerodepedido INT,
  cliente_id INT,
  producto_id INT
);

ALTER TABLE pedidos
ADD COLUMN Identificador INT AUTO_INCREMENT PRIMARY KEY;

SHOW TABLES;