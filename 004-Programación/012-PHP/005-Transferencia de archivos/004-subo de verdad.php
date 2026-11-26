<?php
	if(isset($_FILE)){
		move_uploaded_file($_FILE['tmp_name'],'subidas/'.$_FILE['name']);
	}
?>

<form action="?" method="POST" enctype="multipart/form-data">
  <input type="text" name="nombre" placeholder="Introduce tu nombre">
  <label for="archivo">Adjunta tu archivo</label>
  <input type="file" name="archivo" id="archivo">
  <input type="submit">
</form>