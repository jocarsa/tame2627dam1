sudo mysql -u root -p



SELECT 
anio,
COUNT(cliente) 
FROM pedidos2
GROUP BY anio;