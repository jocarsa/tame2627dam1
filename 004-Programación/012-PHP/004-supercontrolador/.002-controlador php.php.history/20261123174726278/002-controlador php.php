<?php

$db = new SQLite3('empresa.db');

$resultado = $db->query("SELECT * FROM productos");

while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    echo $fila['codigo']." - ".$fila['nombre']." - ".$fila['precio']."<br>";
}

// Cerrar conexión
$db->close();

?>