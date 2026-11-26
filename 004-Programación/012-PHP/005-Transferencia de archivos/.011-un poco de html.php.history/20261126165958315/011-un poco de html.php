<!doctype html>
<html>
	<head>
  	<style>
    	
    </style>
  </head>
  <body>
  	<main>
      <?php
        $directorio = scandir("subidas");
        foreach($directorio as $archivo){
          if($archivo != "." && $archivo != ".."){
            echo "<img src='subidas/".$archivo."'>";
          }
        }
      ?>
    </main>
  </body>
</html>