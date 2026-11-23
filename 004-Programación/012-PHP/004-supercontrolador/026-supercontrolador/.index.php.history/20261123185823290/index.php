<!doctype html>
<html>
	<head>
  	<link rel="stylesheet" href="estilo.css">
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