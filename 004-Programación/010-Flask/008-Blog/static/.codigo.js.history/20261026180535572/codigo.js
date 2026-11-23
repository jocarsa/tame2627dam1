 let principal = document.querySelector("main")
      fetch("/articulos")
      .then(function(resultado){return resultado.json()}) // Lo que viene, viene como json
      .then(function(datos){
      	datos.forEach(function(articulo){ // Para cada uno de los articulos que han llegado
          // A principal, añadele algo
        	principal.innerHTML += `
          	<article>
            	<h3>`+articulo.titulo+`</h3>
              <time>`+articulo.fecha+`</time>
              <p>`+articulo.contenido+`</p>
            </article>
          `	// Te voy a añadir un artículo
        })
      })