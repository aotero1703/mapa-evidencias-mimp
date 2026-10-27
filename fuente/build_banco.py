# Genera las páginas del Banco de Evidencias (portada, tablero y fuentes) con la misma cabecera y pie.
# Uso: python3 fuente/build_banco.py   (desde la raíz del repositorio)
POWERBI="https://app.powerbi.com/view?r=eyJrIjoiZTdiNmUwZGItN2QzOS00OTY0LWExYWMtZWE1MzlhMTg1MjFmIiwidCI6IjY4MTljNDYzLTVkZWItNDA3MC1hY2I2LTlmZGQzY2FhZTk4NCJ9"
SITE="https://mapa-evidencias-mimp.vercel.app/"
ICON="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='26' fill='none' stroke='%232f3e8f' stroke-width='8'/%3E%3Ccircle cx='32' cy='32' r='11' fill='%23f2a93b' stroke='%23e5463c' stroke-width='4'/%3E%3C/svg%3E"

def head(title,desc,path=""):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:site_name" content="Observatorio Nacional · MIMP">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}og-banco.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="es_PE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}og-banco.png">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;600;700&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700;6..12,800&display=swap">
<link rel="stylesheet" href="banco.css">
</head>
<body>
'''
def header(cur):
    items=[('evidencia.html','Evidencia científica','ev'),('tablero.html','Indicadores','in'),('fuentes.html','Fuentes externas','fx')]
    nav=''.join(f'<a href="{h}"{" aria-current=\"page\"" if k==cur else ""}>{t}</a>' for h,t,k in items)
    return f'''<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="./" aria-label="Inicio del Banco de Evidencias">
      <img src="img/logo-mimp.png" alt="Ministerio de la Mujer y Poblaciones Vulnerables">
      <span class="sep"></span>
      <img class="on" src="img/logo-on.png" alt="Observatorio Nacional de la Violencia contra las Mujeres y los Integrantes del Grupo Familiar">
    </a>
    <nav class="site-nav" aria-label="Secciones del banco">{nav}</nav>
  </div>
</header>
'''
FOOTER='''<footer class="site-footer">
  <div class="wrap">
    <div class="partners">
      <span class="label">Elabora</span>
      <span class="chip"><img src="img/logo-mimp.png" alt="Ministerio de la Mujer y Poblaciones Vulnerables"></span>
      <span class="chip"><img src="img/logo-on.png" alt="Observatorio Nacional de la Violencia contra las Mujeres y los Integrantes del Grupo Familiar"></span>
    </div>
    <p class="fine">Banco de Evidencias del Observatorio Nacional de la Violencia contra las Mujeres y los Integrantes del Grupo Familiar, en el marco del artículo 43 de la Ley N.° 30364 y de los Lineamientos aprobados por la R.M. N.° 027-2025-MIMP.</p>
    <p class="fine">¿Consultas? <a href="https://www.gob.pe/institucion/mimp/tema/observatorio-nacional-de-la-violencia-contra-las-mujeres-y-los-integrantes-del-grupo-familiar" target="_blank" rel="noopener">Observatorio Nacional</a> · observatorioviolencia@mimp.gob.pe · (01) 626-1600, anexo 8503</p>
    <p class="visits" id="visits" hidden><span class="vdot" aria-hidden="true"></span><span><b id="visitsN"></b> visitas al banco de evidencias</span></p>
  </div>
</footer>
<script>
(async()=>{try{
  let nueva=true;try{nueva=!sessionStorage.getItem('bancoVisita');sessionStorage.setItem('bancoVisita','1')}catch(e){}
  const r=await fetch('/api/visitas',{method:nueva?'POST':'GET',cache:'no-store'});if(!r.ok)return;
  const {total}=await r.json();if(!total)return;
  document.getElementById('visitsN').textContent=total.toLocaleString('es-PE');document.getElementById('visits').hidden=false;
}catch(e){}})();
</script>
'''

ART_EV='''<svg class="art" viewBox="0 0 200 200" aria-hidden="true"><g fill="none" stroke="rgba(255,255,255,.22)" stroke-width="2">
<circle cx="120" cy="80" r="70"/><circle cx="120" cy="80" r="48"/></g>
<g fill="#fff"><rect x="62" y="40" width="16" height="16" rx="4" opacity=".35"/><rect x="84" y="40" width="16" height="16" rx="4" opacity=".7"/><rect x="106" y="40" width="16" height="16" rx="4" opacity=".2"/><rect x="128" y="40" width="16" height="16" rx="4" opacity=".9"/>
<rect x="62" y="62" width="16" height="16" rx="4" opacity=".9"/><rect x="84" y="62" width="16" height="16" rx="4" opacity=".2"/><rect x="106" y="62" width="16" height="16" rx="4" opacity=".55"/><rect x="128" y="62" width="16" height="16" rx="4" opacity=".2"/>
<rect x="62" y="84" width="16" height="16" rx="4" opacity=".2"/><rect x="84" y="84" width="16" height="16" rx="4" opacity=".55"/><rect x="106" y="84" width="16" height="16" rx="4" opacity=".9"/><rect x="128" y="84" width="16" height="16" rx="4" opacity=".35"/></g>
<circle cx="136" cy="70" r="5" fill="#f2a93b"/></svg>'''
ART_IN='''<svg class="art" viewBox="0 0 200 200" aria-hidden="true"><g fill="none" stroke="rgba(255,255,255,.22)" stroke-width="2"><circle cx="120" cy="80" r="70"/></g>
<g fill="#fff"><rect x="58" y="92" width="18" height="34" rx="3" opacity=".5"/><rect x="82" y="72" width="18" height="54" rx="3" opacity=".7"/><rect x="106" y="56" width="18" height="70" rx="3" opacity=".9"/><rect x="130" y="80" width="18" height="46" rx="3" opacity=".6"/></g>
<polyline points="67,78 91,58 115,44 139,64" fill="none" stroke="#f2a93b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="139" cy="64" r="5" fill="#f2a93b"/></svg>'''
ART_FX='''<svg class="art" viewBox="0 0 200 200" aria-hidden="true"><g fill="none" stroke="rgba(255,255,255,.22)" stroke-width="2"><circle cx="120" cy="80" r="70"/></g>
<g fill="none" stroke="#fff" stroke-width="3" opacity=".85"><ellipse cx="104" cy="50" rx="34" ry="11"/><path d="M70 50v58c0 6 15 11 34 11s34-5 34-11V50"/><path d="M70 79c0 6 15 11 34 11s34-5 34-11" opacity=".6"/></g>
<g stroke="#f2a93b" stroke-width="4" stroke-linecap="round" fill="none"><path d="M138 118l22 22"/><path d="M146 140h14v-14"/></g></svg>'''

INDEX=head('Banco de Evidencias · Observatorio Nacional','Evidencia científica, indicadores y fuentes de datos oficiales sobre la violencia contra las mujeres y los integrantes del grupo familiar. Observatorio Nacional, MIMP (Ley N.° 30364).')+header('')+f'''
<main>
<section class="hero" id="hero">
  <canvas id="heroCanvas" aria-hidden="true"></canvas>
  <div class="wrap">
    <div>
      <span class="eyebrow">Observatorio Nacional · Ley N.° 30364</span>
      <h1>Banco de Evidencias <span>sobre la violencia contra las mujeres y los integrantes del grupo familiar</span></h1>
      <p class="lede">Reúne en un solo lugar la evidencia científica, los indicadores y las fuentes de datos oficiales que el Observatorio usa para orientar las políticas de prevención y erradicación de la violencia.</p>
    </div>
    <div class="law">
      <q>Su misión es desarrollar un sistema de información permanente que brinde insumos para el diseño, implementación y gestión de políticas públicas.</q>
      <small>Ley N.° 30364, artículo 43</small>
    </div>
  </div>
</section>

<section class="doors" aria-label="Elige por dónde empezar">
  <div class="wrap">
    <a class="door ev" href="evidencia.html">
      <div class="top">{ART_EV}<span class="kicker">Evidencia científica</span></div>
      <div class="body">
        <h2>Estudios e investigaciones</h2>
        <p>Artículos, evaluaciones de impacto y revisiones nacionales e internacionales, con su ficha, sus resultados y el enlace al estudio original.</p>
        <div class="facts"><span>133 estudios</span><span>102 nacionales</span><span>23 evalúan intervenciones</span></div>
        <div class="basis"><b>Art. 43:</b> el Observatorio elabora informes, estudios y propuestas.</div>
        <span class="go">Buscar estudios <i>→</i></span>
      </div>
    </a>
    <a class="door in" href="tablero.html">
      <div class="top">{ART_IN}<span class="kicker">Datos e indicadores</span></div>
      <div class="body">
        <h2>Tablero de indicadores principales</h2>
        <p>Las cifras clave sobre violencia contra las mujeres y los integrantes del grupo familiar, con datos de las entidades del Sistema Nacional.</p>
        <div class="facts"><span>Indicadores principales</span><span>Power BI</span></div>
        <div class="basis"><b>Art. 43:</b> monitorear, recolectar, producir y sistematizar datos e información.</div>
        <span class="go">Ver el tablero <i>→</i></span>
      </div>
    </a>
    <a class="door fx" href="fuentes.html">
      <div class="top">{ART_FX}<span class="kicker">Fuentes externas</span></div>
      <div class="body">
        <h2>Datos oficiales de otras entidades</h2>
        <p>Acceso directo a las encuestas y registros del INEI, el Poder Judicial, el Ministerio Público y el Programa Warmi Ñan.</p>
        <div class="facts"><span>6 fuentes</span><span>Encuestas y registros</span></div>
        <div class="basis"><b>R.M. N.° 027-2025-MIMP:</b> articular la información de las entidades del Sistema Nacional.</div>
        <span class="go">Ver las fuentes <i>→</i></span>
      </div>
    </a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Marco normativo</h2>
    <p class="section-lede">El banco forma parte del sistema de información que la ley encarga al Observatorio, para que las decisiones de política pública se basen en evidencia.</p>
    <div class="norms">
      <div class="norm"><b>Ley N.° 30364</b><p>Ley para prevenir, sancionar y erradicar la violencia contra las mujeres y los integrantes del grupo familiar. Su artículo 43 crea el Observatorio Nacional.</p></div>
      <div class="norm"><b>R.M. N.° 027-2025-MIMP</b><p>Lineamientos para el funcionamiento del Observatorio: gestionar información y conocimiento y facilitar la toma de decisiones basadas en evidencia.</p></div>
      <div class="norm"><b>Sistema Nacional</b><p>El Observatorio articula la información de las entidades que previenen, atienden, protegen y sancionan la violencia.</p></div>
    </div>
  </div>
</section>
</main>
'''+FOOTER+'''<script>
/* anillos del logo del Observatorio en el fondo de la portada */
(function(){const hero=document.getElementById('hero'),cv=document.getElementById('heroCanvas'),ctx=cv.getContext('2d');
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches,C=['#3b4c9e','#7ec4d4','#e5463c','#f2a93b'];let w,h,cx,cy,R,dots=[],mx=0,my=0,t0=performance.now();
function size(){const d=Math.min(devicePixelRatio||1,2);w=hero.clientWidth;h=hero.clientHeight;cv.width=w*d;cv.height=h*d;ctx.setTransform(d,0,0,d,0,0);
 cx=w<900?w*.86:w*.62;cy=h*.42;R=Math.max(h*.5,240);dots=Array.from({length:w<640?22:44},(_,i)=>({ring:i%4,a:Math.random()*6.283,s:(Math.random()*.6+.4)*(i%2?1:-1),r:Math.random()*1.8+1.2}))}
function f(now){const t=(now-t0)/1000;ctx.clearRect(0,0,w,h);const px=mx*12,py=my*8;
 for(let i=0;i<4;i++){const rr=R*(1-i*.2),gap=.9+i*.15,rot=t*.04*(i%2?-1:1)+i;ctx.beginPath();ctx.arc(cx+px*(i+1)/4,cy+py*(i+1)/4,rr,rot+gap/2,rot+6.283-gap/2);
  ctx.strokeStyle=C[i];ctx.globalAlpha=.12+i*.03;ctx.lineWidth=Math.max(10,rr*.11);ctx.lineCap='round';ctx.stroke()}
 for(const d of dots){const rr=R*(1-d.ring*.2);d.a+=reduce?0:d.s*.0016;ctx.beginPath();ctx.arc(cx+px*(d.ring+1)/4+Math.cos(d.a)*rr,cy+py*(d.ring+1)/4+Math.sin(d.a)*rr,d.r,0,6.283);ctx.fillStyle=C[(d.ring+1)%4];ctx.globalAlpha=.6;ctx.fill()}
 ctx.globalAlpha=1;if(!reduce)requestAnimationFrame(f)}
size();addEventListener('resize',size);hero.addEventListener('mousemove',e=>{const r=hero.getBoundingClientRect();mx=(e.clientX-r.left)/r.width-.5;my=(e.clientY-r.top)/r.height-.5});requestAnimationFrame(f)})();
</script>
</body>
</html>
'''

TABLERO=head('Indicadores principales · Banco de Evidencias','Tablero de indicadores principales sobre la violencia contra las mujeres y los integrantes del grupo familiar. Observatorio Nacional, MIMP.','tablero.html')+header('in')+f'''
<main>
<section class="page-hero in">
  <div class="wrap">
    <a class="crumb" href="./">← Banco de Evidencias</a>
    <h1>Tablero de indicadores principales</h1>
    <p>Las cifras clave sobre la violencia contra las mujeres y los integrantes del grupo familiar. Usa los filtros del tablero para explorar cada indicador.</p>
    <div class="actions"><a class="btn btn-light" href="{POWERBI}" target="_blank" rel="noopener">Abrir en pantalla completa ↗</a></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="embed">
      <div class="frame"><iframe title="Tablero de indicadores principales del Observatorio Nacional" src="{POWERBI}" allowfullscreen loading="lazy"></iframe></div>
      <div class="cap"><span>Tablero publicado en Power BI.</span><span>Si no carga, ábrelo en pantalla completa.</span></div>
    </div>
  </div>
</section>
</main>
'''+FOOTER+'</body>\n</html>\n'

SRC=[('Encuestas nacionales','Encuestas',[
  ('INEI','Encuesta Demográfica y de Salud Familiar (ENDES)','Prevalencia de violencia familiar contra mujeres de 15 a 49 años y castigo físico a hijas e hijos, con resultados nacionales y por región.','https://proyectos.inei.gob.pe/endes/'),
  ('INEI','Microdatos por encuesta','Bases de datos de ENDES, ENARES, ENAHO y otras encuestas para hacer análisis propios.','https://proyectos.inei.gob.pe/microdatos/Consulta_por_Encuesta.asp')]),
 ('Registros administrativos','Registros',[
  ('Programa Warmi Ñan · MIMP','Banco de datos del Portal Estadístico','Casos atendidos en los Centros Emergencia Mujer y Familia y en los demás servicios del programa.','https://portalestadistico.warminan.gob.pe/banco-de-datos/'),
  ('Ministerio Público','Casos fiscales en fiscalías especializadas','Indicadores de las fiscalías especializadas en violencia contra las mujeres y los integrantes del grupo familiar.','https://portal.mpfn.gob.pe/pedmp/index.php/indicador/fiscalias-especializadas/18'),
  ('Poder Judicial','Portal Estadístico','Estadísticas judiciales, entre ellas los procesos y medidas de protección por violencia familiar.','https://portalestadistico.pj.gob.pe/')]),
 ('Ministerio de la Mujer','MIMP',[
  ('MIMP · gob.pe','Datos y evidencias','Página del Ministerio con datos, estudios y evidencias sobre las poblaciones que atiende.','https://www.gob.pe/75037-datos-y-evidencias')])]
from urllib.parse import urlparse
groups=''
for g,tag,items in SRC:
    cards=''.join(f'''<a class="src" href="{u}" target="_blank" rel="noopener"><span class="ent">{e}</span><h3>{t}</h3><p>{d}</p><span class="dom">{urlparse(u).netloc} ↗</span></a>''' for e,t,d,u in items)
    groups+=f'<div class="group"><h2>{g} <span class="tag">{tag}</span></h2><div class="src-grid">{cards}</div></div>\n'
FUENTES=head('Fuentes externas · Banco de Evidencias','Acceso directo a las fuentes oficiales de datos sobre violencia contra las mujeres y los integrantes del grupo familiar: INEI, Poder Judicial, Ministerio Público y Warmi Ñan.','fuentes.html')+header('fx')+f'''
<main>
<section class="page-hero fx">
  <div class="wrap">
    <a class="crumb" href="./">← Banco de Evidencias</a>
    <h1>Fuentes externas de datos</h1>
    <p>Las encuestas y registros oficiales de las entidades del Sistema Nacional. Cada enlace te lleva al sitio de la entidad que produce los datos.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
{groups}  </div>
</section>
</main>
'''+FOOTER+'</body>\n</html>\n'


EVID=head('Evidencia científica · Banco de Evidencias','Estudios nacionales e internacionales sobre igualdad de oportunidades, sistema de cuidados y violencia contra las mujeres y los integrantes del grupo familiar, con ficha y resultados.','evidencia.html')+header('ev')+'''
<main>
<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="./">← Banco de Evidencias</a>
    <h1>Evidencia científica</h1>
    <p>Estudios nacionales e internacionales revisados por el Observatorio. Busca por tema, población o palabra clave, y abre la ficha de cada estudio para ver qué se evaluó y qué se encontró.</p>
    <div class="actions"><a class="btn btn-light" href="matriz/Matriz_evidencias_MIMP_revisada.xlsx" download>Descargar la matriz (Excel)</a></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="levels" aria-label="Niveles de evidencia">
      <div class="A"><b>A</b><strong>Más sólida.</strong> Metaanálisis, revisiones sistemáticas y ensayos aleatorios.</div>
      <div class="B"><b>B</b><strong>Cuasi-experimental.</strong> Regresión discontinua, variables instrumentales, panel, emparejamiento.</div>
      <div class="C"><b>C</b><strong>Observacional.</strong> Factores asociados, correlaciones, registros administrativos.</div>
      <div class="D"><b>D</b><strong>Exploratoria.</strong> Estudios cualitativos, opinión de expertos y marcos conceptuales.</div>
    </div>
    <div class="lib">
      <aside class="filters" aria-label="Filtros">
        <h3>Tema</h3><div id="fTem"></div>
        <h3>Nivel de evidencia</h3><div id="fLv"></div>
        <h3>Ámbito</h3><div id="fAmb"></div>
        <h3>Tipo de estudio</h3><div id="fInt"></div>
        <h3>Dimensión</h3><div id="fDim"></div>
        <button type="button" class="clear" id="clear">Quitar filtros</button>
      </aside>
      <div>
        <div class="searchbar">
          <input type="search" id="q" placeholder="Buscar: Cuna Más, Línea 100, alcohol, adolescentes…" aria-label="Buscar estudios">
          <select id="sort" aria-label="Ordenar"><option value="y">Más recientes primero</option><option value="lv">Evidencia más sólida primero</option><option value="t">Por título (A–Z)</option></select>
        </div>
        <p class="count" id="count"></p>
        <div class="cards" id="cards"></div>
        <button type="button" class="more" id="more" hidden>Ver más estudios</button>
      </div>
    </div>
  </div>
</section>
</main>
'''+FOOTER+r'''<script>
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const nac=r=>r.o==='peru'||r.o==='multi';
const amb=r=>nac(r)?'Nacional':(r.o==='intl'?'Internacional':'Sin dato');
const LV={A:'A · Más sólida',B:'B · Cuasi-experimental',C:'C · Observacional',D:'D · Exploratoria'};
let R=[],S={tem:new Set(),lv:new Set(),amb:new Set(),int:new Set(),dim:new Set(),q:'',sort:'y',open:null,shown:20};
function gist(r){const t=(r.res||r.prop||'').replace(/\s+/g,' ').trim();const m=t.match(/^.{40,280}?[.;](\s|$)/);return m?m[0].trim():(t.length>260?t.slice(0,260).trim()+'…':t)}
function pass(r,skip){const q=S.q.trim().toLowerCase();
  return (skip==='tem'||!S.tem.size||S.tem.has(r.tem))&&(skip==='lv'||!S.lv.size||S.lv.has(r.g))&&(skip==='amb'||!S.amb.size||S.amb.has(amb(r)))
   &&(skip==='int'||!S.int.size||S.int.has(r.tipo?'Evalúa una intervención':'Otros estudios'))&&(skip==='dim'||!S.dim.size||S.dim.has(r.dim))
   &&(!q||[r.t,r.a,r.dim,r.tem,r.pob,r.prop,r.res,r.tipo,r.vy,r.vx,r.paises.join(' ')].join(' ').toLowerCase().includes(q))}
function facet(id,key,vals,lab){const c={};R.filter(r=>pass(r,key)).forEach(r=>{const v=vals(r);c[v]=(c[v]||0)+1});
  const all=[...new Set(R.map(vals))];const order=key==='lv'?['A','B','C','D']:all.sort((a,b)=>(c[b]||0)-(c[a]||0)||a.localeCompare(b));
  $(id).innerHTML=order.filter(v=>key!=='dim'||S.tem.size===0||R.some(r=>r.dim===v&&S.tem.has(r.tem))).map(v=>`<label><input type="checkbox" data-k="${key}" value="${esc(v)}" ${S[key].has(v)?'checked':''}><span>${esc(lab?lab(v):v)}</span><em>${c[v]||0}</em></label>`).join('')}
function render(){
  facet('fTem','tem',r=>r.tem);facet('fLv','lv',r=>r.g,v=>LV[v]);facet('fAmb','amb',amb);facet('fInt','int',r=>r.tipo?'Evalúa una intervención':'Otros estudios');facet('fDim','dim',r=>r.dim);
  document.querySelectorAll('.filters input').forEach(i=>i.onchange=()=>{const s=S[i.dataset.k];i.checked?s.add(i.value):s.delete(i.value);if(i.dataset.k==='tem')S.dim.clear();S.shown=20;render()});
  let L=R.filter(r=>pass(r));
  L.sort(S.sort==='lv'?(a,b)=>a.sub.localeCompare(b.sub)||(+b.y||0)-(+a.y||0):S.sort==='t'?(a,b)=>a.t.localeCompare(b.t,'es'):(a,b)=>(+b.y||0)-(+a.y||0));
  const p=L.filter(nac).length;
  $('count').innerHTML=`<b>${L.length}</b> ${L.length===1?'estudio':'estudios'}${L.length?` · ${p} nacionales · ${(k=>k+(k===1?' evalúa':' evalúan'))(L.filter(r=>r.tipo).length)} una intervención`:''}`;
  $('cards').innerHTML=L.length?L.slice(0,S.shown).map(card).join(''):'<div class="empty">No hay estudios con esos filtros. Prueba con otra palabra o quita algún filtro.</div>';
  $('more').hidden=L.length<=S.shown;$('more').textContent=`Ver más estudios (${L.length-S.shown} restantes)`;
  document.querySelectorAll('.paper [data-open]').forEach(b=>b.onclick=()=>{const n=+b.dataset.open;S.open=S.open===n?null:n;render()});
}
function card(r){const o=S.open===r.n,au=r.a?r.a.split(';')[0].trim()+(r.a.includes(';')?' et al.':''):'Autor no registrado';
  const pais=nac(r)?'Perú':(r.paises.length>2?'Varios países':r.paises.join(', ')||'País no registrado');
  const f=(t,v)=>v?`<dt>${t}</dt><dd>${esc(v)}</dd>`:'';
  return `<article class="paper"><div class="tags"><span class="tag lv ${r.g}">Nivel ${r.sub}</span><span class="tag">${esc(r.subl)}</span><span class="tag ${nac(r)?'pe':'int'}">${esc(pais)}</span>${r.tipo?'<span class="tag iv">Evalúa una intervención</span>':''}</div>
   <h3>${esc(r.t)}</h3><div class="by">${esc(au)} · ${esc(r.y||'s. f.')} · ${esc(r.tem)}${r.dim?' / '+esc(r.dim):''}</div>
   <p class="gist">${esc(gist(r))}</p>
   <div class="row"><button type="button" data-open="${r.n}" aria-expanded="${o}">${o?'Cerrar ficha':'Ver ficha completa'}</button>${r.link?`<a href="${esc(r.link)}" target="_blank" rel="noopener">Leer el estudio ↗</a>`:''}</div>
   ${o?`<dl>${f('Autoría',r.a)}${f('Población',r.pob)}${f('Propósito',r.prop)}${f('Intervención',[r.tipo,r.det].filter(Boolean).join('\n\n'))}${f('Diseño de aleatorización',r.ale)}${f('Estado de la evaluación',r.est)}${f('Qué se mide (Y)',r.vy)}${f('Qué lo explica (X)',r.vx)}${f('Resultados',r.res)}${f('Publicado en',r.pub)}${f('N.° en la matriz',String(r.n))}</dl>`:''}</article>`}
$('q').oninput=e=>{S.q=e.target.value;S.shown=20;render()};
$('sort').onchange=e=>{S.sort=e.target.value;render()};
$('more').onclick=()=>{S.shown+=20;render()};
$('clear').onclick=()=>{['tem','lv','amb','int','dim'].forEach(k=>S[k].clear());S.q='';$('q').value='';S.shown=20;render()};
fetch('data/estudios.json').then(r=>r.json()).then(d=>{R=d.rows;render()}).catch(()=>{$('cards').innerHTML='<div class="empty">No se pudieron cargar los estudios. Recarga la página.</div>'});
</script>
</body>
</html>
'''

for name,html in (('evidencia.html',EVID),('index.html',INDEX),('tablero.html',TABLERO),('fuentes.html',FUENTES)):
    open(name,'w',encoding='utf-8').write(html)
print('ok')
