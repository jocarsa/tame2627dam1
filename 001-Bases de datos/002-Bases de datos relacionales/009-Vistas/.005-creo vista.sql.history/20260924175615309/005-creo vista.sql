CREATE VIEW vista_completa AS
SELECT 

pedidos.fecha AS 'fecha del pedido',
pedidos.numerodepedido AS 'numero de pedido',
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