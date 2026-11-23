<table border=1>
<?php
	$db = new SQLite3('tienda.db');						// Abro la base de datos
  $peticion = "SELECT * FROM productos";		// Lo que le pido a la base de datos
  
  $resultado = $db->query($peticion);				// Petición a la base de datos

  while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
      echo '<tr>
      	<td>'.$fila['nombre'].'</td>
        <td>'.$fila['marca'].'</td>
        <td>'.$fila['descripcion'].'</td>
        <td>'.$fila['categoria'].'</td>
      </tr>'
  }																				// Creo una tabla con los resultados

  $db->close();														// Ahora cierro la base de datos
?>
</table>