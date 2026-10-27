# Banco de Evidencias – Observatorio Nacional (MIMP)

Banco de evidencias sobre la violencia contra las mujeres y los integrantes del grupo familiar (Ley N.° 30364, art. 43; R.M. N.° 027-2025-MIMP).

- `index.html`: portada con las tres secciones.
- `mapa.html`: evidencia científica, el mapa de brechas de evidencia (datos y logos incluidos en la página).
- `tablero.html`: tablero de indicadores principales (Power BI incrustado).
- `fuentes.html`: fuentes externas de datos oficiales.
- `banco.css`, `img/`: estilos y logos de la portada y las páginas internas.
- `api/visitas.js`: contador de visitas (requiere una base Upstash Redis conectada en Vercel).
- `fuente/`: plantillas, datos y scripts para regenerar las páginas (`build_banco.py`, `template.html`, `data.json`).

Se publica en Vercel automáticamente con cada `git push` a `main`.
