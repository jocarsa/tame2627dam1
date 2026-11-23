<!doctype html>
<html>
	<head>
  	<style>
    	
      * {
          padding: 0;
          margin: 0;
          box-sizing: border-box;
      }

      body {
          background: #f0f0f2;
          font-family: Ubuntu, sans-serif;
          color: #252530;
          min-height: 100vh;
      }

      /* CONTENEDORES */

      header, main, footer {
          background: white;
          padding: 40px;
          margin: auto;
          width: 100%;
          max-width: 1200px;
      }

      /* CABECERA */

      header {
          margin-top: 40px;
          padding: 55px 40px;
          text-align: center;
          border-radius: 20px 20px 0 0;
          border-bottom: 1px solid #eee;
      }

      header h1 {
          font-size: 38px;
          font-weight: 300;
          letter-spacing: 3px;
          color: #292438;
      }

      header h1::after {
          content: "";
          display: block;
          width: 70px;
          height: 3px;
          background: indigo;
          margin: 22px auto 0;
          border-radius: 10px;
      }

      /* CATÁLOGO */

      main {
          display: grid;
          grid-template-columns: repeat(3, minmax(0, 1fr));
          gap: 25px;
          padding: 40px;
          align-items: stretch;
      }

      /* TARJETAS */

      main article {
          background: #fff;
          border: 1px solid #ededf0;
          border-radius: 16px;
          padding: 15px;
          display: flex;
          flex-direction: column;
          gap: 14px;
          overflow: hidden;
          transition:
              transform 0.3s ease,
              box-shadow 0.3s ease,
              border-color 0.3s ease;
      }

      main article:hover {
          transform: translateY(-7px);
          box-shadow: 0 18px 35px rgba(0,0,0,0.09);
          border-color: #d8cce8;
      }

      /* IMÁGENES */

      main article img {
          display: block;
          width: 100%;
          aspect-ratio: 1 / 1;
          object-fit: contain;
          background: linear-gradient(
              145deg,
              #f7f5fa,
              #eae6f0
          );
          border-radius: 12px;
          padding: 20px;
          transition: transform 0.4s ease;
      }

      main article:hover img {
          transform: scale(1.025);
      }

      /* NOMBRE DEL PERFUME */

      main article h4 {
          font-size: 19px;
          font-weight: 600;
          line-height: 1.4;
          color: #292438;
          letter-spacing: -0.3px;
      }

      /* DESCRIPCIÓN */

      main article p {
          font-size: 14px;
          line-height: 1.7;
          color: #777582;
          flex-grow: 1;
      }

      /* PRECIO */

      main article button {
          background: indigo;
          color: white;
          border: none;
          border-radius: 9px;
          padding: 14px 20px;
          width: 100%;
          font-family: inherit;
          font-size: 17px;
          font-weight: 600;
          cursor: pointer;
          transition:
              background 0.25s ease,
              transform 0.25s ease,
              box-shadow 0.25s ease;
      }

      main article button:hover {
          background: #6532a0;
          transform: translateY(-2px);
          box-shadow: 0 6px 15px rgba(75,0,130,0.2);
      }

      main article button:active {
          transform: scale(0.98);
      }

      /* PIE */

      footer {
          min-height: 90px;
          border-top: 1px solid #eee;
          border-radius: 0 0 20px 20px;
          margin-bottom: 40px;
      }

      /* TABLETS */

      @media (max-width: 900px) {
          header, main, footer {
              padding: 30px;
          }

          main {
              grid-template-columns: repeat(2, minmax(0, 1fr));
              gap: 20px;
          }

          header {
              margin-top: 0;
          }
      }

      /* MÓVILES */

      @media (max-width: 550px) {
          header, main, footer {
              padding: 20px;
          }

          header h1 {
              font-size: 28px;
          }

          main {
              grid-template-columns: 1fr;
              gap: 20px;
          }

          main article {
              padding: 14px;
          }

          header, footer {
              border-radius: 0;
          }

          footer {
              margin-bottom: 0;
          }
      }
		aside{
    	width:300px;
      height:500px;
      background:white;
      position:fixed;
      bottom:10px;
      right:10px;
    }
    </style>
  </head>
  <body>
    <header>
    	<h1>Tienda de perfumes</h1>
    </header>
    <main>
    	<?php
      	// Devuelve los productos que hay en la base de datos /////////////////////////////
        $db = new SQLite3('tienda.db');						// Abro la base de datos
        $peticion = "SELECT * FROM productos";		// Lo que le pido a la base de datos
        $resultado = $db->query($peticion);				// Petición a la base de datos
        while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {
            echo '<article>
            	<img src="producto.png">
              <h4>'.$fila['nombre'].'</h4>
              <p>'.$fila['descripcion'].'</p>
              <button 
              	precio="'.$fila['precio'].'"
                producto = "'.$fila['nombre'].'"
                
                >'.$fila['precio'].' €</button>
            </article>';
        }																				// Creo una tabla con los resultados
        $db->close();														// Ahora cierro la base de datos
        // Devuelve los productos que hay en la base de datos /////////////////////////////
      ?>
    </main>
    <footer>
    </footer>
    <aside>
    	Carrito
    </aside>
    <script>
    	// En Javascript voy a crear el carrito de compra
      let carrito = [];  		// El carrito es un array pero ahora mismo está vacío
      // Cuando pulse un boton, quiero añadir el producto al carrito
      // Selecciono todos los botones
      let botones = document.querySelectorAll("button");
      // Ya sabemos que cuando queremos recorrer algo que es "Muchos" es un foreach
      botones.forEach(function(boton){
      	boton.onclick = function(){				// Cuando haga click en el boton
        	console.log("Añado algo al carrito")
          // Como cada boton ahora transporta el precio y el nombre del producto
          // Añado un producto al carrito
          carrito.push(
          	{
            	"producto":boton.getAttribute("producto"),
              "precio":boton.getAttribute("precio")
            }
          )
          // Y ahora saco el carrito por consola
          console.log(carrito)
        }
      })
    </script>
  </body>
</html>








