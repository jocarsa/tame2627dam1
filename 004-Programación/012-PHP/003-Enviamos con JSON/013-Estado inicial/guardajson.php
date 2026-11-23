<?php
	// Primero recibe el JSON
  $json = $_GET['json']; // Estoy recibiendo el JSON por GET
  
  // Ahora abro un archivo en modo de escritura
  $archivo = fopen("json/".date('U').".json",'w');
  // en el archivo escribo el JSON
  fwrite($archivo,$json);
  // Y por ultimo cierro el archivo
  fclose($archivo);
  
?>