<?php

// Conectar a SQLite
$db = new SQLite3('empresa.db');

// Ejecutar SELECT
$resultado = $db->query("SELECT * FROM productos");

// Recorrer resultados
while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    echo "ID: " . $fila['id'] . "<br>";
    echo "Nombre: " . $fila['nombre'] . "<br>";
    echo "Precio: " . $fila['precio'] . " €<br>";
    echo "<hr>";
}

// Cerrar conexión
$db->close();

?>