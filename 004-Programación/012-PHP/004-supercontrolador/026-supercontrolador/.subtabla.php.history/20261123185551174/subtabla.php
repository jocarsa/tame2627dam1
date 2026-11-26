<?php
	$sub_resultado = $db->query("SELECT * FROM ".$fk['table']." WHERE id=".$fila['id']);
                      while ($sub_fila = $sub_resultado->fetchArray(SQLITE3_ASSOC)) {
                      	foreach($sub_fila as $sub_clave=>$sub_valor){
                        	echo $sub_valor." - ";
                        }
                      }
?>