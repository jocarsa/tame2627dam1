SELECT 
nombre,
precio,
precio > 500 AS 'Susceptible de descuento',
stock,
stock < 10 AS 'Me quedan pocos',
precio > 500 AND stock < 10 AS 'Vale te aplico el descuento'
FROM productos;
