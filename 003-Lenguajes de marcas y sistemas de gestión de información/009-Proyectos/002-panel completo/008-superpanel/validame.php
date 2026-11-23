<?php
	session_start();
  // Primero recojo el formulario
  $usuario = $_POST['usuario'];
  $contrasena = $_POST['contrasena'];
  
  $db = new SQLite3('db/empresa.db');
  
  $resultado = $db->query("
  	SELECT * FROM usuarios
    WHERE 
    usuario = '".$usuario."'
    AND
    contrasena = '".$contrasena."'
    LIMIT 1
    ;");
    
  if ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
  	$_SESSION['usuario'] = $fila['usuario'];
    header("Location:admin/index.php");	// Nos vamos al admin
  }else{
  	header("Location:index.php");				// Volvemos al login
  }
  
  $db->close();
  
?>