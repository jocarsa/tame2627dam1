<?php
	$archivo = fopen('archivo.txt','r');
 	$contenido = fread($archivo);
  echo $contenido;
  fclose($archivo);
?>