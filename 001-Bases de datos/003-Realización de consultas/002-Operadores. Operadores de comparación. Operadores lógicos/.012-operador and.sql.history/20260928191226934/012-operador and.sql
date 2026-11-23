SELECT 
nombre,
precio,
precio > 500 AS 'Susceptible de descuento',
stock,
stock < 10 AS 'Me quedan pocos'
FROM productos;
