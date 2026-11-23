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
    	/* GENERAL /////////////////////////////////////////// */

        *{
          box-sizing:border-box;
        }

        html,body{
          padding:0;
          margin:0;
          width:100%;
          height:100%;
          font-family:Ubuntu,Arial,sans-serif;
          font-size:14px;
          color:#252536;
        }

        body{
          display:flex;
          background:#f4f5f9;
          overflow:hidden;
        }

        /* NAVEGACIÓN //////////////////////////////////////// */

        nav{
          background:linear-gradient(180deg,#31206a,#1c123f);
          flex:0 0 230px;
          padding:25px 15px;
          display:flex;
          flex-direction:column;
          gap:8px;
          box-shadow:4px 0 20px rgba(30,20,70,.12);
          overflow-y:auto;
        }

        nav::before{
          content:"TIENDA";
          display:block;
          color:white;
          font-size:23px;
          font-weight:700;
          letter-spacing:3px;
          padding:15px 12px 30px;
          margin-bottom:15px;
          border-bottom:1px solid rgba(255,255,255,.15);
        }

        nav a{
          display:flex;
          align-items:center;
          text-decoration:none;
          color:#d5d0e8;
          background:transparent;
          padding:14px 16px;
          border-radius:9px;
          font-size:14px;
          font-weight:500;
          cursor:pointer;
          transition:all .2s ease;
          border:1px solid transparent;
        }

        nav a:hover{
          background:rgba(255,255,255,.12);
          color:white;
          transform:translateX(4px);
        }

        nav a:first-of-type{
          background:rgba(255,255,255,.16);
          color:white;
          font-weight:600;
          border-left:3px solid #b9a5ff;
        }

        /* CONTENIDO PRINCIPAL /////////////////////////////// */

        main{
          background:#f4f5f9;
          flex:1;
          min-width:0;
          padding:35px;
          overflow:auto;
        }

        main::before{
          content:"Gestión de productos";
          display:block;
          font-size:28px;
          font-weight:700;
          color:#292044;
          margin-bottom:8px;
        }

        main::after{
          content:"";
          display:block;
          height:30px;
        }

        /* TABLA ///////////////////////////////////////////// */

        table{
          width:100%;
          border:0;
          border-collapse:separate;
          border-spacing:0;
          background:white;
          border-radius:12px;
          box-shadow:0 5px 25px rgba(30,20,70,.07);
          overflow:hidden;
          font-size:13px;
        }

        table thead{
          background:#382477;
        }

        table thead tr:first-child{
          background:#382477;
        }

        table th{
          padding:17px 13px;
          color:white;
          text-align:left;
          font-size:11px;
          font-weight:600;
          letter-spacing:.5px;
          text-transform:uppercase;
          white-space:nowrap;
          border:0;
        }

        table thead tr:first-child th{
          position:relative;
        }

        table thead tr:first-child th:not(:last-child)::after{
          content:"";
          position:absolute;
          right:0;
          top:25%;
          height:50%;
          width:1px;
          background:rgba(255,255,255,.15);
        }

        /* FILA DE INSERCIÓN ///////////////////////////////// */

        table thead tr:nth-child(2){
          background:#eeeaf8;
        }

        table thead tr:nth-child(2) th{
          padding:12px 8px;
          border-bottom:2px solid #dcd4f0;
        }

        table input{
          width:100%;
          min-width:75px;
          padding:10px 9px;
          border:1px solid #d9d5e5;
          border-radius:6px;
          background:white;
          color:#292044;
          font-family:inherit;
          font-size:12px;
          font-weight:400;
          outline:none;
          transition:all .2s ease;
        }

        table input:hover{
          border-color:#a99bcf;
        }

        table input:focus{
          border-color:#6346b2;
          box-shadow:0 0 0 3px rgba(99,70,178,.12);
          background:#fff;
        }

        table input[type="submit"]{
          background:#49318e;
          color:white;
          border:0;
          cursor:pointer;
          font-weight:600;
          min-width:85px;
          padding:11px;
          box-shadow:0 2px 6px rgba(73,49,142,.2);
        }

        table input[type="submit"]:hover{
          background:#6346b2;
          transform:translateY(-1px);
          box-shadow:0 4px 12px rgba(73,49,142,.25);
        }

        table input[type="submit"]:active{
          transform:translateY(0);
        }

        /* FILAS DE DATOS //////////////////////////////////// */

        table tbody tr{
          background:white;
          transition:background .15s ease;
        }

        table tbody tr:nth-child(even){
          background:#faf9fd;
        }

        table tbody tr:hover{
          background:#f0ecfa;
        }

        table td{
          padding:14px 13px;
          font-size:12px;
          min-width:75px;
          color:#454253;
          border-bottom:1px solid #eeedf2;
          line-height:1.5;
          vertical-align:middle;
        }

        table tbody tr:last-child td{
          border-bottom:0;
        }

        table td:first-child{
          font-weight:600;
          color:#302254;
        }

        table td:nth-child(7){
          font-weight:700;
          color:#49318e;
          white-space:nowrap;
        }

        table td:nth-child(8){
          font-weight:600;
          text-align:center;
        }

        table td:nth-child(9){
          color:#888394;
          white-space:nowrap;
        }

        /* BOTÓN BORRAR ////////////////////////////////////// */

        table td a{
          display:inline-flex;
          align-items:center;
          justify-content:center;
          text-decoration:none;
          color:#b33446;
          background:#fff0f2;
          padding:8px 13px;
          border-radius:6px;
          font-size:11px;
          font-weight:600;
          border:1px solid #f5d8de;
          transition:all .2s ease;
          white-space:nowrap;
        }

        table td a:hover{
          background:#c43d50;
          color:white;
          border-color:#c43d50;
          box-shadow:0 3px 10px rgba(196,61,80,.2);
          transform:translateY(-1px);
        }

        /* SCROLLBARS //////////////////////////////////////// */

        main::-webkit-scrollbar,
        nav::-webkit-scrollbar{
          width:8px;
          height:8px;
        }

        main::-webkit-scrollbar-track{
          background:#f4f5f9;
        }

        main::-webkit-scrollbar-thumb{
          background:#c9c2dc;
          border-radius:10px;
        }

        main::-webkit-scrollbar-thumb:hover{
          background:#9988bf;
        }

        nav::-webkit-scrollbar-thumb{
          background:rgba(255,255,255,.2);
          border-radius:10px;
        }

        /* RESPONSIVE //////////////////////////////////////// */

        @media(max-width:1100px){

          nav{
            flex:0 0 180px;
            padding:20px 10px;
          }

          main{
            padding:20px;
          }

          table th,
          table td{
            padding:10px 8px;
          }

          table input{
            min-width:65px;
          }
        }

        @media(max-width:700px){

          body{
            flex-direction:column;
          }

          nav{
            flex:none;
            flex-direction:row;
            padding:10px;
            overflow-x:auto;
            gap:6px;
          }

          nav::before{
            display:none;
          }

          nav a{
            flex-shrink:0;
            padding:10px 14px;
            font-size:12px;
          }

          main{
            padding:15px;
            flex:1;
          }

          main::before{
            font-size:22px;
          }

          table{
            min-width:1100px;
          }
        }
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