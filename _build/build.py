"""Genera el sitio estático de Parcelas con Río en español e inglés.

Uso:  python3 _build/build.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import (DOMAIN, FB, FB_SVG, ICONS, IG, IG_SVG, MAIL, PATHS, WA, WA_TXT, esc, footer,  # noqa: E402
                  head, header, lead_form, pretty, rel, root, wa_link, write)
from data import IMG, MANIHUALES_LOTS, PROJECTS  # noqa: E402
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
    <video class="is-active" muted playsinline loop autoplay preload="auto" poster="{r}assets/img/bienvenida/home-poster-1280.jpg" data-desktop="{r}assets/video/bienvenida/manihuales-home-1280.mp4" data-mobile="{r}assets/video/bienvenida/manihuales-home-960.mp4" data-poster-mobile="{r}assets/img/bienvenida/home-poster-960.jpg"></video>
  </div>
  <div class="wrap">
    <span class="eyebrow light">{L(lang, 'Patagonia chilena · Sur de Chile', 'Chilean Patagonia · Southern Chile')}</span>
    <h1>{L(lang, 'Tu refugio junto al <em>río</em>, en el fin del mundo', 'Your riverside <em>refuge</em> at the end of the world')}</h1>
    <p class="lead">{L(lang, 'Parcelas con rol propio frente a ríos de Aysén y del sur de Chile. Bosques, ríos de pesca, lagos y nieve a tu alcance, con crédito directo.', 'Land plots with their own title facing rivers in Aysén and southern Chile. Forests, fishing rivers, lakes and snow within reach, with direct financing.')}</p>
    <div class="hero-ctas">
      <a class="btn btn-sun" href="{rel(path, PATHS['projects'][0 if lang == 'es' else 1])}" data-cta="home-hero-proyectos">{L(lang, 'Ver parcelas disponibles', 'See available plots')}</a>
      <a class="btn btn-ghost" href="{rel(path, PATHS['patagonia'][0 if lang == 'es' else 1])}" data-cta="home-hero-patagonia">{L(lang, 'Descubrir la Patagonia', 'Discover Patagonia')}</a>
    </div>
    <div class="hero-meta">
      <div><b>5</b><span>{L(lang, 'proyectos', 'projects')}</span></div>
      <div><b>3</b><span>{L(lang, 'regiones del sur', 'southern regions')}</span></div>
      <div><b>{L(lang, 'Rol propio', 'Own title')}</b><span>{L(lang, 'en cada parcela', 'on every plot')}</span></div>
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
      <p class="lead">{L(lang, 'Proyectos en las regiones de Aysén, Los Ríos y el Maule. Todos con rol propio y opción de crédito directo.', 'Projects in the Aysén, Los Ríos and Maule regions. All with their own title and direct financing options.')}</p>
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
    <p>{L(lang, 'Financiamiento directo con la inmobiliaria, parcelas con rol propio listas para escriturar y acompañamiento en todo el proceso.', 'Direct financing with the developer, plots with their own title ready for the deed, and support throughout the process.')}</p>
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
         L(lang, "Parcelas con rol propio frente a ríos en Aysén, Los Ríos y el Maule. Tu refugio en la Patagonia chilena, cerca de Coyhaique, con crédito directo.",
           "Riverside land plots with their own title in Aysén, Los Ríos and Maule. Your refuge in Chilean Patagonia near Coyhaique, with direct financing."),
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
         L(lang, "Parcelas con rol propio frente a ríos en la Patagonia (Aysén), Los Ríos y el Maule. Disponibilidad, superficies y crédito directo.",
           "Plots with their own title next to rivers in Patagonia (Aysén), Los Ríos and Maule. Availability, sizes and direct financing."),
         IMG["lago_reflejo"]["src"], body, current="projects")


def attrs_section(path, lang):
    items = [
        ("river", L(lang, "Frente a ríos", "Riverfront"), L(lang, "Proyectos junto al Mañihuales, el Emperador Guillermo y otros cursos de agua.", "Projects next to the Mañihuales, the Emperador Guillermo and other rivers.")),
        ("road", L(lang, "Acceso", "Access"), L(lang, "Caminos y servidumbres de tránsito hasta cada lote.", "Roads and rights-of-way to every lot.")),
        ("doc", L(lang, "Rol propio", "Own title"), L(lang, "Todas las parcelas con rol propio, listas para escriturar.", "Every plot has its own property title, ready for the deed.")),
        ("key", L(lang, "Crédito directo", "Direct financing"), L(lang, "Financiamiento directo con la inmobiliaria, sin pasar por el banco.", "Direct financing with the developer, no bank needed.")),
    ]
    cells = "".join(f'<div class="attr reveal"><span class="ic">{ICONS[i]}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in items)
    return f"""<section style="background:var(--cream)">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Por qué El Roble', 'Why El Roble')}</span><h2>{L(lang, 'Comprar tranquilo, desde el primer día', 'Buy with peace of mind from day one')}</h2></div>
    <div class="attrs">{cells}</div>
  </div>
</section>"""


def project_page(p, lang):
    es_p, en_p = proj_path(p, "es"), proj_path(p, "en")

    def body(path):
        extra = ""
        if p["slug"] == "horizontes-de-manihuales":
            lots = "".join(
                f'<div class="lot{" reserved" if res else ""}"><div class="n">{n}</div><div><h3>{L(lang, "Lote", "Lot")} {n}</h3><div class="sz">{es if lang == "es" else en}</div></div><span class="pill {"res" if res else "ok"}">{L(lang, "Reservado", "Reserved") if res else L(lang, "Disponible", "Available")}</span></div>'
                for n, es, en, res in MANIHUALES_LOTS)
            extra = f"""<section class="split">
  <div class="wrap">
    <figure>{img(path, 'plano_manihuales', lang, cls='plan')}<figcaption>{L(lang, 'Plano referencial. Servidumbre de tránsito de 7 m.', 'Reference plan. 7 m right-of-way.')}</figcaption></figure>
    <div>
      <span class="eyebrow">{L(lang, 'Lotes', 'Lots')}</span>
      <h2>{L(lang, 'Cuatro lotes, todos mirando al río', 'Four lots, all facing the river')}</h2>
      <p>{L(lang, 'Todos los lotes tienen frente hacia el río Mañihuales, acceso por servidumbre de tránsito y factibilidad eléctrica.', 'Every lot faces the Mañihuales River, with access via right-of-way and electricity feasibility.')}</p>
      <div class="lots">{lots}</div>
      <p style="margin-top:14px;font-size:.9rem">{L(lang, 'Superficies según plano del loteo. Precios por WhatsApp o formulario.', 'Areas according to the subdivision plan. Prices on request.')}</p>
    </div>
  </div>
</section>"""
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
      <a class="btn btn-ghost" href="{rel(path, PATHS['simulator'][0 if lang == 'es' else 1])}?proyecto={p['name'].replace(' ', '+')}" data-cta="proyecto-{p['slug']}-simulador">{L(lang, 'Simular crédito', 'Simulate financing')}</a>
    </div>
  </div>
  {'' if p.get('real') else '<span class="photo-credit">' + L(lang, 'Imagen referencial del territorio', 'Illustrative image of the region') + '</span>'}
</section>
{story}
{gallery_section(path, p, lang)}
{extra}
{attrs_section(path, lang)}
{contact_section(path, lang, p['name'])}"""
    page(lang, (es_p, en_p), f"{p['name']} · {L(lang, 'Parcelas en venta', 'Land for sale')} | Parcelas con Río",
         f"{p['short_' + lang]} {L(lang, 'Rol propio y crédito directo.', 'Own title and direct financing.')}",
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
        <p>{L(lang, 'Parcelas con rol propio frente a ríos de Aysén, con crédito directo.', 'Plots with their own title facing rivers in Aysén, with direct financing.')}</p>
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
PLANS = [(30, 18), (40, 24), (50, 36)]


def simulator(lang):
    def body(path):
        opts = "".join(f'<option value="{esc(n)}">{esc(n)}</option>' for n in PROJECT_NAMES)
        plans = "".join(f"""<label class="plan"><input type="radio" name="plan" value="{pie}-{n}"{' checked' if i == 0 else ''}>
          <span class="plan-in"><b>{pie}% {L(lang, 'de pie', 'down')}</b><span>{n} {L(lang, 'cuotas', 'instalments')}</span><em data-cuota="{pie}-{n}">—</em></span></label>""" for i, (pie, n) in enumerate(PLANS))
        return f"""<section class="page-hero" style="min-height:56svh">
  {img(path, 'lengas', lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span>{L(lang, 'Simulador', 'Financing')}</nav>
    <span class="eyebrow light">{L(lang, 'Crédito directo sin interés', 'Interest-free direct financing')}</span>
    <h1>{L(lang, 'Simula tu plan de pago', 'Simulate your payment plan')}</h1>
    <p class="lead">{L(lang, 'Elige el proyecto, escribe el precio de la parcela y compara las tres modalidades de crédito directo con la inmobiliaria.', 'Choose the project, enter the plot price and compare the three direct financing options with the developer.')}</p>
  </div>
</section>
<section class="sim">
  <div class="wrap sim-grid">
    <div class="sim-box reveal" id="sim" data-lang="{lang}">
      <div class="row2">
        <label>{L(lang, 'Proyecto', 'Project')}<select id="simProject">{opts}</select></label>
        <label>{L(lang, 'Precio de la parcela (CLP)', 'Plot price (CLP)')}<input id="simPrice" inputmode="numeric" autocomplete="off" placeholder="{L(lang, 'Ej: 25.000.000', 'e.g. 25,000,000')}"></label>
      </div>
      <p class="sim-help">{L(lang, '¿No tienes el precio? Pídelo por WhatsApp y vuelve a simular.', "Don't have the price? Ask us on WhatsApp and come back to simulate.")} <a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp {WA_TXT}</a></p>
      <fieldset class="plans"><legend>{L(lang, 'Modalidad de crédito directo', 'Direct financing option')}</legend>{plans}</fieldset>
    </div>
    <aside class="sim-result reveal" aria-live="polite">
      <span class="eyebrow light">{L(lang, 'Tu simulación', 'Your simulation')}</span>
      <p class="sim-label">{L(lang, 'Cuota mensual estimada', 'Estimated monthly instalment')}</p>
      <p class="sim-big" id="simCuota">—</p>
      <p class="sim-plan" id="simPlan"></p>
      <dl>
        <div><dt>{L(lang, 'Precio', 'Price')}</dt><dd id="simTotal">—</dd></div>
        <div><dt>{L(lang, 'Pie inicial', 'Down payment')}</dt><dd id="simPie">—</dd></div>
        <div><dt>{L(lang, 'Saldo a financiar', 'Balance financed')}</dt><dd id="simSaldo">—</dd></div>
      </dl>
      <a class="btn btn-sun" id="simWa" href="https://wa.me/{WA}" target="_blank" rel="noopener" data-cta="simulador-whatsapp">{ICONS['wa']}{L(lang, 'Enviar simulación por WhatsApp', 'Send simulation on WhatsApp')}</a>
      <p class="sim-note">{L(lang, 'Simulación referencial en pesos chilenos. Las cuotas se expresan en UF y no tienen intereses. Precios, condiciones y disponibilidad sujetos a confirmación comercial.', 'Illustrative simulation in Chilean pesos. Instalments are set in UF (Chile’s inflation-indexed unit) with no interest. Prices, terms and availability subject to commercial confirmation.')}</p>
    </aside>
  </div>
</section>
{contact_section(path, lang)}"""
    page(lang, "simulator", L(lang, "Simulador de crédito directo para parcelas | Parcelas con Río", "Direct financing simulator for land plots | Parcelas con Río"),
         L(lang, "Calcula el pie y la cuota de tu parcela con crédito directo sin interés: 30% de pie en 18 cuotas, 40% en 24 o 50% en 36.",
           "Calculate the down payment and instalment for your plot with interest-free direct financing: 30% down over 18 months, 40% over 24 or 50% over 36."),
         IMG["lengas"]["src"], body, current="simulator")


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
        content.patagonia(lang, page, img, L, rel, PATHS, ARTICLES, art_path, post_cards, contact_section)
        content.about(lang, page, img, L, rel, PATHS, IMG)
        content.contact(lang, page, img, L, contact_section)
        simulator(lang)
        thanks(lang)
        blog_index(lang)
        for a in ARTICLES:
            article(a, lang)
    sitemap()
    print("Páginas:", len(SITEMAP))


if __name__ == "__main__":
    main()
