const productos = JSON.parse(document.getElementById('datosProductos').textContent);
const mapa = new Map(productos.map(p => [p.id, p]));
let carrito;
try { carrito = JSON.parse(localStorage.getItem('sportlab_cart') || '{}'); } catch { carrito = {}; }
const $ = s => document.querySelector(s);
const euro = n => new Intl.NumberFormat('es-ES',{style:'currency',currency:'EUR'}).format(n);
const guardar = () => localStorage.setItem('sportlab_cart', JSON.stringify(carrito));
function pintar(){
  let total=0, unidades=0;
  const cont=$('#itemsCarrito'); cont.replaceChildren();
  for(const [id, qty] of Object.entries(carrito)){
    const p=mapa.get(Number(id)); if(!p || qty<=0) continue;
    const n=Math.min(qty,p.stock); if(!n) continue;
    unidades+=n; total+=p.precio*n;
    const fila=document.createElement('div'); fila.className='cart-line';
    const info=document.createElement('div');
    const titulo=document.createElement('strong'); titulo.textContent=p.nombre;
    const precio=document.createElement('small'); precio.textContent=euro(p.precio)+' / unidad';
    info.append(titulo,precio);
    const controls=document.createElement('div'); controls.className='qty';
    const minus=document.createElement('button'); minus.textContent='−'; minus.type='button'; minus.onclick=()=>cambiar(id,-1);
    const number=document.createElement('span'); number.textContent=n;
    const plus=document.createElement('button'); plus.textContent='+'; plus.type='button'; plus.disabled=n>=p.stock; plus.onclick=()=>cambiar(id,1);
    controls.append(minus,number,plus); fila.append(info,controls); cont.append(fila);
  }
  if(!unidades) cont.textContent='Tu bolsa está vacía. Añade algo del catálogo.';
  $('#contador').textContent=unidades; $('#total').textContent=euro(total);
  $('#comprar').disabled=!unidades;
}
function cambiar(id,d){const p=mapa.get(Number(id));if(!p)return;const n=Math.max(0,Math.min(p.stock,(carrito[id]||0)+d));if(n)carrito[id]=n;else delete carrito[id];guardar();pintar();}
function abrir(){ $('#drawer').classList.add('open');$('#drawer').setAttribute('aria-hidden','false');$('#overlay').hidden=false; }
function cerrar(){ $('#drawer').classList.remove('open');$('#drawer').setAttribute('aria-hidden','true');$('#overlay').hidden=true; }
$('.cart-trigger').onclick=abrir;$('#cerrarCarrito').onclick=cerrar;$('#overlay').onclick=cerrar;
document.addEventListener('keydown',e=>{if(e.key==='Escape')cerrar()});
document.querySelectorAll('.add').forEach(b=>b.onclick=()=>{cambiar(b.dataset.id,1);abrir()});
$('#checkout').onsubmit=async e=>{
  e.preventDefault();const boton=$('#comprar'),msg=$('#mensaje');msg.textContent='';
  const f=new FormData(e.target); const items=Object.entries(carrito).filter(([id,q])=>q>0).map(([id,cantidad])=>({id:Number(id),cantidad}));
  if(!items.length)return;boton.disabled=true;boton.textContent='PROCESANDO...';
  try{
    const r=await fetch('/api/pedidos',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({cliente:Object.fromEntries(f.entries()),items})});
    const data=await r.json();if(!r.ok)throw new Error(data.error||'Error en el pedido');
    carrito={};guardar();pintar();e.target.reset();msg.textContent=`Pedido #${data.pedido_id} registrado correctamente. Total: ${euro(data.total)}.`;
  }catch(err){msg.textContent=err.message}finally{boton.textContent='CONFIRMAR PEDIDO ↗';boton.disabled=!Object.keys(carrito).length}
};
pintar();
