Concesionario de coches

-Coche
	-Modelo - string
  -Marca - string
  -Año - int
  -Matrícula - string
  -Número de bastidor - string
  -Color - string
  -Precio - float
 
-Clientes
	-Nombre
  -Apellidos
  -DNI 1:1
  -Fecha de nacimiento 1:1
  -Número de teléfono 1:n
  -Coreo electrónico 1:n

-Pedidos
	-Numero de pedido
  -Fecha de pedido
  -Id cliente FK
  -Id Coche FK