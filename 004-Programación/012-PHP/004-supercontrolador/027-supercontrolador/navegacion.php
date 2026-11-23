<?php
	//////////////// PRIMERO COJO LAS TABLAS Y LAS CONVIERTO EN BOTONES /////////////////////

  $resultado = $db->query("
  SELECT name
  FROM sqlite_master
  WHERE type = 'table'
  ORDER BY name
  ");
  while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
  echo "<a href='?tabla=".$fila['name'] . "'>".$fila['name'] . "</a>";
  }
  //////////////// PRIMERO COJO LAS TABLAS Y LAS CONVIERTO EN BOTONES /////////////////////
?>