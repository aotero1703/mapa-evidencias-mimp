# Paso 1: lee la matriz (CSV exportado de Google Sheets o Excel) y genera fuente/data.json limpio.
# Uso: python3 fuente/build_data.py [ruta/al/archivo.csv]   (por defecto: fuente/matriz.csv)
import csv, json, re, io, sys
_p=sys.argv[1] if len(sys.argv)>1 else 'fuente/matriz.csv'
src=open(_p,encoding='utf-8-sig').read()
if src.startswith('## Sheet name'): src=src.split('\n',1)[1]
rows=list(csv.DictReader(io.StringIO(src)))
def clean(s):
    s=(s or '').replace('\r','')
    s=re.sub(r'CopyRetryClaude can make mistakes\. Please double-check responses\.','',s)
    lines=[l.strip() for l in s.split('\n')]
    out=[];blank=False
    for l in lines:
        if not l:
            if out and not blank: out.append('')
            blank=True
        else: out.append(l); blank=False
    return '\n'.join(out).strip()
VIO={'Violencia de pareja':[74,75,79,80,82,83,84,85,87,89,90,91,93,96,121,124,133,134,135],
 'Violencia sexual':[71,92,97,119,122,125],'Trata y explotación':[45,46,95,123],'Feminicidio':[73],
 'Ciberviolencia':[94],'Alcohol como factor de riesgo':[70,81,86],
 'Prevalencia y factores generales':[68,69,72,76,77,78,88,118,120],
 'Marcos conceptuales y justicia':[49,51,98],'Servicios de atención':[136]}
vmap={n:k for k,v in VIO.items() for n in v}
GROUP={'A':'Experimental y síntesis','B':'Cuasi-experimental','C':'Observacional','D':'Cualitativa y conceptual'}
SUB={'A.1':'Metaanálisis','A.2':'Revisión sistemática','A.3':'Experimental (ECA)',
 'B.1':'Regresión discontinua','B.2':'Variables instrumentales','B.3':'Datos longitudinales','B.4':'Emparejamiento',
 'C.1':'Factores asociados','C.2':'Modelos multivariados','C.3':'Correlaciones','C.4':'Registros administrativos',
 'D.1':'Cualitativos','D.2':'Opinión de expertos','D.3':'Marcos conceptuales'}
DUP={72:21,86:70,61:62}
FLAGS={125:'Autores y país parecen copiados de otra fila (n.° 99); el país dice "Cacao" y el estudio es de Sudáfrica.',
 112:'La población objetivo es la del estudio n.° 111 (reclutas en Noruega), no la de este estudio.',
 115:'Los resultados son los del estudio n.° 114 (evaluación entre pares), no los de este estudio.',
 61:'Fila sin autor ni año; duplica el n.° 62.',
 89:'Variables Y y X vacías.',
 50:'Resultados vacíos.'}
out=[]
for r in rows:
    n=int(r['N°'])
    code=re.match(r'([A-D])\.?\s?(\d)',r['Nivel de evidencia'].strip())
    g,sub=code.group(1),code.group(1)+'.'+code.group(2)
    tem=r['Temática'].strip(); dim=r['Dimensiones'].strip(); sug=False
    if tem.startswith('Violencia') and not dim: dim=vmap[n]; sug=True
    pais=clean(r['País']); pl=[p.strip(' ,') for p in re.split(r'[\n,]+',pais) if p.strip(' ,')]
    if n==125: pl=['Sudáfrica']
    hasPeru=any(p.lower().startswith('per') for p in pl)
    origin='sd' if not pl else ('peru' if pl==['Peru'] or pl==['Perú'] else ('multi' if hasPeru else 'intl'))
    pl=['Perú' if p.lower().startswith('per') else p for p in pl]
    tipo=clean(r['Tipo de intervención'])
    out.append(dict(n=n,tem=tem,dim=dim,sug=sug,g=g,sub=sub,subl=SUB[sub],
      t=clean(r['Título']).replace('\n',' '),a=clean(r['Autor']).replace('\n','; '),y=r['Año'].strip(),
      paises=pl,o=origin,pob=clean(r['Población objetivo de la evidencia encontrada']),prop=clean(r['Propósito del estudio']),
      tipo=tipo if tipo.lower()!='no corresponde' else '',det=clean(r['Detalles de la intervención']) if clean(r['Detalles de la intervención']).lower()!='no corresponde' else '',
      ale=clean(r['Diseño de aleatorización']) if clean(r['Diseño de aleatorización']).lower()!='no corresponde' else '',
      est=clean(r['Estado de la evaluación de impacto']).replace('Completa','Completo') if clean(r['Estado de la evaluación de impacto']).lower()!='no corresponde' else '',
      vy=clean(r['Variable(s) Y']),vx=clean(r['Variable(s) X']),res=clean(r['Resultados']),
      link=r['Vínculo'].strip(),pub=clean(r['Lugar de publicación']).replace('\n',' '),
      dup=DUP.get(n),flag=FLAGS.get(n,'')))
TEMR={'Género': 'Igualdad de oportunidades', 'Violencia de género': 'Violencia contra las mujeres e integrantes del grupo familiar'}
DIMR={'Brechas de género': 'Brechas entre mujeres y hombres', 'Violencia de pareja': 'Violencia en relación de pareja', 'Trata y explotación': 'Trata y explotación sexual', 'Ciberviolencia': 'Acoso y violencia en espacios virtuales', 'Alcohol como factor de riesgo': 'Prevalencia y factores de riesgo', 'Prevalencia y factores generales': 'Prevalencia y factores de riesgo', 'Marcos conceptuales y justicia': 'Acceso a la justicia y marcos conceptuales', 'Servicios de atención': 'Servicios de prevención y atención'}
for x in out: x['tem']=TEMR.get(x['tem'],x['tem']); x['dim']=DIMR.get(x['dim'],x['dim'])
json.dump(dict(rows=out,groups=GROUP,subs=SUB),open('fuente/data.json','w',encoding='utf-8'),ensure_ascii=False)
import collections
print(collections.Counter(x['o'] for x in out), sum(1 for x in out if x['tipo']), len(json.dumps(out,ensure_ascii=False)))
