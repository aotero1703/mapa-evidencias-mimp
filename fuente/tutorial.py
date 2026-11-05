# Intro en formato de video tutorial (escenas animadas con controles), segunda pantalla de la portada.
# Dato: ENDES 2025, primer semestre (INEI), tomado del Microinforme Ley 30364 – ENDES del MIMP.
MICRO='https://cdn.www.gob.pe/uploads/document/file/9457006/7512874-microinformes-30364-endes-02.pdf'
_IC={'fis':'<path d="M12 21s-7-4.3-7-10a4 4 0 0 1 7-2.7A4 4 0 0 1 19 11c0 5.7-7 10-7 10z"/><path d="M12 8.5l-1.5 3.5h3L12 15.5"/>',
 'psi':'<path d="M9.5 20v-3.2A6.5 6.5 0 1 1 18 11c0 1-.2 1.8-.6 2.6L19 17h-3v3z"/><path d="M10 9.5c.3-1 1.1-1.5 2-1.5 1.2 0 2 .8 2 1.8 0 1.5-2 1.7-2 3"/>',
 'sex':'<circle cx="12" cy="12" r="8.5"/><path d="M7 7l10 10"/>',
 'eco':'<rect x="3" y="6.5" width="18" height="12" rx="2"/><path d="M3 10.5h18"/><path d="M7 15h3"/>'}
def _i(k): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_IC[k]}</svg>'
_dots=''.join(f'<i style="--d:{i}"></i>' for i in range(100))
ESCENAS=[
 ('dato',f'''<div class="sc-stat"><div class="sc-num"><b data-count="50">0</b><span>de cada 100</span></div>
  <p class="sc-big">mujeres de 15 a 49 años en el Perú vivieron alguna vez violencia de parte de su pareja.</p>
  <div class="sc-dots" aria-hidden="true">{_dots}</div>
  <p class="sc-src">ENDES 2025, primer semestre (INEI) · <a href="{MICRO}" target="_blank" rel="noopener">Microinforme del MIMP ↗</a></p></div>'''),
 ('porque','''<div class="sc-mid"><p class="sc-lead">Detrás de cada cifra hay historias distintas.</p>
  <div class="sc-cards"><span>La controla y no la deja salir</span><span>Le quita su sueldo</span><span>Difunde sus fotos en redes</span></div>
  <p class="sc-big">Para registrarlas, atenderlas y estudiarlas, la <b>Ley N.° 30364</b> nos da un lenguaje común. Se basa en tres preguntas.</p></div>'''),
 ('tipo',f'''<div class="sc-q"><span class="sc-qn t">1</span><p class="sc-qt">¿Qué daño se produce?</p><p class="sc-qa">Es el <b>tipo</b> de violencia</p>
  <div class="sc-tipos"><span>{_i('fis')}Física</span><span>{_i('psi')}Psicológica</span><span>{_i('sex')}Sexual</span><span>{_i('eco')}Económica</span></div>
  <p class="sc-src">Ley N.° 30364, artículo 8</p></div>'''),
 ('vinculo','''<div class="sc-q"><span class="sc-qn v">2</span><p class="sc-qt">¿Quién la ejerce?</p><p class="sc-qa">Es el <b>vínculo</b> con quien agrede</p>
  <div class="sc-vin"><span>Pareja o expareja</span><span>Un familiar</span><span>Otra persona</span></div>
  <p class="sc-src">Ley N.° 30364, artículo 7</p></div>'''),
 ('modalidad','''<div class="sc-q"><span class="sc-qn m">3</span><p class="sc-qt">¿Hay un contexto particular?</p><p class="sc-qa">Es la <b>modalidad</b></p>
  <div class="sc-mods"><span>Por redes sociales</span><span>En la vida política</span><span>Contra mujeres indígenas</span><span>Contra mujeres migrantes</span><span>En el trabajo</span><span>…y más</span></div>
  <p class="sc-src">21 modalidades en el Reglamento de la Ley N.° 30364, artículo 8.1</p></div>'''),
 ('ejemplo','''<div class="sc-ex"><p class="sc-lead">Juntas describen un caso:</p>
  <p class="sc-sent"><mark class="x v">Su expareja</mark> <mark class="x t">comparte fotos íntimas de ella sin su permiso</mark> <mark class="x m">en redes sociales</mark>.</p>
  <div class="sc-tags"><span class="v">Vínculo: Pareja</span><span class="t">Tipo de violencia: Sexual</span><span class="m">Modalidad: Tecnologías (TIC)</span></div></div>'''),
 ('fin','''<div class="sc-mid"><p class="sc-lead">Con este mismo lenguaje se ordena la evidencia de este banco.</p>
  <p class="sc-big">Así puedes buscar estudios por tipo, por modalidad o por población.</p>
  <div class="sc-end"><a class="btn-a tm-go2" href="#banco">Entrar al banco →</a><a class="sc-guia" href="comprender-violencia.html">Ver la guía completa</a></div></div>'''),
]
DUR=[7500,7000,6500,6000,6500,7500,9000]
def html():
    sc=''.join(f'<div class="sc sc-{k}" data-i="{i}"{"" if i==0 else " hidden"}>{c}</div>' for i,(k,c) in enumerate(ESCENAS))
    seg=''.join(f'<button type="button" class="vp-seg" data-i="{i}" aria-label="Escena {i+1}"><i></i></button>' for i in range(len(ESCENAS)))
    return f'''<div class="vp" id="vp" data-dur="{','.join(map(str,DUR))}">
  <div class="vp-top"><span class="vp-k">Antes de entrar · 1 minuto</span><a class="tm-skip" href="#banco">Omitir intro →</a></div>
  <div class="vp-stage" aria-live="polite">{sc}</div>
  <div class="vp-bar"><button type="button" class="vp-b vp-prev" aria-label="Anterior">‹</button><button type="button" class="vp-b vp-play" aria-label="Pausar">❚❚</button><button type="button" class="vp-b vp-next" aria-label="Siguiente">›</button><div class="vp-segs">{seg}</div></div>
</div>'''
JS=r'''<script>
(function(){const v=document.getElementById('vp');if(!v)return;const S=[...v.querySelectorAll('.sc')],G=[...v.querySelectorAll('.vp-seg')],D=v.dataset.dur.split(',').map(Number),pb=v.querySelector('.vp-play');
 let k=0,t0=0,el=0,run=false,raf=null;
 const count=sc=>sc.querySelectorAll('[data-count]').forEach(n=>{const to=+n.dataset.count,s=performance.now();const f=x=>{const p=Math.min(1,(x-s)/1600);n.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)});
 const show=i=>{k=Math.max(0,Math.min(S.length-1,i));S.forEach((s,j)=>{s.hidden=j!==k;s.classList.remove('on')});void S[k].offsetWidth;S[k].classList.add('on');count(S[k]);
  G.forEach((g,j)=>{g.classList.toggle('done',j<k);g.firstChild.style.width=j<k?'100%':'0%'});el=0;t0=performance.now()};
 const tick=x=>{if(!run)return;const p=Math.min(1,(el+x-t0)/D[k]);G[k].firstChild.style.width=(p*100)+'%';if(p>=1){if(k<S.length-1)show(k+1);else{pause();return}}raf=requestAnimationFrame(tick)};
 const play=()=>{if(run)return;run=true;t0=performance.now();pb.textContent='❚❚';pb.setAttribute('aria-label','Pausar');raf=requestAnimationFrame(tick)};
 const pause=()=>{if(!run)return;run=false;el+=performance.now()-t0;cancelAnimationFrame(raf);pb.textContent='▶';pb.setAttribute('aria-label','Reproducir')};
 pb.onclick=()=>run?pause():play();v.querySelector('.vp-prev').onclick=()=>{show(k-1)};v.querySelector('.vp-next').onclick=()=>{show(k+1)};
 G.forEach((g,j)=>g.onclick=()=>show(j));
 window.bancoTutorial={start(){show(0);if(matchMedia('(prefers-reduced-motion: reduce)').matches){pause()}else{run=false;play()}},stop(){pause()}};
 document.addEventListener('visibilitychange',()=>{if(document.hidden)pause()});
 if(document.documentElement.classList.contains('paso2'))window.bancoTutorial.start()})();
</script>'''
