<?php

$db = new SQLite3('empresa.db');

$resultado = $db->query("
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name
");

while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    echo $fila['name'] . "<br>";
}

$db->close();

?>