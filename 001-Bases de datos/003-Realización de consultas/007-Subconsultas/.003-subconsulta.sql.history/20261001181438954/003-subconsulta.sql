SELECT
pedidos.fecha,
pedidos.cliente,
pedidos.importe
porencima > (
	SELECT AVG(importe) FROM pedidos
)
FROM pedidos;