<?php
  if(isset($_FILES['archivo'])){
    $fecha = date('U');

    move_uploaded_file(
      $_FILES['archivo']['tmp_name'],
      'subidas/'.$fecha.$_FILES['archivo']['name']
    );

    $db = new SQLite3('fototeca.db');

    $consulta = $db->prepare("
      INSERT INTO fotos VALUES(
        NULL,
        :titulo,
        :nombre,
        :tipo,
        :tamano,
        :categoria,
        :fecha
      )
    ");

    $consulta->bindValue(':titulo', $_POST['titulo']);
    $consulta->bindValue(':nombre', $fecha.$_FILES['archivo']['name']);
    $consulta->bindValue(':tipo', $_FILES['archivo']['type']);
    $consulta->bindValue(':tamano', $_FILES['archivo']['size']);
    $consulta->bindValue(':categoria', $_POST['categoria']);
    $consulta->bindValue(':fecha', $fecha);

    $consulta->execute();
    $db->close();
  }
?>
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mi fototeca</title>
    <link rel="stylesheet" href="estilo/estilo.css">
  </head>

  <body>

    <header>

      <form action="?" method="POST" enctype="multipart/form-data">

        <input
          type="text"
          name="titulo"
          placeholder="Introduce el título de la imagen"
          required
        >

        <input
          type="text"
          name="categoria"
          placeholder="Introduce la categoría de la imagen"
          required
        >

        <input
          type="file"
          name="archivo"
          id="archivo"
          accept="image/*"
          required
        >

        <input type="submit" value="Subir fotografía">

      </form>

      <!-- Chips de categorías -->

      <nav>

        <button
          type="button"
          class="activo"
          data-todas="true"
        >Todas</button>

        <?php
          include "inc/botones_categorias.php";
        ?>

      </nav>

    </header>

    <!-- Galería de fotografías -->

    <main>

      <?php
        include "inc/galeria_fotografias.php";
      ?>

    </main>

    <!-- Modal de fotografía -->

    <aside>
      <div></div>
    </aside>

    <script>


    </script>

  </body>
</html>