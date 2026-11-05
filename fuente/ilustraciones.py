# Ilustraciones vectoriales propias del Banco de Evidencias (sin imágenes externas).
# RED_APOYO: siete personas diversas tomadas de la mano sobre un paisaje de costa, sierra y selva.

def _arm(x1,y1,x2,y2,sleeve,skin):
    return (f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{sleeve}" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cx="{x2}" cy="{y2}" r="6" fill="{skin}"/>')

def _legs(cx,top,skin,shoe='#1b1f36',gap=7,bottom=316):
    return (f'<rect x="{cx-gap-4}" y="{top}" width="8" height="{bottom-top}" rx="3" fill="{skin}"/>'
            f'<rect x="{cx+gap-4}" y="{top}" width="8" height="{bottom-top}" rx="3" fill="{skin}"/>'
            f'<rect x="{cx-gap-7}" y="{bottom-4}" width="12" height="6" rx="3" fill="{shoe}"/>'
            f'<rect x="{cx+gap-5}" y="{bottom-4}" width="12" height="6" rx="3" fill="{shoe}"/>')

H=[(115,240),(202,252),(288,252),(375,240),(465,240),(553,250)]   # manos que se juntan

def _fondo():
    s=''
    s+='<circle cx="478" cy="78" r="34" fill="#f2a93b" opacity=".95"/>'
    s+='<circle cx="478" cy="78" r="50" fill="#f2a93b" opacity=".12"/>'
    # sierra
    s+='<path d="M120 304L250 140L318 226L392 128L540 304Z" fill="#2f3e8f" opacity=".85"/>'
    s+='<path d="M250 140L236 160L251 155L263 163Z M392 128L377 150L393 145L407 152Z" fill="#eef1fa"/>'
    s+='<path d="M60 304L170 196L262 304Z" fill="#26306b"/>'
    # costa
    for i,y in enumerate((276,290,304)):
        s+=f'<path d="M0 {y}q15 -8 30 0t30 0t30 0t30 0" fill="none" stroke="#7ec4d4" stroke-width="3" stroke-linecap="round" opacity="{.8-i*.2}"/>'
    # selva
    s+='<g opacity=".55">'
    for x,y,r in ((556,246,24),(588,226,30),(626,246,26),(530,266,18)):
        s+=f'<rect x="{x-3}" y="{y}" width="6" height="{304-y}" fill="#2b5b47"/><circle cx="{x}" cy="{y}" r="{r}" fill="#3f8f6b"/><circle cx="{x-r*.35}" cy="{y-r*.3}" r="{r*.45}" fill="#56a77f"/>'
    s+='</g><path d="M640 300q-30 4 -48 14t-30 10" fill="none" stroke="#7ec4d4" stroke-width="5" opacity=".7"/>'
    # suelo
    s+='<defs><linearGradient id="sueloG" x1="0" x2="1"><stop offset="0" stop-color="#7ec4d4" stop-opacity="0"/><stop offset=".15" stop-color="#7ec4d4" stop-opacity=".35"/><stop offset=".85" stop-color="#7ec4d4" stop-opacity=".35"/><stop offset="1" stop-color="#7ec4d4" stop-opacity="0"/></linearGradient></defs>'
    s+='<rect x="0" y="303" width="640" height="3" fill="url(#sueloG)"/><ellipse cx="330" cy="322" rx="300" ry="10" fill="#000" opacity=".12"/>'
    # red: arcos punteados que unen a las personas
    heads=[(70,112),(160,104),(245,170),(330,104),(420,104),(510,104),(598,170)]
    for (a,b),(c,d) in zip(heads,heads[1:]):
        mx=(a+c)/2;my=min(b,d)-34
        s+=f'<path d="M{a} {b}Q{mx} {my} {c} {d}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="1.5" stroke-dasharray="3 5"/>'
    for x,y in heads: s+=f'<circle cx="{x}" cy="{y}" r="3.5" fill="#fff" opacity=".7"/>'
    return s

def _p1():  # adulta mayor con bastón
    cx,sk,cl='70','#c68a5e','#8f74c9';cx=70
    s=f'<path d="M{cx-14} 178L{cx+14} 178L{cx+22} 300L{cx-22} 300Z" fill="{cl}"/>'
    s+=_legs(cx,298,sk)
    s+=f'<path d="M36 252L28 316" stroke="#e8d5b0" stroke-width="4" stroke-linecap="round"/>'
    s+=_arm(cx-14,186,38,250,cl,sk)+_arm(cx+14,186,*H[0],cl,sk)
    s+=f'<rect x="{cx-5}" y="164" width="10" height="16" fill="{sk}"/><circle cx="{cx}" cy="150" r="18" fill="{sk}"/>'
    s+=f'<path d="M{cx-18} 148a18 18 0 0 1 36 0q-6 -8 -18 -9t-18 9Z" fill="#d9dbe4"/><circle cx="{cx+6}" cy="129" r="8" fill="#d9dbe4"/>'
    return s

def _p2():  # mujer andina con montera, lliclla y pollera
    cx,sk=160,'#a86b45'
    s=f'<rect x="{cx-21}" y="146" width="7" height="88" rx="3.5" fill="#15131a"/><rect x="{cx+14}" y="146" width="7" height="88" rx="3.5" fill="#15131a"/>'
    s+=f'<path d="M{cx-14} 178L{cx+14} 178L{cx+16} 236L{cx-16} 236Z" fill="#f4f1ea"/>'
    s+=f'<path d="M{cx-18} 232L{cx+18} 232L{cx+34} 300L{cx-34} 300Z" fill="#e5463c"/>'
    s+=f'<path d="M{cx-27} 270L{cx+27} 270L{cx+29} 278L{cx-29} 278Z" fill="#f2a93b"/><path d="M{cx-31} 286L{cx+31} 286L{cx+32} 291L{cx-32} 291Z" fill="#7ec4d4"/>'
    s+=_legs(cx,298,sk,gap=8)
    s+=f'<path d="M{cx-20} 176L{cx+20} 176L{cx} 214Z" fill="#f2a93b"/><path d="M{cx-12} 186L{cx+12} 186M{cx-7} 196L{cx+7} 196" stroke="#e5463c" stroke-width="2.5"/>'
    s+=_arm(cx-14,186,*H[0],'#f2a93b',sk)+_arm(cx+14,186,*H[1],'#f2a93b',sk)
    s+=f'<rect x="{cx-5}" y="164" width="10" height="16" fill="{sk}"/><circle cx="{cx}" cy="150" r="18" fill="{sk}"/>'
    s+=f'<path d="M{cx-18} 150a18 18 0 0 1 36 0q-18 -6 -36 0Z" fill="#15131a"/>'
    s+=f'<ellipse cx="{cx}" cy="134" rx="31" ry="6" fill="#e5463c"/><rect x="{cx-15}" y="118" width="30" height="16" rx="3" fill="#e5463c"/><rect x="{cx-15}" y="127" width="30" height="4" fill="#f2a93b"/>'
    return s

def _p3():  # niña
    cx,sk=245,'#b98058'
    s=f'<path d="M{cx-11} 214L{cx+11} 214L{cx+18} 290L{cx-18} 290Z" fill="#7ec4d4"/>'
    s+=_legs(cx,288,sk,gap=5)
    s+=_arm(cx-11,222,*H[1],'#7ec4d4',sk)+_arm(cx+11,222,*H[2],'#7ec4d4',sk)
    s+=f'<rect x="{cx-4}" y="200" width="8" height="16" fill="{sk}"/><circle cx="{cx}" cy="188" r="15" fill="{sk}"/>'
    s+=f'<path d="M{cx-15} 187a15 15 0 0 1 30 0q-15 -9 -30 0Z" fill="#3a2418"/><circle cx="{cx-17}" cy="190" r="6" fill="#3a2418"/><circle cx="{cx+17}" cy="190" r="6" fill="#3a2418"/>'
    return s

def _p4():  # hombre
    cx,sk=330,'#8d5a3b'
    s=f'<path d="M{cx-16} 178L{cx+16} 178L{cx+15} 252L{cx-15} 252Z" fill="#2a96ad"/>'
    s+=f'<rect x="{cx-15}" y="248" width="13" height="66" rx="4" fill="#4a5bb5"/><rect x="{cx+2}" y="248" width="13" height="66" rx="4" fill="#4a5bb5"/>'
    s+=f'<rect x="{cx-17}" y="310" width="16" height="7" rx="3" fill="#1b1f36"/><rect x="{cx+1}" y="310" width="16" height="7" rx="3" fill="#1b1f36"/>'
    s+=_arm(cx-16,186,*H[2],'#2a96ad',sk)+_arm(cx+16,186,*H[3],'#2a96ad',sk)
    s+=f'<rect x="{cx-5}" y="164" width="10" height="16" fill="{sk}"/><circle cx="{cx}" cy="150" r="18" fill="{sk}"/>'
    s+=f'<path d="M{cx-18} 148a18 18 0 0 1 36 0q-4 -7 -18 -7t-18 7Z" fill="#15131a"/>'
    return s

def _p5():  # mujer afroperuana
    cx,sk=420,'#5b3826'
    s=''.join(f'<circle cx="{cx+dx}" cy="{150+dy}" r="{r}" fill="#1a1210"/>' for dx,dy,r in ((0,-12,20),(-16,-4,15),(16,-4,15),(-19,10,12),(19,10,12),(-9,-20,12),(9,-20,12)))
    s+=f'<path d="M{cx-14} 178L{cx+14} 178L{cx+26} 300L{cx-26} 300Z" fill="#f2a93b"/>'
    s+=''.join(f'<circle cx="{cx+dx}" cy="{y}" r="2.6" fill="#e5463c"/>' for y in (220,250,280) for dx in (-12,0,12))
    s+=_legs(cx,298,sk)
    s+=_arm(cx-14,186,*H[3],'#f2a93b',sk)+_arm(cx+14,186,*H[4],'#f2a93b',sk)
    s+=f'<rect x="{cx-5}" y="164" width="10" height="16" fill="{sk}"/><circle cx="{cx}" cy="152" r="17" fill="{sk}"/>'
    return s

def _p6():  # mujer amazónica con falda de diseño geométrico
    cx,sk=510,'#b07a4f'
    s=f'<rect x="{cx-19}" y="140" width="38" height="70" rx="12" fill="#15131a"/>'
    s+=f'<path d="M{cx-14} 178L{cx+14} 178L{cx+15} 236L{cx-15} 236Z" fill="#f4f1ea"/>'
    s+=f'<path d="M{cx-17} 232L{cx+17} 232L{cx+24} 300L{cx-24} 300Z" fill="#efe6d2"/>'
    s+=f'<path d="M{cx-20} 250l6 -6l6 6l6 -6l6 6l6 -6l6 6M{cx-22} 266h44M{cx-23} 280l7 7l7 -7l7 7l7 -7l7 7l7 -7" fill="none" stroke="#1d2552" stroke-width="2.2"/>'
    s+=_legs(cx,298,sk)
    s+=_arm(cx-14,186,*H[4],'#f4f1ea',sk)+_arm(cx+14,186,*H[5],'#f4f1ea',sk)
    s+=f'<rect x="{cx-5}" y="164" width="10" height="16" fill="{sk}"/><circle cx="{cx}" cy="150" r="18" fill="{sk}"/>'
    s+=f'<path d="M{cx-18} 150a18 18 0 0 1 36 0v-2h-36Z" fill="#15131a"/><rect x="{cx-17}" y="136" width="34" height="9" rx="4" fill="#15131a"/>'
    s+=f'<rect x="{cx-18}" y="141" width="36" height="4" fill="#e5463c"/>'
    return s

def _p7():  # joven en silla de ruedas, mirando al grupo
    cx,sk=600,'#d29b6c'
    s=f'<circle cx="{cx+4}" cy="288" r="26" fill="#1d2552" stroke="#dfe4f3" stroke-width="5"/><circle cx="{cx+4}" cy="288" r="4" fill="#dfe4f3"/>'
    s+=f'<path d="M{cx+20} 204V262H{cx-22}" fill="none" stroke="#dfe4f3" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    s+=f'<path d="M{cx-12} 212H{cx+12}V262H{cx-12}Z" fill="#3f8f6b"/>'
    s+=f'<rect x="{cx-30}" y="250" width="44" height="13" rx="6" fill="#4a5bb5"/>'
    s+=f'<rect x="{cx-31}" y="256" width="11" height="46" rx="5" fill="#4a5bb5"/><rect x="{cx-38}" y="298" width="17" height="7" rx="3" fill="#1b1f36"/>'
    s+=f'<path d="M{cx-26} 312H{cx-12}" stroke="#dfe4f3" stroke-width="4" stroke-linecap="round"/><circle cx="{cx-28}" cy="314" r="4" fill="#dfe4f3"/>'
    s+=_arm(cx-11,220,*H[5],'#3f8f6b',sk)
    s+=f'<rect x="{cx-4}" y="198" width="8" height="16" fill="{sk}"/><circle cx="{cx}" cy="186" r="16" fill="{sk}"/>'
    s+=f'<path d="M{cx-16} 186a16 16 0 0 1 32 0q-16 -8 -32 0Z" fill="#6b3f22"/><path d="M{cx+14} 180q12 6 6 26" fill="none" stroke="#6b3f22" stroke-width="7" stroke-linecap="round"/>'
    return s

RED_APOYO=('<svg class="sv-art" viewBox="0 0 640 360" role="img" aria-label="Ilustración: siete personas diversas se toman de la mano frente a un paisaje de costa, sierra y selva, como una red de apoyo" xmlns="http://www.w3.org/2000/svg">'
  +_fondo()+_p1()+_p2()+_p3()+_p4()+_p5()+_p6()+_p7()+'</svg>')

# Pequeñas escenas para "Llegamos a todo el país"
ESC_CIUDAD=('<svg viewBox="0 0 160 90" aria-hidden="true"><rect width="160" height="90" rx="12" fill="#e9edf8"/>'
  '<path d="M0 70q20 -6 40 0t40 0t40 0t40 0V90H0Z" fill="#cfe8ee"/>'
  '<rect x="22" y="30" width="26" height="44" fill="#2f3e8f"/><rect x="52" y="18" width="30" height="56" fill="#3b4c9e"/><rect x="86" y="36" width="22" height="38" fill="#2f3e8f"/><rect x="112" y="26" width="26" height="48" fill="#4a5bb5"/>'
  '<g fill="#f2a93b">'+''.join(f'<rect x="{x}" y="{y}" width="5" height="6"/>' for x in (28,38,58,70,92,118,128) for y in (38,52))+'</g>'
  '<rect x="60" y="50" width="16" height="24" rx="2" fill="#e5463c"/><text x="68" y="64" font-size="7" font-weight="800" fill="#fff" text-anchor="middle" font-family="sans-serif">CEM</text></svg>')
ESC_SIERRA=('<svg viewBox="0 0 160 90" aria-hidden="true"><rect width="160" height="90" rx="12" fill="#eef4ee"/>'
  '<circle cx="124" cy="22" r="10" fill="#f2a93b"/><path d="M0 74L46 24L78 58L104 34L160 80V90H0Z" fill="#7d8fd0"/><path d="M46 24L39 34L47 31L53 35ZM104 34L98 43L105 40L111 44Z" fill="#fff"/>'
  '<path d="M0 78q40 -10 80 -2t80 -4V90H0Z" fill="#9cc79b"/><path d="M60 82h26l-4 -12h-18Z" fill="#c9844f"/><path d="M58 70l15 -10l15 10Z" fill="#e5463c"/><rect x="70" y="74" width="6" height="8" fill="#5a3a22"/></svg>')
ESC_RIO=('<svg viewBox="0 0 160 90" aria-hidden="true"><rect width="160" height="90" rx="12" fill="#e6f2ec"/>'
  + ''.join(f'<rect x="{x-2}" y="{y}" width="4" height="{50-y+20}" fill="#2b5b47"/><circle cx="{x}" cy="{y}" r="{r}" fill="#3f8f6b"/>' for x,y,r in ((18,30,14),(40,22,16),(124,26,15),(146,32,13)))
  + '<path d="M0 62q40 -8 80 0t80 0V90H0Z" fill="#7ec4d4"/><path d="M50 66h60l-8 9h-44Z" fill="#fff"/><rect x="62" y="56" width="34" height="10" rx="2" fill="#2f3e8f"/><rect x="74" y="48" width="12" height="8" fill="#e5463c"/>'
  + '<path d="M20 80q10 -3 20 0M110 82q10 -3 20 0" stroke="#fff" stroke-width="2" fill="none" opacity=".7"/></svg>')
ESC_FONO=('<svg viewBox="0 0 160 90" aria-hidden="true"><rect width="160" height="90" rx="12" fill="#f6ecee"/>'
  '<rect x="58" y="12" width="44" height="70" rx="8" fill="#2f3e8f"/><rect x="63" y="20" width="34" height="50" rx="3" fill="#fff"/>'
  '<rect x="67" y="26" width="22" height="9" rx="4" fill="#e9edf8"/><rect x="71" y="40" width="22" height="9" rx="4" fill="#7ec4d4"/><rect x="67" y="54" width="18" height="9" rx="4" fill="#e9edf8"/>'
  '<text x="30" y="52" font-size="20" font-weight="800" fill="#e5463c" text-anchor="middle" font-family="sans-serif">100</text>'
  '<path d="M118 34q8 10 0 20M126 28q14 16 0 32" stroke="#e5463c" stroke-width="3" fill="none" stroke-linecap="round"/></svg>')
