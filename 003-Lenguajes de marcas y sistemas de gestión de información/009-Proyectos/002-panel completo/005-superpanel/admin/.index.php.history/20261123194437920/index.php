<?php 
session_start();
// Vamos a comprobar si alguien se intenta colar

?>
<?php $db = new SQLite3('../db/empresa.db'); ?>
<!doctype html>
<html>
	<head>
  	<link rel="stylesheet" href="estilo/estilo.css">
  </head>
  <body>
  	<nav>
      <?php
        include "inc/navegacion.php";
      ?>
    </nav>
    <main>
      <table>
        <thead>
          <?php  include "inc/cabeceras.php"; ?>
        </thead>
        <tbody>
          <?php include "inc/supertabla.php"; ?>
        </tbody>
      </table>
    </main>
	</body>
</html>
<?php $db->close(); ?>