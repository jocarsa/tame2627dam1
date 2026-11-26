<!doctype html>
<html>
	<head>
  	<style>
    	html,body{width:100%;height:100%;padding:0px;margin:0px;font-family:ubuntu,sans-serif;}
      body{display:flex;}
      nav{background:indigo;flex:1;display:flex;flex-direction:column;gap:10px;padding:20px;}
      nav a{text-decoration:none;color:white;}
      main{flex:5;padding:20px;}
      main table{width:100%;}
      main table thead{background:indigo;color:white;}
      main table tbody tr:nth-child(odd){background:aliceblue;}
    </style>
  </head>
  <body>
  	<nav>
      <?php
        $db = new SQLite3('empresa.db');

        //////////////// PRIMERO COJO LAS TABLAS Y LAS CONVIERTO EN BOTONES /////////////////////

          $resultado = $db->query("
              SELECT name
              FROM sqlite_master
              WHERE type = 'table'
              ORDER BY name
          ");
          while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
              echo "<a href='?tabla=".$fila['name'] . "'>".$fila['name'] . "</a>";
          }
        //////////////// PRIMERO COJO LAS TABLAS Y LAS CONVIERTO EN BOTONES /////////////////////
        ?>
        </nav>
        <main>
        <table>
        <thead>
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
          echo "</thead>";
          echo "<tbody>";
          
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
					
          $db->close();

        ?>
        </tbody>
      </table>
    </main>
	</body>
</html>