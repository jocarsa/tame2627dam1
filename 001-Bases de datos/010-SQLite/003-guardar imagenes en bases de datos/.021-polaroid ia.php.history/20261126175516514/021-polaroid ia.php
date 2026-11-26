<?php
  if(isset($_FILES['archivo'])){
  	$fecha = date('U');
    move_uploaded_file(
      $_FILES['archivo']['tmp_name'],
      'subidas/'.$fecha.$_FILES['archivo']['name']
    );
    $db = new SQLite3('fototeca.db');
    $db->exec("
    	INSERT INTO fotos VALUES(
      	NULL,
        '".$_POST['titulo']."',
        '".$fecha.$_FILES["archivo"]["name"]."',
        '".$_FILES["archivo"]["type"]."',
        '".$_FILES["archivo"]["size"]."',
        '".$_POST['categoria']."',
        '".$fecha."'
      );
    ");
    $db->close();
  }
?>
<!doctype html>
<html>
	<head>
  	<style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&display=swap');

*{
  box-sizing:border-box;
}

body{
  margin:0;
  padding:30px;
  background-color:#e8e2d8;
  background-image:radial-gradient(#c8c0b3 0.7px, transparent 0.7px);
  background-size:6px 6px;
  font-family:Arial,sans-serif;
  color:#444;
}

/* Cabecera */

header{
  max-width:1400px;
  margin:0 auto 50px auto;
  padding:25px;
  background:#fffefa;
  border-radius:4px;
  box-shadow:0 5px 20px rgba(0,0,0,0.08);
}

header::before{
  content:"Mi fototeca";
  display:block;
  font-family:'Caveat',cursive;
  font-size:42px;
  font-weight:bold;
  text-align:center;
  margin-bottom:20px;
}

form{
  display:flex;
  flex-direction:column;
  gap:15px;
}

input{
  width:100%;
  padding:12px;
  background:#f8f6f1;
  border:1px solid #ddd5c8;
  border-radius:4px;
  font-family:inherit;
  font-size:14px;
}

input:focus{
  outline:none;
  border-color:#9c8b75;
}

input[type="file"]::file-selector-button{
  border:none;
  padding:10px 15px;
  margin-right:15px;
  border-radius:4px;
  background:#e8e2d8;
  cursor:pointer;
}

input[type="submit"]{
  background:#51483d;
  color:white;
  border:none;
  padding:15px 25px;
  font-weight:bold;
  cursor:pointer;
  transition:background 0.3s;
}

input[type="submit"]:hover{
  background:#786957;
}

/* Galería de fotografías */

main{
  max-width:1400px;
  margin:auto;
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(240px,1fr));
  gap:40px;
  padding:20px;
  align-items:start;
}

/* Marco Polaroid */

main article{
  position:relative;
  background:#fffefa;
  padding:12px 12px 25px 12px;
  box-shadow:
    0 2px 4px rgba(0,0,0,0.12),
    3px 8px 15px rgba(0,0,0,0.18);
  transform:rotate(-3deg);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

/* Rotaciones alternas */

main article:nth-child(2n){
  transform:rotate(3deg);
}

main article:nth-child(3n){
  transform:rotate(-1.5deg);
}

main article:nth-child(5n){
  transform:rotate(2deg);
}

main article:nth-child(7n){
  transform:rotate(-4deg);
}

/* Efecto al pasar el ratón */

main article:hover{
  transform:rotate(0deg) translateY(-10px) scale(1.06);
  box-shadow:0 20px 35px rgba(0,0,0,0.25);
  z-index:10;
}

/* Fotografía */

main article img{
  display:block;
  width:100%;
  aspect-ratio:1/1;
  object-fit:cover;
  border:none;
  border-radius:0;
  cursor:zoom-in;
  filter:contrast(0.95) saturate(0.85) sepia(0.08);
  transition:filter 0.3s;
}

main article:hover img{
  filter:none;
}

/* Título manuscrito */

main article p{
  margin:0;
  text-align:center;
  overflow-wrap:anywhere;
}

main article p:first-of-type{
  font-family:'Caveat',cursive;
  font-size:30px;
  font-weight:700;
  line-height:1.1;
  color:#303d50;
  margin-top:15px;
  margin-bottom:8px;
}

/* Categoría */

main article p:nth-of-type(2){
  font-family:'Caveat',cursive;
  font-size:21px;
  color:#888;
  margin-bottom:10px;
}

/* Fecha */

main article time{
  display:block;
  text-align:right;
  font-family:'Caveat',cursive;
  font-size:16px;
  color:#999;
  margin-top:10px;
}

/* Modal */

aside{
  position:fixed;
  inset:0;
  width:100%;
  height:100%;
  background:rgba(25,20,15,0.85);
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
  padding:15px 15px 60px 15px;
  background:#fffefa;
  box-shadow:0 20px 80px rgba(0,0,0,0.5);
  animation:aparecer 0.3s ease;
}

aside div img{
  display:block;
  width:auto;
  height:auto;
  max-width:calc(90vw - 30px);
  max-height:calc(90vh - 75px);
  object-fit:contain;
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

/* Animación del modal */

@keyframes aparecer{
  from{
    opacity:0;
    transform:scale(0.8) rotate(-5deg);
  }

  to{
    opacity:1;
    transform:scale(1) rotate(0deg);
  }
}

/* Adaptación a móviles */

@media(max-width:600px){

  body{
    padding:15px;
  }

  main{
    grid-template-columns:repeat(2,minmax(0,1fr));
    gap:20px;
    padding:5px;
  }

  main article{
    padding:7px 7px 15px 7px;
  }

  main article p:first-of-type{
    font-size:23px;
  }

  main article p:nth-of-type(2){
    font-size:17px;
  }

  main article time{
    font-size:13px;
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
        $db = new SQLite3('fototeca.db');										// Abro la base de datos
        $resultado = $db->query("SELECT * FROM fotos");	// Petición a la base de datos
        while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
            echo '
            <article>
            	<img src="subidas/'.$fila['nombre'].'">
              <p>'.$fila['titulo'].'</p>
              <p>'.$fila['categoria'].'</p>
              <time>'.echo date("d/m/Y H:i:s",$fila['fecha']).'</time>
            </article>
            ';
        }																										// Devuelvo el contenido
        $db->close();																				// Ahora cierro la base de datos
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