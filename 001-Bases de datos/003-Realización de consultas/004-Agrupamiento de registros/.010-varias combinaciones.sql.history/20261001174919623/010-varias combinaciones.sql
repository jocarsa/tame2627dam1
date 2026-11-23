SELECT 
anio,
ciudad,
COUNT(cliente) 
FROM pedidos2
GROUP BY anio,ciudad
ORDER BY anio ASC;