<?php
  $conexion = new mysqli("localhost", "crud", "TAME123$", "crud");
  $resultado = $conexion->query("SELECT * FROM alumnos");
  $conexion->close();
?>