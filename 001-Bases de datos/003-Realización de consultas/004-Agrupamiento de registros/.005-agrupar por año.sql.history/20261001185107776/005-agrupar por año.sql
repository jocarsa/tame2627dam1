sudo mysql -u root -p

CREATE DATABASE tienda2627;

USE tienda2627;

SELECT 
anio,
COUNT(cliente) 
FROM pedidos2
GROUP BY anio;