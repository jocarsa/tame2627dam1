sudo mysql -u root -p



SELECT 
COUNT(anio),
ciudad
FROM pedidos2
GROUP BY ciudad;