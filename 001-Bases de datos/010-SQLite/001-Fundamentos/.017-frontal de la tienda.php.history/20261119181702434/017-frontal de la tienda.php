<!doctype html>
<html>
	<head>
  	<style>
    	body{background:grey;}
    </style>
  </head>
  <body>
    <header>
    	<h1>Tienda de perfumes</h1>
    </header>
    <main>
    	<?php
      	// Devuelve los productos que hay en la base de datos /////////////////////////////
        $db = new SQLite3('tienda.db');						// Abro la base de datos
        $peticion = "SELECT * FROM productos";		// Lo que le pido a la base de datos
        $resultado = $db->query($peticion);				// Petición a la base de datos
        while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
            echo '<article>
              '.$fila['nombre'].'
            </article>';
        }																				// Creo una tabla con los resultados
        $db->close();														// Ahora cierro la base de datos
        // Devuelve los productos que hay en la base de datos /////////////////////////////
      ?>
    </main>
    <footer>
    </footer>
  </body>
</html>