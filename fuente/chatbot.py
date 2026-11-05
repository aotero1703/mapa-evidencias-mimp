# Asistente guiado (respuestas predefinidas, sin IA) para la página de Evidencia científica.
# Explica tipo de violencia, vínculo y modalidad, y aplica filtros de la lista de estudios.
import json
L30364='https://www.gob.pe/74905-ley-n-30364-ley-para-prevenir-sancionar-y-erradicar-la-violencia-contra-las-mujeres-y-los-integrantes-del-grupo-familiar'
# id: (palabras clave, respuesta HTML, acción opcional, sugerencias siguientes)
KB={
 'hola':([],'¡Hola! Te ayudo a entender cómo están ordenados los estudios del banco. ¿Qué quieres saber?',None,['tipo','modalidad','diferencia','ejemplo','filtrar']),
 'tipo':(['tipo','tipos','que es tipo','tipo de violencia'],'El <b>tipo de violencia</b> es la forma que toma la violencia. La Ley N.° 30364 (art. 8) reconoce cuatro: <b>física</b>, <b>psicológica</b>, <b>sexual</b> y <b>económica o patrimonial</b>. Un mismo hecho puede tener más de un tipo.',None,['fis','psi','sex','eco']),
 'modalidad':(['modalidad','modalidades'],'La <b>modalidad</b> señala si la violencia ocurre en una situación particular: por ejemplo, el <b>acoso político</b>, la violencia <b>por redes sociales</b> o contra <b>mujeres indígenas</b>. El Reglamento de la Ley (art. 8.1) enumera 21. Muchos casos no tienen una modalidad adicional.',None,['diferencia','ejemplo','politico','tic']),
 'diferencia':(['diferencia','diferencian','distinto','igual','mismo','vs','o modalidad'],'El <b>tipo</b> dice qué violencia se ejerció; la <b>modalidad</b>, si ocurre en una situación particular. Son independientes: una misma modalidad puede incluir varios tipos, y un tipo aparece en muchas modalidades.',None,['ejemplo','vinculo','filtrar']),
 'ejemplo':(['ejemplo','caso'],'«Su expareja comparte fotos íntimas de ella sin su permiso en redes sociales».<br><span class="cb-t v">Vínculo: pareja</span> <span class="cb-t t">Tipo de violencia: sexual</span> <span class="cb-t m">Modalidad: tecnologías (TIC)</span>',None,['vinculo','guia','filtrar']),
 'vinculo':(['vinculo','vínculo','quien','quién','agresor','pareja','familiar'],'El <b>vínculo</b> es la relación con quien ejerce la violencia: la <b>pareja o expareja</b>, un <b>familiar</b> u <b>otra persona</b> (un vecino, un docente, un jefe). La Ley N.° 30364 lo define en su artículo 7.',None,['tipo','modalidad']),
 'filtrar':(['filtro','filtrar','buscar','encontrar','estudios'],'Arriba de la lista tienes los filtros <b>Tipo de violencia</b> y <b>Modalidad de violencia</b>. Se pueden usar por separado o juntos. Te llevo a ellos.',{'focus':'fTipo'},['fis','sex','politico']),
 'guia':(['guia','guía','aprender','mas','más'],'En la guía <a href="comprender-violencia.html">Tipos y modalidades</a> hay ejemplos en pizarra y las 21 modalidades explicadas.',None,['tipo','modalidad']),
 'fis':(['fisica','física','golpe','golpes'],'<b>Violencia física</b>: golpes y otros daños al cuerpo o a la salud, incluido el maltrato por negligencia.',{'tipo':'Violencia física'},['psi','sex','eco']),
 'psi':(['psicologica','psicológica','insulto','humilla','control'],'<b>Violencia psicológica</b>: insultos, humillaciones, amenazas y control contra la voluntad de la persona.',{'tipo':'Violencia psicológica'},['fis','sex','eco']),
 'sex':(['sexual','violacion','violación','acoso sexual','hostigamiento'],'<b>Violencia sexual</b>: actos de naturaleza sexual sin consentimiento o bajo coacción, incluso sin contacto físico. Incluye, por ejemplo, el hostigamiento y el acoso sexual.',{'tipo':'Violencia sexual'},['fis','psi','eco']),
 'eco':(['economica','económica','patrimonial','dinero','sueldo'],'<b>Violencia económica o patrimonial</b>: quitar o controlar el dinero, los bienes o los documentos de la persona.',{'tipo':'Violencia económica o patrimonial'},['fis','psi','sex']),
 'politico':(['politico','político','politica','política','regidora','candidata'],'<b>Acoso político</b>: conductas contra mujeres, por ser mujeres, para limitar o impedir que ejerzan sus derechos políticos (Ley N.° 31155).',None,['modalidad','tic']),
 'tic':(['redes','tic','internet','tecnologia','tecnología','digital','fotos'],'<b>Violencia a través de las tecnologías</b>: la que se ejerce o facilita por internet, redes sociales u otros medios digitales.',{'mod':'Violencia a través de las tecnologías de la información'},['modalidad','politico']),
 'pareja_mod':(['relacion de pareja','relación de pareja'],'<b>Violencia en relación de pareja</b>: la que ejerce una pareja o expareja. Es una de las 21 modalidades del Reglamento.',{'mod':'Violencia en relación de pareja'},['vinculo','modalidad']),
 'feminicidio':(['feminicidio'],'<b>Feminicidio</b>: el asesinato de una mujer por su condición de tal. Es una de las 21 modalidades del Reglamento.',{'mod':'Feminicidio'},['modalidad']),
 'armado':(['conflicto armado','armado'],'<b>Violencia en conflicto armado</b>: violencia contra las mujeres en situaciones de conflicto armado, sobre todo sexual, como ocurrió en el Perú entre 1980 y 2000.',{'mod':'Violencia en conflicto armado'},['modalidad']),
 'trata':(['trata','explotacion','explotación'],'<b>Trata con fines de explotación sexual</b>: captar, trasladar o retener a una persona para explotarla sexualmente.',{'mod':'Trata de personas con fines de explotación sexual'},['modalidad']),
 'indigena':(['indigena','indígena','originaria','racismo','racista'],'<b>Violencia contra mujeres indígenas u originarias</b>: violencia en la que se suman la discriminación de género y la étnico-racial.',None,['modalidad','ejemplo']),
}
LABEL={'hola':'Empezar de nuevo','tipo':'¿Qué es un tipo de violencia?','modalidad':'¿Qué es una modalidad?','diferencia':'¿En qué se diferencian?','ejemplo':'Dame un ejemplo','vinculo':'¿Y el vínculo?','filtrar':'¿Cómo filtro los estudios?','guia':'Quiero aprender más','fis':'Física','psi':'Psicológica','sex':'Sexual','eco':'Económica','politico':'Acoso político','tic':'Redes sociales'}
def data():
    return json.dumps({'kb':{k:{'kw':v[0],'a':v[1],'act':v[2],'next':v[3]} for k,v in KB.items()},'label':LABEL},ensure_ascii=False)
LOGO='<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="15" fill="none" stroke="#2f3e8f" stroke-width="5" stroke-dasharray="70 30"/><circle cx="20" cy="20" r="9" fill="none" stroke="#7ec4d4" stroke-width="4" stroke-dasharray="40 20"/><circle cx="20" cy="20" r="4" fill="#f2a93b"/></svg>'
HTML=f'''<div class="cb" id="cb">
  <button type="button" class="cb-fab" id="cbFab" aria-expanded="false" aria-controls="cbWin"><span class="cb-av">{LOGO}</span><span class="cb-fl">¿Tipo o modalidad?<small>Pregúntame</small></span></button>
  <div class="cb-win" id="cbWin" role="dialog" aria-label="Asistente del banco" hidden>
    <div class="cb-h"><span class="cb-av">{LOGO}</span><div><b>Asistente del banco</b><small>Respuestas predefinidas · sin IA</small></div><button type="button" class="cb-x" id="cbX" aria-label="Cerrar">×</button></div>
    <div class="cb-log" id="cbLog" aria-live="polite"></div>
    <div class="cb-sug" id="cbSug"></div>
    <form class="cb-in" id="cbForm"><input id="cbQ" type="text" placeholder="Escribe, por ejemplo: acoso político" aria-label="Escribe tu pregunta" autocomplete="off"><button type="submit" aria-label="Enviar">→</button></form>
  </div>
</div>'''
JS=r'''<script>
(function(){const D='''+'__DATA__'+r''',K=D.kb,$=id=>document.getElementById(id),log=$('cbLog'),sug=$('cbSug'),win=$('cbWin'),fab=$('cbFab');let started=false;
 const norm=t=>t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'');
 const add=(who,html)=>{const m=document.createElement('div');m.className='cb-m '+who;m.innerHTML=html;log.appendChild(m);log.scrollTop=log.scrollHeight};
 const typing=()=>{const m=document.createElement('div');m.className='cb-m bot cb-dots';m.innerHTML='<i></i><i></i><i></i>';log.appendChild(m);log.scrollTop=log.scrollHeight;return m};
 const act=a=>{if(!a)return '';if(a.tipo)return `<button type="button" class="cb-go" data-k="tipo" data-v="${a.tipo}">Ver estudios de ${a.tipo.toLowerCase()} →</button>`;
  if(a.mod)return `<button type="button" class="cb-go" data-k="mod" data-v="${a.mod}">Ver estudios de esta modalidad →</button>`;return ''};
 const chips=ks=>{sug.innerHTML=ks.map(k=>`<button type="button" data-k="${k}">${D.label[k]||k}</button>`).join('')};
 const answer=k=>{const e=K[k];const t=typing();setTimeout(()=>{t.remove();add('bot',e.a+act(e.act));if(e.act&&e.act.focus)focusF(e.act.focus);chips(e.next||['hola'])},550)};
 const focusF=id=>{const el=$(id);if(!el)return;el.scrollIntoView({behavior:'smooth',block:'center'});el.classList.add('cb-hl');setTimeout(()=>el.classList.remove('cb-hl'),2200)};
 const apply=(k,v)=>{const sel=$(k==='tipo'?'fTipo':'fMod');if(!sel)return;if(![...sel.options].some(o=>o.value===v)){add('bot','Todavía no hay estudios con esa clasificación en el banco.');return}
  sel.value=v;sel.dispatchEvent(new Event('change'));add('bot','Listo, apliqué el filtro. Mira la lista de estudios.');focusF('count')};
 const ask=q=>{add('user',q.replace(/[<>]/g,''));const n=norm(q);let best=null,sc=0;
  for(const [k,e] of Object.entries(K)){for(const w of e.kw){const ww=norm(w);if(n.includes(ww)&&ww.length>sc){best=k;sc=ww.length}}}
  if(best)answer(best);else{const t=typing();setTimeout(()=>{t.remove();add('bot','No tengo una respuesta para eso. Prueba con una de estas preguntas:');chips(['tipo','modalidad','diferencia','ejemplo','filtrar'])},500)}};
 sug.onclick=e=>{const b=e.target.closest('button');if(!b)return;add('user',b.textContent);answer(b.dataset.k)};
 log.onclick=e=>{const b=e.target.closest('.cb-go');if(b)apply(b.dataset.k,b.dataset.v)};
 $('cbForm').onsubmit=e=>{e.preventDefault();const q=$('cbQ').value.trim();if(!q)return;$('cbQ').value='';ask(q)};
 const open=o=>{win.hidden=!o;fab.setAttribute('aria-expanded',o);fab.classList.toggle('on',o);if(o&&!started){started=true;answer('hola')}if(o)setTimeout(()=>$('cbQ').focus({preventScroll:true}),300)};
 fab.onclick=()=>open(win.hidden);$('cbX').onclick=()=>open(false);
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!win.hidden)open(false)})})();
</script>'''.replace('__DATA__',data())
JS=JS.replace('__DATA__',data())
