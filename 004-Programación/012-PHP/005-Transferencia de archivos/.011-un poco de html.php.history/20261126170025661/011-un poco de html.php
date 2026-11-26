<!doctype html>
<html>
	<head>
  	<style>
    	main{display:grid;grid-template-columns:repeat(4,1fr);}
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