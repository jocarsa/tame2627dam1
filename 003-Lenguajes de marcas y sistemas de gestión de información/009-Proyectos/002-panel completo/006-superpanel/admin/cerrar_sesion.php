<?php
	session_start();									// Inicia la sesión
  
  session_destroy();								// Destruye la sesion
  
  header("Location:../index.php");	// Vete al login
?>