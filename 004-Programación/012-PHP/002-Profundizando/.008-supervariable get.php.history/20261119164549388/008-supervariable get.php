<?php
	/* GET coge cosas de la url y las baja a PHP
   GET es una de las formas de hacer input en PHP - los datos se ponen en la URL:
   008-supervariable%20get.php?edad=49
   008-supervariable%20get.php = es el script
   ? = quiere decir que empezamos a enviar parámetros
   edad = 49 = clave y el valor del parámetro que hemos pasado
   */
  
  
  $edad = $_GET['edad'];
  
  echo "Tu edad es de ".$edad." años";
?>