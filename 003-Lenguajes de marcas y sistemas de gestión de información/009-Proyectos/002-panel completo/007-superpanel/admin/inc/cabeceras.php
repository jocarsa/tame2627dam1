<?php
	///////////////// VOY A CREAR LA CABECERA DE CUALQUIER TABLA ////////////////////////
          $resultado = $db->query("SELECT * FROM ".$_GET['tabla']." LIMIT 1");

          while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
          		echo '<tr>';
              foreach($fila as $clave=>$valor){
                echo "<th>".$clave."</th>";			// La clave es el nombre de la columna!!!
              }
              echo '</tr>';
          }
          ///////////////// VOY A CREAR LA CABECERA DE CUALQUIER TABLA ////////////////////////
?>