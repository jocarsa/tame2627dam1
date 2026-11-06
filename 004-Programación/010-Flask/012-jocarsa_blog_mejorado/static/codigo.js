const destino=document.getElementById('articulos');
fetch('/articulos').then(r=>{if(!r.ok)throw Error('Error al consultar artículos');return r.json()}).then(datos=>{
 destino.replaceChildren();
 if(!datos.length){const p=document.createElement('p');p.className='loading';p.textContent='Todavía no hay publicaciones.';destino.append(p);return;}
 datos.forEach((articulo,i)=>{
  const item=document.createElement('article');
  const num=document.createElement('span');num.className='article-index';num.textContent=String(i+1).padStart(2,'0');
  const body=document.createElement('div');body.className='article-body';
  const fecha=document.createElement('time');fecha.textContent=articulo.fecha||'';
  const titulo=document.createElement('h3');titulo.textContent=articulo.titulo||'';
  const texto=document.createElement('p');texto.textContent=articulo.contenido||'';
  body.append(fecha,titulo,texto);item.append(num,body);destino.append(item);
 });
}).catch(()=>{destino.textContent='No se pudieron cargar las publicaciones. Inténtalo de nuevo más tarde.'});
