<?php
  if(isset($_FILES['archivo'])){
    move_uploaded_file(
      $_FILES['archivo']['tmp_name'],
      'subidas/'.$_FILES['archivo']['name']
    );
    $db = new SQLite3('fototeca.db');
  }
?>
<!doctype html>
<html>
	<head>
  	<style>
    *{
  box-sizing:border-box;
}

body{
  margin:0;
  padding:30px;
  background:#f4f5f7;
  font-family:Arial,sans-serif;
  color:#333;
}

/* Cabecera */

header{
  max-width:1400px;
  margin:0 auto 30px auto;
  padding:25px;
  background:white;
  border-radius:12px;
  box-shadow:0 4px 15px rgba(0,0,0,0.05);
}

header::before{
  content:"Fotogalería";
  display:block;
  font-size:28px;
  font-weight:bold;
  margin-bottom:20px;
}

form{
  display:flex;
  align-items:space-between;
  gap:15px;
  flex-wrap:wrap;
  flex-direction:column;
}

input{
  flex:1;
  padding:12px;
  background:#f4f5f7;
  border:1px dashed #ccc;
  border-radius:8px;
  cursor:pointer;
}

input[type="file"]::file-selector-button{
  border:none;
  padding:10px 15px;
  margin-right:15px;
  border-radius:6px;
  background:#e2e5e9;
  cursor:pointer;
}

input[type="submit"]{
  background:#2563eb;
  color:white;
  border:none;
  padding:15px 25px;
  border-radius:8px;
  font-weight:bold;
  cursor:pointer;
  transition:background 0.3s;
}

input[type="submit"]:hover{
  background:#1d4ed8;
}

/* Galería */

main{
  max-width:1400px;
  margin:auto;
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(240px,1fr));
  gap:20px;
}

main img{
  display:block;
  width:100%;
  aspect-ratio:4/3;
  object-fit:cover;
  border:5px solid white;
  border-radius:12px;
  box-shadow:0 4px 12px rgba(0,0,0,0.1);
  cursor:zoom-in;
  transition:
    transform 0.3s,
    box-shadow 0.3s,
    filter 0.3s;
}

main img:hover{
  transform:translateY(-5px) scale(1.02);
  box-shadow:0 12px 25px rgba(0,0,0,0.2);
  filter:brightness(1.05);
}

/* Modal */

aside{
  position:fixed;
  inset:0;
  width:100%;
  height:100%;
  background:rgba(0,0,0,0.85);
  backdrop-filter:blur(10px);
  display:none;
  justify-content:center;
  align-items:center;
  z-index:1000;
  padding:40px;
  cursor:zoom-out;
}

aside div{
  display:flex;
  justify-content:center;
  align-items:center;
  width:auto;
  height:auto;
  max-width:90vw;
  max-height:90vh;
  padding:10px;
  background:white;
  border-radius:12px;
  box-shadow:0 20px 80px rgba(0,0,0,0.5);
  animation:aparecer 0.3s ease;
}

aside div img{
  display:block;
  width:auto;
  height:auto;
  max-width:calc(90vw - 20px);
  max-height:calc(90vh - 20px);
  object-fit:contain;
  border-radius:6px;
}

aside::after{
  content:"×";
  position:absolute;
  top:20px;
  right:30px;
  color:white;
  font-size:45px;
  cursor:pointer;
}

/* Animaciones */

@keyframes aparecer{
  from{
    opacity:0;
    transform:scale(0.9);
  }
  to{
    opacity:1;
    transform:scale(1);
  }
}

/* Adaptación a móviles */

@media(max-width:600px){
  body{
    padding:15px;
  }

  main{
    grid-template-columns:repeat(2,minmax(0,1fr));
    gap:10px;
  }

  form{
    flex-direction:column;
    align-items:stretch;
  }

  input[type="file"]{
    width:100%;
  }

  aside{
    padding:10px;
  }
}
    </style>
  </head>
  <body>
  	<header>
    	<form action="?" method="POST" enctype="multipart/form-data">
      	<input type="text" name="titulo" placeholder="Introduce el título de la imagen">
        <input type="text" name="categoria" placeholder="Introduce la categoría de la imagen">
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
      	imagen.onclick = function(){
        	modal.style.display = "flex"
      		imagenmodal.innerHTML = '<img src="'+imagen.getAttribute("src")+'">'
        }
      })
      
      modal.onclick = function(){
      	modal.style.display = "none"
      }
      
      
    </script>
  </body>
</html>