# Escena de aula (dibujo propio): profesora junto a la pizarra y adolescentes sentadas mirándola.
import retratos as R

def profesora():
    sk='#c48c64';hair='#2a1a12'
    s='<svg class="profe" viewBox="0 0 220 420" role="img" aria-label="Profesora explicando junto a la pizarra" xmlns="http://www.w3.org/2000/svg">'
    # piernas y zapatos
    s+=f'<rect x="88" y="318" width="14" height="80" rx="6" fill="{sk}"/><rect x="118" y="318" width="14" height="80" rx="6" fill="{sk}"/>'
    s+='<path d="M82 396h24v10h-26z" fill="#2a1d3a"/><path d="M114 396h24v10h-26z" fill="#2a1d3a"/>'
    # falda
    s+='<path d="M74 236h72l14 92H60Z" fill="#2f3e8f"/>'
    # brazo derecho (señalando hacia la pizarra, a la izquierda)
    s+=f'<path d="M78 170C56 160 36 136 22 112" stroke="#e5463c" stroke-width="20" stroke-linecap="round" fill="none"/><circle cx="20" cy="108" r="10" fill="{sk}"/><path d="M14 102l-10 -8" stroke="#f4f1e8" stroke-width="5" stroke-linecap="round"/>'
    # torso (chompa)
    s+='<path d="M70 150C70 136 82 128 96 126Q110 140 124 126C138 128 150 136 150 150L148 240H72Z" fill="#e5463c"/>'
    s+='<path d="M98 128L110 168L122 128" fill="#f4f1e8"/>'
    # brazo izquierdo con libro
    s+=f'<path d="M146 160C160 190 160 214 150 230" stroke="#e5463c" stroke-width="20" stroke-linecap="round" fill="none"/><rect x="128" y="214" width="34" height="26" rx="3" fill="#f2a93b" transform="rotate(-10 145 227)"/><circle cx="146" cy="232" r="9" fill="{sk}"/>'
    # cabeza (cabello detrás, rostro y melena)
    s+=f'<g transform="translate(110 78) scale(.74)"><path d="M-40 -30C-46 20 -44 60 -34 80H34C44 60 46 20 40 -30Z" fill="{hair}"/>'
    s+=R.rostro(sk,hair,w=30)
    s+=f'<path d="M-32 -16C-34 -52 -14 -62 0 -62C16 -62 34 -52 32 -16C26 -40 8 -46 -6 -44C-16 -40 -26 -32 -32 -16Z" fill="{hair}"/></g>'
    s+='</svg>'
    return s

def _alumna(x,hair_svg,uni,skin,scale=1):
    # vista de espaldas: hombros, cuello, cabeza con peinado
    return (f'<g transform="translate({x} 0) scale({scale})">'
            f'<path d="M-46 150C-46 118 -30 104 -12 100H12C30 104 46 118 46 150Z" fill="{uni}"/>'
            f'<rect x="-8" y="82" width="16" height="22" fill="{skin}"/>'
            f'<ellipse cx="-27" cy="66" rx="5" ry="8" fill="{skin}"/><ellipse cx="27" cy="66" rx="5" ry="8" fill="{skin}"/>'
            f'{hair_svg}</g>')

def alumnas():
    neg='#17100d';cas='#4a2e1c';cl='#7a4a2a'
    a=[]
    # 1. trenzas (sierra)
    a.append(_alumna(90,f'<ellipse cx="0" cy="58" rx="27" ry="32" fill="{neg}"/><path d="M-6 36v-4M6 36v-4" stroke="#2b201a" stroke-width="1.5"/><path d="M-12 84C-14 110 -14 128 -12 142" stroke="{neg}" stroke-width="10" stroke-linecap="round" fill="none"/><path d="M12 84C14 110 14 128 12 142" stroke="{neg}" stroke-width="10" stroke-linecap="round" fill="none"/><circle cx="-12" cy="146" r="5" fill="#e5463c"/><circle cx="12" cy="146" r="5" fill="#f2a93b"/>','#8b8f9c','#a86a45'))
    # 2. rizos recogidos (costa)
    a.append(_alumna(230,''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{neg}"/>' for x,y,r in ((0,58,28),(-14,40,14),(14,40,14),(0,30,16),(-24,60,12),(24,60,12)))+'<circle cx="0" cy="22" r="14" fill="#140d0a"/>','#e5e2ea','#6b4029'))
    # 3. cabello largo suelto con vincha (Amazonía)
    a.append(_alumna(370,f'<path d="M-28 56C-28 22 -14 26 0 26C14 26 28 22 28 56C30 90 26 120 22 132H-22C-26 120 -30 90 -28 56Z" fill="{neg}"/><path d="M-27 46Q0 32 27 46" stroke="#1d8a9e" stroke-width="6" fill="none"/>','#8b8f9c','#c08a62'))
    # 4. cola de caballo castaña (ciudad)
    a.append(_alumna(510,f'<ellipse cx="0" cy="58" rx="27" ry="31" fill="{cas}"/><path d="M0 40C18 54 14 100 6 124" stroke="{cas}" stroke-width="14" stroke-linecap="round" fill="none"/><circle cx="2" cy="40" r="6" fill="#6a4fb0"/>','#e5e2ea','#e0b48f'))
    carpetas='<rect x="0" y="146" width="600" height="18" rx="6" fill="#a8743f"/><rect x="0" y="146" width="600" height="5" rx="2" fill="#c18c54"/>'
    return ('<svg class="alumnas" viewBox="0 0 600 170" role="img" aria-label="Cuatro adolescentes sentadas en sus carpetas mirando la pizarra" xmlns="http://www.w3.org/2000/svg">'
            +''.join(a)+carpetas+'</svg>')
