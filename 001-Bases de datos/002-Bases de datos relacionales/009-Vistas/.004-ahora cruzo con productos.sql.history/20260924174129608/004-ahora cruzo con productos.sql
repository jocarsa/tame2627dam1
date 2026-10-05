SELECT 

pedidos.fecha,
pedidos.numerodepedido,
clientes.nombre,
clientes.apellidos

FROM pedidos
LEFT JOIN clientes
ON pedidos.cliente_id = clientes.Identificador
;