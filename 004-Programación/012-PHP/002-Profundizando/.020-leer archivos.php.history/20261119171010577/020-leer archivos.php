<?php
	$archivo = fopen('archivo.txt','r');
 	$contenido = fread($achivo);
  echo $contenido;
  fclose($archivo);
?>