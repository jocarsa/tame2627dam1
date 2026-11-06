3 exámenes que van en pack: bases de datos, lenguajes de marcas, programación.

Yo llegaré al examen, y diré:
Tenéis que hacer un ejercicio sobre [ejemplo: tienda online: entidad: producto, campos: id, nombre, descripcion, precio]

- Bases de datos
	- Entráis en MySQL
  - Creáis una base de datos
  - Usáis la base de datos
  - Creáis la tabla correspondiente a la entidad que yo haya dicho
  - Insertáis datos de ejemplo (para esta parte concreta se puede usar IA)
  - Seleccionáis para comprobar que está ok
  - Creáis un usuario con permisos para poder conectaros desde Python
  
- Programación
	- Os aseguráis de que leeís los datos desde MySQL (mysql.connector)
  - Los imprimis en consola
  - Ahora usáis flask
  - Podéis elegir dos caminos para el camino de vuelta:
  	- Camino fácil: Pintar la plantilla mediante Flask y Jinja= render_template + {{}}
    - Camino no tan fácil: Dos endpoints, uno para plantilla, otro para JSON, y la plantilla carga datos con JSON y los pinta en HTML
  - Ahora en el camino de ida, podéis elegir también dos caminos:
  	- Camino fácil: Enviar la información mediante formularios HTML, usando request, usando methods=['POST']
    - Camino no tan fácil: Dos endpoints, uno para el "formulario", y otro para recibir datos de inserción  mediante JSON y fetch
  - En el examen de programación simplemente os aseguráis que podéis
  	- Leer de base de datos y escribir en la base de datos
    - Levantar endpoints y enviar y recibir información de lenguaje de marcas
    
    
    
    
    
    
  