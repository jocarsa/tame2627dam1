<?php
  ///////////////// Y LUEGO CARGO LA TABLA CORRESPONDIENTE AL BOTON QUE SE HA PULSADO ///////////////
    $resultado = $db->query("SELECT * FROM ".$_GET['tabla']);

    while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
    	echo '<tr>';
    foreach($fila as $clave=>$valor){
    	include "comprobarfk.php";
    	if($fk){
        // Si es una FK nos vamos a la otra tabla 
        echo "<td>";
        include "subtabla.php";
        echo "</td>";
    	}else{
    		// Y si no, te muestro el dato real
   		 echo "<td>".$fila[$clave]."</td>";
    	}
    }
    echo '</tr>';
    }
  ///////////////// Y LUEGO CARGO LA TABLA CORRESPONDIENTE AL BOTON QUE SE HA PULSADO ///////////////
?>