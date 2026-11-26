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