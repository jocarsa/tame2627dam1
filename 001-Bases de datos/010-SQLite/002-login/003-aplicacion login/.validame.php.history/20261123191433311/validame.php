<?php
	
  // Primero recojo el formulario
  $usuario = $_POST['usuario'];
  $contrasena = $_POST['contrasena'];
  
  if($usuario == "jocarsa" && $contrasena == "jocarsa"){
  	echo "pasas";
  }else{
  	echo "no pasas";
  }
  
?>