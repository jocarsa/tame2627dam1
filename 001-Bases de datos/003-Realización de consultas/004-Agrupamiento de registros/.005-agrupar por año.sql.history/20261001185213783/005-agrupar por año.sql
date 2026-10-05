sudo mysql -u root -p


USE tienda2627;

SELECT 
anio,
ciudad
COUNT(cliente) 
FROM pedidos2
GROUP BY ciudad;