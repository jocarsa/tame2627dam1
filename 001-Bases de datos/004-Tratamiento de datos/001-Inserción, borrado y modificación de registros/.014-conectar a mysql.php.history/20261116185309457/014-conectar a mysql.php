<?php
// Creo una conexión a la base de datos
$conexion = new mysqli("localhost", "crud", "TAME123$", "crud");

$resultado = $conexion->query("SELECT * FROM alumnos");

while ($fila = $resultado->fetch_assoc()) {
    echo $fila["nombre"] . "<br>";
}

$conexion->close();
?>