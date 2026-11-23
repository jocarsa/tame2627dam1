<?php
  // Voy a comprobar si es una FK o no
  $tabla = $_GET['tabla'];					// Primero cojo la tabla
  $campo = $clave;									// Ahora cojo el campo

  // Y compruebo si es una clave externa o no
  $stmt = $db->prepare('SELECT * FROM pragma_foreign_key_list(:tabla) WHERE "from" = :campo');
  $stmt->bindValue(':tabla', $tabla, SQLITE3_TEXT);
  $stmt->bindValue(':campo', $campo, SQLITE3_TEXT);

  $resultado_fk = $stmt->execute();
  $fk = $resultado_fk->fetchArray(SQLITE3_ASSOC);
?>