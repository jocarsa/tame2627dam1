Yo te voy a procesar lo que viene

<?php
	var_dump($_POST);
  var_dump($_FILES);
  foreach($_FILES as $clave=>$valor){
  	echo $clave.": ".$valor."<br>";
  }
?>