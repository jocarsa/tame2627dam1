<?php
  $conexion = new mysqli("localhost", "crud", "TAME123$", "crud");
  $resultado = $conexion->query("
  	INSERT INTO alumnos VALUES(
    	NULL,
      'a',
      'a',
      'a'
    )
  ");
  $conexion->close();
?>
ok