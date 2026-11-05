# Paso 3: genera las páginas del Banco de Evidencias (portada, tablero y fuentes) con la misma cabecera y pie.
# Uso: python3 fuente/build_banco.py   (desde la raíz del repositorio)
POWERBI="https://app.powerbi.com/view?r=eyJrIjoiZTdiNmUwZGItN2QzOS00OTY0LWExYWMtZWE1MzlhMTg1MjFmIiwidCI6IjY4MTljNDYzLTVkZWItNDA3MC1hY2I2LTlmZGQzY2FhZTk4NCJ9"
SITE="https://banco-evidencias-mimp.vercel.app/"
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
    items=[('comprender-violencia.html','Tipos y modalidades','cv'),('evidencia.html','Evidencia científica','ev'),('tablero.html','Indicadores','in'),('fuentes.html','Fuentes externas','fx'),('servicios.html','Servicios','sv')]
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

ART_SV='''<svg class="art" viewBox="0 0 200 200" aria-hidden="true"><g fill="none" stroke="rgba(255,255,255,.22)" stroke-width="2"><circle cx="120" cy="80" r="70"/><circle cx="120" cy="80" r="46"/></g>
<path d="M70 120 C 95 120, 95 80, 120 80 S 145 40, 170 40" fill="none" stroke="rgba(255,255,255,.75)" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 12"/>
<circle cx="70" cy="120" r="10" fill="#fff"/><circle cx="120" cy="80" r="10" fill="#fff" fill-opacity=".85"/><circle cx="170" cy="40" r="12" fill="#f2a93b"/></svg>'''
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
        <p>Investigaciones para comprender la violencia y programas evaluados para saber qué ayuda a enfrentarla, en el marco de la Ley N.° 30364.</p>
        <div class="facts"><span>Programas evaluados</span><span>Estudios sobre violencia</span></div>
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
    <a class="door sv" href="servicios.html">
      <div class="top">{ART_SV}<span class="kicker">Servicios</span></div>
      <div class="body">
        <h2>Servicios frente a la violencia</h2>
        <p>Qué hace el Estado en cada paso, de la prevención a la reparación, y qué dicen los estudios sobre esos servicios.</p>
        <div class="facts"><span>Ruta en 7 pasos</span><span>Catálogo 2026</span></div>
        <div class="basis"><b>Ley N.° 30364:</b> identifica los servicios pertinentes para la prevención y respuesta frente a la violencia.</div>
        <span class="go">Conocer los servicios <i>→</i></span>
      </div>
    </a>
  </div>
</section>
<section class="guide-band" aria-label="Guía de tipos y modalidades">
  <div class="wrap">
    <a class="gb" href="comprender-violencia.html">
      <div class="gb-copy">
        <span class="gb-k">Antes de explorar</span>
        <h2>Tipo y modalidad: dos formas de describir un mismo hecho</h2>
        <p>El <b>tipo</b> dice qué daño se produce. La <b>modalidad</b> dice en qué relación o contexto ocurre. Una misma situación tiene las dos.</p>
        <span class="go">Ver la guía con ejemplos <i>→</i></span>
      </div>
      <div class="gb-art" aria-hidden="true">
        <div class="gb-row"><span class="gb-tag m">En la pareja</span><span class="gb-dot on">Física</span><span class="gb-dot on">Psicológica</span><span class="gb-dot">Sexual</span><span class="gb-dot on">Económica</span></div>
        <div class="gb-row"><span class="gb-tag m">Hostigamiento</span><span class="gb-dot">Física</span><span class="gb-dot on">Psicológica</span><span class="gb-dot on">Sexual</span><span class="gb-dot">Económica</span></div>
        <div class="gb-row"><span class="gb-tag m">Por redes y TIC</span><span class="gb-dot">Física</span><span class="gb-dot on">Psicológica</span><span class="gb-dot on">Sexual</span><span class="gb-dot">Económica</span></div>
      </div>
    </a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Marco normativo y alcance</h2><p class="section-lede">La Ley N.° 30364 orienta qué evidencia se incorpora, cómo se clasifica y para qué decisiones puede resultar útil. Los recursos generales del sector se presentan como información complementaria.</p>
    <p class="section-lede">El banco forma parte del sistema de información que la ley encarga al Observatorio, para facilitar el acceso a evidencia pertinente para la prevención y respuesta frente a la violencia.</p>
    <div class="norms">
      <a class="norm" href="https://www.gob.pe/74905-ley-n-30364-ley-para-prevenir-sancionar-y-erradicar-la-violencia-contra-las-mujeres-y-los-integrantes-del-grupo-familiar" target="_blank" rel="noopener"><b>Ley N.° 30364</b><p>Ley para prevenir, sancionar y erradicar la violencia contra las mujeres y los integrantes del grupo familiar. Su artículo 43 crea el Observatorio Nacional.</p><span class="nlink">Leer la ley ↗</span></a>
      <a class="norm" href="https://cdn.www.gob.pe/uploads/document/file/7588151/6439639-anexo-rm-n-027-2025-mimp.pdf?v=1738852952" target="_blank" rel="noopener"><b>R.M. N.° 027-2025-MIMP</b><p>Lineamientos para el funcionamiento del Observatorio: gestionar información y conocimiento y facilitar la toma de decisiones basadas en evidencia.</p><span class="nlink">Ver los lineamientos (PDF) ↗</span></a>
      <a class="norm" href="https://www.gob.pe/54353-sistema-nacional" target="_blank" rel="noopener"><b>Sistema Nacional</b><p>El Observatorio articula la información de las entidades que previenen, atienden, protegen y sancionan la violencia.</p><span class="nlink">Conocer el Sistema Nacional ↗</span></a>
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
  ('INEI','Encuesta Nacional sobre Relaciones Sociales (ENARES) 2024','Tolerancia social hacia la violencia contra las mujeres y violencia contra niñas, niños y adolescentes en el hogar y la escuela.','https://www.gob.pe/institucion/inei/campa%C3%B1as/112686-resultados-de-la-encuesta-nacional-sobre-relaciones-sociales-2024-enares')]),
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
    <h1>Fuentes externas de datos</h1><p>Fuentes para estudiar la violencia comprendida en la Ley N.° 30364. Cada institución conserva la responsabilidad sobre sus datos; los registros administrativos no equivalen a prevalencia.</p>
    <p>Las encuestas y registros oficiales de las entidades del Sistema Nacional. Cada enlace te lleva al sitio de la entidad que produce los datos.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
{groups}  </div>
</section>
</main>
'''+FOOTER+'</body>\n</html>\n'


EVID=head('Evidencia científica · Banco de Evidencias','Estudios nacionales e internacionales sobre la violencia contra las mujeres y los integrantes del grupo familiar, ordenados por tipo y modalidad de violencia según la Ley N.° 30364.','evidencia.html')+header('ev')+'''
<main>
<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="./">← Banco de Evidencias</a>
    <h1>Evidencia científica</h1>
    <p>Lo que se ha investigado sobre la violencia contra las mujeres y los integrantes del grupo familiar, organizado según la Ley N.° 30364.</p>
    <div class="hsearch"><input type="search" id="q" placeholder="Buscar en todo el banco: CEM, Línea 100, feminicidio, adolescentes…" aria-label="Buscar en todo el banco"></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="tabs" role="tablist" aria-label="Secciones de la evidencia">
      <button type="button" role="tab" id="tE" aria-selected="true" aria-controls="tabE"><b>Comprender la violencia</b><span class="td">Investigaciones sobre la violencia que comprende la Ley N.° 30364: sus causas y consecuencias, y la respuesta del Estado.</span></button>
      <button type="button" role="tab" id="tF" aria-selected="false" aria-controls="tabF"><b>¿Qué ayuda a enfrentar la violencia?</b><span class="td">Intervenciones evaluadas y resultados reportados. Una evaluación no implica que el programa sea efectivo.</span></button>
    </div>
    <div id="tabF" role="tabpanel" aria-labelledby="tF" hidden>
      <div id="solHome">
        <h3 class="ejes-h">Respuestas frente a la violencia</h3><p class="fdesc">Ejes de consulta propuestos a partir de la Ley N.° 30364; no son una clasificación oficial de estudios. Los resultados se presentan según el alcance y las limitaciones de cada evaluación.</p>
        <div class="ejes" id="ejes"></div>
      </div>
      <div id="ejeDet" hidden></div>
      <div id="solDet" hidden></div>
    </div>
    <div id="tabE" role="tabpanel" aria-labelledby="tE">
      <div class="guide-panel" role="note"><div class="guide-mark" aria-hidden="true">?</div><div class="guide-copy"><strong>¿Tipo o modalidad de violencia? No son lo mismo.</strong><p>El <b>tipo</b> describe qué daño se produce; la <b>modalidad</b>, en qué relación o contexto ocurre. Puedes filtrar por cada uno por separado.</p></div><a class="guide-action" href="comprender-violencia.html">Ver la guía <span aria-hidden="true">→</span></a></div><p class="filter-context">Solo se incluyen estudios sobre la violencia que comprende la Ley N.° 30364. La clasificación de cada estudio es orientativa.</p><div class="filt f5">
        <label>Tema de investigación<select id="fTema"></select></label>
        <label>Tipo de violencia<select id="fTipo"></select></label>
        <label>Modalidad de violencia<select id="fMod"></select></label>
        <label>Población<select id="fPob"></select></label>
        <label>Ámbito<select id="fAmb"><option value="">Nacional e internacional</option><option value="Nacional">Nacional</option><option value="Internacional">Internacional</option></select></label>
      </div>
      <details class="filter-explain" id="filterExplain" hidden><summary>¿Qué significa el filtro seleccionado?</summary><div id="fDesc"></div></details>
      <div class="toolbar rbar">
        <p class="count" id="count"></p>
        <button type="button" class="clear" id="clear" hidden>Limpiar filtros</button>
        <select id="sort" aria-label="Ordenar"><option value="y">Publicación más reciente</option><option value="t">Orden alfabético (A–Z)</option></select>
      </div>
      <div class="cards" id="cards"></div>
      <button type="button" class="more" id="more" hidden>Ver más estudios</button>
      <p class="dl-note">¿Necesitas toda la base? <a href="matriz/Matriz_evidencias_MIMP_revisada.xlsx" download>Descarga la matriz completa en Excel</a>.</p>
    </div>
  </div>
</section>
</main>
'''+FOOTER+r'''<script>
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const TIPOS=['Violencia física','Violencia psicológica','Violencia sexual','Violencia económica o patrimonial'];
const TDESC={'Violencia física':'Daño a la integridad corporal o a la salud, incluido el maltrato por negligencia o descuido.','Violencia psicológica':'Controlar o aislar a la persona contra su voluntad, humillarla, avergonzarla, insultarla, estigmatizarla o estereotiparla.','Violencia sexual':'Actos de naturaleza sexual sin consentimiento o bajo coacción, incluso sin contacto físico.','Violencia económica o patrimonial':'Menoscabo de los recursos económicos o patrimoniales: quitar o retener bienes, documentos o ingresos, o no cumplir con los alimentos.'};
const DDESC={'Cuidados domésticos':'Las tareas del hogar y la atención a la familia: cocinar, limpiar, cuidar a hijas e hijos. Las hacen las propias familias sin pago o trabajadoras del hogar remuneradas.','Cuidados domiciliarios':'La atención que una persona cuidadora brinda en la vivienda a quien depende de otras personas: personas adultas mayores, con discapacidad o con una enfermedad.','Cuidados institucionales':'Servicios de cuidado fuera del hogar, como cunas, guarderías, centros de día o residencias.','Cuidados comunitarios':'Cuidado que organiza la propia comunidad, como ollas comunes, comedores populares y redes vecinales.','Empleo':'Acceso de las mujeres al trabajo y a ingresos propios, y la brecha salarial.','Educación':'Acceso, permanencia y estereotipos en la escuela y la universidad.','Salud':'Salud física, mental, sexual y reproductiva de las mujeres.','Brechas entre mujeres y hombres':'Diferencias entre mujeres y hombres medidas en varios ámbitos a la vez.','Acceso a tecnología':'Uso de internet, celulares y habilidades digitales.','Participación y liderazgo':'Presencia de mujeres en cargos de decisión, la política y las organizaciones.','Enfoques transversales':'Estudios que miran las diferencias por edad, etnia u otras condiciones.'};
const GROUPS=[['Igualdad de oportunidades','Condiciones que fortalecen la autonomía de las mujeres y reducen el riesgo de violencia.'],['Sistema de cuidados','Quién cuida, dónde y en qué condiciones. Cuando el cuidado recae solo en las mujeres, limita su autonomía económica.']];
const GEN='Varias o sin modalidad específica';
let R=[],S={tema:'',tipo:'',pob:'',mod:'',amb:'',q:'',sort:'y',open:null,shown:20};
const pl=(n,a,b)=>n+' '+(n===1?a:b);
function gist(r){return (r.abstract||r.resumen||'').trim()}
const TEMAS=[['Causas y consecuencias de la violencia','Factores que explican la violencia, cómo se presenta y qué efectos tiene en la salud, la educación, el empleo y el bienestar.','Ley N.° 30364, arts. 42 y 45, inc. 1.f'],['Prevención de la violencia','Acciones para evitar que la violencia ocurra, como el trabajo con varones, colegios y comunidades.','Ley N.° 30364, arts. 1 y 27'],['Atención y recuperación de las víctimas','Servicios que atienden a las víctimas y las ayudan a recuperarse.','Ley N.° 30364, arts. 1, 10 y 27 al 29'],['Protección de las víctimas','Medidas de protección, denuncia y respuesta de la policía y el sistema de justicia para proteger a las víctimas.','Ley N.° 30364, arts. 1 y 13 al 26'],['Persecución y sanción','Investigación, procesamiento y sanción de los hechos de violencia.','Ley N.° 30364, arts. 1, 16 al 20'],['Reeducación de las personas agresoras','Tratamiento para que las personas agresoras dejen de ejercer violencia.','Ley N.° 30364, arts. 1 y 30 al 32'],['Reparación del daño','Medidas para reparar el daño causado a las víctimas y restituir sus derechos.','Ley N.° 30364, arts. 1 y 33']];
const NOTIPO='No trata un tipo de violencia en particular';
const POBS=['Mujeres','Integrantes del grupo familiar','Niñas, niños y adolescentes','Personas adultas mayores','Personas con discapacidad','Varones y personas agresoras','Operadores del sistema'];
const PDESC={'Mujeres':'Durante todo su ciclo de vida: niña, adolescente, joven, adulta y adulta mayor (art. 7).','Integrantes del grupo familiar':'Cónyuges, convivientes, padres, hijos y demás parientes que señala el art. 7.','Niñas, niños y adolescentes':'En especial situación de vulnerabilidad (art. 1).','Personas adultas mayores':'En especial situación de vulnerabilidad (art. 1).','Personas con discapacidad':'En especial situación de vulnerabilidad (art. 1).','Varones y personas agresoras':'Programas para varones y reeducación de personas agresoras (arts. 27 y 30 al 32).','Operadores del sistema':'Policía, Ministerio Público, Poder Judicial y servicios de atención (arts. 2, 18 y 45).'};
const tipoOf=r=>(r.tipos||[]).filter(t=>t!=='Estudios sobre varios tipos de violencia');
function match(r,skip){const q=S.q.trim().toLowerCase();
  if(S.ns&&!S.ns.includes(r.n))return false;
  return (skip==='tema'||!S.tema||(r.temas||[]).includes(S.tema))&&(skip==='tipo'||!S.tipo||tipoOf(r).includes(S.tipo))&&(skip==='pob'||!S.pob||(r.pob_g||[]).includes(S.pob))&&(skip==='amb'||!S.amb||r.amb===S.amb)
   &&(skip==='mod'||!S.mod||(r.mod||[]).includes(S.mod))&&(!q||[r.t,r.a,r.dim,r.pob,r.prop,r.res,r.tipo,r.vy,r.vx,(r.paises||[]).join(' '),(r.mod||[]).join(' '),(r.temas||[]).join(' ')].join(' ').toLowerCase().includes(q))}
function opts(id,all,vals,cur,key){const n=v=>R.filter(r=>match(r,key)&&(key==='tema'?(r.temas||[]).includes(v):key==='tipo'?tipoOf(r).includes(v):key==='mod'?(r.mod||[]).includes(v):(r.pob_g||[]).includes(v))).length;
  $(id).innerHTML=`<option value="">${all}</option>`+vals.map(v=>{const c=n(v);return `<option value="${esc(v)}"${v===cur?' selected':''}${c||v===cur?'':' disabled'}>${esc(v)} (${c})</option>`}).join('')}
function home(){}
function show(){
  opts('fTema','Todos los temas',TEMAS.map(t=>t[0]),S.tema,'tema');
  opts('fTipo','Todos los tipos',TIPOS,S.tipo,'tipo');
  opts('fMod','Todas las modalidades',[...new Set(R.flatMap(r=>r.mod||[]))].filter(m=>m!==GEN).sort((a,b)=>a.localeCompare(b,'es')),S.mod,'mod');
  opts('fPob','Todas las poblaciones',POBS,S.pob,'pob');$('fAmb').value=S.amb;
  const d=[];if(S.tema){const t=TEMAS.find(t=>t[0]===S.tema);d.push(`<b>${esc(S.tema)}:</b> ${t[1]} <span class="base">${t[2]}</span>`)};if(S.tipo&&TDESC[S.tipo])d.push(`<b>${esc(S.tipo)} (art. 8 de la Ley):</b> ${TDESC[S.tipo]}`);if(S.pob&&PDESC[S.pob])d.push(`<b>${esc(S.pob)}:</b> ${PDESC[S.pob]}`);
  if(S.mod)d.push(`<b>${esc(S.mod)}:</b> modalidad de violencia según el marco conceptual del MIMP. <a href="comprender-violencia.html#modalidades">Ver en la guía</a>`);
  $('fDesc').innerHTML=d.join('<br>');$('filterExplain').hidden=!d.length;
  const L=R.filter(r=>match(r));
  L.sort(S.sort==='t'?(a,b)=>a.t.localeCompare(b.t,'es'):(a,b)=>(+b.y||0)-(+a.y||0));
  const any=S.tema||S.tipo||S.mod||S.pob||S.amb||S.q.trim()||S.ns;
  $('count').textContent=any?pl(L.length,'investigación encontrada','investigaciones encontradas'):`Todas las investigaciones (${L.length})`;$('clear').hidden=!any;
  $('cards').innerHTML=L.length?L.slice(0,S.shown).map(card).join(''):'<div class="empty">No hay investigaciones con esos filtros. Prueba quitando alguno.</div>';
  $('more').hidden=L.length<=S.shown;$('more').textContent=`Ver más investigaciones (${L.length-S.shown} restantes)`;
  document.querySelectorAll('.paper [data-open]').forEach(b=>b.onclick=()=>{const n=+b.dataset.open;S.open=S.open===n?null:n;show()});
}
function card(r){const o=S.open===r.n,au=r.a?r.a.split(';')[0].trim()+(r.a.includes(';')?' et al.':'') :'';
  const pais=r.amb==='Nacional'?'Perú':((r.paises||[]).length>2?'Varios países':(r.paises||[]).join(', ')||'Varios países');
  const tags=(r.temas||[]).map(t=>`<span class="tag dimtag">${esc(t)}</span>`).join('');
  const tipos=(r.tipos||[]).filter(t=>t!=='Estudios sobre varios tipos de violencia').map(t=>t.replace('Violencia ',''));
  const f=(t,v)=>v?`<dt>${t}</dt><dd>${esc(v)}</dd>`:'';
  return `<article class="paper"><div class="tags">${tags}<span class="tag ${r.amb==='Nacional'?'pe':'int'}">${r.amb} · ${esc(pais)}</span></div>
   <h3>${esc(r.t)}</h3><div class="by">${[au,r.y].filter(Boolean).map(esc).join(' · ')}${tipos.length?` · Violencia ${tipos.join(', ')}`:''}</div>
   ${gist(r)?`<p class="gist">${esc(gist(r))}</p>`:''}
   <div class="row"><button type="button" data-open="${r.n}" aria-expanded="${o}">${o?'Cerrar ficha':'Ver ficha completa'}</button>${r.link?`<a href="${esc(r.link)}" target="_blank" rel="noopener">Leer el estudio ↗</a>`:''}</div>
   ${o?`<dl>${f('Autoría',r.a)}${f('País',(r.paises||[]).join(', '))}${f('Tema',(r.temas||[]).join(', '))}${f('Tipo de violencia',(r.tipos||[]).filter(t=>t!=='Estudios sobre varios tipos de violencia').join(', '))}${f('Modalidad',(r.mod||[]).filter(m=>m!==GEN).join(', '))}${f('Población',r.pob)}${f('Propósito',r.prop)}${f('Intervención',[r.tipo,r.det].filter(Boolean).join('\n\n'))}${f('Estado de la evaluación',r.est)}${f('Qué se mide (Y)',r.vy)}${f('Qué lo explica (X)',r.vx)}${f('Resultados',r.res)}${f('Publicado en',r.pub)}${f('N.° en la matriz',String(r.n))}</dl>`:''}</article>`}
$('q').oninput=e=>{tab('E');S.q=e.target.value;S.shown=20;show()};
$('sort').onchange=e=>{S.sort=e.target.value;show()};
$('fTema').onchange=e=>{S.tema=e.target.value;S.shown=20;show()};
$('fTipo').onchange=e=>{S.tipo=e.target.value;S.shown=20;show()};
$('fMod').onchange=e=>{S.mod=e.target.value;S.shown=20;show()};
$('fPob').onchange=e=>{S.pob=e.target.value;S.shown=20;show()};
$('fAmb').onchange=e=>{S.amb=e.target.value;S.shown=20;show()};
$('clear').onclick=()=>{history.replaceState(null,'',location.pathname);S.ns=null;Object.assign(S,{tema:'',tipo:'',pob:'',amb:'',mod:'',q:'',open:null,shown:20});$('q').value='';show()};
$('more').onclick=()=>{S.shown+=20;show()};
/* ---------- ¿Qué funciona? (tipos de solución por eje de la Ley 30364) ---------- */
let SOL=null,F={eje:'',sol:null};
const RES={'Efectivo':['Funciona','ef-a','Varios estudios rigurosos muestran que reduce la violencia.'],'Prometedor':['Buenos resultados iniciales','ef-b','Un estudio muestra resultados positivos; falta confirmarlos.'],'Evidencias mixtas':['Resultados distintos según el estudio','ef-c','En unos estudios funcionó y en otros no.'],'Sin efecto':['No mostró resultados','ef-d','Los estudios no encontraron cambios.'],'En evaluación':['Aún sin resultados','ef-e','Se está evaluando; los resultados no se publican todavía.']};
const EFE={'Positivo':['Resultado positivo','ef-b'],'Mixto':['Resultado mixto','ef-c'],'Sin efecto':['Sin cambios','ef-d'],'Sin resultados aún':['Aún sin resultados','ef-e']};
const ICO={prevencion:'Evitar que la violencia ocurra',atencion:'Acompañar a quienes la viven',proteccion:'Proteger y sancionar',reeducacion:'Que la persona agresora deje de agredir'};
function tab(w){const f=w==='F';$('tabF').hidden=!f;$('tabE').hidden=f;$('tF').setAttribute('aria-selected',f);$('tE').setAttribute('aria-selected',!f)}
$('tF').onclick=()=>{tab('F');F.eje='';F.sol=null;solRender()};$('tE').onclick=()=>tab('E');
const byN=n=>R.find(r=>r.n===n);
const nS=n=>`${n} ${n===1?'estudio':'estudios'}`;
function solRender(){
  if(!SOL)return;
  const home=!F.eje&&!F.sol;$('solHome').hidden=!home;$('ejeDet').hidden=home;$('solDet').hidden=!F.sol;
  if(F.sol){$('ejeDet').hidden=true;return solDetail(SOL.soluciones.find(x=>x.id===F.sol))}
  if(F.eje)return ejeDetail(SOL.ejes.find(e=>e.id===F.eje));
  $('ejes').innerHTML=SOL.ejes.map(e=>{const L=SOL.soluciones.filter(x=>x.eje===e.id);
    return L.length?`<button type="button" class="eje" data-e="${e.id}"><span class="q">${e.base}</span><b>${e.n}</b><span class="d">${e.d}</span><span class="n">${L.length} ${L.length===1?'programa evaluado':'programas evaluados'}</span><span class="go">Ver evaluaciones →</span></button>`
      :`<div class="eje vacio"><span class="q">${e.base}</span><b>${e.n}</b><span class="d">${e.d}</span><span class="n">Todavía no hay programas evaluados en este tema.</span></div>`}).join('');
  document.querySelectorAll('button.eje').forEach(b=>b.onclick=()=>{F.eje=b.dataset.e;solRender();scrollTo({top:$('tabF').offsetTop-90})});
}
function ejeDetail(e){const L=SOL.soluciones.filter(x=>x.eje===e.id);
  $('ejeDet').innerHTML=`<button type="button" class="back" id="ejeBack">← Todos los ejes</button>
   <div class="eje-head"><p class="kick">${e.base}</p><h2>${e.n}</h2><p>${e.d}</p></div>
   <div class="sols">${L.map(x=>{const t=RES[x.ef];return `<button type="button" class="sol" data-s="${x.id}"><b>${x.n}</b><span class="ev">${x.ev}</span><span class="go">Ver ${x.casos.length===1?'el estudio':'los '+nS(x.casos.length)} →</span></button>`}).join('')}</div>`;
  $('ejeBack').onclick=()=>{F.eje='';solRender()};
  document.querySelectorAll('.sol').forEach(b=>b.onclick=()=>{F.sol=b.dataset.s;solRender();scrollTo({top:$('tabF').offsetTop-90})});
}
function solDetail(x){const eje=SOL.ejes.find(e=>e.id===x.eje),t=RES[x.ef];
  $('solDet').innerHTML=`<button type="button" class="back" id="solBack">← ${eje.n}</button>
   <div class="soldet"><p class="kick">${eje.n}</p><h2>${x.n}</h2><span class="efp ${t[1]}">${t[0]}</span>
   <div class="two"><div><p class="sub">Qué es</p><p>${x.d}</p></div><div><p class="sub">Qué encontraron los estudios</p><p>${x.ev}</p></div></div>
   ${x.tipos.length?`<p class="tv">Tipos de violencia: ${x.tipos.map(t=>`<span class="tag">${t}</span>`).join(' ')}</p>`:''}
   <p class="sub" style="margin-top:22px">Estudios (${x.casos.length})</p></div>
   <div class="cards">${x.casos.map(c=>{const r=byN(c.n),e=EFE[c.efecto];return r?card(r).replace('<div class="tags">',`<div class="tags"><span class="tag efp ${e[1]}">${e[0]}</span>`):''}).join('')}</div>`;
  $('solBack').onclick=()=>{F.sol=null;solRender()};
  document.querySelectorAll('#solDet [data-open]').forEach(b=>b.onclick=()=>{const n=+b.dataset.open;S.open=S.open===n?null:n;solDetail(x)});
}
/* enlaces desde la guía y los servicios: evidencia.html?tipo=…&mod=…&tema=…&n=1,2,3 */
const QP=new URLSearchParams(location.search);['tema','tipo','mod','pob'].forEach(k=>{if(QP.get(k))S[k]=QP.get(k)});
if(QP.get('n'))S.ns=QP.get('n').split(',').map(Number);
Promise.all([fetch('data/estudios.json').then(r=>r.json()),fetch('data/soluciones.json').then(r=>r.json())]).then(([d,s])=>{R=d.rows;SOL=s;home();show();solRender()}).catch(()=>{$('ejes').innerHTML='<div class="empty">No se pudieron cargar los datos. Recarga la página.</div>'});
</script>
</body>
</html>
'''

# ---------- Servicios del MIMP (Catálogo de Servicios 2026), en lenguaje sencillo ----------
import sys as _s,os as _o; _s.path.insert(0,_o.path.dirname(_o.path.abspath(__file__)))
from servicios_data import NIVELES,S as SERVS
from ilustraciones import RED_APOYO,ESC_CIUDAD,ESC_SIERRA,ESC_RIO,ESC_FONO
_P={'a':'<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
 'b':'<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 'c':'<path d="M4 5h16v11H9l-5 4z"/><path d="M12 13.5c-2.2-1.4-3.2-2.4-3.2-3.6 0-.9.7-1.6 1.6-1.6.7 0 1.2.4 1.6 1 .4-.6.9-1 1.6-1 .9 0 1.6.7 1.6 1.6 0 1.2-1 2.2-3.2 3.6z"/>',
 'd':'<circle cx="12" cy="12" r="8.5"/><path d="M12 6.5v11"/><path d="M15 9.3c-.3-1-1.4-1.6-3-1.6-1.7 0-3 .8-3 2.1s1.1 1.8 3 2.2 3 1 3 2.3-1.3 2.1-3 2.1-2.8-.7-3.1-1.7"/>',
 'e':'<path d="M3 10v4h3l8 5V5L6 10z"/><path d="M18 9a4.5 4.5 0 0 1 0 6"/>',
 'f':'<circle cx="12" cy="12" r="8.5"/><path d="M8.3 12.2l2.6 2.6 4.8-5.3"/>',
 'g':'<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3.5 2.3 8.5 2.3 12 0v-5"/><path d="M22 9v5"/>',
 'h':'<path d="M4 20h16"/><path d="M7 16v-5"/><path d="M12 16V6"/><path d="M17 16V9"/>',
 'i':'<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.4-4.4"/>',
 '1':'<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.4 2.7-6 6-6s6 2.6 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16.5 14.2c2.6.2 4.5 2.4 4.5 5.3"/>',
 '2':'<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 3h6v3H9z"/><path d="M9 13l2 2 4-4.5"/>',
 '3':'<path d="M3 10l9-6 9 6"/><path d="M5 10v8M10 10v8M14 10v8M19 10v8"/><path d="M3 20h18"/>'}
def ICO(k): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_P[k]}</svg>'
EMO={k:ICO(k) for k in 'abcdefghi'}
EMON={k:ICO(k) for k in '123'}
CATALOGO='https://cdn.www.gob.pe/uploads/document/file/9387740/7693547-catalogo-de-servicios-del-sector-mujer-y-poblaciones-vulnerables.pdf'
PROGS=['Warmi Ñan','INABIF','MIMP','Gratitud','CONADIS','Varios programas']
PROGN={'Warmi Ñan':'Programa Warmi Ñan','INABIF':'INABIF','MIMP':'MIMP, sede central','Gratitud':'Programa Gratitud','CONADIS':'CONADIS','Varios programas':'Varios programas'}
def _card(n,t,name,d,para,prog,v):
    return f'''<article class="svc t-{t}" data-prog="{prog}" data-v="{v}"><div class="svc-top"><span class="svc-prog">{PROGN[prog]}</span>{'<span class="svc-vio">Frente a la violencia</span>' if v else ''}</div><h4>{name}</h4><p>{d}</p><div class="svc-para"><b>Población objetivo</b><span>{para}</span></div></article>'''
resumen=''.join(f'''<div class="sv-lvl l{k}"><span class="lv-emo">{EMON[k]}</span><span class="lv-n">Nivel {k}</span><h3>{t}</h3><p>{d}</p><ul class="sv-types">{''.join(f'<li class="t-{tk}"><button type="button" data-t="{tk}" aria-pressed="false"><i class="ico">{EMO[tk]}</i><b>{tn}</b><span>Ver servicios →</span></button></li>' for tk,tn,_ in T)}</ul></div>''' for k,t,d,T in NIVELES)
cuerpo=''
for k,t,d,T in NIVELES:
    tipos=''
    for tk,tn,td in T:
        L=[x for x in SERVS if x[1]==tk]
        tipos+=f'''<div class="sv-tipo t-{tk}" id="tipo-{tk}"><div class="sv-tipo-h"><span class="sv-emo">{EMO[tk]}</span><div><h4>{tn}</h4><p>{td}</p></div></div><div class="svc-grid">{''.join(_card(*x) for x in L)}</div></div>'''
    cuerpo+=f'''<section class="sv-nivel" id="nivel-{k}"><div class="sv-nivel-h"><span class="etapa-n">{k}</span><div><span class="etapa-k">Nivel {k}</span><h3>{t}</h3><p>{d}</p></div></div>{tipos}</section>'''
chips=''.join(f'<button type="button" data-p="{p}" aria-pressed="false">{PROGN[p]}</button>' for p in PROGS)
import json as _j,html as _h
from urllib.parse import quote as _q
_EST={r['n']:r for r in _j.load(open('data/estudios.json',encoding='utf-8'))['rows']}
_TCOUNT={}
for _r in _EST.values():
    for _t in _r.get('temas') or []: _TCOUNT[_t]=_TCOUNT.get(_t,0)+1
_SV={x[0]:x for x in SERVS}
# Ruta frente a la violencia: acciones del art. 1 de la Ley N.° 30364 = temas de la evidencia.
# (clave, paso, tema de evidencia, base legal, descripción, servicios del catálogo, estudios por servicio, estudios destacados, ícono)
RUTA=[
 ('prev','Prevenir','Prevención de la violencia','Ley N.° 30364, arts. 1 y 27','Trabajar con varones, adolescentes, familias y colegios para que la violencia no ocurra.',[2,3,4,6,8],{2:[217]},[217,134,92],
  '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>'),
 ('ayuda','Pedir ayuda','Atención y recuperación de las víctimas','Ley N.° 30364, art. 10','Canales gratuitos para pedir información, orientación o apoyo emocional ante un caso de violencia.',[23,26],{23:[75,203,136]},[203,75,136],
  '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>'),
 ('atender','Atender y acompañar','Atención y recuperación de las víctimas','Ley N.° 30364, arts. 10 y 27 al 29','Atención legal, psicológica y social para que las víctimas estén protegidas y se recuperen.',[21,22,25,27,1],{21:[201,228,205]},[201,228,205],
  '<path d="M4 5h16v11H9l-5 4z"/><path d="M12 13.5c-2.2-1.4-3.2-2.4-3.2-3.6 0-.9.7-1.6 1.6-1.6.7 0 1.2.4 1.6 1 .4-.6.9-1 1.6-1 .9 0 1.6.7 1.6 1.6 0 1.2-1 2.2-3.2 3.6z"/>'),
 ('proteger','Proteger','Protección de las víctimas','Ley N.° 30364, arts. 13 al 26','Un lugar seguro cuando la víctima no puede volver a casa, y medidas para resguardarla.',[12,15,39],{},[212,213,201],
  '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>'),
 ('sancion','Investigar y sancionar','Persecución y sanción','Ley N.° 30364, arts. 16 al 20','Está a cargo de la Policía Nacional, el Ministerio Público y el Poder Judicial.',[],{},[206,95,201],
  '<path d="M12 4v16"/><path d="M5 8h14"/><path d="M5 8l-2.5 6a3 3 0 0 0 5 0z"/><path d="M19 8l-2.5 6a3 3 0 0 0 5 0z"/><path d="M8 20h8"/>'),
 ('reeducar','Reeducar a la persona agresora','Reeducación de las personas agresoras','Ley N.° 30364, arts. 30 al 32','Tratamiento para que quien ejerció violencia deje de hacerlo.',[24],{24:[207]},[207,216,222],
  '<path d="M4 12a8 8 0 0 1 14-5.3"/><path d="M18 3v4h-4"/><path d="M20 12a8 8 0 0 1-14 5.3"/><path d="M6 21v-4h4"/>'),
 ('reparar','Reparar el daño','Reparación del daño','Ley N.° 30364, arts. 1 y 33','Medidas para reparar a las víctimas y a sus familias, como el apoyo a hijas e hijos de víctimas de feminicidio.',[43],{},[],
  '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>'),
]
def _ico(path): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'
def _e(s): return _h.escape(str(s or ''))
def _first(s):
    s=(s or '').strip();k=s.find('. ');return s if k<0 else s[:k+1]
def _study(n):
    r=_EST.get(n)
    if not r: return ''
    lugar='Perú' if r.get('amb')=='Nacional' else 'Internacional'
    meta=' · '.join(x for x in (lugar,str(r.get('y') or '')) if x)
    return f'<li><a href="evidencia.html?n={n}"><b>{_e(r["t"])}</b><span>{_e(meta)}</span></a></li>'
def _svc(n,ev):
    _,t,name,d,para,prog,v=_SV[n]
    link=f'<a class="rs-ev" href="evidencia.html?n={",".join(map(str,ev))}">{len(ev)} {"estudio" if len(ev)==1 else "estudios"} sobre este servicio →</a>' if ev else ''
    return f'<article class="rs"><span class="rs-prog">{PROGN[prog]}</span><h4>{_e(name)}</h4><p>{_e(d)}</p><p class="rs-para"><b>Población objetivo:</b> {_e(para)}</p>{link}</article>'
steps=''.join(f'<li class="c{i}"><a href="#r-{k}"><span class="rt-i">{_ico(ic)}</span><span class="rt-t"><small>{i}</small>{t}</span></a></li>' for i,(k,t,tema,art,d,L,EV,ST,ic) in enumerate(RUTA,1))
bloques=''
for i,(k,t,tema,art,d,L,EV,ST,ic) in enumerate(RUTA,1):
    n=_TCOUNT.get(tema,0)
    svcs=''.join(_svc(x,EV.get(x,[])) for x in L) if L else ('<div class="den"><h4>¿Dónde y cómo denunciar?</h4><div class="den-g">'
      '<div><b>Dónde</b><ul><li>Comisarías de la Policía Nacional</li><li>Fiscalías penales o de familia</li><li>Juzgados de familia</li><li>Donde no los haya: juzgados de paz letrados o juzgados de paz</li></ul></div>'
      '<div><b>Cómo</b><ul><li>De forma verbal, por escrito o por medios virtuales</li><li>No se necesita abogado ni pagar una tasa</li><li>Puede denunciar la víctima o cualquier otra persona en su favor</li><li>El personal de salud y de educación está obligado a denunciar</li></ul></div>'
      '</div><p class="den-s">Ley N.° 30364, art. 15. Si acudes a un Centro Emergencia Mujer, su equipo legal te acompaña en la denuncia y durante el proceso.</p></div>')
    if n:
        ev=f'<ul class="rx-list">{"".join(_study(x) for x in ST)}</ul><a class="rx-all" href="evidencia.html?tema={_q(tema)}">Ver los {n} estudios sobre {tema[0].lower()+tema[1:]} →</a>'
    else:
        ev='<p class="rx-none">El banco aún no tiene estudios sobre este tema. Es un vacío de evidencia que conviene cubrir.</p>'
    bloques+=f'''<section class="rb c{i}{' ext' if not L else ''}" id="r-{k}"><div class="rb-h"><span class="rb-i">{_ico(ic)}</span><div><span class="rb-k">Paso {i} · {art}</span><h3>{t}</h3><p>{d}</p></div></div>
<div class="rb-body"><div class="rb-svcs">{svcs}</div><aside class="rx"><span class="rx-k">Qué dice la evidencia</span>{ev}</aside></div></section>'''
SERV=head('Servicios frente a la violencia · Banco de Evidencias','Los servicios del MIMP para prevenir, atender, proteger y reparar frente a la violencia, ordenados según la Ley N.° 30364 y vinculados con la evidencia disponible.','servicios.html')+header('sv')+f'''
<main>
<section class="page-hero sv sv-hero">
  <div class="wrap sv-hero-in">
   <div class="sv-hero-t">
    <a class="crumb" href="./">← Banco de Evidencias</a>
    <h1>Servicios frente a la violencia</h1>
    <p>Nadie debería enfrentar la violencia sola. El Estado tiene servicios para cada momento, desde prevenirla hasta reparar el daño, en la ciudad, en el campo y en la Amazonía.</p>
    <div class="help"><span class="help-k">¿Necesitas ayuda?</span><a href="tel:100"><b>Línea 100</b><span>Llamada gratuita, las 24 horas</span></a><a href="https://www.mimp.gob.pe/chat100" target="_blank" rel="noopener"><b>Chat 100</b><span>Por internet o WhatsApp</span></a><a href="tel:105"><b>105</b><span>Emergencias, Policía Nacional</span></a></div>
   </div>
   <div class="sv-hero-a">'''+RED_APOYO+f'''</div>
  </div>
</section>
<section class="section pais">
  <div class="wrap">
    <div class="sv-intro"><h2>Servicios que llegan a todo el país</h2><p>La atención se adapta al territorio y a la cultura de cada comunidad.</p></div>
    <div class="pais-g">
      <article class="pz"><div class="pz-a">'''+ESC_CIUDAD+f'''</div><span class="pz-k">En las ciudades</span><h3>Centros Emergencia Mujer y Familia</h3><p>439 centros en todo el país, con atención legal, psicológica y social gratuita.</p><a href="#r-atender">Ver en la ruta →</a></article>
      <article class="pz"><div class="pz-a">'''+ESC_SIERRA+f'''</div><span class="pz-k">En el campo</span><h3>Servicio de Atención Rural</h3><p>Atiende en zonas rurales respetando la cultura local y trabajando junto con las autoridades comunales.</p><a href="#r-atender">Ver en la ruta →</a></article>
      <article class="pz"><div class="pz-a">'''+ESC_RIO+f'''</div><span class="pz-k">Por los ríos amazónicos</span><h3>Atención en las PIAS</h3><p>Orientación y primera atención a bordo de las Plataformas Itinerantes que llegan por río a comunidades alejadas.</p><a href="#r-atender">Ver en la ruta →</a></article>
      <article class="pz"><div class="pz-a">'''+ESC_FONO+f'''</div><span class="pz-k">Desde cualquier lugar</span><h3>Línea 100 y Chat 100</h3><p>Llamada gratuita y chat por internet o WhatsApp para pedir orientación o apoyo, sin moverte de casa.</p><a href="#r-ayuda">Ver en la ruta →</a></article>
    </div>
    <p class="sv-src">Número de centros: Sexto Informe de avance de la Ley N.° 31155 (MIMP, 2026). Descripciones: Catálogo de Servicios del Sector 2026.</p>
  </div>
</section>
<section class="section ruta">
  <div class="wrap">
    <div class="sv-intro"><h2>La respuesta frente a la violencia, paso a paso</h2><p>Los pasos no siempre siguen este orden: una persona puede llegar directamente a un Centro Emergencia Mujer o necesitar protección de inmediato.</p></div>
    <nav aria-label="Pasos de la ruta"><ol class="rt">{steps}</ol></nav>
    {bloques}
  </div>
</section>
<section class="section sv-levels" id="catalogo">
  <div class="wrap">
    <div class="sv-intro"><h2>Catálogo completo del sector</h2><p>El MIMP brinda {len(SERVS)} servicios. Además de los vinculados con la violencia, hay servicios para niñas, niños y adolescentes, personas adultas mayores y personas con discapacidad. Elige un tipo para ver cuáles son.</p></div>
    <div class="sv-lvls">{resumen}</div>
  </div>
</section>
<section class="section sv-all" id="svAll" hidden>
  <div class="wrap">
    <div class="sv-filter" role="group" aria-label="Filtrar servicios">
      <button type="button" class="sv-close" id="svClose">← Elegir otro tipo</button><span>Quién lo brinda:</span><button type="button" data-p="" aria-pressed="true">Todos</button>{chips}
      <label class="chk"><input type="checkbox" id="soloV"> Solo servicios frente a la violencia</label>
    </div>
    {cuerpo}
    <p class="sv-empty" id="svEmpty" hidden>No hay servicios con ese filtro.</p>
  </div>
</section>
<section class="section sv-foot"><div class="wrap"><p class="sv-src">Fuente: <a href="{CATALOGO}" target="_blank" rel="noopener">Catálogo de Servicios del Sector Mujer y Poblaciones Vulnerables 2026</a>. Las descripciones están resumidas; el detalle de cada servicio está en el catálogo. La relación entre servicios y estudios es orientativa.</p></div></section>
</main>
'''+FOOTER+r'''<script>
(function(){let P='',T='';const btns=document.querySelectorAll('.sv-filter button[data-p]'),v=document.getElementById('soloV'),all=document.getElementById('svAll'),tb=document.querySelectorAll('.sv-types button');
function apply(){let any=0;document.querySelectorAll('.svc').forEach(c=>{const ok=c.closest('.sv-tipo').id==='tipo-'+T&&(!P||c.dataset.prog===P)&&(!v.checked||c.dataset.v==='1');c.hidden=!ok;if(ok)any++});
 document.querySelectorAll('.sv-tipo').forEach(t=>t.hidden=t.id!=='tipo-'+T);
 document.querySelectorAll('.sv-nivel').forEach(n=>n.hidden=!n.querySelector('#tipo-'+T));
 document.getElementById('svEmpty').hidden=!!any;}
tb.forEach(b=>b.onclick=()=>{T=b.dataset.t;P='';btns.forEach(x=>x.setAttribute('aria-pressed',x.dataset.p===''));tb.forEach(x=>x.setAttribute('aria-pressed',x===b));all.hidden=false;apply();all.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'})});
document.getElementById('svClose').onclick=()=>{all.hidden=true;tb.forEach(x=>x.setAttribute('aria-pressed','false'));document.getElementById('catalogo').scrollIntoView({block:'start'})};
btns.forEach(b=>b.onclick=()=>{P=b.dataset.p;btns.forEach(x=>x.setAttribute('aria-pressed',x===b));apply()});v.onchange=apply;})();
(function(){const L=[...document.querySelectorAll('.rt a')];if(!('IntersectionObserver' in window))return;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)L.forEach(a=>{const on=a.getAttribute('href')==='#'+e.target.id;a.classList.toggle('on',on);if(on){const ol=a.closest('ol');if(ol.scrollWidth>ol.clientWidth)ol.scrollTo({left:a.parentNode.offsetLeft-ol.clientWidth/2+a.parentNode.offsetWidth/2,behavior:'smooth'})}})}),{rootMargin:'-40% 0px -55% 0px'});
document.querySelectorAll('.rb').forEach(s=>io.observe(s))})();
</script>
</body>
</html>
'''

# ---------- Guía: tipos y modalidades de violencia ----------
# Fuentes: Ley N.° 30364 (arts. 7 y 8); Reglamento, art. 8.1 lit. a (D.S. 004-2019-MIMP, modif. D.S. 005-2022-MIMP);
# Instructivo de la Ficha de Registro de Casos del CEM 2023 (ítems A.6.4, B.2 y B.2.1).
L30364='https://www.gob.pe/74905-ley-n-30364-ley-para-prevenir-sancionar-y-erradicar-la-violencia-contra-las-mujeres-y-los-integrantes-del-grupo-familiar'
REGL='https://busquedas.elperuano.pe/dispositivo/NL/2055357-3'
L31155='https://busquedas.elperuano.pe/dispositivo/NL/1941276-2'
DL1410='https://busquedas.elperuano.pe/dispositivo/NL/1690482-3'
FICHA='Instructivo de la Ficha de Registro de Casos del CEM (2023)'
_TIPOS=[('Violencia física','fis','Acción o conducta que causa daño a la integridad corporal o a la salud. Incluye el maltrato por negligencia, descuido o privación de necesidades básicas.',
  '<path d="M12 21s-7-4.3-7-10a4 4 0 0 1 7-2.7A4 4 0 0 1 19 11c0 5.7-7 10-7 10z"/><path d="M12 8.5l-1.5 3.5h3L12 15.5"/>',
  ['Puntapiés o patadas','Puñetazos','Bofetadas','Jalones de cabello','Mordeduras','Empujones, tirar al suelo','Golpes con palos u otros objetos','Latigazos o correazos','Intento de asfixia','Heridas con arma','Quemaduras','Negligencia']),
 ('Violencia psicológica','psi','Acción u omisión que busca controlar o aislar a la persona contra su voluntad, humillarla, avergonzarla, insultarla, estigmatizarla o estereotiparla.',
  '<path d="M9.5 20v-3.2A6.5 6.5 0 1 1 18 11c0 1-.2 1.8-.6 2.6L19 17h-3v3z"/><path d="M10 9.5c.3-1 1.1-1.5 2-1.5 1.2 0 2 .8 2 1.8 0 1.5-2 1.7-2 3"/><path d="M12 15h0"/>',
  ['Gritos e insultos','Insulto étnico-racial','Indiferencia','Rechazo','Desvalorización y humillación','Discriminación por género, orientación sexual o identidad de género','Amenaza de quitarle a sus hijos','Amenazas de daño o muerte','Le impide estudiar, trabajar o salir','Le impide recibir visitas','Rompe cosas en la casa','Vigilancia continua o persecución','Botarla de la casa','Abandono']),
 ('Violencia sexual','sex','Acciones de naturaleza sexual sin consentimiento o bajo coacción, incluso sin penetración ni contacto físico, como la exposición a material pornográfico.',
  '<circle cx="12" cy="12" r="8.5"/><path d="M7 7l10 10"/>',
  ['Violación sexual','Tocamientos sin consentimiento','Hostigamiento sexual','Acoso sexual','Acoso sexual en espacios públicos','Chantaje sexual','Difusión de imágenes o audios con contenido sexual','Trata con fines de explotación sexual','Explotación sexual','Pornografía','Exhibiciones obscenas','Propuestas sexuales a menores por internet']),
 ('Violencia económica o patrimonial','eco','Acción u omisión que perjudica los recursos económicos o patrimoniales: quitar o retener bienes, documentos o ingresos, o incumplir los alimentos.',
  '<rect x="3" y="6.5" width="18" height="12" rx="2"/><path d="M3 10.5h18"/><path d="M7 15h3"/>',
  ['Perturbar la posesión de sus bienes','Quitar, destruir o retener sus documentos, bienes o herramientas de trabajo','Limitar el dinero para sus necesidades','No cumplir con los alimentos','Limitar o controlar sus ingresos','Pagarle menos por el mismo trabajo','Impedir su desarrollo laboral','Quitarle sus ingresos o impedir que los administre','Condicionar los alimentos para someterla'])]
_TK={t[0]:t[1] for t in _TIPOS}
_TI={t[1]:t for t in _TIPOS}
_TSHORT={'fis':'Física','psi':'Psicológica','sex':'Sexual','eco':'Económica'}
def _tic(k): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_TI[k][3]}</svg>'
_Q={'fis':'«Es la acción o conducta, que causa daño a la integridad corporal o a la salud».',
 'psi':'«Es la acción u omisión, tendiente a controlar o aislar a la persona contra su voluntad, a humillarla, avergonzarla, insultarla, estigmatizarla o estereotiparla».',
 'sex':'«Son acciones de naturaleza sexual que se cometen contra una persona sin su consentimiento o bajo coacción».',
 'eco':'«Es la acción u omisión que ocasiona un menoscabo en los recursos económicos o patrimoniales» de la persona.'}
_QL={'fis':'Ley N.° 30364, art. 8, lit. a','psi':'Ley N.° 30364, art. 8, lit. b','sex':'Ley N.° 30364, art. 8, lit. c','eco':'Ley N.° 30364, art. 8, lit. d'}
_VINC=[('Pareja','Cónyuge, conviviente, enamorado/a o novio/a, y sus «ex»; también quien tiene un hijo o hija en común.'),
 ('Familiar','Madre o padre, padrastro o madrastra, hija o hijo, abuelo/a, hermano/a, tío/a, suegro/a, cuñado/a, entre otros.'),
 ('Sin vínculo de pareja ni familiar','Vecino/a, docente, compañero/a de estudios o de trabajo, empleador/a, persona desconocida, entre otros.')]
# Las 21 modalidades del Reglamento, art. 8.1, lit. a (numeración del Reglamento). Tercer campo: dónde la registra la Ficha CEM.
_MODS={1:('Violencia en relación de pareja','Violencia de una pareja o expareja. Puede incluir cualquiera de los cuatro tipos.','vinc','Violencia en relación de pareja'),
 2:('Feminicidio','Asesinato de una mujer por su condición de tal, tipificado en el Código Penal.','fem','Feminicidio'),
 3:('Trata de personas con fines de explotación sexual','Captar, trasladar, acoger o retener a una persona para explotarla sexualmente.','sex','Trata de personas con fines de explotación sexual'),
 4:('Explotación sexual de niñas, niños y adolescentes','Utilizar a niñas, niños o adolescentes en actos sexuales a cambio de un beneficio.','sex',None),
 5:('Acoso sexual','Vigilar, perseguir, hostigar o buscar contacto con una persona, sin su consentimiento, con fines sexuales; también en espacios públicos.','sex',None),
 6:('Violencia en los servicios de salud sexual y reproductiva','Acciones violentas o discriminatorias contra los derechos sexuales y reproductivos de las mujeres durante su atención en salud.','mod',None),
 7:('Esterilizaciones forzadas','Esterilización realizada sin consentimiento libre e informado.','otro',None),
 8:('Hostigamiento sexual','Conducta sexual o sexista no deseada, en el trabajo, el centro de estudios o una relación similar.','sex',None),
 9:('Acoso político','Conductas contra mujeres, por su condición de tal, para limitar o impedir el ejercicio de sus derechos políticos.','mod',None),
 10:('Violencia en conflictos sociales','Violencia de género que se produce o agrava en contextos de conflicto social, ambiental o de desastre.','mod',None),
 11:('Violencia en conflicto armado','Violencia contra las mujeres en situaciones de conflicto armado, sobre todo violencia sexual, como ocurrió entre 1980 y 2000.','mod','Violencia en conflicto armado'),
 12:('Violencia a través de las tecnologías de la información y comunicación','Violencia ejercida o facilitada por internet, redes sociales u otros medios digitales.','mod','Violencia a través de las tecnologías de la información'),
 13:('Violencia por orientación sexual','Actos que causan daño o sufrimiento a una mujer por su orientación sexual.','mod',None),
 14:('Violencia contra mujeres indígenas u originarias','Violencia en la que se cruzan la discriminación de género, la étnica y la racial.','mod',None),
 15:('Violencia contra mujeres afroperuanas','Violencia que se expresa sobre todo en insultos racistas y agresiones sexuales basadas en estereotipos.','mod',None),
 16:('Violencia contra mujeres migrantes','Violencia agravada por estar fuera de su país de origen: riesgo de trata, tráfico de migrantes y violencia de género.','mod',None),
 17:('Violencia contra mujeres con virus de inmunodeficiencia humana','Violencia y discriminación contra mujeres que viven con VIH, en la pareja o en los servicios de salud.','mod',None),
 18:('Violencia en mujeres privadas de libertad','Violencia física, sexual o psicológica contra mujeres en prisión, incluida la de quienes las custodian.','mod',None),
 19:('Violencia contra las mujeres con discapacidad','Mayor riesgo de violencia, abandono o explotación, dentro y fuera del hogar.','mod',None),
 20:('Acoso a través del proceso judicial','Presentar denuncias y demandas en serie contra una expareja para hostigarla y desgastarla.','mod',None),
 21:('Desaparición por particulares','Desaparición de mujeres, a menudo vinculada al feminicidio, la trata o la violencia sexual.','mod',None)}
_DONDE={'vinc':'En la Ficha CEM: vínculo con la persona agresora','fem':'En la Ficha CEM: sección de tentativa de feminicidio','sex':'En la Ficha CEM: forma de violencia sexual','mod':'En la Ficha CEM: «otras modalidades»','otro':''}
_FAM=[('En las relaciones cercanas',[1,2,20,21]),('Violencia sexual y explotación',[3,4,5,8]),('En instituciones y en la vida pública',[6,7,9,18]),('Según el contexto o el medio',[10,11,12]),('Cuando se suma otra discriminación',[13,14,15,16,17,19])]
# Casos: (situación, tipos, formas según la Ficha CEM, vínculo, detalle del vínculo, modalidad en la ficha, explicación de la modalidad, fila del mapa, fuentes)
_CASOS=[('Su conviviente la empuja, la tira al suelo y le da bofetadas.',['fis'],['Empujones, tirar al suelo','Bofetadas'],'Pareja','Conviviente','Ninguna otra modalidad',
  'Al ser su pareja, el Reglamento lo describe como «violencia en relación de pareja». La ficha ya lo recoge en el vínculo, por eso en «otras modalidades» marca «ninguna».','ning',[('Ley N.° 30364, arts. 7 y 8',L30364),('Reglamento, art. 8.1',REGL)]),
 ('Su exenamorado la insulta, la humilla y la vigila a toda hora.',['psi'],['Gritos e insultos','Desvalorización y humillación','Vigilancia continua o persecución'],'Pareja','Exenamorado','Ninguna otra modalidad',
  'Mismo vínculo que el caso anterior, otro tipo de violencia. El vínculo no decide el tipo.','ning',[('Ley N.° 30364, arts. 7 y 8',L30364)]),
 ('Su esposo le quita el sueldo y no la deja administrar su dinero.',['eco'],['Quitarle sus ingresos o impedir que los administre','Limitar o controlar sus ingresos'],'Pareja','Cónyuge','Ninguna otra modalidad',
  'Otra vez la pareja, ahora con violencia económica: cualquiera de los cuatro tipos puede ocurrir dentro de un mismo vínculo.','ning',[('Ley N.° 30364, art. 8, lit. d',L30364)]),
 ('Su jefe la amenaza con despedirla si no accede a sus propuestas sexuales.',['sex'],['Hostigamiento sexual'],'Sin vínculo de pareja ni familiar','Empleador','Ninguna otra modalidad',
  'El hostigamiento sexual es una de las 21 modalidades del Reglamento, pero la ficha lo registra como una forma de violencia sexual. Por eso en «otras modalidades» va «ninguna».','ning',[('Ley N.° 27942 y su Reglamento (D.S. 014-2019-MIMP)','https://www.minedu.gob.pe/reforma-magisterial/pdf/disciplinario/2024/ley27942_ley_de_prevencion_y_sancion_del_hostigamiento_sexual.pdf')]),
 ('Su exnovio publica en redes sociales fotos íntimas de ella, sin su autorización.',['sex'],['Difusión de imágenes o audios con contenido sexual'],'Pareja','Exnovio','Violencia a través de las tecnologías de la información y comunicación',
  'El daño ocurre a través de redes sociales. El Código Penal lo sanciona como delito, con más pena si hubo relación de pareja o se usaron redes sociales.','tic',[('Código Penal, art. 154-B',DL1410),('Reglamento, art. 8.1',REGL)]),
 ('En el concejo municipal, un regidor insulta y humilla a una regidora para que no ejerza su cargo.',['psi'],['Gritos e insultos','Desvalorización y humillación'],'Sin vínculo de pareja ni familiar','Compañero de trabajo','Acoso político',
  'Busca impedir que una autoridad electa ejerza sus derechos políticos. Los CEM registran la mayoría de estos casos como violencia psicológica.','pol',[('Ley N.° 31155, arts. 2 y 3',L31155)]),
 ('Un vecino insulta a una mujer indígena con expresiones racistas por su origen y su lengua.',['psi'],['Insulto étnico-racial'],'Sin vínculo de pareja ni familiar','Vecino','Violencia contra mujeres indígenas u originarias',
  'La agresión se dirige a su identidad indígena: se suman la discriminación de género y la étnico-racial.','ind',[('Reglamento, art. 8.1',REGL)])]
_FILAS=[('ning','Ninguna otra modalidad'),('tic','Tecnologías (TIC)'),('pol','Acoso político'),('ind','Mujeres indígenas u originarias')]
_TCNT={};_MCNT={}
for _r in _EST.values():
    for _t in _r.get('tipos') or []: _TCNT[_t]=_TCNT.get(_t,0)+1
    for _m in _r.get('mod') or []: _MCNT[_m]=_MCNT.get(_m,0)+1
_tipos=''
for n,k,d,ic,forms in _TIPOS:
    c=_TCNT.get(n,0)
    _tipos+=(f'<article class="tp tp-{k}"><span class="tp-i">{_tic(k)}</span><h3>{n}</h3><p>{d}</p>'
      f'<details class="tp-f"><summary>Cómo se manifiesta ({len(forms)} formas)</summary><ul>{"".join(f"<li>{_e(x)}</li>" for x in forms)}</ul><small>Según la Ficha de Registro de Casos del CEM</small></details>'
      +(f'<a href="evidencia.html?tipo={_q(n)}">{c} {"estudio" if c==1 else "estudios"} en el banco →</a>' if c else '<span class="tp-0">Aún no hay estudios en el banco</span>')+'</article>')
_vinc=''.join(f'<article class="vc"><h3>{t}</h3><p>{d}</p></article>' for t,d in _VINC)
_fams=''
for t,L in _FAM:
    items=''
    for n in L:
        nom,res,donde,key=_MODS[n];c=_MCNT.get(key,0) if key else 0
        ev=f'<a href="evidencia.html?mod={_q(key)}">Ver {c} {"estudio" if c==1 else "estudios"} →</a>' if c else ''
        dn=f'<span class="md-d">{_DONDE[donde]}</span>' if _DONDE[donde] else ''
        items+=f'<details class="md"><summary><span class="md-n">{n:02d}</span><span class="md-t">{_e(nom)}</span>{f"<span class=md-c>{c}</span>" if c else ""}</summary><p>{_e(res)}</p>{dn}<div class="md-a">{ev}<a href="{REGL}" target="_blank" rel="noopener">Reglamento, art. 8.1 ↗</a></div></details>'
    _fams+=f'<section class="fam"><h3>{t}</h3><div class="fam-l">{items}</div></section>'
_casos=''.join(f'<button type="button" class="cs" data-c="{i}" aria-pressed="{str(i==0).lower()}"><span class="cs-n">{i+1}</span>{_e(c[0])}</button>' for i,c in enumerate(_CASOS))
_mapa_h=''.join(f'<span class="mp-th">{_tic(k)}<span>{_TSHORT[k]}</span></span>' for _,k,_,_,_ in _TIPOS)
_mapa_r=''
for f,nom in _FILAS:
    cells=''
    for _,k,_,_,_ in _TIPOS:
        ns=[i for i,c in enumerate(_CASOS) if c[7]==f and k in c[1]]
        cells+='<span class="mp-c">'+''.join(f'<button type="button" class="mp-d" data-c="{i}" aria-label="Caso {i+1}">{i+1}</button>' for i in ns)+'</span>'
    _mapa_r+=f'<div class="mp-row" data-f="{f}"><span class="mp-m">{nom}</span>{cells}</div>'
import json as _json
_CJ=_json.dumps([{'s':c[0],'t':[{'n':_TSHORT[k],'ico':_tic(k),'q':_Q[k],'b':_QL[k]} for k in c[1]],'fm':c[2],'v':c[3],'vd':c[4],'m':c[5],'mx':c[6],'f':c[7],
  'src':''.join(f'<a href="{u}" target="_blank" rel="noopener">{l} ↗</a>' for l,u in c[8])} for c in _CASOS],ensure_ascii=False)
CV=head('Tipos y modalidades de violencia · Banco de Evidencias','Cómo se describe un caso de violencia: el tipo (art. 8 de la Ley N.° 30364), el vínculo con la persona agresora y la modalidad (art. 8.1 del Reglamento), con ejemplos.','comprender-violencia.html')+header('cv')+f'''
<main>
<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="./">← Banco de Evidencias</a>
    <h1>Tipos y modalidades de violencia</h1>
    <p>Para describir un hecho de violencia, los Centros Emergencia Mujer responden tres preguntas: qué tipo de violencia es, quién la ejerce y si corresponde a alguna modalidad. Esta guía explica cada una con la norma que la sustenta.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="sv-intro"><h2>Tres preguntas para describir un caso</h2></div>
    <div class="q3">
      <a class="q3-c t" href="#tipos"><span class="q3-n">1</span><span class="q2-k">Tipo de violencia</span><h3>¿Qué daño se produce?</h3><p>Física, psicológica, sexual o económica. Un mismo hecho puede tener más de un tipo.</p><small>Ley N.° 30364, art. 8</small></a>
      <a class="q3-c v" href="#vinculo"><span class="q3-n">2</span><span class="q2-k">Vínculo</span><h3>¿Quién la ejerce?</h3><p>La pareja o expareja, un familiar u otra persona: un vecino, un docente, un jefe, alguien desconocido.</p><small>Ley N.° 30364, art. 7</small></a>
      <a class="q3-c m" href="#modalidades"><span class="q3-n">3</span><span class="q2-k">Modalidad</span><h3>¿Hay una situación o contexto particular?</h3><p>Por ejemplo, si ocurre por redes sociales, en la vida política o contra una mujer indígena. Muchos casos no tienen una modalidad adicional.</p><small>Reglamento de la Ley N.° 30364, art. 8.1</small></a>
    </div>
    <p class="q2-note">Las tres respuestas son independientes: <b>el vínculo o la modalidad no deciden el tipo</b>. Al final de la guía puedes <a href="#casos">practicarlo con siete situaciones</a>.</p>
  </div>
</section>
<section class="section tp-sec" id="tipos">
  <div class="wrap">
    <div class="sv-intro"><span class="q2-k">Pregunta 1 · Artículo 8 de la Ley N.° 30364</span><h2>Los cuatro tipos de violencia</h2><p>Síntesis de las definiciones de la ley. Abre cada tipo para ver cómo se manifiesta, según las formas que registran los Centros Emergencia Mujer.</p></div>
    <div class="tps">{_tipos}</div>
  </div>
</section>
<section class="section" id="vinculo">
  <div class="wrap">
    <div class="sv-intro"><span class="q2-k v">Pregunta 2 · Artículo 7 de la Ley N.° 30364</span><h2>El vínculo con la persona agresora</h2><p>La ley protege a las mujeres en todo su ciclo de vida y a los integrantes del grupo familiar. Para registrar un caso, el CEM agrupa el vínculo en tres categorías.</p></div>
    <div class="vcs">{_vinc}</div>
  </div>
</section>
<section class="section cv-mods" id="modalidades">
  <div class="wrap">
    <div class="sv-intro"><span class="q2-k m">Pregunta 3 · Artículo 8.1 del Reglamento de la Ley N.° 30364</span><h2>Las 21 modalidades de violencia contra las mujeres</h2><p>El Reglamento enumera 21 modalidades, «entre otras»: la lista no es cerrada. Aquí se agrupan en cinco bloques solo para facilitar la lectura; la numeración es la del Reglamento.</p></div>
    <div class="mod-note"><b>¿Cómo las registra el CEM?</b> La ficha no las anota todas en el mismo lugar. La relación de pareja queda en el <b>vínculo</b>; la trata, la explotación sexual, el acoso y el hostigamiento sexual, como <b>formas de violencia sexual</b>; el feminicidio, en su propia sección. El resto va en «otras modalidades», con una sola respuesta, o «ninguna otra modalidad» si no corresponde. Desde 2023 la ficha incluye además la <b>violencia contra mujeres defensoras de derechos humanos</b>.</div>
    <div class="fams">{_fams}</div>
  </div>
</section>
<section class="section gx-sec" id="casos">
  <div class="wrap">
    <div class="sv-intro"><span class="q2-k">Ponlo en práctica</span><h2>¿Cómo se describe un caso?</h2><p>Elige una situación y mira cómo se responden las tres preguntas, con lo que dicen la norma y la ficha de registro.</p></div>
    <div class="gx">
      <div class="gx-cases" role="group" aria-label="Situaciones de ejemplo"><span class="gx-lbl">Elige una situación</span>{_casos}</div>
      <div class="gx-panel" aria-live="polite">
        <p class="gx-sit"><span>La situación</span><b id="gxS"></b></p>
        <div class="gx-step t"><span class="gx-n">1</span><div><h3>¿Qué tipo de violencia es?</h3><div class="gx-ans" id="gxT"></div><p class="gx-fm" id="gxF"></p><div id="gxTQ"></div></div></div>
        <div class="gx-step v"><span class="gx-n">2</span><div><h3>¿Quién la ejerce?</h3><div class="gx-ans"><span class="gx-chip v" id="gxV"></span></div></div></div>
        <div class="gx-step m"><span class="gx-n">3</span><div><h3>¿Hay una modalidad adicional?</h3><div class="gx-ans"><span class="gx-chip m" id="gxM"></span></div><p class="gx-why" id="gxMX"></p></div></div>
        <p class="gx-src" id="gxSrc"></p>
      </div>
    </div>
    <div class="mp">
      <div class="mp-head"><h3>Los siete casos en un solo mapa</h3><p>Los casos 1 a 4 no tienen una modalidad adicional y cada uno es de un tipo distinto. Los casos 2, 6 y 7 son todos de violencia psicológica, con modalidades distintas.</p></div>
      <div class="mp-grid"><div class="mp-row mp-hd"><span class="mp-m"></span>{_mapa_h}</div>{_mapa_r}</div>
    </div>
    <p class="gx-note">Situaciones ilustrativas redactadas a partir de las normas citadas y de las formas que registra la Ficha CEM, con fines pedagógicos. La calificación de un caso real corresponde a las autoridades competentes.</p>
  </div>
</section>
<section class="section cv-end">
  <div class="wrap">
    <div class="cv-end-in">
      <div><h2>De las definiciones a la evidencia</h2><p>Clasificar ayuda a ordenar la información, pero no dice por sí solo cuán frecuente es cada forma de violencia ni si una intervención funciona. Para eso hay que revisar el diseño, la medición y las limitaciones de cada estudio. La OMS recomienda medir la violencia a partir de conductas concretas, y advierte que la violencia psicológica y la económica son las más difíciles de comparar entre encuestas.</p><a class="guide-action" href="evidencia.html">Explorar la evidencia →</a></div>
      <div class="cv-src"><b>Fuentes</b><a href="{L30364}" target="_blank" rel="noopener">Ley N.° 30364, artículos 7 y 8 ↗</a><a href="{REGL}" target="_blank" rel="noopener">Reglamento de la Ley N.° 30364, art. 8.1 (D.S. N.° 005-2022-MIMP) ↗</a><span>{FICHA}, ítems A.6.4, B.2 y B.2.1. Programa Nacional Warmi Ñan.</span><a href="https://iris.who.int/handle/10665/375427" target="_blank" rel="noopener">OMS y ONU Mujeres (2023) · Calidad de las encuestas sobre violencia contra las mujeres ↗</a></div>
    </div>
  </div>
</section>
</main>
'''+FOOTER+'''<script>
(function(){const C='''+_CJ+r''';const B=[...document.querySelectorAll('.cs')],$=id=>document.getElementById(id);
function sel(i){const c=C[i];B.forEach((b,j)=>b.setAttribute('aria-pressed',j===i));
 $('gxS').textContent=c.s;
 $('gxT').innerHTML=c.t.map(t=>`<span class="gx-chip t">${t.ico}Violencia ${t.n.toLowerCase()}</span>`).join('');
 $('gxF').innerHTML='<b>Forma registrada:</b> '+c.fm.join(' · ');
 $('gxTQ').innerHTML=c.t.map(t=>`<blockquote class="gx-q">${t.q}<cite>${t.b}</cite></blockquote>`).join('');
 $('gxV').textContent=c.v+' · '+c.vd;
 $('gxM').textContent=c.m;$('gxM').classList.toggle('none',c.f==='ning');$('gxMX').textContent=c.mx;
 $('gxSrc').innerHTML='Base: '+c.src;
 document.querySelectorAll('.mp-d').forEach(d=>d.classList.toggle('on',+d.dataset.c===i))}
B.forEach((b,i)=>b.onclick=()=>sel(i));
document.querySelectorAll('.mp-d').forEach(d=>d.onclick=()=>{sel(+d.dataset.c);document.querySelector('.gx').scrollIntoView({behavior:'smooth',block:'start'})});sel(0)})();
</script>
</body>
</html>
'''

for name,html in (('evidencia.html',EVID),('index.html',INDEX),('tablero.html',TABLERO),('fuentes.html',FUENTES),('servicios.html',SERV),('comprender-violencia.html',CV)):
    open(name,'w',encoding='utf-8').write(html)
print('ok')
