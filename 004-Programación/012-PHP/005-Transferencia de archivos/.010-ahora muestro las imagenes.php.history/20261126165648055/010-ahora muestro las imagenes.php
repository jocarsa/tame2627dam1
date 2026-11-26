<?php
	$directorio = scandir("subidas");
  foreach($directorio as $archivo){
  	if($archivo != "." && $archivo != ".."){
  		echo "<img src='subidas/".$archivo."'>";
    }
  }
?>