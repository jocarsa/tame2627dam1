<?php $db = new SQLite3('../db/empresa.db'); ?>
<!doctype html>
<html>
	<head>
  	<link rel="stylesheet" href="estilo.css">
  </head>
  <body>
  	<nav>
      <?php
        include "navegacion.php";
      ?>
    </nav>
    <main>
      <table>
        <thead>
          <?php  include "cabeceras.php"; ?>
        </thead>
        <tbody>
          <?php include "supertabla.php"; ?>
        </tbody>
      </table>
    </main>
	</body>
</html>
<?php $db->close(); ?>