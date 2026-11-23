<!doctype html>
<html>
	<head>
  	
    <style>
      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        padding: 40px;
        background: #f4f6f8;
        font-family: Arial, sans-serif;
        color: #333;
      }

      table {
        width: 100%;
        border-collapse: collapse;
        background: white;
        border: none;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
      }

      thead {
        background: #2c3e50;
        color: white;
      }

      th {
        padding: 18px 20px;
        text-align: left;
        font-size: 14px;
        font-weight: 600;
        border: none;
      }

      td {
        padding: 15px 20px;
        font-size: 14px;
        border: none;
        border-bottom: 1px solid #eee;
      }

      tbody tr:nth-child(even) {
        background: #f8fafc;
      }

      tbody tr:hover {
        background: #eaf3ff;
        transition: background 0.2s;
      }

      tbody tr:last-child td {
        border-bottom: none;
      }

      td:first-child {
        font-weight: bold;
        color: #64748b;
        width: 70px;
      }

      td:last-child {
        color: #2563eb;
      }

      @media (max-width: 600px) {
        body {
          padding: 15px;
        }

        th, td {
          padding: 10px;
          font-size: 12px;
        }
      }
    </style>

  </head>
  <body>
  
    <table border=1>
      <thead>
        <tr>
          <th>id</th>
          <th>Nombre</th>
          <th>Apellidos</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
      
        <?php
          $conexion = new mysqli("localhost", "crud", "TAME123$", "crud");
          $resultado = $conexion->query("SELECT * FROM alumnos");
          while ($fila = $resultado->fetch_assoc()) {
              echo '
              	<!-- Esto es lo que se repite -->
                <tr>
                  <td>'.$fila['id'].'</td>
                  <td>'.$fila['nombre'].'</td>
                  <td>'.$fila['apellidos'].'</td>
                  <td>'.$fila['email'].'</td>
                </tr>
                <!-- Esto es lo que se repite -->
              ';
          }
          $conexion->close();
        ?>
      	<tr>
        	<form action="?" method="POST">
          	<td></td>	
            <td></td>
            <td></td>
          </form>
        </tr>
      </tbody>
    </table>
    
  </body>
</html>