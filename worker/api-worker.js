/* DoraPDF API worker  —  api.dorapdf.com  +  go.dorapdf.com (short links)
   Bindings (set in Cloudflare dashboard → Worker → Settings):
     KV namespace  LINKS        (for the link shortener)
     Secret        CF_API_TOKEN (API token with "Browser Rendering - Edit")
     Variable      CF_ACCOUNT_ID
     Workers AI    AI           (binding for the AI Assignment Maker)
     Variable      GOOGLE_CLIENT_ID  (OAuth client ID for "Sign in with Google")
     Secret        ADMIN_KEY    (password for the admin page)
     Variables (optional, manual payments in Pakistan):
                   PAY_JAZZCASH, PAY_EASYPAISA, PAY_NAYAPAY  e.g. "0300-1234567 · Asad Masroor"
                   PRICE_PKR_PRO (default 1699), PRICE_PKR_MAX (default 5299)
*/
const SITE = 'https://dorapdf.com';
const ALLOW = ['https://dorapdf.com', 'https://www.dorapdf.com'];

const cors = (req) => {
  const o = req.headers.get('Origin') || '';
  return {
    'Access-Control-Allow-Origin': ALLOW.includes(o) ? o : SITE,
    'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Admin-Key',
    'Vary': 'Origin',
  };
};
const json = (req, data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json', ...cors(req) } });

function cleanUrl(raw) {
  let u;
  try { u = new URL(String(raw || '').trim().match(/^https?:\/\//i) ? raw.trim() : 'https://' + String(raw).trim()); }
  catch (e) { return null; }
  if (!/^https?:$/.test(u.protocol)) return null;
  const h = u.hostname.toLowerCase();
  if (h === 'localhost' || h.endsWith('.local') || h.endsWith('.internal') || !h.includes('.')) return null;
  if (/^(127\.|10\.|0\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(h) || h.startsWith('[')) return null;
  return u.toString();
}

/* very small per-IP rate limit (per worker instance) */
const hits = new Map();
function limited(req, max = 30) {
  const ip = req.headers.get('CF-Connecting-IP') || 'x';
  const now = Date.now(), win = 60_000;
  const a = (hits.get(ip) || []).filter((t) => now - t < win);
  a.push(now); hits.set(ip, a);
  return a.length > max;
}

async function browser(env, kind, body) {
  if (!env.CF_API_TOKEN || !env.CF_ACCOUNT_ID) throw new Error('Browser Rendering is not configured yet');
  const r = await fetch(`https://api.cloudflare.com/client/v4/accounts/${env.CF_ACCOUNT_ID}/browser-rendering/${kind}`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${env.CF_API_TOKEN}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw new Error('Could not open that page (' + r.status + ')');
  return r;
}

async function og(url) {
  const r = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0 (compatible; DoraPDF-OG-Checker/1.0; +https://dorapdf.com)' }, redirect: 'follow' });
  const html = (await r.text()).slice(0, 600_000);
  const meta = {};
  const re = /<meta\s+[^>]*?(?:property|name)\s*=\s*["']([^"']+)["'][^>]*?content\s*=\s*["']([^"']*)["'][^>]*>|<meta\s+[^>]*?content\s*=\s*["']([^"']*)["'][^>]*?(?:property|name)\s*=\s*["']([^"']+)["'][^>]*>/gi;
  let m;
  while ((m = re.exec(html))) { const k = (m[1] || m[4]).toLowerCase(); const v = m[2] ?? m[3]; if (!(k in meta)) meta[k] = v; }
  const title = (html.match(/<title[^>]*>([^<]*)<\/title>/i) || [])[1] || '';
  const icon = (html.match(/<link[^>]+rel=["'][^"']*icon[^"']*["'][^>]*href=["']([^"']+)["']/i) || [])[1] || '/favicon.ico';
  const abs = (x) => { try { return x ? new URL(x, r.url).toString() : ''; } catch (e) { return ''; } };
  const dec = (s) => String(s || '').replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').trim();
  return {
    url: r.url, status: r.status,
    title: dec(meta['og:title'] || meta['twitter:title'] || title),
    description: dec(meta['og:description'] || meta['twitter:description'] || meta['description']),
    image: abs(meta['og:image'] || meta['og:image:url'] || meta['twitter:image']),
    site: dec(meta['og:site_name'] || new URL(r.url).hostname),
    icon: abs(icon),
    card: meta['twitter:card'] || '',
    raw: Object.fromEntries(Object.entries(meta).filter(([k]) => /^(og:|twitter:|description$)/.test(k)).slice(0, 40)),
  };
}


/* ================= AI Assignment Maker: accounts, plans, generation ================= */
const PLANS = {
  trial: { days: 3, assign: 3, slides: 3 },
  pro:   { usd: 6,  was: 12, assign: 6, slides: 6 },
  max:   { usd: 19, was: 29, daily: 30 },
};
const MODEL = '@cf/meta/llama-3.3-70b-instruct-fp8-fast';
const now = () => Date.now();
const monthKey = (t = now()) => new Date(t).toISOString().slice(0, 7);
const dayKey = (t = now()) => new Date(t).toISOString().slice(0, 10);
const rand = (n = 32) => Array.from(crypto.getRandomValues(new Uint8Array(n)), (b) => b.toString(16).padStart(2, '0')).join('');
const getU = async (env, email) => JSON.parse((await env.LINKS.get('u:' + email)) || 'null');
const putU = (env, u) => env.LINKS.put('u:' + u.email, JSON.stringify(u));

function planOf(u) {
  const t = now();
  if ((u.plan === 'pro' || u.plan === 'max') && u.paidUntil > t) return u.plan;
  if (t - u.trialStart < PLANS.trial.days * 864e5) return 'trial';
  return 'none';
}
function quota(u) {
  const p = planOf(u), t = now();
  u.use = u.use || {};
  if (p === 'trial') {
    const a = u.use.trialA || 0, s = u.use.trialS || 0;
    return { plan: p, endsAt: u.trialStart + PLANS.trial.days * 864e5, assignLeft: Math.max(0, PLANS.trial.assign - a), slidesLeft: Math.max(0, PLANS.trial.slides - s) };
  }
  if (p === 'pro') {
    const m = u.use.m === monthKey() ? u.use : { a: 0, s: 0 };
    return { plan: p, endsAt: u.paidUntil, assignLeft: Math.max(0, PLANS.pro.assign - (m.a || 0)), slidesLeft: Math.max(0, PLANS.pro.slides - (m.s || 0)) };
  }
  if (p === 'max') {
    const d = u.use.d === dayKey() ? (u.use.da || 0) : 0;
    const left = Math.max(0, PLANS.max.daily - d);
    return { plan: p, endsAt: u.paidUntil, assignLeft: left, slidesLeft: left, fairUse: true };
  }
  return { plan: 'none', assignLeft: 0, slidesLeft: 0, trialUsed: true };
}
function spend(u, kind) {
  const p = planOf(u); u.use = u.use || {};
  if (p === 'trial') { if (kind === 'a') u.use.trialA = (u.use.trialA || 0) + 1; else u.use.trialS = (u.use.trialS || 0) + 1; }
  else if (p === 'pro') { if (u.use.m !== monthKey()) { u.use.m = monthKey(); u.use.a = 0; u.use.s = 0; } u.use[kind] = (u.use[kind] || 0) + 1; }
  else if (p === 'max') { if (u.use.d !== dayKey()) { u.use.d = dayKey(); u.use.da = 0; } u.use.da = (u.use.da || 0) + 1; }
}
const pub = (u, req) => ({ email: u.email, name: u.name, picture: u.picture, country: req.cf && req.cf.country || '', docs: (u.docs || []).slice(0, 30), ...quota(u) });

async function authUser(req, env) {
  const tok = (req.headers.get('Authorization') || '').replace(/^Bearer\s+/i, '');
  if (!tok) return { err: 'login' };
  const email = await env.LINKS.get('s:' + tok);
  if (!email) return { err: 'login' };
  const u = await getU(env, email);
  if (!u) return { err: 'login' };
  if (u.sess !== tok) return { err: 'other-device' };
  if (u.banned) return { err: 'banned' };
  return { u };
}

async function verifyGoogle(cred, env) {
  if (!env.GOOGLE_CLIENT_ID) throw new Error('Google login is not configured yet');
  const r = await fetch('https://oauth2.googleapis.com/tokeninfo?id_token=' + encodeURIComponent(cred));
  if (!r.ok) throw new Error('Google sign-in failed, please try again');
  const j = await r.json();
  if (j.aud !== env.GOOGLE_CLIENT_ID) throw new Error('Google sign-in failed (wrong app)');
  if (!(j.email_verified === true || j.email_verified === 'true')) throw new Error('Your Google email is not verified');
  if (!['accounts.google.com', 'https://accounts.google.com'].includes(j.iss)) throw new Error('Google sign-in failed');
  return { email: String(j.email).toLowerCase(), name: j.name || '', picture: j.picture || '' };
}

function repairJson(txt) {
  if (txt && typeof txt === 'object') return txt;
  let s = String(txt || '').replace(/```(?:json)?/gi, '');
  const a = s.indexOf('{');
  if (a < 0) throw new Error('no json');
  s = s.slice(a);
  const b = s.lastIndexOf('}');
  if (b > 0) { try { return JSON.parse(s.slice(0, b + 1)); } catch (e) {} }
  /* fix raw newlines inside strings, trailing commas and a cut-off ending */
  let out = '', inStr = false, esc = false; const stack = [];
  for (const ch of s) {
    if (inStr) {
      if (esc) { esc = false; out += ch; continue; }
      if (ch === '\\') { esc = true; out += ch; continue; }
      if (ch === '"') { inStr = false; out += ch; continue; }
      if (ch === '\n') { out += '\\n'; continue; }
      if (ch === '\r' || ch === '\t') { out += ' '; continue; }
      out += ch; continue;
    }
    if (ch === '"') { inStr = true; out += ch; continue; }
    if (ch === '{') stack.push('}'); else if (ch === '[') stack.push(']');
    else if (ch === '}' || ch === ']') stack.pop();
    out += ch;
  }
  if (inStr) out += '"';
  out = out.replace(/,\s*"[^"]*"\s*:\s*("[^"]*")?\s*$/, '').replace(/,\s*$/, '').replace(/:\s*$/, ': ""');
  while (stack.length) out += stack.pop();
  out = out.replace(/,\s*([}\]])/g, '$1');
  return JSON.parse(out);
}
const ASSIGN_SCHEMA = { type: 'object', properties: { title: { type: 'string' }, subtitle: { type: 'string' }, sections: { type: 'array', items: { type: 'object', properties: { heading: { type: 'string' }, paragraphs: { type: 'array', items: { type: 'string' } }, bullets: { type: 'array', items: { type: 'string' } }, figure: { type: 'boolean' }, image_query: { type: 'string' } }, required: ['heading', 'paragraphs'] } }, references: { type: 'array', items: { type: 'string' } } }, required: ['title', 'sections', 'references'] };
const SLIDES_SCHEMA = { type: 'object', properties: { title: { type: 'string' }, subtitle: { type: 'string' }, slides: { type: 'array', items: { type: 'object', properties: { title: { type: 'string' }, bullets: { type: 'array', items: { type: 'string' } }, notes: { type: 'string' }, image: { type: 'boolean' }, image_query: { type: 'string' } }, required: ['title', 'bullets'] } } }, required: ['title', 'slides'] };
async function llmJson(env, system, user, maxTokens, schema) {
  if (!env.AI) throw new Error('The AI engine is not connected yet');
  const messages = [{ role: 'system', content: system }, { role: 'user', content: user }];
  const tries = [
    { messages, max_tokens: maxTokens, temperature: 0.5, response_format: { type: 'json_schema', json_schema: schema } },
    { messages, max_tokens: maxTokens, temperature: 0.4 },
    { messages: [messages[0], { role: 'user', content: user + '\nKeep it shorter if needed so the JSON is complete. Output only the JSON object.' }], max_tokens: maxTokens, temperature: 0.3 },
  ];
  let lastErr = null;
  for (const t of tries) {
    try {
      const r = await env.AI.run(MODEL, t);
      const d = repairJson(r && r.response !== undefined ? r.response : r);
      if (d && typeof d === 'object') return d;
    } catch (e) { lastErr = e; console.log('llm try failed:', String(e && e.message || e).slice(0, 300)); }
  }
  throw new Error('The AI is busy right now. Please try again in a minute.' + (lastErr && /limit|quota|neuron|429/i.test(String(lastErr.message)) ? ' (daily free AI limit reached)' : ''));
}
const clip = (s, n) => String(s || '').slice(0, n);

async function genAssignment(env, b) {
  const len = Math.min(3000, Math.max(300, +b.length || 1000));
  const system = 'You are an expert academic writer. You always answer with one valid JSON object and nothing else.';
  const user = `Write a complete, original student assignment.
Topic: ${clip(b.topic, 300)}
Subject: ${clip(b.subject, 120) || '(infer from topic)'}
Academic level: ${clip(b.level, 40) || 'University'}
Target length: at least ${len} words of body text (this is important: write ${Math.max(4, Math.round(len / 220))}-${Math.max(5, Math.round(len / 160))} sections, each with 2-4 full paragraphs).
Citation style: ${clip(b.cite, 30) || 'APA 7'}
Language: ${clip(b.language, 30) || 'English'}
Extra instructions: ${clip(b.extra, 600) || 'none'}
${b.hasImage ? 'The student attached a reference image. Mark exactly one section with "figure": true where an image fits best.' : ''}
${b.autoImages ? 'For 2-3 key sections set "image_query" to a short 2-4 word English search phrase for a real photo or diagram that illustrates that section (e.g. "human lungs anatomy"). Use an empty string for the other sections.' : ''}
Writing style: sound like a thoughtful, well-prepared human student, not a template. Use clear, natural language with varied sentence length, concrete examples and specific facts, and smooth but not formulaic transitions. Avoid clichés and filler such as "delve", "in today's fast-paced world", "tapestry", "plays a crucial role", "it is important to note", "in conclusion, it is evident". Do not repeat the same sentence openings.
Rules: numbered headings (1. Introduction ... n. Conclusion), academic tone, paragraphs of 3-6 sentences, in-text citations in the chosen style. References must be real, well-known, verifiable sources (books, journals, official reports); never invent DOIs or URLs.
Return JSON: {"title":string,"subtitle":string,"sections":[{"heading":string,"paragraphs":[string],"bullets":[string],"figure":boolean,"image_query":string}],"references":[string]}`;
  const d = await llmJson(env, system, user, 4096, ASSIGN_SCHEMA);
  if (d && !d.sections && Array.isArray(d.content)) d.sections = d.content;
  if (!d || !Array.isArray(d.sections) || !d.sections.length) throw new Error('The AI returned an empty assignment. Please try again.');
  d.sections = d.sections.map((s) => ({ heading: String(s.heading || s.title || ''), paragraphs: (Array.isArray(s.paragraphs) ? s.paragraphs : [s.paragraphs || s.content || '']).map(String).filter(Boolean), bullets: Array.isArray(s.bullets) ? s.bullets.map(String) : [], figure: !!s.figure, image_query: String(s.image_query || '') })).filter((s) => s.heading || s.paragraphs.length);
  d.references = Array.isArray(d.references) ? d.references.map(String) : [];
  return d;
}
async function genSlides(env, b) {
  const n = Math.min(20, Math.max(5, +b.slides || 10));
  const system = 'You are an expert presentation designer and teacher. You always answer with one valid JSON object and nothing else.';
  const user = `Create a ${n}-slide presentation.
Topic: ${clip(b.topic, 300)}
Subject: ${clip(b.subject, 120) || '(infer from topic)'}
Audience / level: ${clip(b.level, 40) || 'University'}
Language: ${clip(b.language, 30) || 'English'}
Extra instructions: ${clip(b.extra, 600) || 'none'}
${b.hasImage ? 'The presenter attached a reference image. Set "image": true on exactly one content slide where it fits best.' : ''}
${b.autoImages ? 'For 3-5 content slides set "image_query" to a short 2-4 word English search phrase for a real photo or diagram that fits the slide. Use an empty string for the others.' : ''}
Write bullets in plain, natural, human language (no buzzwords or filler).
Rules: slide 1 is the title slide, the last slide is "Conclusion" or "Thank you". Each content slide has 3-5 short bullet points (max 14 words each) and speaker notes of 2-4 sentences. Add a "References" slide before the last slide whose bullets are 2-5 real, verifiable sources. The last slide ("Conclusion") must have 3 bullet points summarising the key takeaways. No slide may have an empty bullets list except the title slide.
Return JSON: {"title":string,"subtitle":string,"slides":[{"title":string,"bullets":[string],"notes":string,"image":boolean,"image_query":string}]}`;
  const d = await llmJson(env, system, user, 4096, SLIDES_SCHEMA);
  if (!d || !Array.isArray(d.slides) || !d.slides.length) throw new Error('The AI returned an empty presentation. Please try again.');
  d.slides = d.slides.map((s) => ({ title: String(s.title || ''), bullets: Array.isArray(s.bullets) ? s.bullets.map(String) : [], notes: String(s.notes || ''), image: !!s.image, image_query: String(s.image_query || '') }));
  return d;
}


/* free images from Wikimedia Commons (with credit) */
async function commonsImage(q) {
  const url = 'https://commons.wikimedia.org/w/api.php?action=query&format=json&origin=*&generator=search&gsrnamespace=6&gsrlimit=6&gsrsearch=' + encodeURIComponent('filetype:bitmap ' + q) + '&prop=imageinfo&iiprop=url|extmetadata|mime&iiurlwidth=900';
  try {
    const r = await fetch(url, { headers: { 'User-Agent': 'DoraPDF/1.0 (https://dorapdf.com; hello@dorapdf.com)' } });
    const j = await r.json();
    const pages = Object.values((j.query && j.query.pages) || {}).sort((a, b) => (a.index || 0) - (b.index || 0));
    for (const p of pages) {
      const ii = p.imageinfo && p.imageinfo[0]; if (!ii || !ii.thumburl || !/jpe?g|png/.test(ii.mime || '')) continue;
      const m = ii.extmetadata || {};
      const strip = (s) => String(s || '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim().slice(0, 80);
      return { thumb: ii.thumburl, page: ii.descriptionurl, credit: [strip(m.Artist && m.Artist.value), strip(m.LicenseShortName && m.LicenseShortName.value)].filter(Boolean).join(', ') + ' · Wikimedia Commons' };
    }
  } catch (e) {}
  /* fallback: Openverse (Creative Commons images) */
  try {
    const r = await fetch('https://api.openverse.org/v1/images/?page_size=3&mature=false&q=' + encodeURIComponent(q), { headers: { 'User-Agent': 'DoraPDF/1.0 (https://dorapdf.com; hello@dorapdf.com)' } });
    const j = await r.json();
    const it = (j.results || [])[0];
    if (it && it.thumbnail) return { thumb: it.thumbnail, page: it.foreign_landing_url, credit: [it.creator, (it.license ? 'CC ' + String(it.license).toUpperCase() + ' ' + (it.license_version || '') : '').trim()].filter(Boolean).join(', ') + ' · ' + (it.source || 'Openverse') };
  } catch (e) {}
  return null;
}
async function addImages(list, max, origin) {
  const picks = list.filter((s) => s.image_query).slice(0, max);
  await Promise.all(picks.map(async (s) => { const im = await commonsImage(s.image_query); if (im) s.img = { src: origin + '/img?u=' + encodeURIComponent(im.thumb), credit: im.credit, page: im.page }; }));
}

async function aiRoutes(req, env, u) {
  const p = u.pathname;
  if (p === '/config') return json(req, { googleClientId: env.GOOGLE_CLIENT_ID || '', plans: PLANS, pkr: { pro: +(env.PRICE_PKR_PRO || 1699), max: +(env.PRICE_PKR_MAX || 5299) }, pay: { jazzcash: env.PAY_JAZZCASH || '', easypaisa: env.PAY_EASYPAISA || '', nayapay: env.PAY_NAYAPAY || '' }, country: req.cf && req.cf.country || '' });

  if (p === '/auth/google' && req.method === 'POST') {
    if (!env.LINKS) return json(req, { error: 'Accounts are not configured yet' }, 503);
    const b = await req.json().catch(() => ({}));
    const g = await verifyGoogle(b.credential, env);
    let user = await getU(env, g.email);
    if (!user) user = { email: g.email, created: now(), trialStart: now(), plan: 'trial', use: {} };
    if (user.banned) return json(req, { error: 'This account is suspended. Contact hello@dorapdf.com' }, 403);
    user.name = g.name; user.picture = g.picture;
    /* one device: the new session replaces the old one; the old token now gets "other-device" */
    const tok = rand(); user.sess = tok; user.lastLogin = now();
    user.ua = clip(req.headers.get('User-Agent'), 160);
    await env.LINKS.put('s:' + tok, user.email, { expirationTtl: 60 * 60 * 24 * 60 });
    await putU(env, user);
    return json(req, { token: tok, user: pub(user, req) });
  }

  if (p === '/me' || p === '/auth/logout' || p.startsWith('/ai/') || p === '/pay/claim' || p === '/docs/add') {
    const a = await authUser(req, env);
    if (a.err === 'other-device') return json(req, { error: 'You were signed out because this account was opened on another device.', code: 'other-device' }, 401);
    if (a.err === 'banned') return json(req, { error: 'This account is suspended. Contact hello@dorapdf.com', code: 'banned' }, 403);
    if (a.err) return json(req, { error: 'Please sign in first', code: 'login' }, 401);
    const user = a.u;
    if (p === '/me') return json(req, { user: pub(user, req) });
    if (p === '/docs/add' && req.method === 'POST') {
      const b = await req.json().catch(() => ({}));
      const link = String(b.link || '');
      if (!/^https:\/\/(docs|drive)\.google\.com\//.test(link)) return json(req, { error: 'bad link' }, 400);
      user.docs = [{ t: clip(b.title, 120), type: b.type === 'slides' ? 'slides' : 'assignment', link, at: now() }, ...(user.docs || [])].slice(0, 30);
      await putU(env, user);
      return json(req, { ok: true, user: pub(user, req) });
    }
    if (p === '/auth/logout') { await env.LINKS.delete('s:' + user.sess); user.sess = ''; await putU(env, user); return json(req, { ok: true }); }
    if (p === '/pay/claim' && req.method === 'POST') {
      const b = await req.json().catch(() => ({}));
      if (!['pro', 'max'].includes(b.plan)) return json(req, { error: 'Pick a plan' }, 400);
      const claim = { id: rand(6), email: user.email, plan: b.plan, method: clip(b.method, 20), txn: clip(b.txn, 60), amount: clip(b.amount, 20), at: now(), status: 'pending' };
      if (!claim.txn) return json(req, { error: 'Enter the transaction ID' }, 400);
      await env.LINKS.put('c:' + claim.at + ':' + claim.id, JSON.stringify(claim), { expirationTtl: 60 * 60 * 24 * 120 });
      return json(req, { ok: true, message: 'Payment received for review. Your plan will be active within a few hours.' });
    }
    if (p === '/ai/assignment' || p === '/ai/slides') {
      const kind = p === '/ai/assignment' ? 'a' : 's';
      const q = quota(user);
      if (q.plan === 'none') return json(req, { error: 'Your free trial has ended. Upgrade to keep creating.', code: 'upgrade', user: pub(user, req) }, 402);
      if ((kind === 'a' ? q.assignLeft : q.slidesLeft) <= 0) return json(req, { error: q.plan === 'max' ? 'Daily fair-use limit reached. Try again tomorrow.' : 'You have used all your ' + (kind === 'a' ? 'assignments' : 'presentations') + ' for this ' + (q.plan === 'trial' ? 'trial' : 'month') + '. Upgrade for more.', code: 'upgrade', user: pub(user, req) }, 402);
      const b = await req.json().catch(() => ({}));
      if (!String(b.topic || '').trim()) return json(req, { error: 'Enter a topic' }, 400);
      const doc = kind === 'a' ? await genAssignment(env, b) : await genSlides(env, b);
      if (b.autoImages) await addImages(kind === 'a' ? doc.sections : doc.slides, kind === 'a' ? 3 : 5, u.origin);
      const fresh = await getU(env, user.email) || user; spend(fresh, kind); await putU(env, fresh);
      return json(req, { doc, user: pub(fresh, req) });
    }
  }

  if (p.startsWith('/admin/')) {
    if (!env.ADMIN_KEY || req.headers.get('X-Admin-Key') !== env.ADMIN_KEY) return json(req, { error: 'Wrong admin key' }, 403);
    if (p === '/admin/claims') {
      const l = await env.LINKS.list({ prefix: 'c:' });
      const items = await Promise.all(l.keys.slice(-100).map(async (k) => JSON.parse(await env.LINKS.get(k.name) || 'null')));
      return json(req, { claims: items.filter(Boolean).reverse() });
    }
    if (p === '/admin/plan' && req.method === 'POST') {
      const b = await req.json().catch(() => ({}));
      const email = String(b.email || '').toLowerCase().trim();
      const user = await getU(env, email);
      if (!user) return json(req, { error: 'No account with that email (they must sign in once first)' }, 404);
      if (b.ban !== undefined) user.banned = !!b.ban;
      if (b.plan) {
        const months = Math.min(24, Math.max(0, +b.months || 1));
        const from = Math.max(now(), user.paidUntil || 0);
        user.plan = b.plan; user.paidUntil = b.plan === 'none' ? 0 : from + months * 30 * 864e5;
      }
      await putU(env, user);
      if (b.claim) { const l = await env.LINKS.list({ prefix: 'c:' }); for (const k of l.keys) { if (k.name.endsWith(':' + b.claim)) { const c = JSON.parse(await env.LINKS.get(k.name)); c.status = b.plan ? 'approved' : 'rejected'; await env.LINKS.put(k.name, JSON.stringify(c), { expirationTtl: 60 * 60 * 24 * 120 }); } } }
      return json(req, { ok: true, user: { email: user.email, plan: planOf(user), paidUntil: user.paidUntil, banned: !!user.banned } });
    }
    if (p === '/admin/aitest') {
      const kind = u.searchParams.get('kind') || 'a';
      const t0 = now();
      try { const doc = kind === 'a' ? await genAssignment(env, { topic: u.searchParams.get('topic') || 'Respiratory system', subject: 'Anatomy', level: 'University', length: 1000, autoImages: true }) : await genSlides(env, { topic: u.searchParams.get('topic') || 'Respiratory system', slides: 8, autoImages: true });
        await addImages(doc.sections || doc.slides, kind === 'a' ? 3 : 5, u.origin);
        return json(req, { ok: true, ms: now() - t0, sections: (doc.sections || doc.slides || []).length, words: JSON.stringify(doc).split(/\s+/).length, doc });
      } catch (e) { return json(req, { ok: false, ms: now() - t0, error: String(e.message || e) }, 500); }
    }
    if (p === '/admin/user') {
      const user = await getU(env, String(u.searchParams.get('email') || '').toLowerCase().trim());
      return user ? json(req, { user: { ...user, sess: user.sess ? 'active' : '' , ...quota(user) } }) : json(req, { error: 'Not found' }, 404);
    }
  }
  return null;
}

const ABC = 'abcdefghjkmnpqrstuvwxyz23456789';
const code = (n = 6) => Array.from(crypto.getRandomValues(new Uint8Array(n)), (b) => ABC[b % ABC.length]).join('');

export default {
  async fetch(req, env) {
    const u = new URL(req.url);
    if (req.method === 'OPTIONS') return new Response(null, { headers: cors(req) });

    /* short links: go.dorapdf.com/<code>  or  <worker>/go/<code> */
    if (u.hostname.startsWith('go.') || u.pathname.startsWith('/go/')) {
      const c = u.hostname.startsWith('go.') ? u.pathname.slice(1) : u.pathname.slice(4);
      if (!c) return Response.redirect(SITE + '/link-shortener/', 302);
      const dest = env.LINKS && (await env.LINKS.get('l:' + c));
      return dest ? Response.redirect(dest, 301) : new Response('Link not found', { status: 404 });
    }

    try {
      if (u.pathname === '/health') return json(req, { ok: true, browser: !!(env.CF_API_TOKEN && env.CF_ACCOUNT_ID), links: !!env.LINKS, ai: !!env.AI, google: !!env.GOOGLE_CLIENT_ID, admin: !!env.ADMIN_KEY });
      if (limited(req, u.pathname.startsWith('/admin/') ? 120 : 30)) return json(req, { error: 'Too many requests — wait a minute.' }, 429);
      const ar = await aiRoutes(req, env, u);
      if (ar) return ar;

      if (u.pathname === '/img') {
        let src; try { src = new URL(u.searchParams.get('u')); } catch (e) { return json(req, { error: 'bad url' }, 400); }
        if (!(/(^|\.)wikimedia\.org$/.test(src.hostname) || src.hostname === 'api.openverse.org')) return json(req, { error: 'not allowed' }, 400);
        const r = await fetch(src.toString(), { headers: { 'User-Agent': 'DoraPDF/1.0 (https://dorapdf.com; hello@dorapdf.com)' }, cf: { cacheTtl: 86400 } });
        return new Response(r.body, { status: r.status, headers: { 'Content-Type': r.headers.get('Content-Type') || 'image/jpeg', 'Cache-Control': 'public, max-age=86400', ...cors(req) } });
      }
      if (u.pathname === '/og') {
        const url = cleanUrl(u.searchParams.get('url'));
        if (!url) return json(req, { error: 'Enter a valid public web address' }, 400);
        return json(req, await og(url));
      }

      if (u.pathname === '/short' && req.method === 'POST') {
        if (!env.LINKS) return json(req, { error: 'Link shortener is not configured yet' }, 503);
        const b = await req.json().catch(() => ({}));
        const url = cleanUrl(b.url);
        if (!url) return json(req, { error: 'Enter a valid public web address' }, 400);
        let c = code();
        for (let i = 0; i < 5 && (await env.LINKS.get('l:' + c)); i++) c = code();
        await env.LINKS.put('l:' + c, url);
        const short = (env.SHORT_BASE || (u.origin + '/go/')) + c;
        return json(req, { code: c, short, url });
      }

      if (u.pathname === '/shot' || u.pathname === '/pdf') {
        const url = cleanUrl(u.searchParams.get('url'));
        if (!url) return json(req, { error: 'Enter a valid public web address' }, 400);
        const w = Math.min(1920, Math.max(320, +u.searchParams.get('w') || 1366));
        const cacheKey = new Request(u.toString(), { method: 'GET' });
        const cache = caches.default;
        const hit = await cache.match(cacheKey);
        if (hit) { const r = new Response(hit.body, hit); Object.entries(cors(req)).forEach(([k, v]) => r.headers.set(k, v)); return r; }
        let r;
        if (u.pathname === '/shot') {
          r = await browser(env, 'screenshot', { url, viewport: { width: w, height: Math.round(w * (w < 800 ? 2.1 : 0.62)) }, screenshotOptions: { fullPage: u.searchParams.get('full') === '1', type: 'png' }, gotoOptions: { waitUntil: 'networkidle2', timeout: 30000 } });
        } else {
          r = await browser(env, 'pdf', { url, pdfOptions: { format: (u.searchParams.get('size') || 'a4'), printBackground: true, landscape: u.searchParams.get('land') === '1' }, gotoOptions: { waitUntil: 'networkidle2', timeout: 30000 } });
        }
        const out = new Response(r.body, { headers: { 'Content-Type': u.pathname === '/shot' ? 'image/png' : 'application/pdf', 'Cache-Control': 'public, max-age=1800', ...cors(req) } });
        await cache.put(cacheKey, out.clone());
        return out;
      }

      return json(req, { error: 'Not found' }, 404);
    } catch (e) {
      return json(req, { error: String(e.message || e) }, 502);
    }
  },
};
