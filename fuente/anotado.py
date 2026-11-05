# Componente "frase anotada": muestra en una situación quién agrede (vínculo), qué daño hace (tipo)
# y si hay una modalidad, resaltando cada parte. Casos basados en la Ley N.° 30364 (arts. 7 y 8), su Reglamento
# (art. 8.1), la Ley N.° 31155, el Código Penal (art. 154-B) y las formas de la Ficha de Registro de Casos del CEM (2023).
import html as _h
# Cada caso: lista de tramos (texto, rol, etiqueta) con rol en v (vínculo), t (tipo), m (modalidad) o None; modalidad si no hay; base legal.
CASOS=[
 ([('Su pareja','v','Pareja'),(' ',None,''),('la controla y no la deja ver a sus amigas','t','Psicológica'),('.',None,'')],'Ninguna adicional','Ley N.° 30364, arts. 7 y 8, lit. b'),
 ([('Su expareja','v','Pareja'),(' ',None,''),('comparte fotos íntimas de ella sin su permiso','t','Sexual'),(' ',None,''),('en redes sociales','m','Tecnologías (TIC)'),('.',None,'')],None,'Ley N.° 30364, art. 8, lit. c · Reglamento, art. 8.1 · Código Penal, art. 154-B'),
 ([('En el concejo, ',None,''),('sus colegas','v','Sin vínculo familiar'),(' ',None,''),('descalifican a una regidora por ser mujer','t','Psicológica'),(' y ',None,''),('no la dejan hablar en las sesiones','m','Acoso político'),('.',None,'')],None,'Ley N.° 31155, arts. 3 y 4'),
 ([('Su esposo','v','Pareja'),(' ',None,''),('decide sobre todo el dinero de la casa, incluido el sueldo de ella','t','Económica'),('.',None,'')],'Ninguna adicional','Ley N.° 30364, art. 8, lit. d'),
 ([('Su jefe','v','Sin vínculo familiar'),(' ',None,''),('le insinúa que tendrá problemas en el trabajo si no acepta sus propuestas sexuales','t','Sexual'),('.',None,'')],'Ninguna adicional','Ley N.° 27942 (hostigamiento sexual); la Ficha CEM lo registra como violencia sexual'),
 ([('Un vecino','v','Sin vínculo familiar'),(' ',None,''),('se burla de una mujer','t','Psicológica'),(' ',None,''),('por su origen indígena y su lengua','m','Mujeres indígenas u originarias'),('.',None,'')],None,'Reglamento de la Ley N.° 30364, art. 8.1'),
 ([('Su pareja','v','Pareja'),(' ',None,''),('la lastima físicamente durante las discusiones','t','Física'),('.',None,'')],'Ninguna adicional','Ley N.° 30364, arts. 7 y 8, lit. a'),
]
ROL={'v':'Quién','t':'Tipo','m':'Modalidad'}
def _frase(c):
    tramos,sinmod,base=c
    s=''.join((f'<mark class="an {r}">{_h.escape(t)}</mark>' if r else _h.escape(t)) for t,r,l in tramos)
    lab={r:l for t,r,l in tramos if r}
    chips=(f'<span class="ch v"><b>¿Quién?</b> {_h.escape(lab["v"])}</span>'
           f'<span class="ch t"><b>¿Qué daño?</b> Violencia {_h.escape(lab["t"].lower())}</span>'
           +(f'<span class="ch m"><b>¿Contexto?</b> {_h.escape(lab["m"])}</span>' if 'm' in lab else '<span class="ch n"><b>¿Contexto?</b> Ninguna modalidad adicional</span>'))
    return f'<p class="an-s">{s}</p><div class="an-ch">{chips}</div><p class="an-b">Base: {_h.escape(base)}</p>'
def componente(idx,uid,titulo=True):
    """idx: índices de CASOS a mostrar; uid: prefijo único."""
    tabs=''.join(f'<button type="button" role="tab" aria-selected="{str(j==0).lower()}" data-i="{j}">{j+1}</button>' for j,_ in enumerate(idx))
    panes=''.join(f'<div class="an-p" data-i="{j}"{"" if j==0 else " hidden"}>{_frase(CASOS[i])}</div>' for j,i in enumerate(idx))
    leyenda=''
    return (f'<div class="an-box" id="{uid}">{leyenda}<div class="an-card">{panes}</div>'
            f'<div class="an-nav"><span>Otro ejemplo</span><div class="an-tabs" role="tablist" aria-label="Ejemplos">{tabs}</div><button type="button" class="an-next">Siguiente →</button></div></div>')
JS=r'''<script>
document.querySelectorAll('.an-box').forEach(box=>{const T=[...box.querySelectorAll('.an-tabs button')],P=[...box.querySelectorAll('.an-p')];let k=0;
 const go=i=>{k=(i+P.length)%P.length;P.forEach((p,j)=>p.hidden=j!==k);T.forEach((t,j)=>t.setAttribute('aria-selected',j===k))};
 T.forEach((t,j)=>t.onclick=()=>go(j));box.querySelector('.an-next').onclick=()=>go(k+1)});
</script>'''
