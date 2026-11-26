# Documentación del proyecto

## Descripción general del software

El software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. La aplicación está construida utilizando tecnologías web, incluyendo HTML, CSS, JavaScript y PHP para la lógica de back-end.

La finalidad del software es ofrecer una plataforma donde los usuarios puedan subir imágenes de fotos, categorizarlas y visualizarlas en una galería que permite una navegación intuitiva y una experiencia de usuario atractiva. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atención del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada y un sistema de categorías para organizar las fotos.

El software está organizado en un sistema de archivos que contiene un directorio raíz con tres subdirectorios: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css` que define el aspecto visual del sitio, incluyendo el diseño de la cabecera, el formulario de subida de fotos y los chips de categorías. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js` que maneja la interactividad y animaciones de la galería.

El software funciona de la siguiente manera: cuando un usuario sube una foto, se le solicita un título y una categoría. La foto se almacena en una base de datos SQLite y se muestra en la galería. Los usuarios pueden navegar entre las categorías y visualizar las fotos asociadas. La galería utiliza animaciones y efectos de CSS para mostrar las fotos de manera atractiva. Además, el software permite al usuario visualizar una foto de manera detallada en un modal.

Los principales componentes del software incluyen el formulario de subida de fotos, la galería de fotos, los botones de categorías y el modal de visualización de fotos. El formulario de subida de fotos permite a los usuarios subir imágenes con títulos y categorías. La galería de fotos muestra las imágenes subidas y permite a los usuarios navegar entre las categorías. Los botones de categorías permiten a los usuarios seleccionar y visualizar fotos de una categoría específica. El modal de visualización de fotos permite a los usuarios ver una foto de manera detallada.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

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

## Código fuente documentado

### estilo/estilo.css

# Descripción General del Software

El software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. La aplicación está construida utilizando tecnologías web como HTML, CSS, JavaScript y PHP para la lógica de back-end y la gestión de la base de datos. La finalidad es ofrecer una plataforma donde los usuarios puedan subir imágenes de fotos con títulos y categorías, navegar entre las categorías y visualizar las fotos asociadas en una galería atractiva y organizada. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con un directorio raíz que contiene tres subdirectorios: `estilo`, `inc` y `js`. El directorio `estilo` alberga el archivo `estilo.css` que define el aspecto visual del sitio, incluyendo el diseño de la cabecera, el formulario de subida de fotos y los chips de categorías. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js` que maneja la interactividad y animaciones de la galería.

El software funciona de la siguiente manera: cuando un usuario sube una foto, se le solicita un título y una categoría. La foto se almacena en una base de datos SQLite y se muestra en la galería. Los usuarios pueden navegar entre las categorías y visualizar las fotos asociadas. La galería utiliza animaciones y efectos de CSS para mostrar las fotos de manera atractiva. Además, el software permite al usuario visualizar una foto de manera detallada en un modal.

Los principales componentes del software incluyen el formulario de subida de fotos, la galería de fotos, los botones de categorías y el modal de visualización de fotos. El formulario de subida de fotos permite a los usuarios subir imágenes con títulos y categorías. La galería de fotos muestra las imágenes subidas y permite a los usuarios navegar entre las categorías. Los botones de categorías permiten a los usuarios seleccionar y visualizar fotos de una categoría específica. El modal de visualización de fotos permite a los usuarios ver una foto de manera detallada.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.


# Estrutura del Proyecto

El proyecto está estructurado de la siguiente manera:

- Directorio raíz
  - Estilo
    - Estilo.css
  - Inc
    - botones_categorias.php
    - galeria_fotografias.php
    - guardar_foto.php
  - JS
    - codigo.js
  - index.php


# Código Fuente

El archivo `estilo.css` contiene los estilos CSS para el diseño visual del sitio web. Los estilos incluyen el diseño de la cabecera, el formulario de subida de fotos y los chips de categorías. Los estilos también incluyen el aspecto de las fotos en la galería y el modal de visualización.

El archivo `codigo.js` contiene el código JavaScript para la interactividad y animaciones de la galería. El código maneja los eventos de ratón y controla la animación de la galería.

El archivo `botones_categorias.php` genera los elementos de botones de categorías y el archivo `galeria_fotografias.php` genera la galería de fotos. El archivo `guardar_foto.php` maneja la subida de fotos a la base de datos SQLite.

El archivo `index.php` es el punto de entrada de la aplicación y contiene el código HTML que llama a los archivos PHP y JavaScript para mostrar la interfaz de usuario.


# Cómo funciona el software

Cuando un usuario sube una foto, se le solicita un título y una categoría. El software almacena la foto en una base de datos SQLite y la muestra en la galería. Los usuarios pueden navegar entre las categorías y visualizar las fotos asociadas. La galería utiliza animaciones y efectos de CSS para mostrar las fotos de manera atractiva. Además, el software permite al usuario visualizar una foto de manera detallada en un modal.

Los principales componentes del software son el formulario de subida de fotos, la galería de fotos, los botones de categorías y el modal de visualización de fotos. El formulario de subida de fotos permite a los usuarios subir imágenes con títulos y categorías. La galería de fotos muestra las imágenes subidas y permite a los usuarios navegar entre las categorías. Los botones de categorías permiten a los usuarios seleccionar y visualizar fotos de una categoría específica. El modal de visualización de fotos permite a los usuarios ver una foto de manera detallada.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.


# Cómo se relaciona con el resto del proyecto

El software se relaciona con el resto del proyecto a través de los archivos PHP y JavaScript que se encuentran en el directorio `inc`. El archivo `botones_categorias.php` genera los elementos de botones de categorías y el archivo `galeria_fotografias.php` genera la galería de fotos. Estos archivos se llaman desde el archivo `index.php`, que es el punto de entrada de la aplicación. Además, el archivo `codigo.js` se llama desde el archivo `index.php` para manejar la interactividad y animaciones de la galería.

El software también se relaciona con el resto del proyecto a través de la base de datos SQLite que almacena las fotos subidas. El archivo `guardar_foto.php` maneja la subida de fotos a la base de datos y se llama desde el archivo `index.php`.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva. Se relaciona con el resto del proyecto a través de los archivos PHP y JavaScript que se encuentran en el directorio `inc` y la base de datos SQLite que almacena las fotos subidas.


# Resumen

El software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva. Está estructurado en un sistema de archivos con un directorio raíz que contiene tres subdirectorios: `estilo`, `inc` y `js`. Los principales componentes del software son el formulario de subida de fotos, la galería de fotos, los botones de categorías y el modal de visualización de fotos. El software utiliza tecnologías web para su funcionamiento y la interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. El software se relaciona con el resto del proyecto a través de los archivos PHP y JavaScript que se encuentran en el directorio `inc` y la base de datos SQLite que almacena las fotos subidas.

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

## Descripción General del Software

El software en cuestión es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Su finalidad es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera intuitiva y atractiva. La galería presenta las imágenes en un formato polaroid con efectos de rotaciones y animaciones para capturar la atención del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web, incluyendo el diseño de la cabecera, el formulario de subida de fotos y los chips de categorías. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento, como HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos. La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

## Código del Software

El archivo `inc/botones_categorias.php` contiene el siguiente código fuente:

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
      '.htmlspecialchars($fila['categoria']
    '
    '
  ';

}

$db->close();
```

Este código se encarga de generar los botones de categorías utilizando las categorías disponibles almacenadas en una base de datos SQLite. Cada botón representa una categoría y se muestra en la interfaz de usuario.

## Responsabilidad del Archivo

El archivo `inc/botones_categorias.php` tiene la responsabilidad de generar dinámicamente los botones de categorías a partir de las categorías disponibles almacenadas en la base de datos. Esto permite a los usuarios seleccionar y visualizar fotos de una categoría específica.

## Cómo Funciona el Código

El código PHP utiliza la extensión SQLite3 para conectarse a la base de datos `fototeca.db` y recuperar las categorías disponibles. Luego, genera los botones de categorías utilizando una consulta SQL que selecciona las categorías distintas y las ordena. Cada botón representa una categoría y se muestra en la interfaz de usuario. El código PHP utiliza la función `fetchArray` para obtener los resultados de la consulta y los imprime como elementos HTML.

## Cómo se Relaciona con el Resto del Proyecto

El archivo `inc/botones_categorias.php` se integra con el resto del proyecto a través de la generación de botones de categorías que se muestran en la interfaz de usuario. Estos botones se generan dinámicamente utilizando PHP y se muestran en la interfaz de usuario gracias a la interacción con JavaScript. Además, el archivo `botones_categorias.php` se comunica con el archivo `galeria_fotografias.php` para mostrar las fotos asociadas a cada categoría seleccionada.

El archivo `botones_categorias.php` también se integra con el archivo `guardar_foto.php` para almacenar las fotos subidas en la base de datos.

En resumen, el archivo `inc/botones_categorias.php` es un componente esencial del software que permite a los usuarios seleccionar y visualizar fotos de una categoría específica, y se integra con otros archivos para almacenar y mostrar imágenes en la galería.

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

# Descripción General del Software

El software en cuestión es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. La aplicación está construida utilizando tecnologías web como HTML, CSS, JavaScript y PHP para la lógica de back-end y la gestión de la base de datos. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera intuitiva y atractiva. La galería presenta las imágenes en un formato polaroid con efectos de rotaciones y animaciones para capturar la atención del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css` que define el aspecto visual del sitio web, incluyendo el diseño de la cabecera, el formulario de subida de fotos y los chips de categorías. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. Por último, el directorio `js` contiene el archivo `codigo.js` que maneja la interactividad y animaciones de la galería.

El software funciona de la siguiente manera: cuando un usuario sube una foto, se le solicita un título y una categoría. La foto se almacena en una base de datos SQLite y se muestra en la galería. Los usuarios pueden navegar entre las categorías y visualizar las fotos asociadas. La galería utiliza animaciones y efectos de CSS para mostrar las fotos de manera atractiva. Además, el software permite al usuario visualizar una foto de manera detallada en un modal.

Los principales componentes del software incluyen el formulario de subida de fotos, la galería de fotos, los botones de categorías y el modal de visualización de fotos. El formulario de subida de fotos permite a los usuarios subir imágenes con títulos y categorías. La galería de fotos muestra las imágenes subidas y permite a los usuarios navegar entre las categorías. Los botones de categorías permiten a los usuarios seleccionar y visualizar fotos de una categoría específica. El modal de visualización de fotos permite a los usuarios ver una foto de manera detallada.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.


# Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

- Directorio raíz
  - `estilo`
    - `estilo.css`
  - `inc`
    - `botones_categorias.php`
    - `galeria_fotografias.php`
    - `guardar_foto.php`
  - `js`
    - `codigo.js`
  - `index.php`


# Código Fuente

El archivo `inc/galeria_fotografias.php` contiene el siguiente código fuente:

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
```

Este código se encarga de recuperar las fotos de la base de datos SQLite, mostrarlas en la galería y generar los elementos HTML correspondientes para cada foto. Además, utiliza el atributo `data-categoria` para asociar cada foto con su categoría correspondiente. El atributo `loading="lazy"` se utiliza para cargar las imágenes de manera eficiente. El código también muestra el título y la fecha de cada foto.

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

# Descripción General del Software

El software en cuestión es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Esta aplicación se basa en tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está estructurado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` alberga el archivo `estilo.css`, que define el aspecto visual del sitio web, incluyendo el diseño de la cabecera, el formulario de subida de fotos y los chips de categorías. El directorio `inc` contiene los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. Por último, el directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El código PHP `guardar_foto.php` es responsable de almacenar las fotos subidas en una base de datos SQLite. Cuando un usuario sube una foto, se le solicita un título y una categoría. La foto se almacena en la base de datos y se muestra en la galería. Los usuarios pueden navegar entre las categorías y visualizar las fotos asociadas.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

# Descripción del Archivo `guardar_foto.php`

El archivo `guardar_foto.php` es un componente esencial del software, ya que se encarga de almacenar las fotos subidas en una base de datos SQLite. Este archivo utiliza la tecnología PHP para interactuar con la base de datos y realizar la inserción de los datos de la foto.

Cuando un usuario sube una foto, se le solicita un título y una categoría. El código PHP `guardar_foto.php` verifica si se ha enviado un archivo mediante el método POST y, en caso afirmativo, se obtiene la fecha actual, el nombre del archivo y la categoría seleccionada. Luego, se realiza la inserción de la foto en la base de datos con la fecha, título, nombre, tipo, tamaño y categoría correspondientes. Finalmente, se cierra la conexión con la base de datos.

El código PHP `guardar_foto.php` se encarga de:

- Verificar si se ha enviado un archivo mediante el método POST.
- Obtener la fecha actual.
- Obtener el nombre del archivo subido.
- Obtener la categoría seleccionada por el usuario.
- Realizar la inserción de la foto en la base de datos con los datos correspondientes.
- Cerrar la conexión con la base de datos.

El código PHP `guardar_foto.php` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

En resumen, el archivo `guardar_foto.php` es responsable de almacenar las fotos subidas en una base de datos SQLite y se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php`.

# Descripción del Directorio `inc`

El directorio `inc` es un componente esencial del software, ya que alberga los archivos PHP que generan los elementos de botones de categorías y la galería de fotos. Este directorio contiene los siguientes archivos:

- `botones_categorias.php`: genera los elementos de botones de categorías.
- `galeria_fotografias.php`: genera la galería de fotos.
- `guardar_foto.php`: almacena las fotos subidas en una base de datos SQLite.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

# Descripción del Directorio `js`

El directorio `js` es un componente esencial del software, ya que contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería. Este directorio también puede contener otros archivos relacionados con la interactividad y animaciones.

El archivo `codigo.js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

El archivo `codigo.js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

El directorio `js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

En resumen, el directorio `js` es un componente esencial del software, ya que contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería. Este archivo se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos.

# Descripción del Directorio `estilo`

El directorio `estilo` es un componente esencial del software, ya que alberga el archivo `estilo.css`, que define el aspecto visual del sitio web. Este directorio también puede contener otros archivos relacionados con el diseño y el estilo.

El archivo `estilo.css` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera el formulario de subida de fotos y maneja el diseño de la cabecera y los chips de categorías.

El directorio `estilo` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera el formulario de subida de fotos y maneja el diseño de la cabecera y los chips de categorías.

El directorio `estilo` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera el formulario de subida de fotos y maneja el diseño de la cabecera y los chips de categorías.

En resumen, el directorio `estilo` es un componente esencial del software, ya que alberga el archivo `estilo.css`, que define el aspecto visual del sitio web. Este archivo se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos.

# Descripción del Software en General

El software en cuestión es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

# Descripción del Archivo `guardar_foto.php`

El archivo `guardar_foto.php` es un componente esencial del software, ya que se encarga de almacenar las fotos subidas en una base de datos SQLite. Este archivo utiliza la tecnología PHP para interactuar con la base de datos y realizar la inserción de los datos de la foto.

Cuando un usuario sube una foto, se le solicita un título y una categoría. El código PHP `guardar_foto.php` verifica si se ha enviado un archivo mediante el método POST y, en caso afirmativo, se obtiene la fecha actual, el nombre del archivo y la categoría seleccionada. Luego, se realiza la inserción de la foto en la base de datos con los datos correspondientes. Finalmente, se cierra la conexión con la base de datos.

El código PHP `guardar_foto.php` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El archivo `guardar_foto.php` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

En resumen, el archivo `guardar_foto.php` es responsable de almacenar las fotos subidas en una base de datos SQLite y se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php`.

# Descripción del Directorio `inc`

El directorio `inc` es un componente esencial del software, ya que alberga los archivos PHP que generan los elementos de botones de categorías y la galería de fotos. Este directorio contiene los siguientes archivos:

- `botones_categorias.php`: genera los elementos de botones de categorías.
- `galeria_fotografias.php`: genera la galería de fotos.
- `guardar_foto.php`: almacena las fotos subidas en una base de datos SQLite.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

# Descripción del Directorio `js`

El directorio `js` es un componente esencial del software, ya que contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería. Este directorio también puede contener otros archivos relacionados con la interactividad y animaciones.

El archivo `codigo.js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

El archivo `codigo.js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

El directorio `js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

El directorio `estilo` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera el formulario de subida de fotos y maneja el diseño de la cabecera y los chips de categorías.

En resumen, el directorio `estilo` es un componente esencial del software, ya que alberga el archivo `estilo.css`, que define el aspecto visual del sitio web. Este archivo se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

# Descripción del Archivo `guardar_foto.php`

El archivo `guardar_foto.php` es un componente esencial del software, ya que se encarga de almacenar las fotos subidas en una base de datos SQLite. Este archivo utiliza la tecnología PHP para interactuar con la base de datos y realizar la inserción de los datos de la foto.

Cuando un usuario sube una foto, se le solicita un título y una categoría. El código PHP `guardar_foto.php` verifica si se ha enviado un archivo mediante el método POST y, en caso afirmativo, se obtiene la fecha actual, el nombre del archivo y la categoría seleccionada. Luego, se realiza la inserción de la foto en la base de datos con los datos correspondientes. Finalmente, se cierra la conexión con la base de datos.

El archivo `guardar_foto.php` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El archivo `guardar_foto.php` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

En resumen, el archivo `guardar_foto.php` es responsable de almacenar las fotos subidas en una base de datos SQLite y se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php`.

# Descripción del Directorio `inc`

El directorio `inc` es un componente esencial del software, ya que alberga los archivos PHP que generan los elementos de botones de categorías y la galería de fotos. Este directorio contiene los siguientes archivos:

- `botones_categorias.php`: genera los elementos de botones de categorías.
- `galeria_fotografias.php`: genera la galería de fotos.
- `guardar_foto.php`: almacena las fotos subidas en una base de datos SQLite.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

El directorio `inc` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea subir una foto. Este archivo genera el formulario de subida de fotos y maneja la lógica de subida y almacenamiento de imágenes.

# Descripción del Directorio `js`

El directorio `js` es un componente esencial del software, ya que contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería. Este directorio también puede contener otros archivos relacionados con la interactividad y animaciones.

El archivo `codigo.js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

El archivo `codigo.js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

El directorio `js` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera la galería de fotos y maneja la interactividad y animaciones de la misma.

El directorio `estilo` se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos. Este archivo genera el formulario de subida de fotos y maneja el diseño de la cabecera y los chips de categorías.

En resumen, el directorio `estilo` es un componente esencial del software, ya que alberga el archivo `estilo.css`, que define el aspecto visual del sitio web. Este archivo se relaciona con el resto del proyecto al ser llamado desde el archivo `galeria_fotografias.php` cuando un usuario desea visualizar la galería de fotos.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usueneros puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellala y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

En resumen, el software es una fototeca digital que ofrece una plataforma para subir, categorizar y visualizar fotos en una galería atractiva y organizada. Utiliza tecnologías web para su funcionamiento y proporciona una experiencia de usuario intuitiva y atractiva.

En resumen, el software es una fototeca digital que permite a los usuarios subir, categorizar y visualizar fotos en una galería interactiva. Está construido utilizando tecnologías web como HTML, CSS, JavaScript y PHP para su desarrollo y funcionamiento. Su objetivo es ofrecer una plataforma donde los usuarios puedan subir imágenes con títulos y categorías, navegar entre ellas y visualizar las fotos de manera atractiva y organizada. La galería presenta las fotos en un formato polaroid con efectos de rotaciones y animaciones para capturar la atencialidad del usuario. Además, el software incluye un modal para visualizar imágenes de manera detallada.

El software está organizado en un sistema de archivos con tres subdirectorios principales: `estilo`, `inc` y `js`. El directorio `estilo` contiene el archivo `estilo.css`, que define el aspecto visual del sitio web. El directorio `inc` alberga los archivos PHP `botones_categorias.php` y `galeria_fotografias.php`, que generan los elementos de botones de categorías y la galería de fotos respectivamente. El directorio `js` contiene el archivo `codigo.js`, que maneja la interactividad y animaciones de la galería.

El software utiliza tecnologías web para su funcionamiento. Estas tecnologías incluyen HTML para la estructura del sitio web, CSS para el estilo visual, JavaScript para la interactividad y animaciones, y PHP para la lógica de back-end y la gestión de la base de datos.

La interacción entre los componentes se realiza a través de eventos y funciones de JavaScript. Por ejemplo, cuando un usuario selecciona una categoría, se inicia una animación que oculta las fotos de otras categorías y muestra las fotos de la categoría seleccionada. Además, el software utiliza eventos de ratón para controlar la animación de la galería.

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

