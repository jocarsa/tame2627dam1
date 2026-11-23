<?php
	$archivo = fopen('archivo.txt','w');
 	fwrite($archivo,"esto es un contenido que te pongo en PHP");
  fclose($archivo);
?>