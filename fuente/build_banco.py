# Paso 3: genera las páginas del Banco de Evidencias (portada, tablero y fuentes) con la misma cabecera y pie.
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
    items=[('evidencia.html','Evidencia científica','ev'),('tablero.html','Indicadores','in'),('fuentes.html','Fuentes externas','fx'),('servicios.html','Servicios','sv'),('territorios-prioritarios.html','Territorios Prioritarios','tp')]
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
        <h2>Servicios del MIMP</h2>
        <p>Servicios vinculados con la Ley N.° 30364 y acceso complementario al catálogo general del sector MIMP.</p>
        <div class="facts"><span>Tres niveles</span><span>Catálogo 2026</span></div>
        <div class="basis"><b>Ley N.° 30364:</b> identifica los servicios pertinentes para la prevención y respuesta frente a la violencia.</div>
        <span class="go">Conocer los servicios <i>→</i></span>
      </div>
    </a>
    <a class="door tp" href="territorios-prioritarios.html">
      <div class="top"><svg class="art" viewBox="0 0 200 200" aria-hidden="true"><g fill="none" stroke="rgba(255,255,255,.24)" stroke-width="2"><circle cx="120" cy="80" r="70"/><circle cx="120" cy="80" r="46"/></g><path d="M70 54l30-15 28 13 29-13v82l-29 13-28-13-30 15z" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/><path d="M100 39v82m28-69v82" fill="none" stroke="#fff" stroke-width="2" opacity=".65"/><path d="M118 67c-13 0-21 9-21 21 0 16 21 35 21 35s21-19 21-35c0-12-8-21-21-21z" fill="#f2a93b"/><circle cx="118" cy="88" r="7" fill="#fff"/></svg><span class="kicker">Análisis territorial</span></div>
      <div class="body">
        <h2>Territorios Prioritarios</h2>
        <p>Explora los casos atendidos por los servicios especializados y sus diferencias territoriales. Estos registros no miden la prevalencia de violencia.</p>
        <div class="facts"><span>Mapa interactivo</span><span>Priorización territorial</span></div>
        <div class="basis"><b>Art. 43:</b> generar información para orientar decisiones y políticas públicas basadas en evidencia.</div>
        <span class="go">Explorar territorios <i>→</i></span>
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
      <p class="fdesc">Solo se incluyen estudios sobre la violencia que comprende la Ley N.° 30364. Los temas siguen las acciones del artículo 1 de la Ley y las poblaciones, sus sujetos de protección (arts. 1 y 7). La clasificación de cada estudio es orientativa.</p><div class="filt">
        <label>Tema de investigación<select id="fTema"></select></label>
        <label>Tipo de violencia<select id="fTipo"></select></label>
        <label>Población<select id="fPob"></select></label>
        <label>Ámbito<select id="fAmb"><option value="">Nacional e internacional</option><option value="Nacional">Nacional</option><option value="Internacional">Internacional</option></select></label>
      </div>
      <p class="fdesc" id="fDesc" hidden></p>
      <div class="mods" id="mods" role="group" aria-label="Modalidad de violencia" hidden></div>
      <div class="toolbar rbar">
        <p class="count" id="count"></p>
        <button type="button" class="clear" id="clear" hidden>Limpiar filtros</button>
        <select id="sort" aria-label="Ordenar"><option value="y">Más recientes primero</option><option value="t">Por título (A–Z)</option></select>
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
const TIPOS=['Violencia física','Violencia psicológica','Violencia sexual','Violencia económica o patrimonial','Estudios generales sobre violencia'];
const TDESC={'Violencia física':'Daño a la integridad corporal o a la salud, incluido el maltrato por negligencia o descuido.','Violencia psicológica':'Controlar o aislar a la persona contra su voluntad, humillarla, avergonzarla, insultarla, estigmatizarla o estereotiparla.','Violencia sexual':'Actos de naturaleza sexual sin consentimiento o bajo coacción, incluso sin contacto físico.','Violencia económica o patrimonial':'Menoscabo de los recursos económicos o patrimoniales: quitar o retener bienes, documentos o ingresos, o no cumplir con los alimentos.','Estudios generales sobre violencia':'Marcos conceptuales, prevalencia general, factores de riesgo y servicios.'};
const DDESC={'Cuidados domésticos':'Las tareas del hogar y la atención a la familia: cocinar, limpiar, cuidar a hijas e hijos. Las hacen las propias familias sin pago o trabajadoras del hogar remuneradas.','Cuidados domiciliarios':'La atención que una persona cuidadora brinda en la vivienda a quien depende de otras personas: personas adultas mayores, con discapacidad o con una enfermedad.','Cuidados institucionales':'Servicios de cuidado fuera del hogar, como cunas, guarderías, centros de día o residencias.','Cuidados comunitarios':'Cuidado que organiza la propia comunidad, como ollas comunes, comedores populares y redes vecinales.','Empleo':'Acceso de las mujeres al trabajo y a ingresos propios, y la brecha salarial.','Educación':'Acceso, permanencia y estereotipos en la escuela y la universidad.','Salud':'Salud física, mental, sexual y reproductiva de las mujeres.','Brechas entre mujeres y hombres':'Diferencias entre mujeres y hombres medidas en varios ámbitos a la vez.','Acceso a tecnología':'Uso de internet, celulares y habilidades digitales.','Participación y liderazgo':'Presencia de mujeres en cargos de decisión, la política y las organizaciones.','Enfoques transversales':'Estudios que miran las diferencias por edad, etnia u otras condiciones.'};
const GROUPS=[['Igualdad de oportunidades','Condiciones que fortalecen la autonomía de las mujeres y reducen el riesgo de violencia.'],['Sistema de cuidados','Quién cuida, dónde y en qué condiciones. Cuando el cuidado recae solo en las mujeres, limita su autonomía económica.']];
const GEN='Varias o sin modalidad específica';
let R=[],S={tema:'',tipo:'',pob:'',mod:'',amb:'',q:'',sort:'y',open:null,shown:20};
const pl=(n,a,b)=>n+' '+(n===1?a:b);
function gist(r){if(r.resumen)return r.resumen;const t=(r.res||r.prop||'').replace(/\s+/g,' ').trim();const m=t.match(/^.{40,280}?[.;](\s|$)/);return m?m[0].trim():(t.length>260?t.slice(0,260).trim()+'…':t)}
const TEMAS=[['Causas y consecuencias de la violencia','Factores que explican la violencia, cómo se presenta y qué efectos tiene en la salud, la educación, el empleo y el bienestar.','Ley N.° 30364, arts. 42 y 45, inc. 1.f'],['Prevención de la violencia','Acciones para evitar que la violencia ocurra, como el trabajo con varones, colegios y comunidades.','Ley N.° 30364, arts. 1 y 27'],['Atención y recuperación de las víctimas','Servicios que atienden a las víctimas y las ayudan a recuperarse.','Ley N.° 30364, arts. 1, 10 y 27 al 29'],['Protección de las víctimas','Medidas de protección, denuncia y respuesta de la policía y el sistema de justicia para proteger a las víctimas.','Ley N.° 30364, arts. 1 y 13 al 26'],['Persecución y sanción','Investigación, procesamiento y sanción de los hechos de violencia.','Ley N.° 30364, arts. 1, 16 al 20'],['Reeducación de las personas agresoras','Tratamiento para que las personas agresoras dejen de ejercer violencia.','Ley N.° 30364, arts. 1 y 30 al 32'],['Reparación del daño','Medidas para reparar el daño causado a las víctimas y restituir sus derechos.','Ley N.° 30364, arts. 1 y 33']];
const NOTIPO='No trata un tipo de violencia en particular';
const POBS=['Mujeres','Integrantes del grupo familiar','Niñas, niños y adolescentes','Personas adultas mayores','Personas con discapacidad','Varones y personas agresoras','Operadores del sistema'];
const PDESC={'Mujeres':'Durante todo su ciclo de vida: niña, adolescente, joven, adulta y adulta mayor (art. 7).','Integrantes del grupo familiar':'Cónyuges, convivientes, padres, hijos y demás parientes que señala el art. 7.','Niñas, niños y adolescentes':'En especial situación de vulnerabilidad (art. 1).','Personas adultas mayores':'En especial situación de vulnerabilidad (art. 1).','Personas con discapacidad':'En especial situación de vulnerabilidad (art. 1).','Varones y personas agresoras':'Programas para varones y reeducación de personas agresoras (arts. 27 y 30 al 32).','Operadores del sistema':'Policía, Ministerio Público, Poder Judicial y servicios de atención (arts. 2, 18 y 45).'};
const tipoOf=r=>r.tipos||[];
function match(r,skip){const q=S.q.trim().toLowerCase();
  return (skip==='tema'||!S.tema||r.temas.includes(S.tema))&&(skip==='tipo'||!S.tipo||tipoOf(r).includes(S.tipo))&&(skip==='pob'||!S.pob||r.pob_g.includes(S.pob))&&(skip==='amb'||!S.amb||r.amb===S.amb)
   &&(skip==='mod'||!S.mod||(r.mod||[]).includes(S.mod))&&(!q||[r.t,r.a,r.dim,r.pob,r.prop,r.res,r.tipo,r.vy,r.vx,r.paises.join(' '),(r.mod||[]).join(' '),r.temas.join(' ')].join(' ').toLowerCase().includes(q))}
function opts(id,all,vals,cur,key){const n=v=>R.filter(r=>match(r,key)&&(key==='tema'?r.temas.includes(v):key==='tipo'?tipoOf(r).includes(v):r.pob_g.includes(v))).length;
  $(id).innerHTML=`<option value="">${all}</option>`+vals.map(v=>{const c=n(v);return `<option value="${esc(v)}"${v===cur?' selected':''}${c||v===cur?'':' disabled'}>${esc(v)} (${c})</option>`}).join('')}
function home(){}
function show(){
  opts('fTema','Todos los temas',TEMAS.map(t=>t[0]),S.tema,'tema');
  opts('fTipo','Todos los tipos',TIPOS,S.tipo,'tipo');
  opts('fPob','Todas las poblaciones',POBS,S.pob,'pob');$('fAmb').value=S.amb;
  const d=[];if(S.tema){const t=TEMAS.find(t=>t[0]===S.tema);d.push(`<b>${esc(S.tema)}:</b> ${t[1]} <span class="base">${t[2]}</span>`)};if(S.tipo&&TDESC[S.tipo])d.push(`<b>${esc(S.tipo)} (art. 8 de la Ley):</b> ${TDESC[S.tipo]}`);if(S.pob&&PDESC[S.pob])d.push(`<b>${esc(S.pob)}:</b> ${PDESC[S.pob]}`);
  $('fDesc').innerHTML=d.join('<br>');$('fDesc').hidden=!d.length;
  if(S.tipo&&S.tipo!=='Estudios generales sobre violencia'){const base=R.filter(r=>match(r,'mod')),c={};base.forEach(r=>(r.mod||[]).forEach(m=>c[m]=(c[m]||0)+1));
    const ms=Object.keys(c).sort((a,b)=>(a===GEN)-(b===GEN)||c[b]-c[a]);
    $('mods').innerHTML='<span class="mods-l">Modalidad (Reglamento):</span>'+[`<button type="button" class="dim" data-m="" aria-pressed="${!S.mod}">Todas <em>${base.length}</em></button>`].concat(ms.map(m=>`<button type="button" class="dim" data-m="${esc(m)}" aria-pressed="${S.mod===m}">${esc(m)} <em>${c[m]}</em></button>`)).join('');
    $('mods').hidden=false;document.querySelectorAll('#mods .dim').forEach(b=>b.onclick=()=>{S.mod=b.dataset.m;S.shown=20;show()});
  }else{$('mods').hidden=true;S.mod=''}
  const L=R.filter(r=>match(r));
  L.sort(S.sort==='t'?(a,b)=>a.t.localeCompare(b.t,'es'):(a,b)=>(+b.y||0)-(+a.y||0));
  const any=S.tema||S.tipo||S.pob||S.amb||S.q.trim();
  $('count').textContent=any?pl(L.length,'investigación encontrada','investigaciones encontradas'):`Todas las investigaciones (${L.length})`;$('clear').hidden=!any;
  $('cards').innerHTML=L.length?L.slice(0,S.shown).map(card).join(''):'<div class="empty">No hay investigaciones con esos filtros. Prueba quitando alguno.</div>';
  $('more').hidden=L.length<=S.shown;$('more').textContent=`Ver más investigaciones (${L.length-S.shown} restantes)`;
  document.querySelectorAll('.paper [data-open]').forEach(b=>b.onclick=()=>{const n=+b.dataset.open;S.open=S.open===n?null:n;show()});
}
function card(r){const o=S.open===r.n,au=r.a?r.a.split(';')[0].trim()+(r.a.includes(';')?' et al.':''):'Autor no registrado';
  const pais=r.amb==='Nacional'?'Perú':(r.paises.length>2?'Varios países':r.paises.join(', ')||'Varios países');
  const tags=r.temas.map(t=>`<span class="tag dimtag">${esc(t)}</span>`).join('');
  const tipos=r.tipos?r.tipos.filter(t=>t!=='Estudios generales sobre violencia').map(t=>t.replace('Violencia ','')):[];
  const f=(t,v)=>v?`<dt>${t}</dt><dd>${esc(v)}</dd>`:'';
  return `<article class="paper"><div class="tags">${tags}<span class="tag ${r.amb==='Nacional'?'pe':'int'}">${r.amb} · ${esc(pais)}</span></div>
   <h3>${esc(r.t)}</h3><div class="by">${esc(au)} · ${esc(r.y||'s. f.')}${tipos.length?` · Violencia ${tipos.join(', ')}`:''}</div>
   <p class="gist">${esc(gist(r))}</p>
   <div class="row"><button type="button" data-open="${r.n}" aria-expanded="${o}">${o?'Cerrar ficha':'Ver ficha completa'}</button>${r.link?`<a href="${esc(r.link)}" target="_blank" rel="noopener">Leer el estudio ↗</a>`:''}</div>
   ${o?`<dl>${f('Autoría',r.a)}${f('País',r.paises.join(', '))}${f('Tema',r.temas.join(', '))}${f('Tipo de violencia',r.tipos?r.tipos.join(', '):'')}${f('Modalidad',r.tipos?r.mod.join(', '):'')}${f('Población',r.pob)}${f('Propósito',r.prop)}${f('Intervención',[r.tipo,r.det].filter(Boolean).join('\n\n'))}${f('Estado de la evaluación',r.est)}${f('Qué se mide (Y)',r.vy)}${f('Qué lo explica (X)',r.vx)}${f('Resultados',r.res)}${f('Publicado en',r.pub)}${f('N.° en la matriz',String(r.n))}</dl>`:''}</article>`}
$('q').oninput=e=>{tab('E');S.q=e.target.value;S.shown=20;show()};
$('sort').onchange=e=>{S.sort=e.target.value;show()};
$('fTema').onchange=e=>{S.tema=e.target.value;S.shown=20;show()};
$('fTipo').onchange=e=>{S.tipo=e.target.value;S.mod='';S.shown=20;show()};
$('fPob').onchange=e=>{S.pob=e.target.value;S.shown=20;show()};
$('fAmb').onchange=e=>{S.amb=e.target.value;S.shown=20;show()};
$('clear').onclick=()=>{Object.assign(S,{tema:'',tipo:'',pob:'',amb:'',mod:'',q:'',open:null,shown:20});$('q').value='';show()};
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
Promise.all([fetch('data/estudios.json').then(r=>r.json()),fetch('data/soluciones.json').then(r=>r.json())]).then(([d,s])=>{R=d.rows;SOL=s;home();show();solRender()}).catch(()=>{$('ejes').innerHTML='<div class="empty">No se pudieron cargar los datos. Recarga la página.</div>'});
</script>
</body>
</html>
'''

# ---------- Servicios del MIMP (Catálogo de Servicios 2026), en lenguaje sencillo ----------
import sys as _s,os as _o; _s.path.insert(0,_o.path.dirname(_o.path.abspath(__file__)))
from servicios_data import NIVELES,S as SERVS
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
SERV=head('Servicios del MIMP · Banco de Evidencias','Todos los servicios del Ministerio de la Mujer y Poblaciones Vulnerables, organizados por nivel y tipo, explicados en palabras sencillas.','servicios.html')+header('sv')+f'''
<main>
<section class="page-hero sv">
  <div class="wrap">
    <a class="crumb" href="./">← Banco de Evidencias</a>
    <h1>Servicios del MIMP</h1>
    <p>Consulta primero los servicios relacionados con la prevención y respuesta frente a la violencia en el marco de la Ley N.° 30364. También puedes explorar el catálogo general del sector MIMP, que incluye servicios de otros ámbitos.</p>
  </div>
</section>
<section class="section sv-levels">
  <div class="wrap">
    <div class="sv-intro"><h2>Tres niveles de servicios</h2><p>El MIMP organiza sus servicios en tres niveles, según a quién llegan. Elige un tipo de servicio para ver cuáles son.</p></div>
    <div class="sv-lvls">{resumen}</div>
  </div>
</section>
<section class="section sv-all" id="svAll" hidden>
  <div class="wrap">
    <p class="sv-src"><b>Alcance:</b> por defecto se muestran los servicios identificados como vinculados con la violencia. Desmarca el filtro para consultar el catálogo general del MIMP. Esta identificación temática es orientativa y no sustituye la clasificación institucional.</p><div class="sv-filter" role="group" aria-label="Filtrar servicios">
      <button type="button" class="sv-close" id="svClose">← Elegir otro tipo</button><span>Quién lo brinda:</span><button type="button" data-p="" aria-pressed="true">Todos</button>{chips}
      <label class="chk"><input type="checkbox" id="soloV" checked> Solo servicios vinculados con la Ley N.° 30364</label>
    </div>
    {cuerpo}
    <p class="sv-empty" id="svEmpty" hidden>No hay servicios con ese filtro.</p>
  </div>
</section>
<section class="section sv-data">
  <div class="wrap">
    <div class="sv-intro"><h2>Qué datos hay sobre la violencia y los servicios</h2><p>Dos tipos de fuentes permiten seguir el problema y el uso de los servicios.</p></div>
    <div class="data-grid">
      <a class="dcard" href="https://portalestadistico.warminan.gob.pe/banco-de-datos/" target="_blank" rel="noopener"><span class="dk">Registros de los servicios</span><h3>Portal Estadístico de Warmi Ñan</h3><p>Casos atendidos en los Centros Emergencia Mujer y Familia y en los demás servicios del programa. Dicen cuántas personas llegan a los servicios, no cuánta violencia hay.</p><span class="go">Ir al banco de datos ↗</span></a>
      <a class="dcard" href="https://proyectos.inei.gob.pe/endes/" target="_blank" rel="noopener"><span class="dk">Encuesta del INEI</span><h3>ENDES</h3><p>Cuántas mujeres viven violencia de pareja, en todo el país y por región, y si buscaron ayuda en alguna institución.</p><span class="go">Ir a la ENDES ↗</span></a>
      <a class="dcard" href="fuentes.html"><span class="dk">Encuesta del INEI</span><h3>ENARES 2024</h3><p>Cuánto tolera la sociedad la violencia contra las mujeres, niñas, niños y adolescentes.</p><span class="go">Ver en fuentes externas →</span></a>
    </div>
    <p class="sv-src">Fuente: <a href="{CATALOGO}" target="_blank" rel="noopener">Catálogo de Servicios del Sector Mujer y Poblaciones Vulnerables 2026</a>. Las descripciones están resumidas en lenguaje sencillo; el detalle de cada servicio está en el catálogo.</p>
  </div>
</section>
</main>
'''+FOOTER+r'''<script>
(function(){let P='',T='';const btns=document.querySelectorAll('.sv-filter button[data-p]'),v=document.getElementById('soloV'),all=document.getElementById('svAll'),tb=document.querySelectorAll('.sv-types button');
function apply(){let any=0;document.querySelectorAll('.svc').forEach(c=>{const ok=c.closest('.sv-tipo').id==='tipo-'+T&&(!P||c.dataset.prog===P)&&(!v.checked||c.dataset.v==='1');c.hidden=!ok;if(ok)any++});
 document.querySelectorAll('.sv-tipo').forEach(t=>t.hidden=t.id!=='tipo-'+T);
 document.querySelectorAll('.sv-nivel').forEach(n=>n.hidden=!n.querySelector('#tipo-'+T));
 document.getElementById('svEmpty').hidden=!!any;}
tb.forEach(b=>b.onclick=()=>{T=b.dataset.t;P='';btns.forEach(x=>x.setAttribute('aria-pressed',x.dataset.p===''));tb.forEach(x=>x.setAttribute('aria-pressed',x===b));all.hidden=false;apply();all.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'})});
document.getElementById('svClose').onclick=()=>{all.hidden=true;tb.forEach(x=>x.setAttribute('aria-pressed','false'));document.querySelector('.sv-levels').scrollIntoView({block:'start'})};
btns.forEach(b=>b.onclick=()=>{P=b.dataset.p;btns.forEach(x=>x.setAttribute('aria-pressed',x===b));apply()});v.onchange=apply;})();
</script>
</body>
</html>
'''

for name,html in (('evidencia.html',EVID),('index.html',INDEX),('tablero.html',TABLERO),('fuentes.html',FUENTES),('servicios.html',SERV)):
    open(name,'w',encoding='utf-8').write(html)
print('ok')
