SELECT 
nombre AS 'Nombre del producto',
precio AS 'Base imponible',
precio * 0.21 AS 'IVA 21%',
precio + precio * 0.21 AS 'Total del producto'
FROM productos;