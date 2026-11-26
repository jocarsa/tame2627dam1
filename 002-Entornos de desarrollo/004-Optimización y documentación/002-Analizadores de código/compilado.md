# Documentación del proyecto

## Estructura del proyecto

```text
027-Refactorizar/
├── estilo
│   └── estilo.css
├── inc
│   ├── botones_categorias.php
│   ├── galeria_fotografias.php
│   └── guardar_foto.php
├── js
│   └── codigo.js
└── index.php
```

## Código fuente

### estilo/estilo.css

```css
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

      /* Formulario */

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

      /* Chips de categorías */

      header nav{
        display:flex;
        flex-wrap:wrap;
        justify-content:center;
        align-items:center;
        gap:10px;
        margin-top:25px;
        padding-top:20px;
        border-top:1px dashed #ddd5c8;
      }

      header nav button{
        border:1px solid #d8cfc1;
        border-radius:30px;
        padding:8px 22px;
        background:#f3efe8;
        color:#786957;
        font-family:'Caveat',cursive;
        font-size:21px;
        font-weight:600;
        cursor:pointer;

        transition:
          background 0.25s ease,
          color 0.25s ease,
          transform 0.25s ease,
          opacity 0.25s ease,
          box-shadow 0.25s ease;
      }

      header nav button:hover{
        background:#e8e2d8;
        transform:translateY(-2px);
        box-shadow:0 3px 8px rgba(0,0,0,0.1);
      }

      header nav button.activo{
        background:#51483d;
        border-color:#51483d;
        color:white;
        box-shadow:0 3px 8px rgba(0,0,0,0.15);
      }

      header nav button:active{
        transform:scale(0.95);
      }

      header nav button:disabled{
        cursor:wait;
        opacity:0.6;
      }

      header nav button.activo:disabled{
        opacity:1;
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
        transform-origin:center center;

        opacity:1;
        scale:1;

        transition:
          transform 0.3s ease,
          box-shadow 0.3s ease,
          opacity 0.3s ease,
          scale 0.3s cubic-bezier(0.34,1.56,0.64,1);
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

      main:not(.animando) article:hover{
        transform:rotate(0deg) translateY(-10px) scale(1.06);
        box-shadow:0 20px 35px rgba(0,0,0,0.25);
        z-index:10;
      }

      /* Animación de desaparición */

      main article.oculto{
        opacity:0;
        scale:0;
        pointer-events:none;

        transition:
          transform 0.3s ease,
          box-shadow 0.3s ease,
          opacity 0.3s ease,
          scale 0.3s ease-in;
      }

      /* Retiro completamente el artículo */

      main article[hidden]{
        display:none;
      }

      /* Desactivo la interacción durante la animación */

      main.animando article{
        pointer-events:none;
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

        header{
          padding:15px;
          margin-bottom:30px;
        }

        header nav{
          gap:6px;
        }

        header nav button{
          padding:6px 14px;
          font-size:18px;
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
```

### inc/botones_categorias.php

```php
<?php
	$db = new SQLite3('fototeca.db');

          $resultado = $db->query("
            SELECT DISTINCT categoria
            FROM fotos
            ORDER BY categoria
          ");

          while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {

            echo '
              <button
                type="button"
                data-categoria="'.htmlspecialchars($fila['categoria']).'"
              >
                '.htmlspecialchars($fila['categoria']).'
              </button>
            ';

          }

          $db->close();
?>
```

### inc/galeria_fotografias.php

```php
<?php
$db = new SQLite3('fototeca.db');

        $resultado = $db->query("SELECT * FROM fotos");

        while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {

          echo '
            <article data-categoria="'.htmlspecialchars($fila['categoria']).'">

              <img
                src="subidas/'.htmlspecialchars(rawurlencode($fila['nombre'])).'"
                alt="'.htmlspecialchars($fila['titulo']).'"
                loading="lazy"
              >

              <p>'.htmlspecialchars($fila['titulo']).'</p>

              <p>'.htmlspecialchars($fila['categoria']).'</p>

              <time>'.date("d/m/Y H:i:s", $fila['fecha']).'</time>

            </article>
          ';

        }

        $db->close();
?>
```

### inc/guardar_foto.php

```php
<?php
if(isset($_FILES['archivo'])){
    $fecha = date('U');

    move_uploaded_file(
      $_FILES['archivo']['tmp_name'],
      'subidas/'.$fecha.$_FILES['archivo']['name']
    );

    $db = new SQLite3('fototeca.db');

    $consulta = $db->prepare("
      INSERT INTO fotos VALUES(
        NULL,
        :titulo,
        :nombre,
        :tipo,
        :tamano,
        :categoria,
        :fecha
      )
    ");

    $consulta->bindValue(':titulo', $_POST['titulo']);
    $consulta->bindValue(':nombre', $fecha.$_FILES['archivo']['name']);
    $consulta->bindValue(':tipo', $_FILES['archivo']['type']);
    $consulta->bindValue(':tamano', $_FILES['archivo']['size']);
    $consulta->bindValue(':categoria', $_POST['categoria']);
    $consulta->bindValue(':fecha', $fecha);

    $consulta->execute();
    $db->close();
  }
?>
```

### js/codigo.js

```javascript

      // ==========================================
      // MODAL DE FOTOGRAFÍAS
      // ==========================================

      let modal = document.querySelector("aside")
      let imagenmodal = document.querySelector("aside div")
      let imagenes = document.querySelectorAll("main img")

      imagenes.forEach(function(imagen){

        imagen.onclick = function(){

          modal.style.display = "flex"

          imagenmodal.replaceChildren(imagen.cloneNode())

          imagenmodal.querySelector("img").loading = "eager"

        }

      })

      modal.onclick = function(){

        modal.style.display = "none"

      }

      document.addEventListener("keydown", function(evento){

        if(evento.key == "Escape"){

          modal.style.display = "none"

        }

      })

      // ==========================================
      // FILTRO DE CATEGORÍAS
      // ==========================================

      let galeria = document.querySelector("main")
      let botones = document.querySelectorAll("header nav button")
      let articulos = document.querySelectorAll("main article")

      // Parámetros de la animación

      let intervalo = 60
      let duracion = 300
      let pausa = 100

      // Estado de la animación

      let animando = false

      // Función para esperar

      function esperar(milisegundos){

        return new Promise(function(resolve){

          setTimeout(resolve, milisegundos)

        })

      }

      // ==========================================
      // EVENTOS DE LOS CHIPS
      // ==========================================

      botones.forEach(function(boton){

        boton.onclick = async function(){

          // Evito animaciones simultáneas

          if(animando){

            return

          }

          // Si ya está seleccionado, no hago nada

          if(boton.classList.contains("activo")){

            return

          }

          // Inicio la animación

          animando = true

          galeria.classList.add("animando")

          // Desactivo temporalmente los chips

          botones.forEach(function(b){

            b.classList.remove("activo")
            b.disabled = true

          })

          // Marco el chip seleccionado

          boton.classList.add("activo")

          // Obtengo la categoría

          let categoria = boton.dataset.categoria
          let todas = boton.dataset.todas == "true"

          // Listas de fotografías

          let salientes = []
          let entrantes = []

          articulos.forEach(function(articulo){

            // Fotografías actualmente visibles

            if(!articulo.hidden){

              salientes.push(articulo)

            }

            // Fotografías de la nueva categoría

            if(
              todas ||
              articulo.dataset.categoria == categoria
            ){

              entrantes.push(articulo)

            }

          })

          try{

            // ======================================
            // FASE 1: DESAPARICIÓN SECUENCIAL
            // ======================================

            for(let articulo of salientes){

              // Encojo la fotografía

              articulo.classList.add("oculto")

              // Espero antes de encoger la siguiente

              await esperar(intervalo)

            }

            // Espero a que termine la última fotografía

            await esperar(duracion)

            // Retiro todas las fotografías de la cuadrícula

            articulos.forEach(function(articulo){

              articulo.hidden = true
              articulo.classList.add("oculto")

            })

            // ======================================
            // FASE 2: PAUSA ENTRE ANIMACIONES
            // ======================================

            await esperar(pausa)

            // ======================================
            // FASE 3: PREPARO LA NUEVA CUADRÍCULA
            // ======================================

            entrantes.forEach(function(articulo){

              articulo.hidden = false

            })

            // Fuerzo al navegador a actualizar la cuadrícula

            void galeria.offsetWidth

            // ======================================
            // FASE 4: APARICIÓN SECUENCIAL
            // ======================================

            for(let articulo of entrantes){

              // La fotografía crece desde cero

              articulo.classList.remove("oculto")

              // Espero antes de mostrar la siguiente

              await esperar(intervalo)

            }

            // Espero a que termine la última animación

            await esperar(duracion)

          }finally{

            // ======================================
            // FASE 5: FINALIZACIÓN
            // ======================================

            // Reactivo los botones

            botones.forEach(function(b){

              b.disabled = false

            })

            // Recupero el efecto hover

            galeria.classList.remove("animando")

            // Permito una nueva animación

            animando = false

          }

        }

      })
```

### index.php

```php
<?php
  include "inc/guardar_foto.php";
?>
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mi fototeca</title>
    <link rel="stylesheet" href="estilo/estilo.css">
  </head>
  <body>
    <header>
      <form action="?" method="POST" enctype="multipart/form-data">
        <input
          type="text"
          name="titulo"
          placeholder="Introduce el título de la imagen"
          required
        >
        <input
          type="text"
          name="categoria"
          placeholder="Introduce la categoría de la imagen"
          required
        >
        <input
          type="file"
          name="archivo"
          id="archivo"
          accept="image/*"
          required
        >
        <input type="submit" value="Subir fotografía">
      </form>
      <!-- Chips de categorías -->
      <nav>
        <button
          type="button"
          class="activo"
          data-todas="true"
        >Todas</button>
        <?php
          include "inc/botones_categorias.php";
        ?>
      </nav>
    </header>
    <!-- Galería de fotografías -->
    <main>
      <?php
        include "inc/galeria_fotografias.php";
      ?>
    </main>
    <!-- Modal de fotografía -->
    <aside>
      <div></div>
    </aside>
    <script src="js/codigo.js"></script>
  </body>
</html>
```

