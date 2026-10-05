SELECT 

pedidos.fecha,
pedidos.numerodepedido,
clientes.nombre,
clientes.apellidos,
productos.nombre,
productos.precio

FROM pedidos
LEFT JOIN clientes
ON pedidos.cliente_id = clientes.Identificador
LEFT JOIN productos
ON pedidos.producto_id = productos.Identificador
;