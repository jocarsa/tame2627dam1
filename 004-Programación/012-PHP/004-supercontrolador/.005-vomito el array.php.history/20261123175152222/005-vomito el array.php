<?php

$db = new SQLite3('empresa.db');

$resultado = $db->query("SELECT * FROM clientes");

while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    var_dump($fila);
}

$db->close();

?>