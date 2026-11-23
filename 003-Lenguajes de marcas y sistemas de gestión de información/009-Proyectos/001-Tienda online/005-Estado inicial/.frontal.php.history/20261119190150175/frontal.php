<!doctype html>
<html>
	<head>
  	<style>
    	*{padding:0px;margin:0px;}
    	body{background:grey;font-family:ubuntu,sans-serif;}
      header,main,footer{background:white;padding:40px;margin:auto;width:800px;}
      main{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
      main article img{width:100%;height:200px;background:grey;border-radius:10px;}
      main article button{background:indigo;color:white;padding:5px;border-radius:5px;}
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
            	<img src="producto.png">
              <h4>'.$fila['nombre'].'</h4>
              <p>'.$fila['descripcion'].'</p>
              <button>'.$fila['precio'].' €</button>
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