<?php

$db = new SQLite3('empresa.db');

$resultado = $db->query("SELECT * FROM ".$_GET['tabla']);

while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    foreach($fila as $clave=>$valor){
    	echo $fila[$clave]." - ";
    }
    echo "<hr>";
}

$db->close();

?>