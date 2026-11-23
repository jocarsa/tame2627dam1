<?php
  $conexion = new mysqli("localhost", "crud", "TAME123$", "crud");

  $resultado = $conexion->query("SELECT * FROM alumnos");

  while ($fila = $resultado->fetch_assoc()) {
      // Sacalos por pantalla
      echo $fila["nombre"] . "<br>";
  }

  $conexion->close();
?>