<?php
	$directorio = scandir("subidas");
  foreach($directorio as $archivo){
  	echo $archivo."<br>";
  }
?>