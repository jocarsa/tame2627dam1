<?php
	// Ahora voy a borrar si acaso es cierto que debo borrar //////////////////////////////
  	if(isset($_GET['operacion']) && $_GET['operacion'] == "borrar"){	// Solo si borro
    	$db = new SQLite3('tienda.db');										// Abro la base de datos
      $db->exec("
        DELETE FROM productos
        WHERE id = '".$_GET['id']."';
      ");																								// Borro el elemento de la base de datos que tenga ese id
      $db->close();																				// Ahora cierro la base de datos
    }
  // Ahora voy a borrar si acaso es cierto que debo borrar //////////////////////////////
  
	// Realmente inserto un producto nuevo en la base de dato si corresponde //////////////
  	if(isset($_POST['nombre'])){												// Si viene el formulario por POST
    	$db = new SQLite3('tienda.db');										// Abro la base de datos
    	$db->exec("
        INSERT INTO productos VALUES(
        	NULL,
          '".$_POST['nombre']."',
          '".$_POST['marca']."',
          '".$_POST['descripcion']."',
          '".$_POST['categoria']."',
          '".$_POST['genero']."',
          '".$_POST['capacidad_ml']."',
          '".$_POST['precio']."',
          '".$_POST['stock']."',
          '".$_POST['fecha_creacion']."'
        );
    ");
    $db->close();																				// Ahora cierro la base de datos
    }
  // Realmente inserto un producto nuevo en la base de dato si corresponde //////////////
?>
<!doctype html>
<html>
	<head>
  	<style>
    	html,body{padding:0px;margin:0px;width:100%;height:100%;font-family:ubuntu,sans-serif;}
    	body{display:flex;}
      nav{background:indigo;flex:1;padding:20px;display:flex;flex-direction:column;gap:10px;}
      nav a{text-decoration:none;color:indigo;background:white;padding:10px;}
      main{background:white;flex:5;padding:20px;overflow:scroll;}
    	table{border:2px solid indigo;}
      table tr:nth-child(odd){background:lightgray;}
      table td{padding:5px;font-size:10px;min-width:50px;}
      table input{width:100%;}
    </style>
  </head>
  <body>
  	<nav>
    	<a>Productos</a>
      <a>Clientes</a>
      <a>Pedidos</a>
      <a>Registros</a>
      <a>Tramites</a>
    </nav>
    <main>
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
            <th><input type="submit"></th>
          </form>
        </tr>
      </thead>
      <tbody>
      <?php
      	// Devuelve los productos que hay en la base de datos /////////////////////////////
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
              <td><a href="?operacion=borrar&id='.$fila['id'].'">Borrar</a></td>
            </tr>';
        }																				// Creo una tabla con los resultados
        $db->close();														// Ahora cierro la base de datos
        // Devuelve los productos que hay en la base de datos /////////////////////////////
      ?>
      </tbody>
    </table>
    </main>
  </body>
</html>