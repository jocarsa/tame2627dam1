<?php
///////////////// Y LUEGO CARGO LA TABLA CORRESPONDIENTE AL BOTON QUE SE HA PULSADO ///////////////
          $resultado = $db->query("SELECT * FROM ".$_GET['tabla']);

          while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
          		echo '<tr>';
              foreach($fila as $clave=>$valor){
              	// Voy a comprobar si es una FK o no
                $tabla = $_GET['tabla'];					// Primero cojo la tabla
                $campo = $clave;									// Ahora cojo el campo
                
								// Y compruebo si es una clave externa o no
                $stmt = $db->prepare('SELECT * FROM pragma_foreign_key_list(:tabla) WHERE "from" = :campo');
                $stmt->bindValue(':tabla', $tabla, SQLITE3_TEXT);
                $stmt->bindValue(':campo', $campo, SQLITE3_TEXT);

                $resultado_fk = $stmt->execute();
                $fk = $resultado_fk->fetchArray(SQLITE3_ASSOC);
                if($fk){
                	// Si es una FK nos vamos a la otra tabla 
                   echo "<td>";
                   		$sub_resultado = $db->query("SELECT * FROM ".$fk['table']." WHERE id=".$fila['id']);
                      while ($sub_fila = $sub_resultado->fetchArray(SQLITE3_ASSOC)) {
                      	foreach($sub_fila as $sub_clave=>$sub_valor){
                        	echo $sub_valor." - ";
                        }
                      }
                   echo "</td>";
                }else{
                  // Y si no, te muestro el dato real
                  echo "<td>".$fila[$clave]."</td>";
                }
              }
              echo '</tr>';
          }
          ///////////////// Y LUEGO CARGO LA TABLA CORRESPONDIENTE AL BOTON QUE SE HA PULSADO ///////////////
?>