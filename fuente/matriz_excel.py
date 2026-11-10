# Genera la matriz descargable del banco a partir de data/estudios.json (la misma base que usa la web).
import json, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

SALIDA = 'matriz/Banco_de_Evidencias_MIMP.xlsx'
COLS = [('N.°', 'n', 7), ('Título', 't', 50), ('Autoría', 'a', 30), ('Año', 'y', 8), ('Publicado en', 'pub', 28),
        ('País', 'paises', 18), ('Ámbito', 'amb', 13), ('Tema', 'temas', 30), ('Tipo de violencia', 'tipos', 26),
        ('Modalidad', 'mod', 28), ('Población', 'pob', 34), ('Propósito', 'prop', 45), ('Resultados', 'res', 60),
        ('Resumen', 'abstract', 60), ('Enlace', 'link', 40)]
A = 'Arial'

def generar(ruta_json='data/estudios.json', salida=SALIDA):
    rows = sorted(json.load(open(ruta_json, encoding='utf-8'))['rows'], key=lambda r: r['n'])
    wb = Workbook()
    le = wb.active; le.title = 'Léeme'
    m = wb.create_sheet('Matriz')
    azul = PatternFill('solid', fgColor='2F3E8F'); fino = Side(style='thin', color='D5D9E8')
    # Hoja Matriz
    for j, (h, _, w) in enumerate(COLS, 1):
        c = m.cell(1, j, h); c.font = Font(name=A, bold=True, color='FFFFFF'); c.fill = azul
        c.alignment = Alignment(vertical='center', wrap_text=True); m.column_dimensions[get_column_letter(j)].width = w
    for i, r in enumerate(rows, 2):
        for j, (_, k, _) in enumerate(COLS, 1):
            v = r.get(k)
            if k == 'tipos' and v: v = [t for t in v if t != 'Estudios sobre varios tipos de violencia']
            if isinstance(v, list): v = '; '.join(v)
            if k == 'y' and v: v = str(v)
            c = m.cell(i, j, v if v not in ('', None) else None)
            c.font = Font(name=A, size=10); c.alignment = Alignment(vertical='top', wrap_text=True)
            c.border = Border(bottom=fino)
            if k == 'link' and v: c.hyperlink = v; c.font = Font(name=A, size=10, color='1D5FA8', underline='single')
    m.freeze_panes = 'C2'; m.auto_filter.ref = f'A1:{get_column_letter(len(COLS))}{len(rows)+1}'
    m.row_dimensions[1].height = 30
    # Hoja Léeme
    le.column_dimensions['A'].width = 34; le.column_dimensions['B'].width = 80
    le['A1'] = 'Banco de Evidencias · Matriz de investigaciones'; le['A1'].font = Font(name=A, bold=True, size=14, color='2F3E8F')
    le['A2'] = 'Observatorio Nacional de la Violencia contra las Mujeres y los Integrantes del Grupo Familiar (MIMP)'; le['A2'].font = Font(name=A, size=10, color='555555')
    filas = [('Investigaciones en la matriz', '=COUNTA(Matriz!A2:A1000)'),
             ('Nacionales', '=COUNTIF(Matriz!G2:G1000,"Nacional")'),
             ('Internacionales', '=COUNTIF(Matriz!G2:G1000,"Internacional")'),
             ('Fecha de actualización', datetime.date.today().strftime('%d/%m/%Y')),
             ('Sitio web', 'https://banco-evidencias-mimp.vercel.app/evidencia.html'),
             ('Cómo usarla', 'En la hoja «Matriz» cada fila es una investigación. Use los filtros de la primera fila para buscar por tema, tipo de violencia, modalidad, ámbito o país.'),
             ('Tipo de violencia', 'Física, psicológica, sexual y económica o patrimonial (Ley N.° 30364, art. 8).'),
             ('Modalidad', 'Situación particular en la que ocurre la violencia, según el Reglamento de la Ley N.° 30364 (art. 8.1).'),
             ('Nota', 'Esta matriz se genera automáticamente desde la misma base que usa el sitio web, por lo que ambos siempre coinciden.')]
    for i, (a, b) in enumerate(filas, 4):
        le.cell(i, 1, a).font = Font(name=A, bold=True, size=10)
        c = le.cell(i, 2, b); c.font = Font(name=A, size=10); c.alignment = Alignment(wrap_text=True, vertical='top')
        if isinstance(b, str) and b.startswith('http'): c.hyperlink = b; c.font = Font(name=A, size=10, color='1D5FA8', underline='single')
    wb.save(salida)
    return len(rows)

if __name__ == '__main__':
    print(generar())
