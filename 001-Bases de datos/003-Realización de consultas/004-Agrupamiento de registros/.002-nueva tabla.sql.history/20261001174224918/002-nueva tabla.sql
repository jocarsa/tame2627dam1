CREATE TABLE pedidos2(
	id INT PRIMARY KEY AUTO_INCREMENT,
  anio INT,
  mes INT,
  dia INT,
  cliente VARCHAR(100),
  importe DECIMAL(6,2),
  ciudad VARCHAR(100)
);