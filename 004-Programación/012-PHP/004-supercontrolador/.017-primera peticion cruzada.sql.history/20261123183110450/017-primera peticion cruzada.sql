SELECT 

productos.nombre as producto,
almacen_id as almacen,
cantidad as cantidad,
stock_minimo as stock

FROM inventario

LEFT JOIN productos ON inventario.producto_id = productos.id
;