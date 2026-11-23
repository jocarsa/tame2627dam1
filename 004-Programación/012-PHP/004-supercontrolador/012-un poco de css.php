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
        ?>
        </nav>
        <main>
        <?php
        ///////////////// Y LUEGO CARGO LA TABLA CORRESPONDIENTE AL BOTON QUE SE HA PULSADO ///////////////
        $resultado = $db->query("SELECT * FROM ".$_GET['tabla']);

        while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
            foreach($fila as $clave=>$valor){
              echo $fila[$clave]." - ";
            }
            echo "<hr>";
        }

        $db->close();

      ?>
    </main>
	</body>
</html>