<?php
	/* GET coge cosas de la url y las baja a PHP
   GET es una de las formas de hacer input en PHP - los datos se ponen en la URL:
   
   009-pasar%20varios%20parametros.php?edad=48&nombre=Jose%20Vicente
   
   008-supervariable%20get.php = es el script
   ? = quiere decir que empezamos a enviar parámetros
   edad = 49 = clave y el valor del parámetro que hemos pasado
   & es el siguiente parametro que voy a pasar (encadenador)
   nombre = Jose Vicente = paso la segunda variable
   */
  
  
  $edad = $_GET['edad'];
  $nombre = $_GET['nombre'];
  
  echo "Tu edad es de ".$edad." años y tu nombre es: ".$nombre;
?>