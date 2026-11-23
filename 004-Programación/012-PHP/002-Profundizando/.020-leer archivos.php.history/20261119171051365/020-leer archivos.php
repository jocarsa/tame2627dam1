<?php
	$archivo = fopen('archivo.txt','r');
 	$contenido = fread($archivo,64);
  echo $contenido;
  fclose($archivo);
?>