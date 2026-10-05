sudo mysql -u root -p


USE tienda2627;

SELECT 
COUNT(ciudad),
ciudad
FROM pedidos2
GROUP BY ciudad;