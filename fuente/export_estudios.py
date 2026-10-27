# Exporta data/estudios.json para la página de evidencia científica (sin duplicados).
# Ámbito: solo Nacional o Internacional. Dimensiones de Igualdad de oportunidades agrupadas.
import json
GRUPO={'Brecha salarial':'Empleo','Salud sexual y reproductiva':'Salud','Salud física':'Salud','Salud mental':'Salud',
 'Liderazgo':'Participación y liderazgo','Participación política':'Participación y liderazgo','Institucional/Organizacional':'Participación y liderazgo',
 'Interseccionalidad':'Enfoques transversales','Ciclo de vida':'Enfoques transversales'}
d=json.load(open('fuente/data.json',encoding='utf-8'))
keep=['n','tem','dim','t','a','y','paises','pob','prop','tipo','det','ale','est','vy','vx','res','link','pub']
out=[]
for r in d['rows']:
    if r['dup']: continue
    x={k:r[k] for k in keep}
    x['dim']=GRUPO.get(r['dim'],r['dim'])
    x['amb']='Nacional' if r['o'] in ('peru','multi') else 'Internacional'   # sin país = estudios multipaís internacionales
    out.append(x)
json.dump({'rows':out},open('data/estudios.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
from collections import Counter
print(len(out),Counter(x['amb'] for x in out),Counter(x['dim'] for x in out).most_common())
