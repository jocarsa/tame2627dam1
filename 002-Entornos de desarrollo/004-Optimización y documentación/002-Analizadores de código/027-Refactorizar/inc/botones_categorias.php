<?php
	$db = new SQLite3('fototeca.db');

          $resultado = $db->query("
            SELECT DISTINCT categoria
            FROM fotos
            ORDER BY categoria
          ");

          while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {

            echo '
              <button
                type="button"
                data-categoria="'.htmlspecialchars($fila['categoria']).'"
              >
                '.htmlspecialchars($fila['categoria']).'
              </button>
            ';

          }

          $db->close();
?>