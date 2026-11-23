<?php

$db = new SQLite3('empresa.db');

$resultado = $db->query("SELECT * FROM clientes");

while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    echo $fila['codigo']." - ".$fila['nombre']." - ".$fila['precio']."<br>";
}

$db->close();

?>