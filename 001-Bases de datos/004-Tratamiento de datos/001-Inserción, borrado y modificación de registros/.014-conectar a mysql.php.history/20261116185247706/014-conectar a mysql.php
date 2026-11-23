<?php
$conexion = new mysqli("localhost", "root", "", "mibasededatos");

$resultado = $conexion->query("SELECT * FROM alumnos");

while ($fila = $resultado->fetch_assoc()) {
    echo $fila["nombre"] . "<br>";
}

$conexion->close();
?>