<!doctype html>
<html>
	<head>
  	<style>
    	table{border:2px solid indigo;}
      table tr:nth-child(odd){background:lightblue;}
    </style>
  </head>
  <body>
    <table>
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
            <td>'.$fila['genero'].'</td>
            <td>'.$fila['capacidad_ml'].'</td>
            <td>'.$fila['precio'].'</td>
            <td>'.$fila['stock'].'</td>
            <td>'.$fila['fecha_creacion'].'</td>
          </tr>';
      }																				// Creo una tabla con los resultados

      $db->close();														// Ahora cierro la base de datos
    ?>
    </table>
  </body>
</html>