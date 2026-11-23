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
      <thead>
        <tr>
          <th>nombre</th>
          <th>marca</th>
          <th>descripcion</th>
          <th>categoria</th>
          <th>genero</th>
          <th>capacidad_ml</th>
          <th>precio</th>
          <th>stock</th>
          <th>fecha_creacion</th>
          <th>Acciones</th>
        </tr>
        <tr>
        	<form action="?" method="POST">
            <th><input type="text" name="nombre"></th>
            <th><input type="text" name="marca"></th>
            <th><input type="text" name="descripcion"></th>
            <th><input type="text" name="categoria"></th>
            <th><input type="text" name="genero"></th>
            <th><input type="text" name="capacidad_ml"></th>
            <th><input type="text" name="precio"></th>
            <th><input type="text" name="stock"></th>
            <th><input type="text" name="fecha_creacion"></th>
            <th>Acciones</th>
          </form>
        </tr>
      </thead>
      <tbody>
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
              <td><button>Borrar</button></td>
            </tr>';
        }																				// Creo una tabla con los resultados

        $db->close();														// Ahora cierro la base de datos
      ?>
      </tbody>
    </table>
  </body>
</html>