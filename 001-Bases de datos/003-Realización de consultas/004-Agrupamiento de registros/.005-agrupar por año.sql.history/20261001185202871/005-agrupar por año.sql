sudo mysql -u root -p


USE tienda2627;

SELECT 
anio,
COUNT(cliente) 
FROM pedidos2
GROUP BY ciudad;