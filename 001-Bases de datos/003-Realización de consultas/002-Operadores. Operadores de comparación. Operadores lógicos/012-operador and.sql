SELECT 
nombre,
precio,
precio > 500 AS 'Caro',
stock,
stock < 10 AS 'Me quedan pocos',
precio*(precio > 500 AND stock < 10)*0.1 AS 'Descuento'
FROM productos;
