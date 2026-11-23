<!doctype html>
<html>
	<head>
  	<style>
    	html,body{width:100%;height:100%;padding:0px;margin:0px;}
      body{display:flex;}
      nav{background:indigo;flex:1;display:flex;flex-direction:column;padding:20px;}
      nav a{text-decoration:none;color:white;}
      main{flex:5;padding:20px;}
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
        <table border=1>
          <?php
          
          ///////////////// VOY A CREAR LA CABECERA DE CUALQUIER TABLA ///////////////
          $resultado = $db->query("SELECT * FROM ".$_GET['tabla']." LIMIT 1");

          while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
          		echo '<tr>';
              foreach($fila as $clave=>$valor){
                echo "<th>".$clave."</th>";			// La clave es el nombre de la columna!!!
              }
              echo '</tr>';
          }
          ///////////////// VOY A CREAR LA CABECERA DE CUALQUIER TABLA ///////////////
          
          
          ///////////////// Y LUEGO CARGO LA TABLA CORRESPONDIENTE AL BOTON QUE SE HA PULSADO ///////////////
          $resultado = $db->query("SELECT * FROM ".$_GET['tabla']);

          while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
          		echo '<tr>';
              foreach($fila as $clave=>$valor){
                echo "<td>".$fila[$clave]."</td>";
              }
              echo '</tr>';
          }
          ///////////////// Y LUEGO CARGO LA TABLA CORRESPONDIENTE AL BOTON QUE SE HA PULSADO ///////////////
					
          $db->close();

        ?>
      </table>
    </main>
	</body>
</html>