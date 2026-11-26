<?php
	//////////////// PRIMERO COJO LAS TABLAS Y LAS CONVIERTO EN BOTONES /////////////////////
  $db = new SQLite3('empresa.db');
  $resultado = $db->query("
      SELECT name
      FROM sqlite_master
      WHERE type = 'table'
      ORDER BY name
  ");
  while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
      echo "<a href='?tabla=".$fila['name'] . "'>".$fila['name'] . "</a>";
  }
  ///////////////// Y LUEGO CARGO LA TABLA CORRESPONDIENTE AL BOTON QUE SE HA PULSADO ///////////////
  $resultado = $db->query("SELECT * FROM ".$_GET['tabla']);

  while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
      foreach($fila as $clave=>$valor){
        echo $fila[$clave]." - ";
      }
      echo "<hr>";
  }
  

  $db->close();

?>