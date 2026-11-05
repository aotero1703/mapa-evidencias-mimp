# Retratos ilustrados más humanos para la portada (dibujo propio). Costa, sierra y Amazonía.
# Coordenadas en un marco de radio 100, cabeza centrada cerca de (0,-12).

def _shade(c,f):
    c=c.lstrip('#');r,g,b=(int(c[i:i+2],16) for i in (0,2,4))
    return '#%02x%02x%02x'%tuple(max(0,min(255,int(v*f))) for v in (r,g,b))

def cabeza(skin,w=29,jaw=.62,top=-62,chin=40):
    return f'M{-w} -26C{-w-2} 8 {-w*jaw:.1f} {chin-6} 0 {chin}C{w*jaw:.1f} {chin-6} {w+2} 8 {w} -26C{w-1} {top+4} {-w+1} {top+4} {-w} -26Z'

def rostro(skin,hair='#1c1210',lip=None,smile=True,closed=False,glasses=False,age=0,w=30,jaw=.64,chin=36):
    dk=_shade(skin,.78);dk2=_shade(skin,.62);lip=lip or _shade(skin,.7)
    s=f'<ellipse cx="{-w-1}" cy="-6" rx="5.5" ry="9" fill="{skin}"/><ellipse cx="{w+1}" cy="-6" rx="5.5" ry="9" fill="{skin}"/>'
    s+=f'<ellipse cx="{-w-1}" cy="-6" rx="2.5" ry="5" fill="{dk}"/><ellipse cx="{w+1}" cy="-6" rx="2.5" ry="5" fill="{dk}"/>'
    s+=f'<path d="{cabeza(skin,w,jaw,chin=chin)}" fill="{skin}"/>'
    s+=f'<path d="M{w*.35:.0f} -50C{w+4} -40 {w+3} 6 {w*.55:.0f} {chin-8}C{w*.35:.0f} {chin-2} {w*.15:.0f} {chin} 0 {chin}C{w*.4:.0f} {chin-8} {w*.75:.0f} 4 {w*.35:.0f} -50Z" fill="#000" opacity=".07"/>'
    # cejas
    s+=f'<path d="M-21 -23q8 -6 16 -2" stroke="{hair}" stroke-width="3.2" fill="none" stroke-linecap="round"/><path d="M5 -25q8 -4 16 2" stroke="{hair}" stroke-width="3.2" fill="none" stroke-linecap="round"/>'
    # ojos
    for x in (-12,12):
        if closed:
            s+=f'<path d="M{x-7} -13q7 5 14 0" stroke="#2a1a14" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
        else:
            s+=(f'<path d="M{x-8.5} -13q8.5 -8 17 0q-8.5 6 -17 0Z" fill="#fbf7f2"/>'
                f'<circle cx="{x}" cy="-13.5" r="4.2" fill="#3a2316"/><circle cx="{x}" cy="-13.5" r="1.6" fill="#120a06"/><circle cx="{x+1.2}" cy="-14.8" r=".9" fill="#fff"/>'
                f'<path d="M{x-8.5} -13q8.5 -8 17 0" stroke="#1d120c" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    if age:
        s+=f'<path d="M-20 -6q4 3 8 1M12 -5q4 2 8 -1M-17 -36q17 -4 34 0M-14 -41q14 -3 28 0" stroke="{dk2}" stroke-width="1.3" fill="none" opacity=".7"/>'
        s+=f'<path d="M-14 12q-4 8 0 14M14 12q4 8 0 14" stroke="{dk2}" stroke-width="1.4" fill="none" opacity=".55"/>'
    # nariz
    s+=f'<path d="M1 -8Q4 -1 3 4" stroke="{dk2}" stroke-width="1.6" fill="none" stroke-linecap="round" opacity=".45"/>'
    s+=f'<path d="M-6 5Q-6 9 -2 9Q0 10.5 2 9Q6 9 6 5" stroke="{dk2}" stroke-width="2" fill="none" stroke-linecap="round"/>'
    # boca
    if smile:
        s+=(f'<path d="M-14 16Q0 33 14 16Q0 21 -14 16Z" fill="#6b241d"/><path d="M-12 17Q0 21.5 12 17L11 20Q0 24 -11 20Z" fill="#fff"/>'
            f'<path d="M-13 16Q-6 14 0 15Q6 14 13 16" stroke="{lip}" stroke-width="2" fill="none" stroke-linecap="round" opacity=".8"/>'
)
    else:
        s+=(f'<path d="M-10 18Q-4 14 0 16Q4 14 10 18Q0 20 -10 18Z" fill="{lip}"/><path d="M-10 18Q0 26 10 18Q0 21 -10 18Z" fill="{_shade(lip,1.1)}"/>')
    s+=f'<ellipse cx="-17" cy="5" rx="7" ry="4.5" fill="#e0725a" opacity=".16"/><ellipse cx="17" cy="5" rx="7" ry="4.5" fill="#e0725a" opacity=".16"/>'
    if glasses:
        s+='<g fill="none" stroke="#2a1d3a" stroke-width="2.4"><rect x="-23" y="-22" width="19" height="15" rx="6"/><rect x="4" y="-22" width="19" height="15" rx="6"/><path d="M-4 -15h8M-23 -15l-7 -2M23 -15l7 -2"/></g>'
    return s

def torso(cl,skin,w=82,neck_w=11):
    return (f'<path d="M{-neck_w} 26L{-neck_w} 52Q0 60 {neck_w} 52L{neck_w} 26Z" fill="{skin}"/><path d="M{-neck_w} 30Q0 40 {neck_w} 30L{neck_w} 40Q0 46 {-neck_w} 40Z" fill="#000" opacity=".1"/>'
            f'<path d="M-{w} 120C-{w} 78 -62 54 -24 48Q0 62 24 48C62 54 {w} 78 {w} 120Z" fill="{cl}"/>')

# 1. Mujer andina: sombrero de paja, trenzas con pompones, lliclla
def andina():
    sk='#bd8058';hair='#17100d'
    s=f'<path d="M-30 -20C-36 20 -34 60 -30 96L-20 96C-24 60 -24 20 -22 -10Z" fill="{hair}"/><path d="M30 -20C36 20 34 60 30 96L20 96C24 60 24 20 22 -10Z" fill="{hair}"/>'
    s+=torso('#c23a2f',sk)
    s+='<path d="M-82 120C-80 82 -64 56 -26 48L-6 120ZM82 120C80 82 64 56 26 48L6 120Z" fill="#f2a93b"/>'
    s+=''.join(f'<path d="M{a} {b}L{c} 120" stroke="{col}" stroke-width="4"/>' for a,b,c,col in ((-60,64,-44,'#2f3e8f'),(-44,54,-28,'#e5463c'),(60,64,44,'#2f3e8f'),(44,54,28,'#e5463c')))
    s+='<circle cx="-25" cy="96" r="7" fill="#e5463c"/><circle cx="25" cy="96" r="7" fill="#6a4fb0"/>'
    s+=rostro(sk,hair)
    s+=f'<path d="M-30 -24C-30 -50 -12 -60 0 -60C12 -60 30 -50 30 -24C24 -38 12 -44 0 -44C-12 -44 -24 -38 -30 -24Z" fill="{hair}"/><path d="M0 -60V-44" stroke="#2c201a" stroke-width="1.5"/>'
    s+='<ellipse cx="0" cy="-48" rx="64" ry="12" fill="#efe2c2"/><path d="M-64 -48q64 16 128 0" stroke="#d8c79c" stroke-width="2" fill="none"/>'
    s+='<path d="M-30 -50C-30 -82 -18 -92 0 -92C18 -92 30 -82 30 -50Z" fill="#f3e7c9"/><path d="M-30 -58h60v8h-60Z" fill="#1d2552"/><path d="M-30 -55h60" stroke="#f2a93b" stroke-width="1.5" stroke-dasharray="3 3"/>'
    s+='<circle cx="-30" cy="6" r="3.5" fill="#f2a93b"/><circle cx="30" cy="6" r="3.5" fill="#f2a93b"/>'
    return s

# 2. Mujer afroperuana de la costa: cabello rizado recogido, aretes de aro
def afro_costa():
    sk='#5b3725';hair='#140d0a'
    s=''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{hair}"/>' for x,y,r in ((0,-62,26),(-20,-58,20),(20,-58,20),(-10,-78,18),(12,-78,18),(0,-88,14)))
    s+=torso('#e5463c',sk)+'<path d="M-24 48Q0 70 24 48" stroke="#f2a93b" stroke-width="5" fill="none"/>'
    s+=rostro(sk,hair,lip='#7a3b2f',w=28)
    s+=f'<path d="M-28 -22C-28 -46 -14 -56 0 -56C14 -56 28 -46 28 -22C22 -40 10 -46 0 -46C-10 -46 -22 -40 -28 -22Z" fill="{hair}"/>'
    s+='<circle cx="-30" cy="10" r="7" fill="none" stroke="#f2a93b" stroke-width="2.6"/><circle cx="30" cy="10" r="7" fill="none" stroke="#f2a93b" stroke-width="2.6"/>'
    return s

# 3. Mujer amazónica: cabello largo con flequillo, collar de semillas, túnica con diseño geométrico
def amazonica():
    sk='#cf9a70';hair='#120c0a'
    s=f'<path d="M-36 -30C-40 20 -40 70 -32 110H32C40 70 40 20 36 -30Z" fill="{hair}"/>'
    s+=torso('#f1e6cf',sk)
    s+='<g fill="none" stroke="#7a2e22" stroke-width="3"><path d="M-70 92l10 -10l10 10l10 -10l10 10l10 -10l10 10l10 -10l10 10l10 -10l10 10l10 -10l10 10l10 -10"/><path d="M-74 106h148"/><path d="M-56 70h16v10h16M56 70h-16v10h-16"/></g>'
    s+=''.join(f'<circle cx="{x}" cy="{50+abs(x)*.22:.0f}" r="4.2" fill="{c}"/>' for x,c in ((-22,'#b33a2c'),(-14,'#2b1a12'),(-6,'#b33a2c'),(2,'#2b1a12'),(10,'#b33a2c'),(18,'#2b1a12')))
    s+=rostro(sk,hair,w=28,jaw=.66)
    s+=f'<path d="M-30 -18C-32 -50 -14 -60 0 -60C14 -60 32 -50 30 -18L30 -26H-30Z" fill="{hair}"/><path d="M-29 -30C-20 -36 -8 -34 0 -32C8 -34 20 -36 29 -30V-24H-29Z" fill="{hair}"/>'
    return s

# 4. Adulta mayor: canas en moño, lentes, chompa
def mayor():
    sk='#f1d0b4';hair='#dcd8de'
    s=torso('#6a4fb0',sk)+'<path d="M-24 48L-10 120M24 48L10 120" stroke="#5a3f9e" stroke-width="5"/><circle cx="0" cy="80" r="3" fill="#f2a93b"/><circle cx="0" cy="98" r="3" fill="#f2a93b"/>'
    s+=rostro(sk,'#9c96a0',closed=False,glasses=True,age=1)
    s+=f'<path d="M-31 -16C-34 -52 -14 -62 0 -62C14 -62 34 -52 31 -16C27 -38 14 -48 0 -48C-14 -48 -27 -38 -31 -16Z" fill="{hair}"/><circle cx="0" cy="-66" r="13" fill="{hair}"/><path d="M-8 -52q8 -6 16 0" stroke="#bdb7c2" stroke-width="1.5" fill="none"/>'
    return s

# 5. Padre de la costa con su hija
def familia():
    sk1,sk2='#e2b590','#eac6a2'
    a='<g transform="translate(-24 6) scale(.9)">'+torso('#2a96ad',sk1,neck_w=13)+rostro(sk1,'#3a2618',w=31,jaw=.7,chin=42)
    a+='<path d="M-31 -18C-33 -50 -14 -62 0 -62C16 -62 34 -50 31 -18C28 -40 12 -48 0 -48C-14 -48 -28 -40 -31 -18Z" fill="#3a2618"/>'
    a+='<path d="M-22 14C-20 34 -10 42 0 42C10 42 20 34 22 14" stroke="#16100c" stroke-width="1" fill="none" opacity=".25"/></g>'
    c='<g transform="translate(40 32) scale(.6)">'+torso('#f2a93b',sk2)+rostro(sk2,'#4a2e1c',w=27,chin=36)
    c+='<path d="M-29 -16C-30 -48 -12 -58 0 -58C12 -58 30 -48 29 -16C24 -36 10 -44 0 -44C-10 -44 -24 -36 -29 -16Z" fill="#4a2e1c"/><circle cx="-34" cy="-30" r="11" fill="#4a2e1c"/><circle cx="34" cy="-30" r="11" fill="#4a2e1c"/><circle cx="-26" cy="-36" r="4" fill="#e5463c"/><circle cx="26" cy="-36" r="4" fill="#e5463c"/></g>'
    return a+c

# 6. Joven andino con chullo
def chullo():
    sk='#b8784e'
    s=torso('#3b4c9e',sk)+'<path d="M-24 48Q0 66 24 48" stroke="#2a3780" stroke-width="6" fill="none"/>'
    s+=rostro(sk,'#16100c',w=29,jaw=.68)
    s+='<path d="M-32 -16C-34 -60 -16 -78 0 -78C16 -78 34 -60 32 -16L34 10L26 12L26 -20H-26L-26 12L-34 10Z" fill="#e5463c"/>'
    s+='<path d="M-30 -36h60M-31 -26h62" stroke="#f3e7c9" stroke-width="4"/><path d="M-26 -31l6 -5l6 5l6 -5l6 5l6 -5l6 5l6 -5l6 5" stroke="#1d2552" stroke-width="2.5" fill="none"/>'
    s+='<path d="M-24 -54l8 -6l8 6l8 -6l8 6l8 -6l8 6" stroke="#f2a93b" stroke-width="3" fill="none"/><circle cx="0" cy="-82" r="7" fill="#f2a93b"/>'
    s+='<path d="M-30 12v16M30 12v16" stroke="#f2a93b" stroke-width="3"/><circle cx="-30" cy="30" r="4" fill="#f2a93b"/><circle cx="30" cy="30" r="4" fill="#f2a93b"/>'
    return s

# 7. Niña de la Amazonía con trenza
def nina():
    sk='#dba77d';hair='#2e1d14'
    s=f'<path d="M24 -10C40 20 36 60 30 90" stroke="{hair}" stroke-width="12" stroke-linecap="round" fill="none"/>'
    s+=torso('#b5d334',sk)+rostro(sk,hair,w=27,chin=34)
    s+=f'<path d="M-29 -14C-30 -48 -12 -58 0 -58C12 -58 30 -48 29 -14C26 -34 12 -42 0 -42C-14 -42 -24 -34 -29 -14Z" fill="{hair}"/>'
    s+='<circle cx="24" cy="-40" r="7" fill="#e5463c"/><circle cx="31" cy="-34" r="5" fill="#f2a93b"/>'
    return s
