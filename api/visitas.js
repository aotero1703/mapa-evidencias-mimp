// Contador de visitas del Mapa de Brechas de Evidencia (Vercel Function + Upstash Redis, sin dependencias).
// Usa claves propias ("mapa-evidencias:*") para poder compartir la misma base de datos con otros sitios del Observatorio.
const URL_REDIS = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
const TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
const CLAVE = 'mapa-evidencias:visitas';

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
  try {
    let r;
    if (req.method === 'POST') r = await redis([['INCR', CLAVE]]);        // suma una visita
    else if (req.method === 'GET') r = await redis([['GET', CLAVE]]);     // solo consulta
    else return res.status(405).json({ error: 'Método no permitido' });
    return res.status(200).json({ total: Number(r[0].result) || 0 });
  } catch (e) {
    return res.status(502).json({ error: 'No se pudo leer el contador' });
  }
};
