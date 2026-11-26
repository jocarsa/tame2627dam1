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
        include "navegacion.php";
        ?>
        </nav>
        <main>
        <table>
        <thead>
          <?php
          
          include "cabeceras.php";
          echo "</thead>";
          echo "<tbody>";
          
          include "supertabla.php";
					
          $db->close();

        ?>
        </tbody>
      </table>
    </main>
	</body>
</html>