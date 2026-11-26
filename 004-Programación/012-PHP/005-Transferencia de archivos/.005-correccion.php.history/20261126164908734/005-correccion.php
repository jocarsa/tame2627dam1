<?php
  if(isset($_FILES['archivo'])){
    move_uploaded_file(
      $_FILES['archivo']['tmp_name'],
      'subidas/'.$_FILES['archivo']['name']
    );
  }
?>