sudo mysql -u root -p


USE tienda2627;

SELECT 
anio,
COUNT(ciudad) 
FROM pedidos2
GROUP BY ciudad;