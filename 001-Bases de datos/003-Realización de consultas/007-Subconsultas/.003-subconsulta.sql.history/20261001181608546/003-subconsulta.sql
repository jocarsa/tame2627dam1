SELECT
pedidos.fecha,
pedidos.cliente,
pedidos.importe
pedidos.importe > (
	SELECT AVG(importe) FROM pedidos
) AS porencima
FROM pedidos;