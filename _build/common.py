"""Piezas comunes del sitio Parcelas con Río (cabecera, pie, <head>, íconos).

Cada página se genera en español y en inglés. Las rutas son relativas para que
el sitio funcione igual en GitHub Pages y abriendo los archivos localmente.
"""
import html
import json
import os

DOMAIN = "https://www.parcelasconrio.cl"
WA = "56978893044"
WA_TXT = "+56 9 7889 3044"
MAIL = "contacto@parcelasconrio.cl"
IG = "https://www.instagram.com/inmobiliariaelroble.cl/"
FB = "https://www.facebook.com/Inmobiliariaelroble.cl/"
TEL = "+56978893044"
IG_SVG = '<svg aria-hidden="true" viewBox="0 0 24 24"><rect height="18" rx="5" width="18" x="3" y="3"></rect><circle cx="12" cy="12" r="4.2"></circle><circle class="social-dot" cx="17.4" cy="6.7" r="1"></circle></svg>'
FB_SVG = '<svg aria-hidden="true" viewBox="0 0 24 24"><path d="M14.2 21v-8h2.8l.4-3h-3.2V8.1c0-.9.3-1.5 1.6-1.5h1.7V3.9c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.4V10H8v3h2.8v8h3.4z"></path></svg>'

OUT = os.path.join(os.path.dirname(__file__), "..")

# Rutas equivalentes ES <-> EN (clave = id de página)
PATHS = {
    "home": ("index.html", "en/index.html"),
    "projects": ("proyectos/index.html", "en/projects/index.html"),
    "patagonia": ("patagonia/index.html", "en/patagonia/index.html"),
    "about": ("nosotros.html", "en/about.html"),
    "contact": ("contacto.html", "en/contact.html"),
    "thanks": ("gracias.html", "en/thank-you.html"),
    "blog": ("blog/index.html", "en/blog/index.html"),
    "simulator": ("simulador-credito-directo.html", "en/financing-simulator.html"),
}

NAV = [
    ("projects", "Proyectos", "Projects"),
    ("simulator", "Simulador", "Financing"),
    ("patagonia", "Patagonia", "Patagonia"),
    ("blog", "Blog", "Blog"),
    ("about", "Nosotros", "About us"),
    ("contact", "Contacto", "Contact"),
]

ICONS = {
    "wa": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21h.01c5.46 0 9.91-4.45 9.91-9.91A9.85 9.85 0 0 0 12.04 2Zm5.8 14.06c-.24.68-1.42 1.3-1.96 1.35-.5.05-.97.23-3.27-.68-2.77-1.09-4.52-3.92-4.66-4.1-.13-.18-1.1-1.47-1.1-2.8 0-1.33.7-1.99.95-2.26.24-.27.53-.34.71-.34l.51.01c.16 0 .38-.06.6.46.23.54.77 1.87.84 2 .07.14.11.3.02.48-.09.18-.13.29-.27.45-.13.16-.28.35-.4.47-.13.13-.27.28-.12.55.16.27.7 1.15 1.5 1.86 1.03.92 1.9 1.2 2.17 1.34.27.13.43.11.58-.07.16-.18.67-.78.85-1.05.18-.27.36-.22.6-.13.25.09 1.57.74 1.84.88.27.13.45.2.52.31.07.11.07.65-.17 1.33Z"/></svg>',
    "river": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" d="M2 8c2.5-2 4.5-2 7 0s4.5 2 7 0 4.5-2 6 0M2 13c2.5-2 4.5-2 7 0s4.5 2 7 0 4.5-2 6 0M2 18c2.5-2 4.5-2 7 0s4.5 2 7 0 4.5-2 6 0"/></svg>',
    "road": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" d="M6 22 10 2M18 22 14 2M12 6v2M12 12v2M12 18v2"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M5 3h10l4 4v14H5zM15 3v4h4M9 12h6M9 16h6"/></svg>',
    "key": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="15" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" d="m11 12 9-9M17 6l3 3M14 9l2 2"/></svg>',
    "plane": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M2.5 13.5 21 6l-3.5 13-5-4.5-3 3.5v-5L21 6"/></svg>',
    "tree": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M12 22v-6M12 2 5 12h4l-3 4h12l-3-4h4z"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21h3.1Z"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></svg>',
}


def esc(s):
    return html.escape(s, quote=True)


def rel(from_path, to_path):
    """Ruta relativa desde un archivo a otro dentro del sitio."""
    depth = from_path.count("/")
    return "../" * depth + to_path


def root(from_path):
    return "../" * from_path.count("/")


def pretty(path):
    """URL pública limpia (sin index.html)."""
    if path.endswith("index.html"):
        path = path[: -len("index.html")]
    return f"{DOMAIN}/{path}"


def wa_link(text):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(text, safe='')}"


def head(lang, path, alt_path, title, desc, image, schema=None, noindex=False):
    r = root(path)
    img_abs = image if image.startswith("http") else f"{DOMAIN}/{image}"
    es_p, en_p = (path, alt_path) if lang == "es" else (alt_path, path)
    ld = ""
    if schema:
        ld = '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + "</script>\n"
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large"
    return f"""<!doctype html>
<html lang="{lang}" data-root="{r}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{pretty(path)}">
<link rel="alternate" hreflang="es-CL" href="{pretty(es_p)}">
<link rel="alternate" hreflang="en" href="{pretty(en_p)}">
<link rel="alternate" hreflang="x-default" href="{pretty(es_p)}">
<meta name="theme-color" content="#141c3b">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'es_CL' if lang == 'es' else 'en_US'}">
<meta property="og:site_name" content="Parcelas con Río · Inmobiliaria El Roble">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{pretty(path)}">
<meta property="og:image" content="{img_abs}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{r}assets/img/marca/icono.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Karla:wght@400;500;700;800&display=swap">
<link rel="stylesheet" href="{r}assets/css/styles.css">
{ld}</head>
<body>
<a class="skip" href="#contenido">{'Saltar al contenido' if lang == 'es' else 'Skip to content'}</a>
"""


def header(lang, path, alt_path, current=None, solid=False):
    i = 0 if lang == "es" else 1
    links = []
    for key, es, en in NAV:
        target = rel(path, PATHS[key][i])
        cur = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="{target}"{cur}>{es if lang == "es" else en}</a>')
    home = rel(path, PATHS["home"][i])
    other = rel(path, alt_path)
    lang_label = "EN" if lang == "es" else "ES"
    lang_title = "English version" if lang == "es" else "Versión en español"
    cta_txt = "Hola, quiero información sobre las parcelas." if lang == "es" else "Hello, I would like information about the land plots."
    r = root(path)
    return f"""<header class="top{' always' if solid else ''}">
  <div class="wrap">
    <a class="brand" href="{home}" aria-label="Parcelas con Río, {'inicio' if lang == 'es' else 'home'}">
      <img class="logo-light" src="{r}assets/img/marca/logo-claro.png" width="397" height="400" alt="El Roble Inmobiliaria">
      <img class="logo-dark" src="{r}assets/img/marca/logo.png" width="397" height="400" alt="">
      <span>Parcelas con Río<small>Inmobiliaria El Roble</small></span>
    </a>
    <nav class="nav" id="nav" aria-label="{'Principal' if lang == 'es' else 'Main'}">
      {''.join(links)}
    </nav>
    <div class="top-actions">
      <a class="nav-social" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram de Inmobiliaria El Roble" data-cta="header-instagram">{IG_SVG}</a>
      <a class="nav-social" href="{FB}" target="_blank" rel="noopener" aria-label="Facebook de Inmobiliaria El Roble" data-cta="header-facebook">{FB_SVG}</a>
      <a class="nav-phone" href="tel:{TEL}" data-cta="header-telefono">{WA_TXT}</a>
      <a class="lang" href="{other}" hreflang="{'en' if lang == 'es' else 'es'}" title="{lang_title}">{lang_label}</a>
      <a class="btn btn-sun" href="{wa_link(cta_txt)}" target="_blank" rel="noopener" data-cta="header-whatsapp">{ICONS['wa']}<span>WhatsApp</span></a>
      <button class="menu-btn" id="menuBtn" aria-label="{'Abrir menú' if lang == 'es' else 'Open menu'}" aria-expanded="false" aria-controls="nav">{ICONS['menu']}</button>
    </div>
  </div>
</header>
<main id="contenido">
"""


def footer(lang, path, blog_items=()):
    i = 0 if lang == "es" else 1
    r = root(path)
    L = (lambda es, en: es if lang == "es" else en)
    nav = "".join(f'<li><a href="{rel(path, PATHS[k][i])}">{es if lang == "es" else en}</a></li>' for k, es, en in NAV)
    posts = "".join(f'<li><a href="{rel(path, p)}">{esc(t)}</a></li>' for p, t in blog_items[:5])
    return f"""</main>
<footer class="foot">
  <div class="wrap">
    <div class="grid">
      <div>
        <img src="{r}assets/img/marca/logo-claro.png" width="397" height="400" alt="El Roble Inmobiliaria" loading="lazy">
        <p>{L('Parcelas con rol propio junto a ríos del sur de Chile. Tu refugio en la Patagonia, con crédito directo.', 'Land plots with their own title next to rivers in southern Chile. Your refuge in Patagonia, with direct financing.')}</p>
        <div class="social-links"><a class="social-link" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram de Inmobiliaria El Roble" data-cta="footer-instagram">{IG_SVG}<span>Instagram</span></a><a class="social-link" href="{FB}" target="_blank" rel="noopener" aria-label="Facebook de Inmobiliaria El Roble" data-cta="footer-facebook">{FB_SVG}<span>Facebook</span></a></div>
      </div>
      <div><h4>{L('Sitio', 'Site')}</h4><ul>{nav}</ul></div>
      <div><h4>{L('Guías del blog', 'Travel guides')}</h4><ul>{posts}</ul></div>
      <div><h4>{L('Contacto', 'Contact')}</h4><ul>
        <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener" data-cta="footer-whatsapp">WhatsApp {WA_TXT}</a></li>
        <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        <li><a href="{IG}" target="_blank" rel="noopener">Instagram @inmobiliariaelroble.cl</a></li>
        <li><a href="{FB}" target="_blank" rel="noopener">Facebook Inmobiliaria El Roble</a></li>
      </ul></div>
    </div>
    <div class="bottom"><span>© 2026 Inmobiliaria El Roble · parcelasconrio.cl</span><span>{L('Algunas fotografías son referenciales del territorio.', 'Some photographs are illustrative of the region.')} <a href="{rel(path, PATHS['about'][i])}#creditos">{L('Créditos de fotos', 'Photo credits')}</a></span></div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp" data-cta="flotante-whatsapp">{ICONS['wa']}</a>
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
"""


def lead_form(lang, projects, preset="", title=None):
    L = (lambda es, en: es if lang == "es" else en)
    opts = "".join(f'<option value="{esc(p)}"{" selected" if p == preset else ""}>{esc(p)}</option>' for p in projects)
    any_opt = L("Aún no lo sé", "Not sure yet")
    return f"""<form class="lead-form" novalidate>
      <h3>{title or L('Agenda una visita o pide precios', 'Book a visit or ask for prices')}</h3>
      <input type="hidden" name="_subject" value="{L('Nueva consulta · Parcelas con Río', 'New inquiry · Parcelas con Río (EN)')}">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="_honey" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
      <input type="hidden" name="idioma" value="{lang}">
      <input type="hidden" name="simulacion" value="">
      <label>{L('Nombre', 'Name')}<input name="nombre" required autocomplete="name"></label>
      <div class="row2">
        <label>{L('Correo', 'Email')}<input name="email" type="email" required autocomplete="email"></label>
        <label>{L('Teléfono / WhatsApp', 'Phone / WhatsApp')}<input name="telefono" type="tel" required autocomplete="tel" placeholder="+56 9 ..."></label>
      </div>
      <div class="row2">
        <label>{L('Proyecto de interés', 'Project of interest')}<select name="proyecto"><option>{any_opt}</option>{opts}</select></label>
        <label>{L('País / ciudad', 'Country / city')}<input name="ciudad" autocomplete="address-level2"></label>
      </div>
      <label>{L('Mensaje', 'Message')}<textarea name="mensaje" placeholder="{L('Me gustaría visitar el terreno…', 'I would like to visit the land…')}"></textarea></label>
      <label class="consent"><input type="checkbox" name="consentimiento_contacto" value="si" required>{L('Autorizo a Inmobiliaria El Roble a contactarme por WhatsApp, correo o teléfono para responder mi consulta.', 'I authorize Inmobiliaria El Roble to contact me by WhatsApp, email or phone to answer my inquiry.')}</label>
      <label class="consent"><input type="checkbox" name="consentimiento_promociones" value="si">{L('Acepto recibir novedades, nuevos proyectos y promociones de Inmobiliaria El Roble. Esta autorización es opcional y puedo darme de baja cuando quiera.', 'I agree to receive news, new projects and offers from Inmobiliaria El Roble. This is optional and I can unsubscribe at any time.')}</label>
      <button class="btn btn-night" type="submit">{L('Enviar consulta', 'Send inquiry')}</button>
      <p class="form-status" role="status"></p>
      <p class="form-note">{L('Usamos tus datos solo para responderte. Para modificarlos o eliminarlos escribe a', 'We only use your data to reply to you. To change or delete it, write to')} <a href="mailto:{MAIL}">{MAIL}</a>.</p>
    </form>"""


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)
