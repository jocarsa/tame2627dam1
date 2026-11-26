<?php
	
  // Primero recojo el formulario
  $usuario = $_POST['usuario'];
  $contrasena = $_POST['contrasena'];
  
  $db = new SQLite3('empresa.db');
  
?>