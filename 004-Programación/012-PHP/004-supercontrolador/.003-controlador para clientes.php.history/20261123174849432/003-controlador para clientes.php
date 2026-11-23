<?php

$db = new SQLite3('empresa.db');

$resultado = $db->query("SELECT * FROM clientes");

while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    echo $fila['nombre']." - ".$fila['apellidos']." - ".$fila['email']." - ".$fila['telefono']."<br>";
}

$db->close();

?>