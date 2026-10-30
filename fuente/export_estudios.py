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

# Tema de investigación (puede haber varios) y población. Propuesta del Observatorio; POR VALIDAR.
# CAU=Causas y factores asociados, CON=Consecuencias, PRE=Prevención, ATE=Atención y recuperación,
# PRO=Protección y acceso a la justicia, SAN=Sanción y reeducación, REP=Reparación y restitución de derechos
TEMN={'CAU':'Causas y factores asociados','CON':'Consecuencias de la violencia','PRE':'Prevención de la violencia','ATE':'Atención y recuperación','PRO':'Protección y acceso a la justicia','SAN':'Sanción y reeducación','REP':'Reparación y restitución de derechos'}
TEMA={1:'CAU',2:'PRE',3:'PRE',4:'PRE',5:'CAU',6:'CAU',7:'CAU',8:'CAU',9:'CAU',10:'CAU',11:'CAU',12:'CAU',13:'CAU',14:'PRE',15:'CAU PRE',16:'CAU',17:'CAU',18:'CAU',19:'CAU',20:'CAU',
 21:'CAU',22:'CAU',23:'CAU',24:'CAU',25:'CAU',26:'CAU',27:'CAU',28:'CAU',29:'CAU',30:'CAU',31:'CAU',32:'CAU',33:'CAU',34:'CAU',35:'CAU',36:'CAU',37:'CAU',38:'CAU',39:'CAU',40:'PRE',
 41:'CAU',42:'CAU PRE',43:'CAU',44:'CAU',45:'CAU',46:'PRE',47:'PRE',48:'CAU',49:'PRO',50:'CAU',51:'CAU PRE',52:'CAU',53:'CAU',54:'CAU',55:'CAU PRE',56:'CAU',57:'CAU',58:'CAU',59:'CAU',60:'CAU',
 62:'CAU',63:'CAU',64:'CAU',65:'CAU',66:'CAU',67:'CAU',68:'CAU',69:'CAU',70:'CAU',71:'CAU',73:'CAU',74:'CAU',75:'CAU ATE',76:'CAU',77:'CAU',78:'CAU',79:'CAU CON',80:'CAU',81:'CAU',82:'CAU',
 83:'CAU',84:'CAU',85:'CAU',87:'CON',88:'CAU',89:'CAU',90:'CON',91:'CON',92:'PRE',93:'PRE',94:'CAU',95:'PRO',96:'ATE',97:'CON PRO',98:'PRE',99:'CAU',100:'CAU',101:'CAU',102:'CAU',103:'CAU',
 104:'CAU',105:'CAU',106:'CAU',107:'CAU',108:'CAU',109:'CAU',110:'CAU',111:'PRE',112:'PRE',113:'CAU',114:'CAU',115:'CAU',116:'PRE',117:'CAU',118:'CAU',119:'CAU',120:'SAN',
 121:'PRE',122:'PRE',123:'PRE ATE',124:'PRE',125:'PRE',126:'CAU',127:'CAU',128:'CAU',129:'CAU',130:'CAU',131:'CAU PRE',132:'CAU PRE',133:'PRE',134:'PRE',135:'PRE',136:'ATE'}
# M=Mujeres, N=Niñas, niños y adolescentes, J=Jóvenes, H=Hombres, A=Personas adultas mayores, I=Pueblos indígenas, O=Operadores y servidores públicos, G=Población general
POBN={'M':'Mujeres','N':'Niñas, niños y adolescentes','J':'Jóvenes','H':'Hombres','A':'Personas adultas mayores','I':'Pueblos indígenas','O':'Operadores y servidores públicos','G':'Población en general'}
POB={1:'N',2:'N',3:'M',4:'N',5:'M',6:'M',7:'M',8:'G',9:'N',10:'M',11:'M',12:'NJ',13:'GI',14:'N',15:'N',16:'M',17:'G',18:'G',19:'N',20:'G',21:'MJ',22:'G',23:'M',24:'H',25:'J',26:'M',27:'G',28:'G',29:'N',30:'A',
 31:'JM',32:'J',33:'J',34:'N',35:'M',36:'MI',37:'G',38:'G',39:'G',40:'M',41:'M',42:'M',43:'MI',44:'M',45:'MN',46:'O',47:'O',48:'M',49:'O',50:'M',51:'M',52:'MJ',53:'MJ',54:'M',55:'M',56:'G',57:'G',58:'G',59:'G',60:'G',
 62:'M',63:'M',64:'M',65:'M',66:'G',67:'G',68:'M',69:'M',70:'G',71:'N',73:'M',74:'M',75:'M',76:'M',77:'MI',78:'M',79:'M',80:'M',81:'J',82:'M',83:'M',84:'M',85:'M',87:'M',88:'M',89:'M',90:'MN',91:'M',92:'G',93:'M',94:'N',95:'MI',96:'M',97:'MN',98:'M',99:'G',
 100:'J',101:'O',102:'N',103:'J',104:'G',105:'N',106:'G',107:'N',108:'G',109:'G',110:'G',111:'H',112:'G',113:'G',114:'J',115:'G',116:'G',117:'J',118:'MJ',119:'M',120:'G',121:'H',122:'N',123:'M',124:'HM',125:'N',126:'M',127:'M',128:'M',129:'G',130:'M',131:'M',132:'G',133:'H',134:'HM',135:'G',136:'O'}
out=[]
for r in d['rows']:
    if r['dup']: continue
    x={k:r[k] for k in keep}
    x['dim']=GRUPO.get(r['dim'],r['dim'])
    x['amb']='Nacional' if r['o'] in ('peru','multi') else 'Internacional'   # sin país = estudios multipaís internacionales
    if r['n'] in TIPO:
        x['tipos']=[TN[c] for c in TIPO[r['n']]]
        x['mod']=MOD.get(r['n'],['Varias o sin modalidad específica'])
    x['temas']=[TEMN[k] for k in TEMA[r['n']].split()]
    x['pob_g']=[POBN[c] for c in POB[r['n']]]
    out.append(x)
json.dump({'rows':out},open('data/estudios.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
from collections import Counter
print(Counter(t for x in out for t in x.get('tipos',[]))); print(Counter(m for x in out for m in x.get('mod',[])))
print(len(out),Counter(x['amb'] for x in out),Counter(x['dim'] for x in out).most_common())
