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

    <script>

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

    </script>

  </body>
</html>