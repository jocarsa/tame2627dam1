<?php
	//////////////// PRIMERO COJO LAS TABLAS Y LAS CONVIERTO EN BOTONES /////////////////////

  $resultado = $db->query("
  SELECT name
  FROM sqlite_master
  WHERE type = 'table'
  ORDER BY name
  ");
  while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
  	echo "<a href='?tabla=".$fila['name'] . "'";
    if($fila['name'] == $_GET['tabla']){
    	echo " class='activo' ";					// Marca la tabla que esté activa
    }
    echo ">".$fila['name'] . "</a>";
  }
  //////////////// PRIMERO COJO LAS TABLAS Y LAS CONVIERTO EN BOTONES /////////////////////
?>