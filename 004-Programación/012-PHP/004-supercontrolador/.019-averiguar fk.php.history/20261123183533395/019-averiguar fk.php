<?php
$db = new SQLite3("empresa.db");

$tabla = "inventario";

$resultado = $db->query("PRAGMA foreign_key_list('$tabla')");

while ($fk = $resultado->fetchArray(SQLITE3_ASSOC)) {
    echo "Campo: " . $fk['from'] . "<br>";
    echo "Tabla referenciada: " . $fk['table'] . "<br>";
    echo "Campo referenciado: " . $fk['to'] . "<br>";
    echo "<hr>";
}
?>