SELECT 
ciudad,
COUNT(cliente) 
FROM pedidos2
GROUP BY ciudad
ORDER BY COUNT(cliente) DESC;