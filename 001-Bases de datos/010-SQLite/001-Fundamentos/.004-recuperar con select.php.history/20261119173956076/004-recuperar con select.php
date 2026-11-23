<?php
	$db = new SQLite3('empresa.db');										// Abro la base de datos
  
  $resultado = $db->query("SELECT * FROM clientes");	// Petición a la base de datos

  while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
      echo $fila['nombre'];
      echo "-";
      echo $fila['apellidos'];
      echo "<br>";
  }
  

  $db->close();
?>