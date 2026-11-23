<?php
  $conexion = new mysqli("localhost", "crud", "TAME123$", "crud");
  $resultado = $conexion->query("
  	INSERT INTO alumnos VALUES(
    	NULL,
      '".$_POST['nombre']."',
      '".$_POST['apellidos']."',
      '".$_POST['email']."'
    )
  ");
  $conexion->close();
?>
ok