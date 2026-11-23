<?php
	
  // Primero recojo el formulario
  $usuario = $_POST['usuario'];
  $contrasena = $_POST['contrasena'];
  
  $db = new SQLite3('empresa.db');
  
  $resultado = $db->query("
  	SELECT * FROM usuarios
    WHERE 
    usuario = '".$usuario."'
    AND
    contrasena = '".$contrasena."'
    LIMIT 1
    ;");
    
  if ($fila = $sub_resultado->fetchArray(SQLITE3_ASSOC)) {
    echo "pasas";
  }else{
  	echo "no pasas"
  }
  
  $db->close();
  
?>