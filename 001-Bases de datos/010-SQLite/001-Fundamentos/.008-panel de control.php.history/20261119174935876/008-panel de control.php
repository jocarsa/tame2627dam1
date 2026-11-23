<?php
	$db = new SQLite3('tienda.db');						// Abro la base de datos
  $peticion = "SELECT * FROM productos";		// Lo que le pido a la base de datos
  
  $resultado = $db->query($peticion);				// Petición a la base de datos

  while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
      echo $fila['nombre'];
      echo "-";
      echo $fila['apellidos'];
      echo "<br>";
  }	

  $db->close();														// Ahora cierro la base de datos
?>