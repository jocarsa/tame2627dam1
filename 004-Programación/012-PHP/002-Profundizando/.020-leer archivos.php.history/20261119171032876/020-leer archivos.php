<?php
	$archivo = fopen('archivo.txt','r');
 	$contenido = fread($archivo,2048);
  echo $contenido;
  fclose($archivo);
?>