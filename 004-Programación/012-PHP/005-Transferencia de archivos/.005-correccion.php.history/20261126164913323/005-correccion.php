<?php
  if(isset($_FILES['archivo'])){
    move_uploaded_file(
      $_FILES['archivo']['tmp_name'],
      'subidas/'.$_FILES['archivo']['name']
    );
  }
?>

<form action="?" method="POST" enctype="multipart/form-data">
  <input type="text" name="nombre" placeholder="Introduce tu nombre">
  <label for="archivo">Adjunta tu archivo</label>
  <input type="file" name="archivo" id="archivo">
  <input type="submit">
</form>