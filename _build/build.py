"""Genera el sitio estático de Parcelas con Río en español e inglés.

Uso:  python3 _build/build.py
"""
import json
from urllib.parse import quote
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import (DOMAIN, FB, FB_SVG, ICONS, IG, IG_SVG, MAIL, PATHS, WA, WA_TXT, esc, footer,  # noqa: E402
                  head, header, lead_form, pretty, rel, root, wa_link, write)
from data import IMG, MANIHUALES_LOTS, PROJECTS, SIMULATOR, VIDEOS  # noqa: E402
from articles import ARTICLES  # noqa: E402

LANGS = ("es", "en")
SITEMAP = []


def L(lang, es, en):
    return es if lang == "es" else en


def img(path, key, lang, cls="", eager=False, w=1200, h=800):
    m = IMG[key]
    alt = m.get(f"alt_{lang}", "")
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    w, h = m.get("w", w), m.get("h", h)
    return f'<img{c} src="{root(path)}{m["src"]}" width="{w}" height="{h}" alt="{esc(alt)}" {load} decoding="async">'


def credit(key, lang):
    c = IMG[key].get("credit")
    if not c:
        return ""
    return f'<span class="photo-credit">{L(lang, "Foto", "Photo")}: {c}</span>'


def proj_path(p, lang):
    return f"proyectos/{p['slug']}.html" if lang == "es" else f"en/projects/{p['slug']}.html"


def art_path(a, lang):
    return f"blog/{a['slug_es']}.html" if lang == "es" else f"en/blog/{a['slug_en']}.html"


def blog_items(lang):
    return [(art_path(a, lang), a[f"title_{lang}"]) for a in ARTICLES]


def page(lang, key_or_paths, title, desc, image, body, current=None, solid=False, schema=None, noindex=False):
    if isinstance(key_or_paths, str):
        es_p, en_p = PATHS[key_or_paths]
    else:
        es_p, en_p = key_or_paths
    path, alt = (es_p, en_p) if lang == "es" else (en_p, es_p)
    html = head(lang, path, alt, title, desc, image, schema, noindex) + header(lang, path, alt, current, solid) + body(path) + footer(lang, path, blog_items(lang))
    write(path, html)
    if not noindex:
        SITEMAP.append((es_p, en_p, path))


def project_cards(path, lang, only_available=False):
    out = []
    for p in PROJECTS:
        if only_available and p["sold"]:
            continue
        badge_cls = "badge sold" if p["sold"] else "badge"
        inner = f"""<figure>{img(path, p['img'], lang)}<span class="{badge_cls}">{p['badge_' + lang]}</span>{'' if p.get('real') else '<span class="ref">' + L(lang, 'Imagen referencial', 'Illustrative image') + '</span>'}</figure>
      <div class="body">
        <span class="region">{p['region_' + lang]}</span>
        <h3>{p['name']}</h3>
        <p>{p['short_' + lang]}</p>
        <div class="bar" aria-hidden="true"><i style="width:{p['pct']}%"></i></div>
        <div class="meta"><span>{p['status_' + lang]}</span>{'<span>' + L(lang, 'Ver proyecto', 'View project') + ' →</span>' if p['detail'] else ''}</div>
      </div>"""
        if p["detail"]:
            out.append(f'<a class="pcard reveal" data-r="{p["r"]}" href="{rel(path, proj_path(p, lang))}">{inner}</a>')
        else:
            out.append(f'<article class="pcard is-sold reveal" data-r="{p["r"]}">{inner}</article>')
    return "\n    ".join(out)


def post_cards(path, lang, items):
    out = []
    for a in items:
        out.append(f"""<a class="post reveal" href="{rel(path, art_path(a, lang))}">
      <figure>{img(path, a['img'], lang)}</figure>
      <div class="body"><small>{a['cat_' + lang]}</small><h3>{esc(a['title_' + lang])}</h3><p>{esc(a['desc_' + lang])}</p><span class="more">{L(lang, 'Leer guía', 'Read guide')} →</span></div>
    </a>""")
    return "\n    ".join(out)


def tiles(path, lang):
    by = {a["key"]: a for a in ARTICLES}
    spec = [("marmol", "w2 h2"), ("castillo", ""), ("pesca", ""), ("ski", "w2"), ("carretera", "w2"), ("aeropuerto", "w2")]
    out = []
    for k, cls in spec:
        a = by[k]
        out.append(f"""<a class="tile reveal {cls}" href="{rel(path, art_path(a, lang))}">{img(path, a['img'], lang)}{('<span class="credit">' + re.sub(r'<[^>]+>', '', IMG[a['img']]['credit']) + '</span>') if IMG[a['img']].get('credit') else ''}
      <div class="in"><small>{a['cat_' + lang]}</small><h3>{a['tile_' + lang]}</h3><p>{a['tilep_' + lang]}</p></div></a>""")
    return "\n    ".join(out)


PROJECT_NAMES = [p["name"] for p in PROJECTS if not p["sold"]]


# ---------------------------------------------------------------- Portada
def home(lang):
    def body(path):
        r = root(path)
        return f"""<section class="hero" data-hero-video>
  <div class="hero-media" aria-hidden="true">
    <video class="is-active" muted playsinline loop autoplay preload="auto" poster="{r}assets/img/bienvenida/home-v2-poster-1280.jpg" data-desktop="{r}assets/video/bienvenida/manihuales-home-v2-1280.mp4" data-mobile="{r}assets/video/bienvenida/manihuales-home-v2-960.mp4" data-poster-mobile="{r}assets/img/bienvenida/home-v2-poster-960.jpg"></video>
  </div>
  <div class="wrap">
    <span class="eyebrow light">{L(lang, 'Patagonia chilena · Sur de Chile', 'Chilean Patagonia · Southern Chile')}</span>
    <h1>{L(lang, 'Tu refugio junto al <em>río</em>, en el fin del mundo', 'Your riverside <em>refuge</em> at the end of the world')}</h1>
    <p class="lead">{L(lang, 'Parcelas frente a ríos de Aysén y del sur de Chile. Bosques, ríos de pesca, lagos y nieve a tu alcance, con crédito directo y asesoría legal.', 'Land plots facing rivers in Aysén and southern Chile. Forests, fishing rivers, lakes and snow within reach, with direct financing and legal support.')}</p>
    <div class="hero-ctas">
      <a class="btn btn-sun" href="{rel(path, PATHS['projects'][0 if lang == 'es' else 1])}" data-cta="home-hero-proyectos">{L(lang, 'Ver parcelas disponibles', 'See available plots')}</a>
      <a class="btn btn-ghost" href="{rel(path, PATHS['patagonia'][0 if lang == 'es' else 1])}" data-cta="home-hero-patagonia">{L(lang, 'Descubrir la Patagonia', 'Discover Patagonia')}</a>
    </div>
    <div class="hero-meta">
      <div><b>6</b><span>{L(lang, 'proyectos', 'projects')}</span></div>
      <div><b>3</b><span>{L(lang, 'regiones del sur', 'southern regions')}</span></div>
      <div><b>{L(lang, 'Asesoría', 'Legal')}</b><span>{L(lang, 'legal en la compra', 'support')}</span></div>
      <div><b>{L(lang, 'Crédito', 'Direct')}</b><span>{L(lang, 'directo', 'financing')}</span></div>
    </div>
  </div>
  <span class="season-tag">{L(lang, 'Horizontes de Mañihuales · Región de Aysén', 'Horizontes de Mañihuales · Aysén Region')}</span>
</section>

<section class="statement">
  <div class="wrap grid">
    <p class="big reveal">{L(lang, 'Despertar con el sonido del río, pescar truchas al atardecer y ver nevar desde tu ventana. <em>La Patagonia no se visita: se vive.</em>', 'Wake up to the sound of the river, fish for trout at sunset and watch the snow fall from your window. <em>Patagonia is not just visited: it is lived.</em>')}</p>
    <div class="side reveal">
      <p>{L(lang, 'En Inmobiliaria El Roble elegimos terrenos con agua, acceso y naturaleza intacta, y te acompañamos hasta la escritura. Para tu casa, tu cabaña de fin de semana o tu inversión.', 'At Inmobiliaria El Roble we choose land with water, access and untouched nature, and we guide you all the way to the deed. For your home, your weekend cabin or your investment.')}</p>
      <a class="link-arrow" href="{rel(path, PATHS['about'][0 if lang == 'es' else 1])}">{L(lang, 'Conoce cómo trabajamos', 'How we work')} {ICONS['arrow']}</a>
    </div>
  </div>
</section>

<section id="proyectos">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{L(lang, 'Proyectos en venta', 'Projects for sale')}</span>
      <h2>{L(lang, 'Parcelas frente al agua, con todo en regla', 'Waterfront plots, with everything in order')}</h2>
      <p class="lead">{L(lang, 'Proyectos en las regiones de Aysén, Los Ríos y el Maule, con asesoría legal durante todo el proceso de compra.', 'Projects in the Aysén, Los Ríos and Maule regions, with legal support throughout the purchase.')}</p>
    </div>
    <div class="projects">
    {project_cards(path, lang)}
    </div>
  </div>
</section>

<section class="experiences">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow light">{L(lang, 'Vivir la Patagonia', 'Live Patagonia')}</span>
      <h2>{L(lang, 'Todo esto te espera en Aysén', 'All of this awaits you in Aysén')}</h2>
      <p class="lead">{L(lang, 'Aysén es uno de los destinos naturales más impresionantes del planeta. Estas son algunas de las experiencias que puedes vivir en la región.', 'Aysén is one of the most stunning natural destinations on the planet. These are some of the experiences you can enjoy in the region.')}</p>
    </div>
    <div class="mosaic">
    {tiles(path, lang)}
    </div>
  </div>
</section>

{near_section(path, lang)}

<section class="band">
  {img(path, 'lengas', lang)}
  <div class="wrap">
    <span class="eyebrow light">{L(lang, 'Crédito directo sin interés', 'Interest-free direct financing')}</span>
    <h2>{L(lang, 'Tu parcela en la Patagonia, sin pasar por el banco', 'Your plot in Patagonia, no bank required')}</h2>
    <p>{L(lang, 'Pago al contado, crédito bancario o crédito directo con la inmobiliaria, con asesoría legal durante todo el proceso.', 'Cash, bank loan or direct financing with the developer, with legal support throughout the process.')}</p>
    <div class="hero-ctas">
      <a class="btn btn-sun" href="{wa_link(L(lang, 'Hola, quiero conocer las opciones de crédito directo para una parcela.', 'Hello, I would like to know the direct financing options for a plot.'))}" target="_blank" rel="noopener" data-cta="home-credito-whatsapp">{ICONS['wa']}{L(lang, 'Consultar financiamiento', 'Ask about financing')}</a>
      <a class="btn btn-ghost" href="{rel(path, PATHS['simulator'][0 if lang == 'es' else 1])}" data-cta="home-credito-simulador">{L(lang, 'Simular mi crédito', 'Simulate my financing')}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{L(lang, 'Guías para viajar y vivir en la Patagonia', 'Guides to travel and live in Patagonia')}</span>
      <h2>{L(lang, 'Del blog', 'From the blog')}</h2>
    </div>
    <div class="posts">
    {post_cards(path, lang, ARTICLES[:3])}
    </div>
    <p style="margin-top:34px"><a class="link-arrow" href="{rel(path, PATHS['blog'][0 if lang == 'es' else 1])}">{L(lang, 'Ver todas las guías', 'See all guides')} {ICONS['arrow']}</a></p>
  </div>
</section>

{contact_section(path, lang)}
"""
    schema = {"@context": "https://schema.org", "@type": "RealEstateAgent", "name": "Inmobiliaria El Roble · Parcelas con Río",
              "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/marca/logo.png", "telephone": "+" + WA, "email": MAIL,
              "areaServed": ["Región de Aysén", "Región de Los Ríos", "Región del Maule"], "sameAs": [IG, FB]}
    page(lang, "home",
         L(lang, "Parcelas con Río · Parcelas en la Patagonia con crédito directo", "Parcelas con Río · Land for sale in Chilean Patagonia"),
         L(lang, "Parcelas frente a ríos en Aysén, Los Ríos y el Maule. Tu refugio en la Patagonia chilena, con crédito directo y asesoría legal.",
           "Riverside land plots in Aysén, Los Ríos and Maule. Your refuge in Chilean Patagonia, with direct financing and legal support."),
         IMG["coyhaique"]["src"], body, schema=schema)


def near_section(path, lang):
    by = {a["key"]: a for a in ARTICLES}
    items = by["aeropuerto"]["near"] if "near" in by["aeropuerto"] else []
    cells = "".join(f'<div class="near-item reveal"><b>{n[0]}</b><span>{n[1 if lang == "es" else 2]}</span><p>{n[3 if lang == "es" else 4]}</p></div>' for n in items)
    if not cells:
        return ""
    return f"""<section class="near">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{L(lang, 'Conectividad', 'Getting there')}</span>
      <h2>{L(lang, 'Más cerca de lo que imaginas', 'Closer than you think')}</h2>
    </div>
    <div class="near-grid">{cells}</div>
  </div>
</section>"""


def contact_section(path, lang, preset=""):
    return f"""<section class="contact" id="contacto">
  <div class="wrap">
    <div>
      <span class="eyebrow">{L(lang, 'Contacto', 'Contact')}</span>
      <h2 style="font-size:clamp(2rem,4vw,3rem)">{L(lang, 'Ven a conocer tu parcela', 'Come and see your plot')}</h2>
      <p class="lead" style="margin-top:16px">{L(lang, 'Déjanos tus datos y te enviamos precios, planos y disponibilidad. Coordinamos visitas al terreno.', 'Leave your details and we will send you prices, plans and availability. We arrange site visits.')}</p>
      <div class="contact-list">
        <div><span>WhatsApp</span><a href="https://wa.me/{WA}" target="_blank" rel="noopener" data-cta="contacto-whatsapp">{WA_TXT}</a></div>
        <div><span>{L(lang, 'Correo', 'Email')}</span><a href="mailto:{MAIL}">{MAIL}</a></div>
      </div>
      <div class="contact-social">
        <span>{L(lang, 'También puedes seguirnos en', 'You can also follow us on')}</span>
        <div class="social-links" aria-label="{L(lang, 'Redes sociales', 'Social media')}"><a class="social-link" href="{IG}" target="_blank" rel="noopener" aria-label="Instagram de Inmobiliaria El Roble" data-cta="contacto-instagram">{IG_SVG}<span>Instagram</span></a><a class="social-link" href="{FB}" target="_blank" rel="noopener" aria-label="Facebook de Inmobiliaria El Roble" data-cta="contacto-facebook">{FB_SVG}<span>Facebook</span></a></div>
      </div>
    </div>
    {lead_form(lang, PROJECT_NAMES, preset)}
  </div>
</section>"""


# ---------------------------------------------------------------- Proyectos
def projects_index(lang):
    def body(path):
        return f"""<section class="page-hero">
  {img(path, 'lago_reflejo', lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span>{L(lang, 'Proyectos', 'Projects')}</nav>
    <h1>{L(lang, 'Parcelas en venta en el sur de Chile', 'Land for sale in southern Chile')}</h1>
    <p class="lead">{L(lang, 'Elige tu lugar: Patagonia de Aysén, la selva valdiviana de Los Ríos o el valle del Maule.', 'Choose your place: Aysén Patagonia, the Valdivian forest of Los Ríos or the Maule valley.')}</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="filters" role="group" aria-label="{L(lang, 'Filtrar por región', 'Filter by region')}">
      <button class="chip on" type="button" data-r="all">{L(lang, 'Todas', 'All')}</button>
      <button class="chip" type="button" data-r="XI">{L(lang, 'Aysén', 'Aysén')}</button>
      <button class="chip" type="button" data-r="XIV">{L(lang, 'Los Ríos', 'Los Ríos')}</button>
      <button class="chip" type="button" data-r="VII">{L(lang, 'Maule', 'Maule')}</button>
    </div>
    <div class="projects">
    {project_cards(path, lang)}
    </div>
  </div>
</section>
{attrs_section(path, lang)}
{contact_section(path, lang)}"""
    page(lang, "projects", L(lang, "Proyectos de parcelas en Aysén, Los Ríos y Maule | Parcelas con Río", "Land projects in Aysén, Los Ríos and Maule | Parcelas con Río"),
         L(lang, "Parcelas frente a ríos en la Patagonia (Aysén), Los Ríos y el Maule. Disponibilidad, superficies, precios y formas de pago.",
           "Plots next to rivers in Patagonia (Aysén), Los Ríos and Maule. Availability, sizes, prices and payment options."),
         IMG["lago_reflejo"]["src"], body, current="projects")


def attrs_section(path, lang, p=None):
    if p and p.get("river_es"):
        primero = ("river", p["river_" + lang], L(lang, "Un proyecto junto al río, en el paisaje natural de la Patagonia.", "A riverside project in Patagonia's natural landscape."))
    else:
        primero = ("tree", L(lang, "Entornos naturales elegidos con cuidado", "Carefully chosen natural settings"),
                   L(lang, "Parcelaciones en paisajes de campo y junto a ríos, en distintos lugares de Chile.", "Subdivisions in countryside landscapes and next to rivers, in different parts of Chile."))
    items = [
        primero,
        ("road", L(lang, "Acceso", "Access"), L(lang, "Caminos y servidumbres de tránsito hasta cada lote.", "Roads and rights-of-way to every lot.")),
        ("doc", L(lang, "Asesoría legal", "Legal support"), L(lang, "Te guiamos y asesoramos legalmente en la compra, con nuestro staff de abogados.", "We guide and advise you legally throughout the purchase, with our team of lawyers.")),
        ("key", L(lang, "Crédito directo", "Direct financing"), L(lang, "Financiamiento directo con la inmobiliaria, sin pasar por el banco.", "Direct financing with the developer, no bank needed.")),
    ]
    cells = "".join(f'<div class="attr reveal"><span class="ic">{ICONS[i]}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in items)
    return f"""<section style="background:var(--cream)">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Por qué El Roble', 'Why El Roble')}</span><h2>{L(lang, 'Comprar tranquilo, desde el primer día', 'Buy with peace of mind from day one')}</h2></div>
    <div class="attrs">{cells}</div>
  </div>
</section>"""


def money(n, lang):
    return "$" + f"{n:,}".replace(",", "." if lang == "es" else ",")


def map_section(path, p, lang):
    if not p.get("map"):
        return ""
    lat, lng = p["map"]
    src = f"https://maps.google.com/maps?q={lat},{lng}&z=15&t=k&output=embed"
    link = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
    return f"""<section class="map-sec">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Ubicación', 'Location')}</span><h2>{L(lang, 'Dónde está', 'Where it is')}</h2></div>
    <div class="map-box"><iframe src="{src}" title="{L(lang, 'Mapa de ubicación de', 'Location map of')} {esc(p['name'])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    <p class="map-link"><a class="link-arrow" href="{link}" target="_blank" rel="noopener">{L(lang, 'Abrir en Google Maps', 'Open in Google Maps')} {ICONS['arrow']}</a></p>
  </div>
</section>"""


def manihuales_section(path, lang):
    rows = "".join(
        f"""<tr class="{'res' if res else ''}"><th scope="row">{L(lang, 'Parcela', 'Plot')} {n}</th><td>{tot}</td><td>{serv}</td><td>{util}</td><td><b>{money(price, lang)}</b></td><td><span class="pill {'res' if res else 'ok'}">{L(lang, 'Reservada', 'Reserved') if res else L(lang, 'Disponible', 'Available')}</span></td></tr>"""
        for n, tot, serv, util, price, res in MANIHUALES_LOTS)
    head = "".join(f"<th scope=\"col\">{h}</th>" for h in [L(lang, 'Parcela', 'Plot'), L(lang, 'Superficie total', 'Total area'), L(lang, 'Servidumbre', 'Right-of-way'), L(lang, 'Superficie útil', 'Usable area'), L(lang, 'Precio', 'Price'), L(lang, 'Estado', 'Status')])
    return f"""<section class="split">
  <div class="wrap">
    <figure>{img(path, 'plano_manihuales', lang, cls='plan')}<figcaption>{L(lang, 'Plano referencial del loteo.', 'Reference subdivision plan.')}</figcaption></figure>
    <div>
      <span class="eyebrow">{L(lang, 'El terreno', 'The land')}</span>
      <h2>{L(lang, 'Cuatro parcelas frente al río Mañihuales', 'Four plots facing the Mañihuales River')}</h2>
      <ul class="ticks">
        <li>{L(lang, 'Acceso por camino público, frente al río Mañihuales.', 'Public road access, facing the Mañihuales River.')}</li>
        <li>{L(lang, 'Hermosos árboles nativos y un entorno natural de gran belleza.', 'Beautiful native trees and stunning natural surroundings.')}</li>
        <li>{L(lang, 'A 1 hora y 10 minutos al norte de Coyhaique y a 10 minutos de Villa Mañihuales.', '1 hour 10 minutes north of Coyhaique and 10 minutes from Villa Mañihuales.')}</li>
        <li>{L(lang, 'En venta en verde mientras se obtiene la aprobación del SAG.', 'Sold off-plan while SAG approval is obtained.')}</li>
      </ul>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Parcelas y precios', 'Plots and prices')}</span><h2>{L(lang, 'Elige tu parcela', 'Choose your plot')}</h2></div>
    <div class="table-scroll"><table class="lots-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
    <div class="pay">
      <h3>{L(lang, 'Formas de pago', 'Payment options')}</h3>
      <ul class="pay-list">
        <li><b>{L(lang, 'Contado', 'Cash')}</b></li>
        <li><b>{L(lang, 'Crédito bancario', 'Bank loan')}</b></li>
        <li><b>{L(lang, 'Crédito directo', 'Direct financing')}</b><span>{L(lang, '50% de pie y saldo en 24 cuotas expresadas en UF, sin intereses.', '50% down and the balance in 24 instalments set in UF, with no interest.')}</span></li>
      </ul>
      <a class="btn btn-night" href="{rel(path, PATHS['simulator'][0 if lang == 'es' else 1])}?proyecto=Horizontes+de+Ma%C3%B1ihuales" data-cta="manihuales-simulador">{L(lang, 'Simular crédito directo', 'Simulate direct financing')}</a>
    </div>
  </div>
</section>"""


FACTS = {
    "sag": ("doc", ("Subdivisión aprobada por el SAG", "Subdivision approved by the SAG"), ("La subdivisión cuenta con aprobación del Servicio Agrícola y Ganadero.", "The subdivision is approved by the Agricultural and Livestock Service (SAG).")),
    "rol": ("key", ("Rol propio", "Own property roll"), ("Cada parcela tiene rol propio.", "Each plot has its own property roll number.")),
    "luz": ("bolt", ("Empalme eléctrico previsto", "Planned electricity connection"), ("El proyecto contempla un empalme eléctrico para cada parcela.", "The project includes an electricity connection for each plot.")),
}


def facts_block(p, lang):
    if not p.get("facts"):
        return ""
    cells = "".join(f'<div class="fact"><span class="ic">{ICONS[FACTS[k][0]]}</span><div><b>{L(lang, *FACTS[k][1])}</b><span>{L(lang, *FACTS[k][2])}</span></div></div>' for k in p["facts"])
    return f"""<div class="facts-box"><span class="eyebrow">{L(lang, 'Antecedentes', 'Key facts')}</span><div class="facts">{cells}</div></div>"""


def project_links(path, p, lang, simular=False):
    out = []
    if p.get("directions"):
        out.append(f'<a class="btn btn-night" href="{p["directions"]}" target="_blank" rel="noopener" data-cta="{p["slug"]}-como-llegar">{L(lang, "Cómo llegar", "Get directions")} {ICONS["arrow"]}</a>')
    if p.get("masterplan"):
        out.append(f'<a class="btn btn-line" href="{p["masterplan"]}" target="_blank" rel="noopener" data-cta="{p["slug"]}-masterplan">{L(lang, "Ver Masterplan 360°", "View 360° Masterplan")}</a>')
    if simular:
        out.append(f'<a class="btn btn-line" href="{rel(path, PATHS["simulator"][0 if lang == "es" else 1])}?proyecto={quote(SIM_KEY.get(p["slug"], p["name"]))}" data-cta="{p["slug"]}-simulador">{L(lang, "Simular crédito directo", "Simulate direct financing")}</a>')
    return f'<p class="proj-links">{"".join(out)}</p>' if out else ""


SIM_KEY = {"horizontes-de-manihuales": "Horizontes de Mañihuales", "dona-cecilia": "San Clemente · Parcelación Doña Cecilia"}


def dona_cecilia_section(path, p, lang):
    full = root(path) + IMG["plano_dc_disponibles"]["src"]
    lotes = root(path) + IMG["plano_dc_lotes"]["src"]
    movil = IMG["plano_dc_disponibles_movil"]
    return f"""<section style="padding-top:0">
  <div class="wrap">
    <div class="avail">
      <div><b>6</b><span>{L(lang, 'parcelas disponibles de 18', 'plots available out of 18')}</span></div>
      <div><b>5.000 m²</b><span>{L(lang, 'cada parcela disponible', 'each available plot')}</span></div>
      <div><b>{money(19500000, lang)}</b><span>{L(lang, 'precio al contado (lista: ' + money(21000000, lang) + ')', 'cash price (list price: ' + money(21000000, lang) + ')')}</span></div>
    </div>
    {project_links(path, p, lang, simular=True)}
    {facts_block(p, lang)}
  </div>
</section>
<section class="plan-sec">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Planos', 'Plans')}</span><h2>{L(lang, 'Elige tu parcela en el plano', 'Choose your plot on the plan')}</h2>
      <p class="lead">{L(lang, 'Disponibles en verde: parcelas 6, 8, 14, 15, 16 y 17, todas de 5.000 m². En rojo, las vendidas; en azul, la reservada.', 'Available in green: plots 6, 8, 14, 15, 16 and 17, all 5,000 m². Sold plots in red; reserved in blue.')}</p></div>
    <figure class="plan-wide">
      <a href="{full}" target="_blank" rel="noopener" aria-label="{L(lang, 'Abrir el plano de disponibilidad en tamaño completo', 'Open the availability plan at full size')}"><picture><source media="(max-width: 720px)" srcset="{root(path)}{movil['src']}" width="{movil['w']}" height="{movil['h']}">{img(path, 'plano_dc_disponibles', lang)}</picture></a>
      <figcaption><span class="leyenda"><i class="ok"></i>{L(lang, 'Disponible', 'Available')}</span><span class="leyenda"><i class="res"></i>{L(lang, 'Reservada', 'Reserved')}</span><span class="leyenda"><i class="sold"></i>{L(lang, 'Vendida', 'Sold')}</span>
        <a class="link-arrow" href="{full}" target="_blank" rel="noopener">{L(lang, 'Ver en tamaño completo', 'View full size')} {ICONS['arrow']}</a></figcaption>
    </figure>
    <figure class="plan-wide" style="margin-top:34px">
      <a href="{lotes}" target="_blank" rel="noopener" aria-label="{L(lang, 'Abrir el plano general en tamaño completo', 'Open the general plan at full size')}">{img(path, 'plano_dc_lotes', lang)}</a>
      <figcaption>{L(lang, 'Plano general de la subdivisión: deslindes, camino interior, canales y superficie de cada lote (0,50 ha = 5.000 m²).', 'General subdivision plan: boundaries, internal road, canals and the area of each lot (0.50 ha = 5,000 m²).')}
        <a class="link-arrow" href="{lotes}" target="_blank" rel="noopener">{L(lang, 'Ver en tamaño completo', 'View full size')} {ICONS['arrow']}</a></figcaption>
    </figure>
  </div>
</section>"""


def rofuco_section(path, p, lang):
    return f"""<section style="padding-top:0">
  <div class="wrap">
    <div class="avail">
      <div><b>38 / 60</b><span>{L(lang, 'parcelas vendidas (aprox. 63%)', 'plots sold (approx. 63%)')}</span></div>
      <div><b>22</b><span>{L(lang, 'parcelas disponibles (aprox. 37%)', 'plots available (approx. 37%)')}</span></div>
      <div><b>{money(24500000, lang)} – {money(28000000, lang)}</b><span>{L(lang, 'precios; consúltalos por WhatsApp o formulario', 'prices; ask on WhatsApp or via the form')}</span></div>
    </div>
    {project_links(path, p, lang)}
    {facts_block(p, lang)}
  </div>
</section>"""


def project_page(p, lang):
    es_p, en_p = proj_path(p, "es"), proj_path(p, "en")

    def body(path):
        extra = ""
        if p["slug"] == "horizontes-de-manihuales":
            extra = manihuales_section(path, lang)
        elif p["slug"] == "rofuco-bajo":
            extra = rofuco_section(path, p, lang)
        elif p["slug"] == "dona-cecilia":
            extra = dona_cecilia_section(path, p, lang)
        if p.get("plan"):
            extra += f"""<section class="plan-sec">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Plano del proyecto', 'Project plan')}</span><h2>{L(lang, 'Queda una sola parcela: la B11', 'One plot left: B11')}</h2>
      <p class="lead">{L(lang, 'En rojo, las parcelas vendidas; en blanco, la B11, de 9.500 m², única disponible.', 'Sold plots in red; B11, 9,500 m², the only one available, in white.')}</p></div>
    <figure class="plan-wide">{img(path, p['plan'], lang)}</figure>
  </div>
</section>"""
        sim_btn = ""
        if p.get("sim"):
            sim_btn = f"""<a class="btn btn-ghost" href="{rel(path, PATHS['simulator'][0 if lang == 'es' else 1])}?proyecto={quote(SIM_KEY.get(p['slug'], p['name']))}" data-cta="proyecto-{p['slug']}-simulador">{L(lang, 'Simular crédito', 'Simulate financing')}</a>"""
        else:
            sim_btn = f"""<a class="btn btn-ghost" href="#contacto">{L(lang, 'Agendar visita', 'Book a visit')}</a>"""
        story = PROJECT_STORY.get(p["slug"], {}).get(lang, "")
        return f"""<section class="page-hero">
  {img(path, p['img'], lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span><a href="{rel(path, PATHS['projects'][0 if lang == 'es' else 1])}">{L(lang, 'Proyectos', 'Projects')}</a><span>/</span>{p['name']}</nav>
    <span class="eyebrow light">{p['region_' + lang]} · {p['status_' + lang]}</span>
    <h1>{p['name']}</h1>
    <p class="lead">{p['short_' + lang]}</p>
    <div class="hero-ctas">
      <a class="btn btn-sun" href="{wa_link(L(lang, 'Hola, me interesa ' + p['name'] + '. ¿Me envían precios y disponibilidad?', 'Hello, I am interested in ' + p['name'] + '. Could you send me prices and availability?'))}" target="_blank" rel="noopener" data-cta="proyecto-{p['slug']}-whatsapp">{ICONS['wa']}{L(lang, 'Pedir precios', 'Ask for prices')}</a>
      {sim_btn}
    </div>
  </div>
  {'' if p.get('real') else '<span class="photo-credit">' + L(lang, 'Imagen referencial del territorio', 'Illustrative image of the region') + '</span>'}
</section>
{story}
{extra}
{gallery_section(path, p, lang)}
{map_section(path, p, lang)}
{attrs_section(path, lang, p)}
{contact_section(path, lang, p['name'])}"""
    page(lang, (es_p, en_p), f"{p['name']} · {L(lang, 'Parcelas en venta', 'Land for sale')} | Parcelas con Río",
         f"{p['short_' + lang]} {L(lang, 'Consulta precios y formas de pago.', 'Ask for prices and payment options.')}",
         IMG[p["img"]]["src"], body, current="projects")


def gallery_section(path, p, lang):
    if not p.get("gallery"):
        return ""
    figs = "".join(f'<figure class="g-item reveal">{img(path, k, lang)}</figure>' for k in p["gallery"])
    video = ""
    if p.get("video"):
        poster = root(path) + IMG[p["gallery"][0]]["src"]
        video = f"""<figure class="g-video reveal"><video controls playsinline preload="none" poster="{poster}" src="{root(path)}{p['video']}"></video><figcaption>{L(lang, 'Video del proyecto', 'Project video')}</figcaption></figure>"""
    extra = ""
    if p.get("gallery2"):
        figs2 = "".join(f'<figure class="g-item reveal">{img(path, k, lang)}</figure>' for k in p["gallery2"])
        extra = f"""<div class="section-head" style="margin:56px 0 24px"><span class="eyebrow">{L(lang, 'Entorno', 'Surroundings')}</span><h3 style="font-size:1.8rem">{L(lang, 'Paisajes de la Región del Maule', 'Landscapes of the Maule Region')}</h3></div>
    <div class="gallery g3">{figs2}</div>"""
    return f"""<section class="gallery-sec">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Galería', 'Gallery')}</span><h2>{L(lang, 'Así es el proyecto', 'See the project')}</h2></div>
    <div class="gallery{' with-video' if video else ''}">{video}{figs}</div>
    {extra}
  </div>
</section>"""


PROJECT_STORY = {}  # se completa en content.py


# ---------------------------------------------------------------- Otras páginas
def thanks(lang):
    def body(path):
        return f"""<section class="page-hero" style="min-height:80svh">
  {img(path, 'lago_reflejo', lang, eager=True)}
  <div class="wrap">
    <span class="eyebrow light">{L(lang, '¡Gracias!', 'Thank you!')}</span>
    <h1>{L(lang, 'Recibimos tu consulta', 'We received your inquiry')}</h1>
    <p class="lead">{L(lang, 'Te contactaremos pronto. Si quieres avanzar más rápido, escríbenos por WhatsApp.', 'We will get back to you soon. For a faster reply, write to us on WhatsApp.')}</p>
    <div class="hero-ctas"><a class="btn btn-sun" href="https://wa.me/{WA}" target="_blank" rel="noopener">{ICONS['wa']}WhatsApp</a><a class="btn btn-ghost" href="{rel(path, PATHS['blog'][0 if lang == 'es' else 1])}">{L(lang, 'Leer guías de la Patagonia', 'Read Patagonia guides')}</a></div>
  </div>
</section>"""
    page(lang, "thanks", L(lang, "Gracias | Parcelas con Río", "Thank you | Parcelas con Río"), L(lang, "Recibimos tu consulta.", "We received your inquiry."), IMG["lago_reflejo"]["src"], body, noindex=True)


def blog_index(lang):
    def body(path):
        return f"""<section class="page-hero">
  {img(path, 'carretera', lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span>Blog</nav>
    <span class="eyebrow light">{L(lang, 'Guías de viaje y vida en la Patagonia', 'Travel and living guides to Patagonia')}</span>
    <h1>{L(lang, 'Descubre Aysén antes de llegar', 'Discover Aysén before you arrive')}</h1>
    <p class="lead">{L(lang, 'Cómo llegar, qué ver, dónde pescar, esquiar o caminar, y qué saber para tener tu propio refugio en la Patagonia chilena.', 'How to get there, what to see, where to fish, ski or hike, and what to know to own your refuge in Chilean Patagonia.')}</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="posts all">
    {post_cards(path, lang, ARTICLES)}
    </div>
  </div>
</section>"""
    page(lang, "blog", L(lang, "Blog: guías para viajar y vivir en la Patagonia chilena | Parcelas con Río", "Blog: guides to travel and live in Chilean Patagonia | Parcelas con Río"),
         L(lang, "Guías prácticas de Aysén: cómo llegar a Coyhaique, Catedrales de Mármol, Carretera Austral, pesca con mosca, ski, trekking y cómo comprar una parcela.",
           "Practical Aysén guides: getting to Coyhaique, the Marble Caves, Carretera Austral, fly fishing, skiing, trekking and how to buy land in Patagonia."),
         IMG["carretera"]["src"], body, current="blog")


def article(a, lang):
    es_p, en_p = art_path(a, "es"), art_path(a, "en")

    def body(path):
        toc = "".join(f'<li><a href="#{hid}">{esc(t)}</a></li>' for hid, t in a.get(f"toc_{lang}", []))
        related = [x for x in ARTICLES if x is not a][:3]
        return f"""<section class="page-hero">
  {img(path, a['img'], lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span><a href="{rel(path, PATHS['blog'][0 if lang == 'es' else 1])}">Blog</a></nav>
    <span class="eyebrow light">{a['cat_' + lang]}</span>
    <h1>{esc(a['title_' + lang])}</h1>
    <p class="lead">{esc(a['desc_' + lang])}</p>
    <div class="article-meta"><span>{L(lang, 'Actualizado', 'Updated')}: {a['updated']}</span><span>{a.get('read', 8)} {L(lang, 'min de lectura', 'min read')}</span></div>
  </div>
  {credit(a['img'], lang)}
</section>
<section class="article">
  <div class="wrap">
    <article class="prose">
{a['body_' + lang]}
    </article>
    <aside class="aside">
      {'<nav class="toc"><h4>' + L(lang, 'En esta guía', 'In this guide') + '</h4><ol>' + toc + '</ol></nav>' if toc else ''}
      <div class="box">
        <h3>{L(lang, 'Tu refugio en la Patagonia', 'Your refuge in Patagonia')}</h3>
        <p>{L(lang, 'Parcelas frente a ríos de Aysén, con crédito directo sin interés y asesoría legal.', 'Plots facing rivers in Aysén, with interest-free direct financing and legal support.')}</p>
        <a class="btn btn-sun" href="{rel(path, PATHS['projects'][0 if lang == 'es' else 1])}" data-cta="blog-{a['key']}-proyectos">{L(lang, 'Ver parcelas', 'See plots')}</a>
      </div>
    </aside>
  </div>
</section>
<section style="background:var(--cream)">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Sigue leyendo', 'Keep reading')}</span><h2>{L(lang, 'Más guías de la Patagonia', 'More Patagonia guides')}</h2></div>
    <div class="posts">{post_cards(path, lang, related)}</div>
  </div>
</section>"""
    schema = {"@context": "https://schema.org", "@type": "Article", "headline": a["title_" + lang], "description": a["desc_" + lang],
              "image": DOMAIN + "/" + IMG[a["img"]]["src"], "dateModified": a["updated_iso"], "inLanguage": "es-CL" if lang == "es" else "en",
              "author": {"@type": "Organization", "name": "Inmobiliaria El Roble"},
              "publisher": {"@type": "Organization", "name": "Inmobiliaria El Roble", "logo": {"@type": "ImageObject", "url": DOMAIN + "/assets/img/marca/logo.png"}},
              "mainEntityOfPage": pretty(es_p if lang == "es" else en_p)}
    page(lang, (es_p, en_p), a["seo_" + lang], a["desc_" + lang], IMG[a["img"]]["src"], body, current="blog", schema=schema)



# ---------------------------------------------------------------- Simulador
def simulator(lang):
    def body(path):
        projects = list(SIMULATOR.keys())
        opts = "".join(f'<option value="{esc(n)}">{esc(n)}</option>' for n in projects)
        cfg = json.dumps({k: {"plans": v["plans"], "lots": v["lots"], "list": v.get("list"), "discount": v.get("discount"), "note": v.get("note_" + lang, "")} for k, v in SIMULATOR.items()}, ensure_ascii=False)
        return f"""<section class="page-hero" style="min-height:56svh">
  {img(path, 'lengas', lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span>{L(lang, 'Simulador', 'Financing')}</nav>
    <span class="eyebrow light">{L(lang, 'Crédito directo sin interés', 'Interest-free direct financing')}</span>
    <h1>{L(lang, 'Simula tu plan de pago', 'Simulate your payment plan')}</h1>
    <p class="lead">{L(lang, 'Elige el proyecto y la parcela para ver el pie y la cuota del crédito directo con la inmobiliaria.', 'Choose the project and plot to see the down payment and instalment of direct financing with the developer.')}</p>
  </div>
</section>
<section class="sim">
  <div class="wrap sim-grid">
    <div class="sim-box reveal" id="sim" data-lang="{lang}" data-config='{esc(cfg)}'>
      <div class="row2">
        <label>{L(lang, 'Proyecto', 'Project')}<select id="simProject">{opts}</select></label>
        <label>{L(lang, 'Parcela', 'Plot')}<select id="simLot"></select></label>
      </div>
      <p class="sim-help" id="simPriceRow">{L(lang, 'Precio de la parcela', 'Plot price')}: <b id="simLotPrice">—</b></p>
      <dl class="sim-prices" id="simPrices" hidden>
        <div><dt>{L(lang, 'Precio de lista', 'List price')}</dt><dd id="simList">—</dd></div>
        <div><dt>{L(lang, 'Beneficio por pago al contado', 'Cash payment discount')}</dt><dd id="simDiscount">—</dd></div>
        <div class="tot"><dt>{L(lang, 'Precio final al contado', 'Final cash price')}</dt><dd id="simCash">—</dd></div>
      </dl>
      <fieldset class="plans"><legend>{L(lang, 'Modalidad de crédito directo', 'Direct financing option')}</legend><div id="simPlans"></div></fieldset>
      <p class="sim-help">{L(lang, 'También puedes pagar al contado o con crédito bancario.', 'You can also pay cash or with a bank loan.')} <a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp {WA_TXT}</a></p>
    </div>
    <aside class="sim-result reveal" aria-live="polite">
      <span class="eyebrow light">{L(lang, 'Tu simulación', 'Your simulation')}</span>
      <p class="sim-label">{L(lang, 'Cuota mensual estimada', 'Estimated monthly instalment')}</p>
      <p class="sim-big" id="simCuota">—</p>
      <p class="sim-plan" id="simPlan"></p>
      <dl>
        <div><dt id="simTotalLbl" data-base="{L(lang, 'Base del crédito directo', 'Direct financing base')}" data-price="{L(lang, 'Precio', 'Price')}">{L(lang, 'Precio', 'Price')}</dt><dd id="simTotal">—</dd></div>
        <div><dt>{L(lang, 'Pie inicial', 'Down payment')}</dt><dd id="simPie">—</dd></div>
        <div><dt>{L(lang, 'Saldo a financiar', 'Balance financed')}</dt><dd id="simSaldo">—</dd></div>
      </dl>
      <a class="btn btn-sun" id="simWa" href="https://wa.me/{WA}" target="_blank" rel="noopener" data-cta="simulador-whatsapp">{ICONS['wa']}{L(lang, 'Enviar simulación por WhatsApp', 'Send simulation on WhatsApp')}</a>
      <p class="sim-cond" id="simNote" hidden></p>
      <p class="sim-note">{L(lang, 'Simulación referencial en pesos chilenos. Las cuotas se expresan en UF y no tienen intereses. Disponibilidad sujeta a confirmación comercial.', 'Illustrative simulation in Chilean pesos. Instalments are set in UF (Chile’s inflation-indexed unit) with no interest. Availability subject to commercial confirmation.')}</p>
    </aside>
  </div>
</section>
{contact_section(path, lang, projects[0] if projects else '')}"""
    page(lang, "simulator", L(lang, "Simulador de crédito directo para parcelas | Parcelas con Río", "Direct financing simulator for land plots | Parcelas con Río"),
         L(lang, "Calcula el pie y la cuota del crédito directo sin interés para Horizontes de Mañihuales y San Clemente: 50% de pie y saldo en 24 cuotas en UF.",
           "Calculate the down payment and instalment of interest-free direct financing for Horizontes de Mañihuales and San Clemente: 50% down and 24 instalments in UF."),
         IMG["lengas"]["src"], body, current="simulator")


# ---------------------------------------------------------------- Videos
def video_card(path, v, lang, by):
    a = by.get(v["art"])
    link = f'<a class="link-arrow" href="{rel(path, art_path(a, lang))}">{L(lang, "Leer la guía", "Read the guide")} {ICONS["arrow"]}</a>' if a else ""
    poster = root(path) + IMG[v["poster"]]["src"]
    return f"""<figure class="vcard reveal">
      <div class="vplayer"><video controls playsinline preload="none" poster="{poster}" src="{root(path)}assets/video/patagonia/{v['file']}.mp4" aria-label="{esc(v[lang])}"></video></div>
      <figcaption><h3>{esc(v[lang])}</h3>{link}</figcaption>
    </figure>"""


def videos_page(lang):
    by = {a["key"]: a for a in ARTICLES}

    def body(path):
        cards = "\n    ".join(video_card(path, v, lang, by) for v in VIDEOS)
        return f"""<section class="page-hero">
  {img(path, 'v_salto', lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span><a href="{rel(path, PATHS['patagonia'][0 if lang == 'es' else 1])}">Patagonia</a><span>/</span>{L(lang, 'Videos', 'Videos')}</nav>
    <span class="eyebrow light">{L(lang, 'Filmado por Inmobiliaria El Roble', 'Filmed by Inmobiliaria El Roble')}</span>
    <h1>{L(lang, 'La Patagonia en video', 'Patagonia on video')}</h1>
    <p class="lead">{L(lang, 'Recorre desde el aire la Carretera Austral, el Lago Elizalde, Puerto Ingeniero Ibáñez y el Salto del Río Ibáñez. Así es el territorio donde están nuestras parcelas.', 'Fly over the Carretera Austral, Lake Elizalde, Puerto Ingeniero Ibáñez and the Ibáñez River falls. This is the land where our plots are.')}</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="vgrid">
    {cards}
    </div>
  </div>
</section>
<section class="band">
  {img(path, 'v_elizalde_orilla', lang)}
  <div class="wrap">
    <span class="eyebrow light">{L(lang, 'Tu lugar en el sur', 'Your place in the south')}</span>
    <h2>{L(lang, '¿Te imaginas vivir aquí?', 'Can you picture living here?')}</h2>
    <p>{L(lang, 'Parcelas frente a ríos de Aysén, con crédito directo sin interés y asesoría legal.', 'Plots facing rivers in Aysén, with interest-free direct financing and legal support.')}</p>
    <div class="hero-ctas"><a class="btn btn-sun" href="{rel(path, PATHS['projects'][0 if lang == 'es' else 1])}">{L(lang, 'Ver parcelas', 'See plots')}</a></div>
  </div>
</section>"""
    page(lang, "videos", L(lang, "La Patagonia en video: Lago Elizalde, Puerto Ibáñez y más | Parcelas con Río", "Patagonia on video: Lake Elizalde, Puerto Ibáñez and more | Parcelas con Río"),
         L(lang, "Videos aéreos de la Región de Aysén: Carretera Austral, Lago Elizalde, Puerto Ingeniero Ibáñez, Salto del Río Ibáñez y Valle Simpson.",
           "Aerial videos of the Aysén Region: Carretera Austral, Lake Elizalde, Puerto Ingeniero Ibáñez, Ibáñez River falls and Valle Simpson."),
         IMG["v_salto"]["src"], body, current="patagonia")


def sitemap():
    rows = []
    seen = set()
    for es_p, en_p, path in SITEMAP:
        if path in seen:
            continue
        seen.add(path)
        rows.append(f"""  <url>
    <loc>{pretty(path)}</loc>
    <xhtml:link rel="alternate" hreflang="es-CL" href="{pretty(es_p)}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{pretty(en_p)}"/>
  </url>""")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")


def main():
    import content  # textos largos: Patagonia, nosotros, contacto, historias de proyectos
    PROJECT_STORY.update(content.PROJECT_STORY)
    for lang in LANGS:
        home(lang)
        projects_index(lang)
        for p in PROJECTS:
            if p["detail"]:
                project_page(p, lang)
        content.patagonia(lang, page, img, L, rel, PATHS, ARTICLES, art_path, post_cards, contact_section, video_card, VIDEOS)
        content.about(lang, page, img, L, rel, PATHS, IMG)
        content.contact(lang, page, img, L, contact_section)
        simulator(lang)
        videos_page(lang)
        thanks(lang)
        blog_index(lang)
        for a in ARTICLES:
            article(a, lang)
    sitemap()
    print("Páginas:", len(SITEMAP))


if __name__ == "__main__":
    main()
