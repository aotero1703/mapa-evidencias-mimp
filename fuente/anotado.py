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
_NOTA={'v':'vínculo','t':'tipo de violencia','m':'modalidad'}
def _frase(c):
    tramos,sinmod,base=c
    s=''.join((f'<mark class="ch-{r}">{_h.escape(t)}</mark>' if r else _h.escape(t)) for t,r,l in tramos)
    lab={r:l for t,r,l in tramos if r}
    notas=(f'<span class="nt v">↑ {_NOTA["v"]}: <b>{_h.escape(lab["v"].lower())}</b></span>'
           f'<span class="nt t">↑ {_NOTA["t"]}: <b>{_h.escape(lab["t"].lower())}</b></span>'
           +(f'<span class="nt m">↑ {_NOTA["m"]}: <b>{_h.escape(lab["m"].lower())}</b></span>' if 'm' in lab else '<span class="nt n">modalidad: <b>ninguna adicional</b></span>'))
    return f'<p class="pz-s">{s}</p><div class="pz-n">{notas}</div><span class="pz-i" tabindex="0" title="Base legal: {_h.escape(base)}" aria-label="Base legal: {_h.escape(base)}">ⓘ</span>'
def componente(idx,uid,titulo=True):
    tabs=''.join(f'<button type="button" role="tab" aria-selected="{str(j==0).lower()}" data-i="{j}">{j+1}</button>' for j,_ in enumerate(idx))
    panes=''.join(f'<div class="an-p" data-i="{j}"{"" if j==0 else " hidden"}>{_frase(CASOS[i])}</div>' for j,i in enumerate(idx))
    return (f'<div class="an-box pz-box" id="{uid}"><div class="pz-board">{panes}'
            f'<div class="an-nav"><div class="an-tabs" role="tablist" aria-label="Ejemplos">{tabs}</div><button type="button" class="an-next">otro ejemplo →</button></div></div><div class="pz-tray" aria-hidden="true"><i></i><i></i><i></i></div></div>')
JS=r'''<script>
document.querySelectorAll('.an-box').forEach(box=>{const T=[...box.querySelectorAll('.an-tabs button')],P=[...box.querySelectorAll('.an-p')];let k=0;
 const go=i=>{k=(i+P.length)%P.length;P.forEach((p,j)=>p.hidden=j!==k);T.forEach((t,j)=>t.setAttribute('aria-selected',j===k))};
 T.forEach((t,j)=>t.onclick=()=>go(j));box.querySelector('.an-next').onclick=()=>go(k+1)});
</script>'''
