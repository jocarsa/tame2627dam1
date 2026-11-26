<?php
$db = new SQLite3('fototeca.db');

        $resultado = $db->query("SELECT * FROM fotos");

        while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {

          echo '
            <article data-categoria="'.htmlspecialchars($fila['categoria']).'">

              <img
                src="subidas/'.htmlspecialchars(rawurlencode($fila['nombre'])).'"
                alt="'.htmlspecialchars($fila['titulo']).'"
                loading="lazy"
              >

              <p>'.htmlspecialchars($fila['titulo']).'</p>

              <p>'.htmlspecialchars($fila['categoria']).'</p>

              <time>'.date("d/m/Y H:i:s", $fila['fecha']).'</time>

            </article>
          ';

        }

        $db->close();
?>