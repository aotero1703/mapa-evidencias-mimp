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
    items=[('evidencia.html','Evidencia científica','ev'),('tablero.html','Indicadores','in'),('fuentes.html','Fuentes externas','fx'),('territorios-prioritarios.html','Territorios Prioritarios','tp')]
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
        <p>Investigaciones para comprender la violencia y programas evaluados para saber qué ayuda a enfrentarla, en el marco de la Ley N.° 30364.</p>
        <div class="facts"><span>15 programas evaluados</span><span>112 estudios</span></div>
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
    <a class="door tp" href="territorios-prioritarios.html">
      <div class="top"><svg class="art" viewBox="0 0 200 200" aria-hidden="true"><g fill="none" stroke="rgba(255,255,255,.24)" stroke-width="2"><circle cx="120" cy="80" r="70"/><circle cx="120" cy="80" r="46"/></g><path d="M70 54l30-15 28 13 29-13v82l-29 13-28-13-30 15z" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/><path d="M100 39v82m28-69v82" fill="none" stroke="#fff" stroke-width="2" opacity=".65"/><path d="M118 67c-13 0-21 9-21 21 0 16 21 35 21 35s21-19 21-35c0-12-8-21-21-21z" fill="#f2a93b"/><circle cx="118" cy="88" r="7" fill="#fff"/></svg><span class="kicker">Análisis territorial</span></div>
      <div class="body">
        <h2>Territorios Prioritarios</h2>
        <p>Explora mapas e indicadores territoriales para identificar zonas que requieren mayor atención y orientar las intervenciones frente a la violencia.</p>
        <div class="facts"><span>Mapa interactivo</span><span>Priorización territorial</span></div>
        <div class="basis"><b>Art. 43:</b> generar información para orientar decisiones y políticas públicas basadas en evidencia.</div>
        <span class="go">Explorar territorios <i>→</i></span>
      </div>
    </a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>Marco normativo</h2>
    <p class="section-lede">El banco forma parte del sistema de información que la ley encarga al Observatorio, para que las decisiones de política pública se basen en evidencia.</p>
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


EVID=head('Evidencia científica · Banco de Evidencias','Estudios nacionales e internacionales sobre la violencia contra las mujeres y los integrantes del grupo familiar, ordenados por tipo y modalidad de violencia según la Ley N.° 30364.','evidencia.html')+header('ev')+'''
<main>
<section class="page-hero">
  <div class="wrap">
    <a class="crumb" href="./">← Banco de Evidencias</a>
    <h1>Evidencia científica</h1>
    <p>Lo que se ha investigado sobre la violencia contra las mujeres y los integrantes del grupo familiar, organizado según la Ley N.° 30364.</p>
    <div class="hsearch"><input type="search" id="q" placeholder="Buscar en todo el banco: Cuna Más, Línea 100, alcohol, adolescentes…" aria-label="Buscar en todo el banco"></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="tabs" role="tablist" aria-label="Secciones de la evidencia">
      <button type="button" role="tab" id="tE" aria-selected="true" aria-controls="tabE"><b>Comprender la violencia</b><span class="td">Investigaciones sobre por qué ocurre la violencia, cómo afecta a las personas y cómo responde el Estado.</span></button>
      <button type="button" role="tab" id="tF" aria-selected="false" aria-controls="tabF"><b>¿Qué ayuda a enfrentar la violencia?</b><span class="td">Programas y servicios que fueron evaluados para saber si reducen la violencia, y qué resultados tuvieron.</span></button>
    </div>
    <div id="tabF" role="tabpanel" aria-labelledby="tF" hidden>
      <div id="solHome">
        <h3 class="ejes-h">Según la Ley N.° 30364</h3>
        <div class="ejes" id="ejes"></div>
      </div>
      <div id="ejeDet" hidden></div>
      <div id="solDet" hidden></div>
    </div>
    <div id="tabE" role="tabpanel" aria-labelledby="tE">
      <div class="filt">
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
function gist(r){const t=(r.res||r.prop||'').replace(/\s+/g,' ').trim();const m=t.match(/^.{40,280}?[.;](\s|$)/);return m?m[0].trim():(t.length>260?t.slice(0,260).trim()+'…':t)}
const TEMAS=[['Causas y factores asociados','Desigualdades entre mujeres y hombres, normas sociales, relaciones de poder y factores de riesgo.','Ley N.° 30364, art. 3 (enfoques de género e integralidad) y art. 45, inc. 1.f'],['Consecuencias de la violencia','Efectos de la violencia en la salud, la educación, el empleo y el bienestar.','Ley N.° 30364, art. 42 (el registro consigna causas y consecuencias)'],['Prevención de la violencia','Educación, sensibilización, cambio de normas sociales y programas preventivos.','Ley N.° 30364, arts. 1 y 27'],['Atención y recuperación','Servicios de atención, salud física y mental, acompañamiento y recuperación.','Ley N.° 30364, arts. 1, 10 y 27 al 29'],['Protección y acceso a la justicia','Denuncias, medidas de protección, barreras de acceso y respuesta judicial.','Ley N.° 30364, arts. 1, 10 y 13 al 26'],['Sanción y reeducación','Respuesta penal, sanciones y programas de reeducación de personas agresoras.','Ley N.° 30364, art. 1 y arts. 30 al 32'],['Reparación y restitución de derechos','Reparación del daño, recuperación de derechos y medidas de apoyo.','Ley N.° 30364, arts. 1, 2 (inc. 5) y 33']];
const NOTIPO='No trata un tipo de violencia en particular';
const POBS=['Mujeres','Niñas, niños y adolescentes','Jóvenes','Hombres','Personas adultas mayores','Pueblos indígenas','Operadores y servidores públicos','Población en general'];
const tipoOf=r=>r.tipos?r.tipos:[NOTIPO];
function match(r,skip){const q=S.q.trim().toLowerCase();
  return (skip==='tema'||!S.tema||r.temas.includes(S.tema))&&(skip==='tipo'||!S.tipo||tipoOf(r).includes(S.tipo))&&(skip==='pob'||!S.pob||r.pob_g.includes(S.pob))&&(skip==='amb'||!S.amb||r.amb===S.amb)
   &&(skip==='mod'||!S.mod||(r.mod||[]).includes(S.mod))&&(!q||[r.t,r.a,r.dim,r.pob,r.prop,r.res,r.tipo,r.vy,r.vx,r.paises.join(' '),(r.mod||[]).join(' '),r.temas.join(' ')].join(' ').toLowerCase().includes(q))}
function opts(id,all,vals,cur,key){const n=v=>R.filter(r=>match(r,key)&&(key==='tema'?r.temas.includes(v):key==='tipo'?tipoOf(r).includes(v):r.pob_g.includes(v))).length;
  $(id).innerHTML=`<option value="">${all}</option>`+vals.map(v=>{const c=n(v);return `<option value="${esc(v)}"${v===cur?' selected':''}${c||v===cur?'':' disabled'}>${esc(v)} (${c})</option>`}).join('')}
function home(){}
function show(){
  opts('fTema','Todos los temas',TEMAS.map(t=>t[0]),S.tema,'tema');
  opts('fTipo','Todos los tipos',TIPOS.concat([NOTIPO]),S.tipo,'tipo');
  opts('fPob','Todas las poblaciones',POBS,S.pob,'pob');$('fAmb').value=S.amb;
  const d=[];if(S.tema){const t=TEMAS.find(t=>t[0]===S.tema);d.push(`<b>${esc(S.tema)}:</b> ${t[1]} <span class="base">${t[2]}</span>`)};if(S.tipo&&TDESC[S.tipo])d.push(`<b>${esc(S.tipo)} (art. 8 de la Ley):</b> ${TDESC[S.tipo]}`);
  $('fDesc').innerHTML=d.join('<br>');$('fDesc').hidden=!d.length;
  if(S.tipo&&S.tipo!==NOTIPO&&S.tipo!=='Estudios generales sobre violencia'){const base=R.filter(r=>match(r,'mod')),c={};base.forEach(r=>(r.mod||[]).forEach(m=>c[m]=(c[m]||0)+1));
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
    return L.length?`<button type="button" class="eje" data-e="${e.id}"><span class="q">${e.base}</span><b>${e.n}</b><span class="d">${e.d}</span><span class="n">${L.length} ${L.length===1?'programa evaluado':'programas evaluados'}</span><span class="go">Ver qué funciona →</span></button>`
      :`<div class="eje vacio"><span class="q">${e.base}</span><b>${e.n}</b><span class="d">${e.d}</span><span class="n">Todavía no hay programas evaluados en este tema.</span></div>`}).join('');
  document.querySelectorAll('button.eje').forEach(b=>b.onclick=()=>{F.eje=b.dataset.e;solRender();scrollTo({top:$('tabF').offsetTop-90})});
}
function ejeDetail(e){const L=SOL.soluciones.filter(x=>x.eje===e.id);
  $('ejeDet').innerHTML=`<button type="button" class="back" id="ejeBack">← Todos los ejes</button>
   <div class="eje-head"><p class="kick">${e.base}</p><h2>${e.n}</h2><p>${e.d}</p></div>
   <div class="sols">${L.map(x=>{const t=RES[x.ef];return `<button type="button" class="sol" data-s="${x.id}"><b>${x.n}</b><span class="efp ${t[1]}">${t[0]}</span><span class="ev">${x.ev}</span><span class="go">Ver ${x.casos.length===1?'el estudio':'los '+nS(x.casos.length)} →</span></button>`}).join('')}</div>`;
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

for name,html in (('evidencia.html',EVID),('index.html',INDEX),('tablero.html',TABLERO),('fuentes.html',FUENTES)):
    open(name,'w',encoding='utf-8').write(html)
print('ok')
