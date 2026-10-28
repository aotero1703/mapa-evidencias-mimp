# Paso 2: exporta data/estudios.json para la página de evidencia científica (sin duplicados).
# Ámbito: solo Nacional o Internacional. Dimensiones de Igualdad de oportunidades agrupadas.
import json
GRUPO={'Brecha salarial':'Empleo','Salud sexual y reproductiva':'Salud','Salud física':'Salud','Salud mental':'Salud',
 'Liderazgo':'Participación y liderazgo','Participación política':'Participación y liderazgo','Institucional/Organizacional':'Participación y liderazgo',
 'Interseccionalidad':'Enfoques transversales','Ciclo de vida':'Enfoques transversales'}
d=json.load(open('fuente/data.json',encoding='utf-8'))
keep=['n','tem','dim','t','a','y','paises','pob','prop','tipo','det','ale','est','vy','vx','res','link','pub']
# Codificación según la Ley N.° 30364: tipos (art. 8 de la Ley) y modalidades (art. 8 del Reglamento, D.S. 009-2016-MIMP y modif.)
# F=física, P=psicológica, S=sexual, E=económica o patrimonial, G=estudio general (varios tipos o sin tipo específico). Por validar.
TIPO={45:'S',46:'S',49:'G',51:'G',68:'FPS',69:'G',70:'G',71:'PS',73:'F',74:'FPS',75:'FPS',76:'G',77:'FS',78:'F',79:'F',80:'F',81:'G',82:'F',83:'F',84:'FP',
 85:'FPS',87:'FP',88:'FPS',89:'FP',90:'FP',91:'G',92:'S',93:'F',94:'PS',95:'G',96:'FPS',97:'S',98:'G',118:'FS',119:'S',120:'G',121:'FS',122:'FPS',123:'FPS',
 124:'FS',125:'FS',133:'FP',134:'FS',135:'F',136:'G'}
TN={'F':'Violencia física','P':'Violencia psicológica','S':'Violencia sexual','E':'Violencia económica o patrimonial','G':'Estudios generales sobre violencia'}
PAR='Violencia en relación de pareja'; TRA='Trata de personas con fines de explotación sexual'; IGF='Contra integrantes del grupo familiar'
MOD={45:[TRA],46:[TRA],95:[TRA],73:['Feminicidio'],94:['Violencia a través de las tecnologías de la información'],
 119:['Violencia en conflicto armado'],122:['Violencia en conflicto armado',IGF],124:['Violencia en conflicto armado',PAR],
 71:[IGF],79:[IGF],90:[PAR,IGF],91:[IGF],
 **{n:[PAR] for n in (74,75,80,82,83,84,85,87,89,93,96,121,125,133,134,135)}}
out=[]
for r in d['rows']:
    if r['dup']: continue
    x={k:r[k] for k in keep}
    x['dim']=GRUPO.get(r['dim'],r['dim'])
    x['amb']='Nacional' if r['o'] in ('peru','multi') else 'Internacional'   # sin país = estudios multipaís internacionales
    if r['n'] in TIPO:
        x['tipos']=[TN[c] for c in TIPO[r['n']]]
        x['mod']=MOD.get(r['n'],['Varias o sin modalidad específica'])
    out.append(x)
json.dump({'rows':out},open('data/estudios.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
from collections import Counter
print(Counter(t for x in out for t in x.get('tipos',[]))); print(Counter(m for x in out for m in x.get('mod',[])))
print(len(out),Counter(x['amb'] for x in out),Counter(x['dim'] for x in out).most_common())
