// Contador de visitas del Banco de Evidencias (Vercel Function + Upstash Redis, sin dependencias).
// Cuenta el total y cada página por separado. Usa claves propias ("mapa-evidencias:*") para poder
// compartir la misma base de datos con otros sitios del Observatorio.
const URL_REDIS = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
const TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
const TOTAL = 'mapa-evidencias:visitas';
const PAGINAS = 'mapa-evidencias:paginas';   // hash: página -> visitas
// Solo se aceptan estas páginas, para que nadie pueda llenar la base con claves inventadas.
const VALIDAS = ['inicio', 'tipos-modalidades', 'evidencia', 'indicadores', 'fuentes', 'servicios', 'mapa'];

async function redis(comandos) {
  const r = await fetch(`${URL_REDIS}/pipeline`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${TOKEN}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(comandos),
  });
  if (!r.ok) throw new Error(`Redis respondió ${r.status}`);
  return r.json();
}

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (!URL_REDIS || !TOKEN) return res.status(500).json({ error: 'Falta conectar la base de datos Upstash al proyecto' });
  const p = String((req.query && req.query.p) || '');
  const pagina = VALIDAS.includes(p) ? p : null;
  try {
    const cmd = [];
    if (req.method === 'POST') { cmd.push(['INCR', TOTAL]); if (pagina) cmd.push(['HINCRBY', PAGINAS, pagina, 1]); }
    else if (req.method === 'GET') cmd.push(['GET', TOTAL]);
    else return res.status(405).json({ error: 'Método no permitido' });
    cmd.push(['HGETALL', PAGINAS]);
    const r = await redis(cmd);
    const lista = r[r.length - 1].result || [];
    const paginas = {};
    for (let i = 0; i < lista.length; i += 2) paginas[lista[i]] = Number(lista[i + 1]) || 0;
    return res.status(200).json({ total: Number(r[0].result) || 0, pagina: pagina ? (paginas[pagina] || 0) : null, paginas });
  } catch (e) {
    return res.status(502).json({ error: 'No se pudo leer el contador' });
  }
};
