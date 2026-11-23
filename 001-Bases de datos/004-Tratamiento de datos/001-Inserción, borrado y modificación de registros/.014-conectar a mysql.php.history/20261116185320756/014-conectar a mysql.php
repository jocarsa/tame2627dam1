<?php
// Creo una conexión a la base de datos
$conexion = new mysqli("localhost", "crud", "TAME123$", "crud");

// Ejecuto una petición sobre la base de datos
$resultado = $conexion->query("SELECT * FROM alumnos");

while ($fila = $resultado->fetch_assoc()) {
    echo $fila["nombre"] . "<br>";
}

$conexion->close();
?>