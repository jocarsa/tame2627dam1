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
      aside{position:fixed;width:100%;height:100%;background:rgba(0,0,0,0.8);top:0px;left:0px;
      display:none;justify-content:center;align-items:center;}
      aside div{width:500px;height:500px;background:white;padding:20px;}
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
    <script>
    	let modal = document.querySelector("aside")
      let imagenmodal = document.querySelector("aside div")
      
      let imagenes = document.querySelectorAll("img")
      imagenes.forEach(function(imagen){
      	imagenmodal.innerHTML = '<img src="'+imagen.getAttribute("src")+'">'
      })
      
      
    </script>
  </body>
</html>