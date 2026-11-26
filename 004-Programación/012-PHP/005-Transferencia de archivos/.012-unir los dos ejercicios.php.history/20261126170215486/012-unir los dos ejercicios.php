<!doctype html>
<html>
	<head>
  	<style>
    body{padding:20px;}
    	main{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;}
      main img{width:100%;}
    </style>
  </head>
  <body>
  	<header>
    	<form action="?" method="POST" enctype="multipart/form-data">
        <input type="file" name="archivo" id="archivo">
        <input type="submit">
      </form>
    </header>
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