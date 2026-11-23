<?php
// Creo una conexión a la base de datos
$conexion = new mysqli("localhost", "crud", "TAME123$", "crud");

// Ejecuto una petición sobre la base de datos
$resultado = $conexion->query("SELECT * FROM alumnos");

// Si la base de datos devuelve resultados
while ($fila = $resultado->fetch_assoc()) {
		// Sacalos por pantalla
    echo $fila["nombre"] . "<br>";
}

// Cuando hayas acabado, cierra la conexion
$conexion->close();
?>