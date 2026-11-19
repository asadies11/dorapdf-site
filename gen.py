import json, re, os, shutil, html as H, markdown
from content_tools import CUSTOM
from content_blog import POSTS
from content_pages import PAGES

SITE = 'https://dorapdf.com'
SRC = open('index.html').read()
from content_i18n import UI, TOOLS_I18N
TOOLS = json.load(open('tools.json'))
_G = {i: k for k, v in json.load(open('groups.json')).items() for i in v}
for _t in TOOLS:
    _t['ocat'] = _t['cat']; _t['cat'] = _G.get(_t['id'], _t['cat'])
BYID = {t['id']: t for t in TOOLS}
CATN = {'pdf': 'PDF & Document Tools', 'image': 'Image & Media Tools', 'ai': 'AI Tools', 'design': 'Designer Tools', 'dev': 'Developer Tools', 'text': 'Text Tools', 'business': 'Business & Office Tools', 'calc': 'Calculators & Unit Converters', 'fun': 'Fun & Games', 'convert': 'Converters', 'pro': 'Professional'}
OUT = 'dist'
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
esc = lambda s: H.escape(s, quote=True)

# ---------- shared pieces ----------
base = SRC
_css = re.search(r'<style>(.*?)</style>', base, re.S)
_js = max(re.findall(r'<script>(.*?)</script>', base, re.S), key=len)
_fav = re.search(r'<link rel="icon" href="([^"]*)">', base).group(1)
open_later = {'app.js': _js}
base = base.replace(_css.group(0), '<link rel="stylesheet" href="/style.css">', 1)
base = base.replace('<script>' + _js + '</script>', '<script src="/app.js"></script>', 1)
for f in ['tools-pdf.js', 'tools-image.js', 'tools-text.js', 'tools-calc.js', 'tools-pro.js', 'dora.js', 'account.js']:
    base = base.replace(f'<script src="{f}">', f'<script src="/{f}">')
CSS = re.search(r'<style>(.*?)</style>', SRC, re.S).group(1)
ADS = re.search(r'(<!-- Google AdSense -->.*?</script>)', SRC, re.S).group(1)
NAV = re.search(r'(<nav>.*?</nav>)', SRC, re.S).group(1)
FOOTER = re.search(r'(<footer id="footer">.*?</footer>)', SRC, re.S).group(1)
GTAG = re.search(r'(<!-- Google tag \(GA4\) -->.*?</script>\s*<script>.*?</script>)', SRC, re.S).group(1)
FAVICON = '<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png"><link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png">'
SOCIALJS = re.search(r"(const SOCIAL=\{.*?\n.*?\n.*?\n)", SRC, re.S).group(1)
THEMEHEAD = '<script>try{const t=localStorage.getItem("dp_theme");if(t)document.documentElement.dataset.theme=t}catch(e){}</script>'
open(f'{OUT}/style.css', 'w').write(CSS)
open(f'{OUT}/app.js', 'w').write(_js)
import urllib.parse
open(f'{OUT}/favicon.svg', 'w').write(urllib.parse.unquote(_fav.split(',',1)[1]).replace("'",'"').replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" ',1))
base = base.replace(_fav, '/favicon.svg')
base = re.sub(r'<link rel="icon" href="/favicon.svg"[^>]*>', FAVICON, base, count=1)

def fit_title(t, mx=60):
    t = t.strip()
    if len(t) <= mx: return t
    for suf in (' | DoraPDF Blog', ' | DoraPDF', ' — DoraPDF'):
        if t.endswith(suf) and len(t) - len(suf) <= mx + 8: return t[:-len(suf)]
    for suf in (' | DoraPDF Blog', ' | DoraPDF', ' — DoraPDF'):
        if t.endswith(suf): t = t[:-len(suf)]
    if len(t) > 70:
        for sep in (' : ', ': ', ' — ', ' (', ' - '):
            i = t.find(sep)
            if 25 <= i <= 70: return t[:i]
        cut = t[:66]; t = cut[:cut.rfind(' ')].rstrip(',;:—-')
    return t
def fit_desc(d, mx=158):
    d = ' '.join(d.split())
    if len(d) <= mx: return d
    cut = d[:mx]
    dot = cut.rfind('. ')
    if dot > 90: return cut[:dot+1]
    return cut[:cut.rfind(' ')].rstrip(',;:—-') + '.'

def set_meta(page, title, desc, path, og_title=None):
    title, desc = fit_title(title), fit_desc(desc)
    url = SITE + path
    page = re.sub(r'<title>.*?</title>', f'<title>{esc(title)}</title>', page, count=1, flags=re.S)
    page = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', page, count=1)
    page = page.replace('<link rel="canonical" href="https://dorapdf.com/">', f'<link rel="canonical" href="{url}">')
    page = page.replace('<meta property="og:url" content="https://dorapdf.com/">', f'<meta property="og:url" content="{url}">')
    page = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(og_title or title)}">', page, count=1)
    page = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(desc)}">', page, count=1)
    page = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{esc(og_title or title)}">', page, count=1)
    page = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{esc(desc)}">', page, count=1)
    return page

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

# ---------- home ----------
open(f'{OUT}/index.html', 'w').write(re.sub(r'(<meta name="description" content=")([^"]*)', lambda m: m.group(1)+esc(fit_desc(H.unescape(m.group(2)))), base, count=1).replace('<h1 class="tp-h" id="tpTitle"></h1>','<h2 class="tp-h" id="tpTitle"></h2>',1))

# ---------- tool content ----------
def gen_content(t):
    c = CUSTOM.get(t['id'])
    if c: return c
    n, d, cat = t['name'], t['desc'].rstrip('.'), t.get('ocat', t['cat'])
    priv = 'Everything runs in your browser, so your files are processed on your own device and never uploaded.' if t['file'] else 'Everything runs in your browser — nothing you type is sent to a server.'
    intro = f"{n} — {d[0].lower()+d[1:]}. {priv} It's completely free, works on phones and computers, and needs no sign-up."
    if t['file']:
        steps = ['Drop your file into the box above, or tap it to choose a file from your phone or computer.',
                 'Adjust the options if you need to.', 'Press the button to start — it only takes a few seconds.', 'Download your result.']
    elif cat == 'calc':
        steps = ['Enter your numbers in the fields above.', 'Results update instantly as you type.', 'Change any value to compare different scenarios.']
    elif cat in ('convert',):
        steps = ['Type or paste your text (or value) into the input box.', 'Choose any options you need.', 'Your result appears instantly — press Copy to use it anywhere.']
    else:
        steps = ['Fill in the fields or adjust the controls above.', 'Watch the live preview update.', 'Copy the result or download it.']
    faqs = [(f'Is {n} free?', 'Yes. It is completely free to use, with no sign-up, no limits and no watermark.'),
            ('Is my data private?', priv),
            ('Does it work on mobile?', 'Yes. It works in any modern browser on Android, iPhone, Windows, Mac and Linux.')]
    if cat == 'calc':
        faqs.append(('How accurate are the results?', 'The calculator uses standard formulas and gives reliable estimates for planning. For financial, legal or medical decisions, please confirm with a qualified professional.'))
    return dict(intro=intro, steps=steps, faqs=faqs)

def seo_block(t, c):
    rel = [x for x in TOOLS if x['cat'] == t['cat'] and x['id'] != t['id'] and not x['soon']][:6]
    rel_html = ''.join(f'<li><a href="/{x["id"]}/" style="color:var(--pink2)">{esc(x["name"])}</a> — {esc(x["desc"])}</li>' for x in rel)
    posts = [p for p in POSTS if t['id'] in p['tools']][:3]
    post_html = ''.join(f'<li><a href="/blog/{p["slug"]}/" style="color:var(--pink2)">{esc(p["title"])}</a></li>' for p in posts)
    return (f'<section class="seo"><div><h2>About {esc(t["name"])}</h2><p>{c["intro"]}</p></div>'
            f'<div><h2>How to use {esc(t["name"])}</h2><ol>' + ''.join(f'<li>{s}</li>' for s in c['steps']) + '</ol></div>'
            '<div><h2>Why use DoraPDF?</h2><ul><li><b>Private:</b> files are processed on your device, never uploaded.</li><li><b>Free:</b> no sign-up, no limits, no watermark.</li><li><b>Fast:</b> no waiting in upload queues.</li><li><b>Works everywhere:</b> phone, tablet or computer.</li></ul></div>'
            '<div><h2>Frequently asked questions</h2>' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in c['faqs']) + '</div>'
            + (f'<div><h2>Helpful guides</h2><ul>{post_html}</ul></div>' if post_html else '')
            + f'<div><h2>More {CATN[t["cat"]]}</h2><ul>{rel_html}</ul></div></section>')

def plain(s): return re.sub(r'<[^>]+>', '', s).replace('&amp;', '&')

SEO = {  # from Google Trends keyword research (worldwide)
    'pdf-to-word': ('Convert PDF to Word Free Online (Keeps Layout) | DoraPDF', 'Convert PDF to Word online for free. Keeps the original layout, tables and fonts. No sign-up, no watermark, files stay in your browser.'),
    'word-to-pdf': ('Word to PDF Converter: Convert Word to PDF Online Free | DoraPDF', 'Convert Word to PDF online free. Turn DOCX files into PDF in seconds, no sign-up, no watermark, private in your browser.'),
    'images-to-pdf': ('JPG to PDF: Convert Image to PDF Free Online | DoraPDF', 'Convert JPG to PDF free. Turn pictures, photos and scans into one PDF online, no sign-up, no watermark, private in your browser.'),
    'pdf-to-jpg': ('PDF to JPG: Convert PDF to Image Free Online | DoraPDF', 'Convert PDF to JPG online free in high quality. Every page becomes an image, no sign-up, no watermark, files stay on your device.'),
    'pdf-to-excel': ('Convert PDF to Excel Free Online | DoraPDF', 'Convert PDF to Excel free online. Pull tables from PDF into an editable XLSX sheet, no sign-up, private in your browser.'),
    'heic-to-pdf': ('Convert HEIC to PDF Free: iPhone Photos to PDF | DoraPDF', 'Convert HEIC to PDF free. Turn iPhone photos into a PDF online, no app or sign-up needed, private in your browser.'),
    'png-to-jpg': ('Convert PNG to JPG Free Online | DoraPDF', 'Convert PNG to JPG online free. Fast, high quality, no sign-up, no watermark, images never leave your device.'),
    'pdf-merger': ('Merge PDF Online Free: Combine PDF Files | DoraPDF', 'Merge PDF online free. Combine multiple PDF files into one in any order, no sign-up, no watermark, private in your browser.'),
    'image-compressor': ('Compress JPEG and Images Online Free | DoraPDF', 'Compress JPEG, PNG and WebP images online free. Reduce file size and keep quality, no sign-up, private in your browser.'),
    'pdf-compressor': ('Compress PDF Online Free: Reduce PDF File Size | DoraPDF', 'Compress PDF online free. Reduce PDF file size for email and uploads while keeping it readable. No sign-up, no watermark, private.'),
    'pdf-splitter': ('Split PDF Online Free: Extract PDF Pages | DoraPDF', 'Split PDF online free. Extract pages or cut one PDF into several files in seconds. No sign-up, no watermark, files stay in your browser.'),
    'png-to-pdf': ('PNG to PDF: Convert PNG Images to PDF Free | DoraPDF', 'Convert PNG to PDF free online. Combine one or many PNG images into a single PDF. No sign-up, no watermark, private in your browser.'),
    'pdf-to-png': ('PDF to PNG: Convert PDF Pages to PNG Free | DoraPDF', 'Convert PDF to PNG online free. Every page becomes a sharp PNG image. No sign-up, no watermark, files never leave your device.'),
    'jpeg-to-png': ('Convert JPEG to PNG Free Online | DoraPDF', 'Convert JPEG and JPG to PNG online free. Keep full quality, no sign-up, no watermark, images stay on your device.'),
    'jpg-to-png': ('Convert JPG to PNG Free Online (High Quality) | DoraPDF', 'Convert JPG to PNG online free in high quality. Batch convert, no sign-up, no watermark, private in your browser.'),
    'heic-to-jpg': ('HEIC to JPG: Convert iPhone Photos to JPG Free | DoraPDF', 'Convert HEIC to JPG free online. Open iPhone photos anywhere, batch convert, no app or sign-up, private in your browser.'),
    'webp-to-jpg': ('WebP to JPG: Convert WebP Images Free Online | DoraPDF', 'Convert WebP to JPG online free. Batch convert WebP images to JPG, no sign-up, no watermark, private in your browser.'),
    'image-background-remover': ('Remove Background from Image Free Online | DoraPDF', 'Remove the background from any image free with AI. Get a transparent PNG in seconds, no sign-up, runs privately in your browser.'),
    'image-resizer': ('Resize Image Online Free: Change Image Size | DoraPDF', 'Resize images online free. Change width, height or file size for social media, forms and uploads. No sign-up, private.'),
    'pptx-to-pdf': ('PowerPoint to PDF: Convert PPTX to PDF Free | DoraPDF', 'Convert PowerPoint to PDF online free. Turn PPTX slides into a PDF in seconds, no sign-up, no watermark, private.'),
    'pdf-to-powerpoint': ('PDF to PowerPoint: Convert PDF to PPTX Free | DoraPDF', 'Convert PDF to PowerPoint online free. Every page becomes an editable slide. No sign-up, no watermark, private in your browser.'),
    'url-to-pdf': ('HTML to PDF: Convert Web Page to PDF Free | DoraPDF', 'Convert HTML or any web page URL to PDF online free. Save articles and pages as PDF, no sign-up, no watermark.'),
    'qr-code-generator': ('Free QR Code Generator (No Sign-up, No Expiry) | DoraPDF', 'Create QR codes free for links, Wi-Fi, text and contacts. Download PNG or SVG, no sign-up, codes never expire.'),
    'word-counter': ('Word Counter: Count Words and Characters Free | DoraPDF', 'Free online word counter. Count words, characters, sentences and reading time instantly as you type. Private, no sign-up.'),
    'pdf-ocr': ('PDF OCR Online Free: Make Scanned PDF Searchable | DoraPDF', 'Free PDF OCR online. Turn scanned PDFs and images into searchable, copyable text. No sign-up, private in your browser.'),
    'scan-to-pdf': ('Scan to PDF Online Free: Phone Camera Scanner | DoraPDF', 'Scan documents to PDF free with your phone camera. Auto crop, clean pages, unlimited scans, no app or sign-up needed.'),
}

tool_urls = []
for t in TOOLS:
    if t['soon']: continue
    c = gen_content(t)
    title = f'{t["name"]} — Free Online, No Sign-up | DoraPDF'
    desc = (f'{t["desc"].rstrip(".")}. Free online {t["name"]} — fast, private (files never leave your device), no sign-up, no watermark.')[:300]
    if t['id'] in SEO: title, desc = SEO[t['id']]
    path = f'/{t["id"]}/'
    p = set_meta(base, title, desc, path, f'{t["name"]} — Free | DoraPDF')
    p = p.replace('<body>', '<body class="toolpage">', 1)
    p = p.replace('href="#tools"', 'href="/#tools"').replace('href="#ai"', 'href="/#ai"').replace('href="#pricing"', 'href="/#pricing"').replace('href="#top"', 'href="/"').replace('href="#gen"', 'href="/#gen"')
    p = p.replace('</head>', f'<script>window.TOOL_PAGE={json.dumps(t["id"])}</script>\n' + ld({
        '@context': 'https://schema.org', '@graph': [
            {'@type': 'WebApplication', 'name': t['name'], 'url': SITE + path, 'applicationCategory': 'UtilitiesApplication', 'operatingSystem': 'Any (web browser)',
             'description': t['desc'], 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}, 'publisher': {'@type': 'Organization', 'name': 'DoraPDF', 'url': SITE + '/'}},
            {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': plain(q), 'acceptedAnswer': {'@type': 'Answer', 'text': plain(a)}} for q, a in c['faqs']]},
            {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'DoraPDF', 'item': SITE + '/'},
                                                             {'@type': 'ListItem', 'position': 2, 'name': t['name'], 'item': SITE + path}]}]}) + '\n</head>', 1)
    # demote hidden hero h1
    p = p.replace('<h1>Feed Dora your file.', '<div>Feed Dora your file.', 1).replace('<em>She</em> handles the rest.</h1>', '<em>She</em> handles the rest.</div>', 1)
    # prerender heading + description + seo
    p = p.replace('<h1 class="tp-h" id="tpTitle"></h1>', f'<h1 class="tp-h" id="tpTitle">{esc(t["name"])}</h1>', 1)
    p = p.replace('<p class="tp-d" id="tpDesc"></p>', f'<p class="tp-d" id="tpDesc">{esc(t["long"] or t["desc"])}</p>', 1)
    p = p.replace('<div class="tcrumb" id="tCrumb"></div>', f'<div class="tcrumb" id="tCrumb">{CATN[t["cat"]]}</div>', 1)
    p = p.replace('<p class="note" id="tpNote"></p>', '<p class="note" id="tpNote"></p>' + seo_block(t, c), 1)
    os.makedirs(f'{OUT}{path}', exist_ok=True)
    open(f'{OUT}{path}index.html', 'w').write(p)
    tool_urls.append(path)


# ---------- German / Spanish tool pages ----------
LANGS = ['de', 'es']
def loc_path(lang, tid):
    return f'/{lang}/{TOOLS_I18N[lang][tid][0]}/'
def alt_links(tid):
    if tid not in TOOLS_I18N['de']: return ''
    out = f'<link rel="alternate" hreflang="en" href="{SITE}/{tid}/">'
    for L in LANGS:
        out += f'<link rel="alternate" hreflang="{L}" href="{SITE}{loc_path(L, tid)}">'
    return out + f'<link rel="alternate" hreflang="x-default" href="{SITE}/{tid}/">'
def lang_switch(tid, cur):
    if tid not in TOOLS_I18N['de']: return ''
    items = [('en', 'EN', f'/{tid}/')] + [(L, L.upper(), loc_path(L, tid)) for L in LANGS]
    links = ' · '.join((f'<b style="color:var(--pink2)">{lab}</b>' if L == cur else f'<a href="{href}" hreflang="{L}" style="color:var(--mute)">{lab}</a>') for L, lab, href in items)
    return f'<div class="langsw" style="margin:6px 0 2px;font-size:13px;letter-spacing:.08em">{links}</div>'

# add hreflang + switch to the English pages that have translations
for tid in TOOLS_I18N['de']:
    fp = f'{OUT}/{tid}/index.html'
    if not os.path.exists(fp): continue
    h = open(fp).read()
    h = h.replace('</head>', alt_links(tid) + '\n</head>', 1)
    h = h.replace('<div class="tcrumb" id="tCrumb">', lang_switch(tid, 'en') + '<div class="tcrumb" id="tCrumb">', 1)
    open(fp, 'w').write(h)

loc_urls = []
TMAP = {x['id']: x for x in TOOLS}
for L in LANGS:
    U = UI[L]
    for tid, (slug, title, desc, h1, short, intro) in TOOLS_I18N[L].items():
        t = TMAP[tid]
        path = f'/{L}/{slug}/'
        n = h1
        faqs = [(U['faq_free'][0].format(n=n), U['faq_free'][1]), U['faq_priv'], U['faq_mobile']]
        p = set_meta(base, title, desc, path, title)
        p = p.replace('<html lang="en">', f'<html lang="{L}">', 1)
        p = p.replace('<body>', '<body class="toolpage">', 1)
        p = p.replace('href="#tools"', 'href="/#tools"').replace('href="#ai"', 'href="/#ai"').replace('href="#pricing"', 'href="/#pricing"').replace('href="#top"', 'href="/"').replace('href="#gen"', 'href="/#gen"')
        p = p.replace('</head>', f'<script>window.TOOL_PAGE={json.dumps(tid)};window.TOOL_LANG={json.dumps(L)}</script>\n' + alt_links(tid) + '\n' + ld({
            '@context': 'https://schema.org', '@graph': [
                {'@type': 'WebApplication', 'name': h1, 'url': SITE + path, 'inLanguage': L, 'applicationCategory': 'UtilitiesApplication', 'operatingSystem': 'Any (web browser)',
                 'description': short, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'}, 'publisher': {'@type': 'Organization', 'name': 'DoraPDF', 'url': SITE + '/'}},
                {'@type': 'FAQPage', 'inLanguage': L, 'mainEntity': [{'@type': 'Question', 'name': plain(q), 'acceptedAnswer': {'@type': 'Answer', 'text': plain(a)}} for q, a in faqs]},
                {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'DoraPDF', 'item': SITE + f'/{L}/'},
                                                                 {'@type': 'ListItem', 'position': 2, 'name': h1, 'item': SITE + path}]}]}) + '\n</head>', 1)
        p = p.replace('<h1>Feed Dora your file.', '<div>Feed Dora your file.', 1).replace('<em>She</em> handles the rest.</h1>', '<em>She</em> handles the rest.</div>', 1)
        p = p.replace('<h1 class="tp-h" id="tpTitle"></h1>', f'<h1 class="tp-h" id="tpTitle">{esc(h1)}</h1>', 1)
        p = p.replace('<p class="tp-d" id="tpDesc"></p>', f'<p class="tp-d" id="tpDesc">{esc(short)}</p>', 1)
        p = p.replace('<div class="tcrumb" id="tCrumb"></div>', lang_switch(tid, L) + f'<div class="tcrumb" id="tCrumb"><a href="/{L}/" style="color:inherit">{U["crumb"]}</a></div>', 1)
        others = [(x, TOOLS_I18N[L][x]) for x in TOOLS_I18N[L] if x != tid][:8]
        seo = (f'<section class="seo"><div><p style="color:var(--mute);font-size:13px">{U["ui_note"]}</p><h2>{esc(h1)}</h2><p>{esc(intro)}</p></div>'
               f'<div><h2>{U["how"]}</h2><ol>' + ''.join(f'<li>{s}</li>' for s in U['steps_file']) + '</ol></div>'
               f'<div><h2>{U["why"]}</h2><ul>' + ''.join(f'<li>{w}</li>' for w in U['why_list']) + '</ul></div>'
               f'<div><h2>{U["faq"]}</h2>' + ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faqs) + '</div>'
               f'<div><h2>{U["more"]}</h2><ul>' + ''.join(f'<li><a href="/{L}/{v[0]}/" style="color:var(--pink2)">{esc(v[3])}</a> – {esc(v[4])}</li>' for x, v in others)
               + f'<li><a href="/#tools" style="color:var(--pink2)">{U["all_tools"]}</a></li></ul></div></section>')
        p = p.replace('<p class="note" id="tpNote"></p>', '<p class="note" id="tpNote"></p>' + seo, 1)
        os.makedirs(f'{OUT}{path}', exist_ok=True)
        open(f'{OUT}{path}index.html', 'w').write(p)
        loc_urls.append(path)

import shutil as _sh
if os.path.isdir('vendor'):
    _sh.copytree('vendor', f'{OUT}/vendor', dirs_exist_ok=True)

# ---------- static content pages ----------
ART_CSS = '''
.article{max-width:780px;margin:0 auto;padding:140px 24px 70px;position:relative;z-index:1}
.article .crumb{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--pink)}
.article .crumb a{color:var(--pink)}
.article h1{font-size:clamp(30px,5vw,48px);font-weight:600;line-height:1.1;margin:14px 0 12px}
.article .meta{color:var(--mute);font-size:14px;margin-bottom:34px}
.prose{font-size:17px;line-height:1.8;color:var(--txt)}
.prose h2{font-family:Unbounded;font-size:24px;font-weight:600;margin:42px 0 14px;line-height:1.25}
.prose h3{font-size:19px;margin:28px 0 10px}
.prose p{margin:14px 0;color:var(--txt);opacity:.88}
.prose ul,.prose ol{margin:14px 0 14px 24px;display:grid;gap:8px;opacity:.9}
.prose a{color:var(--pink2);text-decoration:underline;text-underline-offset:3px}
.prose strong{color:var(--txt)}
.prose code{background:var(--card);border:1px solid var(--line);padding:2px 7px;border-radius:6px;font-size:.9em}
.prose table{width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;display:block;overflow-x:auto}
.prose th,.prose td{border:1px solid var(--line);padding:10px 12px;text-align:left}
.prose th{background:var(--card)}
.prose em{color:var(--mute)}
.cta-box{margin:46px 0 10px;padding:28px;border-radius:24px;background:linear-gradient(135deg,rgba(255,46,136,.16),rgba(155,60,255,.1));border:1px solid rgba(255,46,136,.35)}
.cta-box h3{font-family:Unbounded;font-size:18px;margin-bottom:14px}
.cta-box .tl{display:flex;flex-wrap:wrap;gap:10px}
.cta-box a{padding:10px 18px;border-radius:999px;background:linear-gradient(135deg,var(--pink),var(--violet));color:#fff;font-weight:600;font-size:14px}
.postgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;margin-top:30px}
.pcard{display:block;padding:24px;border-radius:22px;background:var(--card);border:1px solid var(--line);transition:transform .3s,border-color .3s}
.pcard:hover{transform:translateY(-5px);border-color:rgba(255,46,136,.5)}
.pcard h2{font-size:18px;font-weight:600;line-height:1.3;margin:10px 0 8px;font-family:Unbounded}
.pcard p{color:var(--mute);font-size:14.5px}
.pcard .tag{font-size:10px}
html[data-theme=light] .pcard{background:#fff}
#dot,#glow{display:none}
'''
PAGE_JS = '''<script>
const $=s=>document.querySelector(s);''' + SOCIALJS + '''
const tb=document.getElementById('themeBtn');if(tb)tb.onclick=()=>{const r=document.documentElement;const t=r.dataset.theme==='light'?'dark':'light';r.dataset.theme=t;try{localStorage.setItem('dp_theme',t)}catch(e){}};
const sb=document.getElementById('sfxBtn');if(sb)sb.style.display='none';
</script>'''

def static_page(path, title, desc, body, extra_ld=None, og_type='website'):
    title, desc = fit_title(title), fit_desc(desc)
    nav = NAV.replace('href="#tools"', 'href="/#tools"').replace('href="#ai"', 'href="/#ai"').replace('href="#pricing"', 'href="/#pricing"').replace('href="#top"', 'href="/"')
    foot = FOOTER.replace('href="#top"', 'href="/"')
    url = SITE + path
    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
{GTAG}
{ADS}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#ff2e88">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="DoraPDF">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
{FAVICON}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;600;800&family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
{THEMEHEAD}
<link rel="stylesheet" href="/style.css">
<style>{ART_CSS}</style>
{ld(extra_ld) if extra_ld else ''}
</head><body>
{nav}
{body}
{foot}
{PAGE_JS}
</body></html>'''
    os.makedirs(f'{OUT}{path}', exist_ok=True)
    open(f'{OUT}{path}index.html', 'w').write(doc)

md = lambda s: markdown.markdown(re.sub(r'(?m)^   ([-*] )', r'    \1', s), extensions=['tables','sane_lists'])

page_urls = []
for slug, pg in PAGES.items():
    path = f'/{slug}/'
    body = f'<main class="article"><div class="crumb"><a href="/">DoraPDF</a> / {esc(pg["title"])}</div><h1>{esc(pg["title"])}</h1><div class="prose">{md(pg["md"])}</div></main>'
    static_page(path, f'{pg["title"]} | DoraPDF', pg['desc'], body)
    page_urls.append(path)

# blog
def read_min(s): return max(2, round(len(s.split()) / 220))
POST_UI = {'en': ('By the DoraPDF team', 'min read', 'Updated', 'Try the tools from this guide — free', 'Keep reading'),
           'de': ('Vom DoraPDF-Team', 'Min. Lesezeit', 'Aktualisiert', 'Die Tools aus diesem Artikel kostenlos testen', 'Weiterlesen'),
           'es': ('Por el equipo de DoraPDF', 'min de lectura', 'Actualizado', 'Prueba gratis las herramientas de esta guía', 'Sigue leyendo'),
           'fr': ("Par l'équipe DoraPDF", 'min de lecture', 'Mis à jour', 'Essayez gratuitement les outils de ce guide', 'À lire aussi'),
           'it': ('Dal team DoraPDF', 'min di lettura', 'Aggiornato', 'Prova gratis gli strumenti di questa guida', 'Continua a leggere'),
           'pt': ('Pela equipe DoraPDF', 'min de leitura', 'Atualizado', 'Experimente grátis as ferramentas deste guia', 'Continue lendo'),
           'nl': ('Door het DoraPDF-team', 'min leestijd', 'Bijgewerkt', 'Probeer de tools uit deze gids gratis', 'Verder lezen')}
def tool_link(tid, L):
    if L in TOOLS_I18N and tid in TOOLS_I18N[L]:
        v = TOOLS_I18N[L][tid]; return f'<a href="/{L}/{v[0]}/">{esc(v[3])} →</a>'
    return f'<a href="/{tid}/">{esc(BYID[tid]["name"])} →</a>'
post_urls = []
for i, p in enumerate(POSTS):
    path = f'/blog/{p["slug"]}/'
    L = p.get('lang', 'en'); PU = POST_UI.get(L, POST_UI['en'])
    tl = ''.join(tool_link(tid, L) for tid in p['tools'] if tid in BYID and not BYID[tid]['soon'])
    same = [q for q in POSTS if q['slug'] != p['slug'] and q.get('lang', 'en') == L]
    others = (same[i % 5: i % 5 + 3] or same[:3]) if len(same) >= 3 else ([q for q in POSTS if q['slug'] != p['slug']][i % 5: i % 5 + 3] or POSTS[:3])
    more = ''.join(f'<a class="pcard" href="/blog/{q["slug"]}/"><span class="tag">Guide</span><h2>{esc(q["title"])}</h2><p>{esc(q["desc"])}</p></a>' for q in others)
    body = (f'<main class="article"><div class="crumb"><a href="/">DoraPDF</a> / <a href="/blog/">Blog</a></div><h1>{esc(p["title"])}</h1>'
            f'<div class="meta">{PU[0]} · {read_min(p["md"])} {PU[1]} · {PU[2]} {p["date"]}</div>'
            f'<div class="prose">{md(p["md"])}</div>'
            f'<div class="cta-box"><h3>{PU[3]}</h3><div class="tl">{tl}</div></div>'
            f'<h2 style="font-family:Unbounded;font-size:20px;margin-top:50px">{PU[4]}</h2><div class="postgrid">{more}</div></main>')
    static_page(path, f'{p["title"]} | DoraPDF', p['desc'], body, {
        '@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': p['title'], 'description': p['desc'], 'datePublished': p['date'], 'dateModified': p['date'],
        'author': {'@type': 'Organization', 'name': 'DoraPDF'}, 'publisher': {'@type': 'Organization', 'name': 'DoraPDF', 'logo': {'@type': 'ImageObject', 'url': SITE + '/og-image.png'}},
        'mainEntityOfPage': SITE + path, 'image': SITE + '/og-image.png', 'inLanguage': L}, 'article')
    if L != 'en':
        fp = f'{OUT}{path}index.html'; _h = open(fp).read(); open(fp, 'w').write(_h.replace('<html lang="en">', f'<html lang="{L}">', 1))
    post_urls.append(path)
cards = ''.join(f'<a class="pcard" href="/blog/{p["slug"]}/"><span class="tag">{read_min(p["md"])} min read</span><h2>{esc(p["title"])}</h2><p>{esc(p["desc"])}</p></a>' for p in POSTS)
static_page('/blog/', 'Blog — PDF, Image & Student Guides | DoraPDF', 'Simple, practical guides for working with PDFs, images, documents and student life.',
            f'<main class="article" style="max-width:1100px"><div class="crumb"><a href="/">DoraPDF</a> / Blog</div><h1>Guides &amp; tips</h1><p class="meta">Practical how-tos for PDFs, images, documents and student life.</p><div class="postgrid">{cards}</div></main>')

# 404
static_page('/404-tmp/', 'Page not found | DoraPDF', 'This page does not exist.',
            '<main class="article" style="text-align:center"><h1>Page not found</h1><p class="meta">The page you are looking for has moved or never existed.</p><p><a href="/" class="btn btn-p" style="display:inline-flex">Go to DoraPDF tools ↗</a></p></main>')
shutil.move(f'{OUT}/404-tmp/index.html', f'{OUT}/404.html'); os.rmdir(f'{OUT}/404-tmp')

# ---------- copy assets ----------
for f in ['tools-pdf.js', 'tools-image.js', 'tools-text.js', 'tools-calc.js', 'tools-pro.js', 'dora.js', 'account.js', 'dora-admin.html', '_headers', 'robots.txt', 'og-image.png', 'ads.txt', 'favicon.ico', 'favicon-48.png', 'favicon-96.png', 'favicon-192.png', 'favicon-512.png', 'apple-touch-icon.png']:
    shutil.copy(f, OUT)


# ---------- /de/ and /es/ hub pages ----------
for L in LANGS:
    U = UI[L]
    cards = ''.join(f'<li><a href="/{L}/{v[0]}/">{esc(v[3])}</a> – {esc(v[4])}</li>' for x, v in TOOLS_I18N[L].items())
    body = f'<main class="article"><div class="crumb"><a href="/">DoraPDF</a> · {U["name"]}</div><h1>{esc(U["home"])}</h1><div class="prose"><p>{esc(U["home_lead"])}</p><ul>{cards}</ul><p><a href="/">English</a> · <a href="/#tools">{U["all_tools"]}</a></p></div></main>'
    static_page(f'/{L}/', f'{U["home"]} | DoraPDF', U['home_desc'], body)
    hp = f'{OUT}/{L}/index.html'
    hh = open(hp).read().replace('<html lang="en">', f'<html lang="{L}">', 1)
    open(hp, 'w').write(hh)
    loc_urls.append(f'/{L}/')

# ---------- sitemap ----------
urls = [('/', '1.0')] + [(u, '0.9') for u in tool_urls] + [('/blog/', '0.7')] + [(u, '0.7') for u in post_urls] + [(u, '0.3') for u in page_urls] + [(u, '0.8') for u in loc_urls]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{SITE}{u}</loc><lastmod>2026-11-06</lastmod><priority>{pr}</priority></url>\n' for u, pr in urls) + '</urlset>\n'
open(f'{OUT}/sitemap.xml', 'w').write(sm)
print('tools', len(tool_urls), 'posts', len(post_urls), 'pages', len(page_urls), 'urls', len(urls))

# ---------- SEO post-pass: unwrap links to pages that don't exist ----------
import glob as _g
def _exists(h):
    p = OUT + h
    return os.path.isfile(p) or os.path.isfile(os.path.join(p, 'index.html'))
_fixed = 0
for _f in _g.glob(f'{OUT}/**/*.html', recursive=True):
    _s = open(_f).read()
    _n = re.sub(r'<a href="(/[^"#?]*)"[^>]*>(.*?)</a>', lambda m: m.group(0) if m.group(1).startswith('//') or _exists(m.group(1)) else m.group(2), _s, flags=re.S)
    if _n != _s:
        open(_f, 'w').write(_n); _fixed += 1
print('unwrapped broken links in', _fixed, 'files')
