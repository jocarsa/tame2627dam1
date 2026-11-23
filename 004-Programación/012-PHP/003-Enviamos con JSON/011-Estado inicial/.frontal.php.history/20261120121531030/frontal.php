
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tienda de perfumes</title>

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

        /* CARRITO */

        aside {
            width: 340px;
            max-height: 500px;
            background: white;
            position: fixed;
            bottom: 20px;
            right: 20px;
            padding: 25px;
            border-radius: 18px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.18);
            z-index: 100;

            display: flex;
            flex-direction: column;
            gap: 20px;

            opacity: 0;
            transform: translateY(40px) scale(0.95);
            pointer-events: none;
            visibility: hidden;

            transition:
                opacity 0.35s ease,
                transform 0.35s ease,
                visibility 0.35s;
        }

        /* CARRITO VISIBLE */

        aside.visible {
            opacity: 1;
            transform: translateY(0) scale(1);
            pointer-events: auto;
            visibility: visible;
        }

        /* CABECERA CARRITO */

        .cabecera-carrito {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
        }

        .cabecera-carrito h2 {
            font-size: 21px;
            font-weight: 600;
            color: #292438;
        }

        .contador-carrito {
            background: indigo;
            color: white;
            border-radius: 20px;
            padding: 5px 10px;
            font-size: 12px;
            font-weight: bold;
        }

        /* LISTA DE PRODUCTOS */

        #productos-carrito {
            overflow-y: auto;
            min-height: 0;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        /* PRODUCTO INDIVIDUAL */

        .producto-carrito {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            padding: 12px;
            background: #f7f6f9;
            border-radius: 10px;
            animation: aparecer 0.3s ease;
        }

        .producto-carrito .nombre {
            font-size: 13px;
            font-weight: 500;
            flex: 1;
            line-height: 1.4;
        }

        .producto-carrito .precio {
            font-size: 14px;
            font-weight: 600;
            color: indigo;
            white-space: nowrap;
        }

        /* BOTÓN ELIMINAR */

        .producto-carrito .eliminar {
            background: transparent;
            border: none;
            color: #aaa;
            cursor: pointer;
            font-size: 21px;
            padding: 2px 5px;
            transition: color 0.2s;
        }

        .producto-carrito .eliminar:hover {
            color: #d33;
        }

        /* TOTAL */

        .total-carrito {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #eee;
            padding-top: 18px;
            font-size: 16px;
        }

        .total-carrito strong {
            font-size: 24px;
            color: indigo;
        }

        /* FINALIZAR COMPRA */

        .finalizar-compra {
            background: indigo;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 15px;
            font-family: inherit;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition:
                background 0.2s,
                transform 0.2s;
        }

        .finalizar-compra:hover {
            background: #6532a0;
            transform: translateY(-2px);
        }

        /* ANIMACIONES */

        @keyframes aparecer {
            from {
                opacity: 0;
                transform: translateY(10px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
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

            aside {
                width: calc(100% - 30px);
                right: 15px;
                bottom: 15px;
                max-height: 70vh;
            }
        }
    </style>
</head>

<body>

    <header>
        <h1>Tienda de perfumes</h1>
    </header>

    <main>
        <?php

        // Devuelve los productos que hay en la base de datos

        $db = new SQLite3('tienda.db');

        $peticion = "SELECT * FROM productos";

        $resultado = $db->query($peticion);

        while ($fila = $resultado->fetchArray(SQLITE3_ASSOC)) {

            $nombre = htmlspecialchars($fila['nombre'], ENT_QUOTES, 'UTF-8');
            $descripcion = htmlspecialchars($fila['descripcion'], ENT_QUOTES, 'UTF-8');
            $precio = (float)$fila['precio'];

            echo '
            <article>

                <img src="producto.png" alt="'.$nombre.'">

                <h4>'.$nombre.'</h4>

                <p>'.$descripcion.'</p>

                <button
                    precio="'.$precio.'"
                    producto="'.$nombre.'"
                >
                    '.number_format($precio, 2, ',', '.').' €
                </button>

            </article>';
        }

        $db->close();

        ?>
    </main>

    <footer>
    </footer>

    <!-- CARRITO DE COMPRA -->

    <aside id="carrito">

        <div class="cabecera-carrito">
            <h2>🛍 Mi carrito</h2>
            <span class="contador-carrito" id="contador">0</span>
        </div>

        <div id="productos-carrito"></div>

        <div class="total-carrito">
            <span>Total</span>
            <strong id="total">0,00 €</strong>
        </div>

        <button class="finalizar-compra" id="finalizar_compra">
            Finalizar compra
        </button>

    </aside>

    <script>

        // En Javascript voy a crear el carrito de compra

        let carrito = [];

        // Selecciono todos los botones de los productos

        let botones = document.querySelectorAll("main article button");

        // Selecciono los elementos del carrito

        let aside = document.querySelector("aside");
        let contenedor = document.querySelector("#productos-carrito");
        let total = document.querySelector("#total");
        let contador = document.querySelector("#contador");

        // Formateo los precios en euros

        function formatearPrecio(precio) {

            return precio.toLocaleString("es-ES", {
                style: "currency",
                currency: "EUR"
            });

        }

        // Cuando pulse un botón, añado el producto

        botones.forEach(function(boton) {

            boton.onclick = function() {

                // Añado el producto al carrito

                carrito.push({
                    "producto": boton.getAttribute("producto"),
                    "precio": parseFloat(boton.getAttribute("precio"))
                });

                // Actualizo visualmente el carrito

                actualizarCarrito();

            };

        });

        // Función para actualizar el carrito

        function actualizarCarrito() {

            // Vacío la representación anterior

            contenedor.innerHTML = "";

            // Acumulador del precio total

            let suma = 0;

            // Recorro los productos del carrito

            carrito.forEach(function(producto, indice) {

                suma += producto.precio;

                // Creo una fila para cada producto

                let fila = document.createElement("div");
                fila.className = "producto-carrito";

                // Nombre

                let nombre = document.createElement("span");
                nombre.className = "nombre";
                nombre.textContent = producto.producto;

                // Precio

                let precio = document.createElement("span");
                precio.className = "precio";
                precio.textContent = formatearPrecio(producto.precio);

                // Botón para eliminar

                let eliminar = document.createElement("button");
                eliminar.className = "eliminar";
                eliminar.textContent = "×";
                eliminar.setAttribute(
                    "aria-label",
                    "Eliminar " + producto.producto
                );

                eliminar.onclick = function() {

                    // Elimino el producto del array

                    carrito.splice(indice, 1);

                    // Actualizo el carrito

                    actualizarCarrito();

                };

                // Introduzco los elementos en la fila

                fila.appendChild(nombre);
                fila.appendChild(precio);
                fila.appendChild(eliminar);

                // Introduzco la fila en el carrito

                contenedor.appendChild(fila);

            });

            // Actualizo el total

            total.textContent = formatearPrecio(suma);

            // Actualizo el contador

            contador.textContent = carrito.length;

            // Muestro el carrito solamente si hay productos

            if (carrito.length > 0) {

                aside.classList.add("visible");

            } else {

                aside.classList.remove("visible");

            }

            // Muestro el carrito por consola

            console.log(carrito);

        }
				// Cuando pulse el boton de finalizar, enviamos el pedido al servidor para guardarlo
        	// Primero cojo el boton
        		let boton_finalizar = document.querySelector("#finalizar_compra")
        
    </script>

</body>
</html>
