SELECT 
anio,
mes,
COUNT(cliente) 
FROM pedidos2
GROUP BY anio,mes;