# Portada del Banco de Evidencias: collage de retratos ilustrados (dibujo propio, sin fotos externas).
import math, random
import retratos as R

INK='#1b1430'
def _face(skin,smile=True,blush='#e8826b',eyes_closed=False):
    s=f'<ellipse cx="0" cy="-8" rx="30" ry="36" fill="{skin}"/>'
    if eyes_closed:
        s+=f'<path d="M-15 -12q4 4 8 0M7 -12q4 4 8 0" stroke="{INK}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    else:
        s+=f'<ellipse cx="-11" cy="-11" rx="3" ry="3.6" fill="{INK}"/><ellipse cx="11" cy="-11" rx="3" ry="3.6" fill="{INK}"/>'
    s+=f'<path d="M-17 -21q6 -4 11 -1M6 -22q6 -3 11 1" stroke="{INK}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".8"/>'
    s+=f'<circle cx="-17" cy="2" r="5" fill="{blush}" opacity=".35"/><circle cx="17" cy="2" r="5" fill="{blush}" opacity=".35"/>'
    s+=(f'<path d="M-10 8q10 10 20 0" stroke="{INK}" stroke-width="2.6" fill="#fff" stroke-linecap="round"/>' if smile
        else f'<path d="M-7 10q7 4 14 0" stroke="{INK}" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    return s
def _body(cl,skin,neck=True):
    s=f'<rect x="-10" y="18" width="20" height="30" fill="{skin}"/>' if neck else ''
    s+=f'<path d="M-80 110C-78 70 -60 48 -30 44Q0 58 30 44C60 48 78 70 80 110Z" fill="{cl}"/>'
    return s

def _sticker(x,y,r,bg,inner,rot=0,shape='circle'):
    cid=f'c{x}{y}'
    clip=(f'<circle r="100"/>' if shape=='circle' else '<path d="M-96 -70Q-100 -100 -70 -98L70 -100Q100 -100 98 -70L100 70Q100 100 70 98L-70 100Q-100 100 -98 70Z"/>')
    outline=(f'<circle r="100"/>' if shape=='circle' else '<path d="M-96 -70Q-100 -100 -70 -98L70 -100Q100 -100 98 -70L100 70Q100 100 70 98L-70 100Q-100 100 -98 70Z"/>')
    k=r/100
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({k})">'
            f'<g filter="url(#sh)"><g fill="#fff" stroke="#fff" stroke-width="16">{outline}</g></g>'
            f'<clipPath id="{cid}">{clip}</clipPath><g clip-path="url(#{cid})"><rect x="-110" y="-110" width="220" height="220" fill="{bg}"/>'
            f'<rect x="-110" y="-110" width="220" height="220" fill="url(#ht)"/><g transform="translate(0 6) scale(1.12)">{inner}</g>'
            f'<rect x="-110" y="-110" width="220" height="220" fill="url(#ht2)"/></g></g>')

def p_andina():
    sk='#a8693f'
    s='<rect x="-34" y="-20" width="11" height="96" rx="5" fill="#1a1216"/><rect x="23" y="-20" width="11" height="96" rx="5" fill="#1a1216"/>'
    s+=_body('#e5463c',sk)+'<path d="M-80 110C-78 70 -60 48 -30 44L0 80L30 44C60 48 78 70 80 110Z" fill="#f2a93b"/><path d="M-60 78h120M-66 92h132" stroke="#e5463c" stroke-width="5"/>'
    s+=_face(sk)
    s+='<path d="M-30 -14q0 -30 30 -32q30 2 30 32q-8 -18 -30 -20q-22 2 -30 20Z" fill="#1a1216"/>'
    s+='<ellipse cx="0" cy="-42" rx="66" ry="13" fill="#f3ead6"/><path d="M-32 -42q2 -36 32 -38q30 2 32 38Z" fill="#f3ead6"/><path d="M-32 -50h64v8h-64Z" fill="#6a4fb0"/>'
    s+='<circle cx="-24" cy="4" r="3.5" fill="#f2a93b"/><circle cx="24" cy="4" r="3.5" fill="#f2a93b"/>'
    return s
def p_joven():
    sk='#c08a62'
    s='<path d="M-40 -20q0 -50 40 -52q40 2 40 52v70h-80Z" fill="#2a1a12"/>'
    s+=_body('#7ec4d4',sk)+_face(sk)
    s+='<path d="M-32 -18q4 -36 34 -36q30 0 32 30q-22 -4 -36 -22q-10 18 -30 28Z" fill="#2a1a12"/>'
    s+='<g fill="none" stroke="#1b1430" stroke-width="2.6"><circle cx="-11" cy="-11" r="9"/><circle cx="11" cy="-11" r="9"/><path d="M-2 -11h4"/></g>'
    return s
def p_mayor():
    sk='#c48a63'
    s=_body('#6a4fb0',sk)+'<path d="M-80 110C-70 60 -40 50 -20 46L0 100L20 46C40 50 70 60 80 110Z" fill="#b5d334" opacity=".9"/>'
    s+=_face(sk,eyes_closed=True)
    s+='<path d="M-30 -10q-4 -40 30 -42q34 2 30 42q-6 -24 -30 -26q-24 2 -30 26Z" fill="#e4e1ea"/><circle cx="0" cy="-54" r="13" fill="#e4e1ea"/>'
    s+='<path d="M-18 14q-4 6 -2 10M18 14q4 6 2 10" stroke="#9a6a48" stroke-width="1.5" fill="none" opacity=".5"/>'
    return s
def p_afro():
    sk='#5a3624'
    s=''.join(f'<circle cx="{dx}" cy="{dy}" r="{r}" fill="#18100c"/>' for dx,dy,r in ((0,-36,38),(-32,-22,26),(32,-22,26),(-38,6,20),(38,6,20),(-18,-56,22),(18,-56,22)))
    s+=_body('#f2a93b',sk)+_face(sk,blush='#c45a3d')
    s+='<circle cx="-30" cy="6" r="4" fill="#e5463c"/><circle cx="30" cy="6" r="4" fill="#e5463c"/>'
    return s
def p_familia():
    sk1,sk2='#8a5638','#b9805a'
    s='<g transform="translate(-26 4) scale(.92)">'+_body('#2a96ad',sk1)+_face(sk1)+'<path d="M-30 -18q0 -34 30 -34q30 0 30 34q-6 -14 -30 -16q-24 2 -30 16Z" fill="#18100c"/></g>'
    s+='<g transform="translate(34 30) scale(.62)">'+_body('#e5463c',sk2)+_face(sk2)+'<path d="M-30 -14q0 -36 30 -36q30 0 30 36q-10 -16 -30 -18q-20 2 -30 18Z" fill="#3a2418"/><circle cx="-34" cy="-6" r="11" fill="#3a2418"/><circle cx="34" cy="-6" r="11" fill="#3a2418"/></g>'
    return s
def p_amazonica():
    sk='#a9744b'
    s='<rect x="-38" y="-40" width="76" height="110" rx="20" fill="#16100e"/>'
    s+=_body('#f3ead6',sk)+'<path d="M-46 64l8 -8l8 8l8 -8l8 8l8 -8l8 8l8 -8l8 8l8 -8l8 8" fill="none" stroke="#2f3e8f" stroke-width="4"/>'
    s+=''.join(f'<circle cx="{x}" cy="{38+abs(x)*.12}" r="4" fill="{c}"/>' for x,c in ((-20,'#e5463c'),(-10,'#f2a93b'),(0,'#e5463c'),(10,'#f2a93b'),(20,'#e5463c')))
    s+=_face(sk)
    s+='<path d="M-31 -16q0 -32 31 -34q31 2 31 34v-6h-62Z" fill="#16100e"/><rect x="-31" y="-36" width="62" height="12" rx="5" fill="#16100e"/>'
    s+='<rect x="-33" y="-32" width="66" height="7" fill="#e5463c"/><path d="M-33 -29h66" stroke="#f2a93b" stroke-width="2" stroke-dasharray="4 4"/>'
    return s
def p_nino():
    sk='#b07a52'
    s=_body('#b5d334',sk)+_face(sk)
    s+='<path d="M-31 -14q-2 -38 31 -40q33 2 31 40q-4 -20 -16 -24l-6 8l-6 -10l-6 8l-6 -8q-18 6 -22 26Z" fill="#20140e"/>'
    return s

def _burst(cx,cy,n,r1,r2,color,seed):
    rnd=random.Random(seed);s=''
    for i in range(n):
        a=i/n*2*math.pi+rnd.uniform(-.08,.08);w=rnd.uniform(.05,.1);L=rnd.uniform(r1,r2)
        p1=(cx+math.cos(a-w)*L*.45,cy+math.sin(a-w)*L*.45);p2=(cx+math.cos(a)*L,cy+math.sin(a)*L);p3=(cx+math.cos(a+w)*L*.45,cy+math.sin(a+w)*L*.45)
        s+=f'<path d="M{p1[0]:.0f} {p1[1]:.0f}L{p2[0]:.0f} {p2[1]:.0f}L{p3[0]:.0f} {p3[1]:.0f}Z" fill="{color}"/>'
    return s
def _leaf(x,y,rot,c,k=1):
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({k})"><path d="M0 0C14 -30 44 -36 64 -30C50 -10 26 4 0 0Z" fill="{c}"/><path d="M4 -2C22 -16 40 -24 58 -28" stroke="#fff" stroke-opacity=".35" stroke-width="2" fill="none"/></g>'

DEFS=('<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#0b0820" flood-opacity=".35"/></filter>'
      '<pattern id="ht" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><circle cx="3.5" cy="3.5" r="1.6" fill="#fff" opacity=".22"/></pattern>'
      '<pattern id="ht2" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(15)"><circle cx="2.5" cy="2.5" r=".8" fill="#1b1430" opacity=".06"/></pattern></defs>')

COLLAGE=('<svg class="cover-art" viewBox="0 0 640 560" role="img" aria-label="Collage ilustrado de mujeres e integrantes del grupo familiar de la costa, la sierra y la Amazonía: una mujer andina con sombrero, una mujer afroperuana, un joven con chullo, un padre con su hija, una adulta mayor, una mujer amazónica y una niña" xmlns="http://www.w3.org/2000/svg">'+DEFS
  +_burst(330,290,22,170,300,'#b5d334',3)+_burst(330,290,14,150,250,'#7ec4d4',7)
  +_leaf(70,470,-20,'#6a4fb0',1.6)+_leaf(560,120,160,'#6a4fb0',1.3)+_leaf(590,430,-60,'#b5d334',1.2)+_leaf(110,110,40,'#e5463c',1)
  +_sticker(200,170,112,'#f2a93b',R.andina(),-6)
  +_sticker(436,140,96,'#b5d334',R.afro_costa(),5,'sq')
  +_sticker(540,320,82,'#ef7a6a',R.chullo(),-4)
  +_sticker(330,335,106,'#7ec4d4',R.familia(),3,'sq')
  +_sticker(118,382,88,'#c9b8ec',R.mayor(),-8)
  +_sticker(452,478,82,'#f3ead6',R.amazonica(),6)
  +_sticker(252,500,60,'#b5d334',R.nina(),-4)
  +'</svg>')
