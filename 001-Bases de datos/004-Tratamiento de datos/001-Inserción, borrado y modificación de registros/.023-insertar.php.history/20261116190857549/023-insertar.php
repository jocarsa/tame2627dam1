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