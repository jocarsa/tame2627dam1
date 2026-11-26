<?php
  if(isset($_FILES['archivo'])){
    move_uploaded_file(
      $_FILES['archivo']['tmp_name'],
      'subidas/'.$_FILES['archivo']['name']
    );
  }
?>
<!doctype html>
<html>
	<head>
  	<style>
    body{padding:20px;}
    	main{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;}
      main img{width:100%;}
      aside{position:fixed;width:100%;height:100%;background:rgba(0,0,0,0.4);top:0px;left:0px;}
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
    <aside>
    	<div>
      </div>
    </aside>
  </body>
</html>