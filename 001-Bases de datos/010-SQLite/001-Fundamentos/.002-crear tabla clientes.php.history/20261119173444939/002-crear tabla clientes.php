<?php
	$db = new SQLite3('empresa.db');
  $db->exec("
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT,
            email TEXT,
            telefono TEXT,
            edad INTEGER
        )
    ");

    $db->close();
?>