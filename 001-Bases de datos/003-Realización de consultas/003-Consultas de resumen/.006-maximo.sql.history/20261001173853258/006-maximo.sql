SELECT 
cliente,
fecha,
MAX(importe) 
FROM pedidos
GROUP BY cliente;