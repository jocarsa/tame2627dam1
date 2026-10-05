SELECT 
anio,
COUNT(cliente) 
FROM pedidos2
GROUP BY anio;