CREATE VIEW vista_completa AS
SELECT 

pedidos.fecha AS 'fecha del pedido',
pedidos.numerodepedido AS 'numero de pedido',
clientes.nombre AS 'nombre del cliente',
clientes.apellidos AS 'apellidos del cliente',
productos.nombre AS 'nombre del producto',
productos.precio

FROM pedidos
LEFT JOIN clientes
ON pedidos.cliente_id = clientes.Identificador
LEFT JOIN productos
ON pedidos.producto_id = productos.Identificador
;