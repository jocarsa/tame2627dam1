SELECT 
nombre AS 'Nombre del producto',
precio AS 'Base imponible',
precio > 500 AS 'Candidato'
FROM productos;