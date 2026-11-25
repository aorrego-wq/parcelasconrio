"""Landings de campaña (Meta Ads) y política de privacidad.

Las landings son páginas enfocadas en un solo proyecto, sin menú, con el
formulario arriba y noindex: se usan solo como destino de los anuncios.
Llevan data-proyecto en <html> para que el píxel identifique el proyecto.
"""
from common import ICONS, MAIL, WA, WA_TXT, esc, head, lead_form, root, wa_link, write

LANDINGS = [
    {
        "path": "lp/horizontes-de-manihuales.html", "slug": "horizontes-de-manihuales",
        "eyebrow": "Patagonia · Región de Aysén · Venta en verde",
        "h1": "Tu parcela frente al <em>río Mañihuales</em>",
        "lead": "Parcelas de 0,53 a 1 ha con acceso por camino público, a 10 minutos de Villa Mañihuales y 1 h 10 min de Coyhaique.",
        "chips": [("3", "parcelas disponibles"), ("$28.000.000", "precio desde"), ("24 cuotas", "crédito directo sin interés")],
        "form_title": "Recibe precios, plano y formas de pago",
        "wa": "Hola, vi el anuncio de Horizontes de Mañihuales. ¿Me envían precios y disponibilidad?",
        "title": "Horizontes de Mañihuales · Parcelas frente al río desde $28.000.000",
        "desc": "Parcelas de 0,53 a 1 ha frente al río Mañihuales, Patagonia. Desde $28.000.000 con crédito directo: 50% de pie y 24 cuotas en UF sin interés.",
        "benefits": [
            ("river", "Frente al río", "Parcelas con vista y cercanía al río Mañihuales, entre árboles nativos."),
            ("road", "Camino público", "Acceso por camino público, a 10 minutos de Villa Mañihuales."),
            ("key", "Crédito directo", "50% de pie y el saldo en 24 cuotas en UF, sin intereses ni banco."),
            ("doc", "Asesoría legal", "Te acompañamos en todo el proceso de compra con nuestro staff de abogados."),
        ],
    },
    {
        "path": "lp/san-clemente.html", "slug": "dona-cecilia",
        "eyebrow": "Región del Maule · San Clemente",
        "h1": "Últimas 6 parcelas de 5.000 m² en <em>San Clemente</em>",
        "lead": "Entre praderas y cerros, con acceso por la ruta asfaltada K-455, a 35 minutos de Talca y 30 del lago Colbún.",
        "chips": [("$19.500.000", "precio al contado"), ("5.000 m²", "cada parcela"), ("Rol propio", "subdivisión aprobada por el SAG")],
        "form_title": "Recibe precios, plano y disponibilidad",
        "wa": "Hola, vi el anuncio de las parcelas en San Clemente. ¿Me envían precios y disponibilidad?",
        "title": "Parcelas en San Clemente · Últimas 6 de 5.000 m² a $19.500.000",
        "desc": "Últimas 6 parcelas de 5.000 m² en San Clemente, Región del Maule. $19.500.000 al contado o crédito directo con 50% de pie y 24 cuotas sin interés.",
        "benefits": [
            ("road", "Ruta asfaltada", "Acceso por la ruta K-455, que une San Clemente con Pelarco."),
            ("doc", "SAG y rol propio", "Subdivisión aprobada por el SAG; cada parcela con rol propio."),
            ("bolt", "Empalme eléctrico", "El proyecto contempla un empalme eléctrico para cada parcela."),
            ("key", "Crédito directo", "50% de pie y el saldo en 24 cuotas en UF, sin intereses ni banco."),
        ],
    },
]

CSS = """<style>
.lp-top{position:sticky;top:0;z-index:50;background:rgba(255,253,249,.97);backdrop-filter:blur(10px);box-shadow:0 6px 24px -14px rgba(20,28,59,.35)}
.lp-top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-block:8px}
.lp-top .brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--night);font-family:var(--display);font-weight:600;line-height:1.1}
.lp-top .brand img{height:44px;width:auto}
.lp-top .brand small{display:block;font-family:var(--body,inherit);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:700}
.lp-top .btn{padding:11px 18px;font-size:.88rem}
.lp-hero{position:relative;color:#fff;overflow:hidden;isolation:isolate}
.lp-hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2}
.lp-hero::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(100deg,rgba(20,28,59,.88) 0%,rgba(20,28,59,.6) 50%,rgba(20,28,59,.35) 100%)}
.lp-hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center;padding-block:64px}
.lp-hero h1{color:#fff;font-size:clamp(2.2rem,4.6vw,3.6rem)}
.lp-hero h1 em{font-style:italic;color:var(--sun);font-weight:400}
.lp-hero .lead{color:rgba(255,255,255,.9);margin-top:18px;font-size:1.12rem;max-width:34em}
.lp-chips{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:28px;max-width:560px}
.lp-chips div{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.25);border-radius:14px;padding:14px;backdrop-filter:blur(4px)}
.lp-chips b{display:block;font-family:var(--display);font-size:1.3rem;font-weight:500;color:#fff;line-height:1.1}
.lp-chips span{display:block;font-size:.8rem;color:rgba(255,255,255,.8);margin-top:4px}
.lp-hero .hero-ctas{margin-top:28px}
.lp-hero form.lead-form{color:var(--ink,#1d2433)}
.lp-benefits{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.lp-benefits div{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px}
.lp-benefits .ic{display:inline-flex;width:44px;height:44px;border-radius:12px;background:var(--cream);color:var(--night);align-items:center;justify-content:center}
.lp-benefits .ic svg{width:24px;height:24px}
.lp-benefits h3{font-size:1.2rem;margin-top:12px}
.lp-benefits p{margin:6px 0 0;color:var(--muted);font-size:.95rem}
.lp-cta{background:var(--night);color:#fff;text-align:center}
.lp-cta h2{color:#fff}
.lp-cta p{color:rgba(255,255,255,.85);max-width:40em;margin:14px auto 0}
.lp-cta .hero-ctas{justify-content:center}
.lp-foot{background:var(--night);color:rgba(255,255,255,.7);font-size:.85rem;padding:22px 0;border-top:1px solid rgba(255,255,255,.12)}
.lp-foot .wrap{display:flex;gap:16px;flex-wrap:wrap;justify-content:space-between}
.lp-foot a{color:#fff}
@media (max-width:960px){.lp-hero .wrap{grid-template-columns:1fr;padding-block:40px}.lp-benefits{grid-template-columns:1fr 1fr}}
@media (max-width:560px){.lp-chips{grid-template-columns:1fr 1fr 1fr;gap:8px}.lp-chips div{padding:10px}.lp-chips b{font-size:1.02rem}.lp-benefits{grid-template-columns:1fr}.lp-top .brand span{display:none}}
</style>
"""


def landing(b, cfg):
    path = cfg["path"]
    p = next(x for x in b.PROJECTS if x["slug"] == cfg["slug"])
    r = root(path)
    lang = "es"
    html = head(lang, path, path, cfg["title"], cfg["desc"], b.IMG[p["img"]]["src"], noindex=True)
    html = html.replace('<html lang="es"', f'<html lang="es" data-proyecto="{p["slug"]}"', 1)
    html = html.replace("</head>", CSS + "</head>", 1)
    wa = wa_link(cfg["wa"])
    chips = "".join(f"<div><b>{v}</b><span>{t}</span></div>" for v, t in cfg["chips"])
    bens = "".join(f'<div><span class="ic">{ICONS[i]}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in cfg["benefits"])
    form = lead_form(lang, b.PROJECT_NAMES, p["name"], cfg["form_title"]).replace(
        '<input type="hidden" name="simulacion" value="">',
        f'<input type="hidden" name="simulacion" value=""><input type="hidden" name="origen" value="Landing campaña {esc(p["name"])}">', 1).replace(
        "Nueva consulta · Parcelas con Río", f"Lead campaña · {esc(p['name'])}", 1).replace(
        '<form class="lead-form"', '<form class="lead-form" id="formulario"', 1)
    if p["slug"] == "horizontes-de-manihuales":
        detalle = b.manihuales_section(path, lang)
    else:
        detalle = b.dona_cecilia_section(path, p, lang)
    body = f"""<header class="lp-top">
  <div class="wrap">
    <a class="brand" href="{r}" data-cta="lp-logo"><img src="{r}assets/img/marca/logo.png" width="397" height="400" alt="El Roble Inmobiliaria"><span>Parcelas con Río<small>Inmobiliaria El Roble</small></span></a>
    <a class="btn btn-sun" href="{wa}" target="_blank" rel="noopener" data-cta="lp-header-whatsapp">{ICONS['wa']}<span>WhatsApp</span></a>
  </div>
</header>
<main id="contenido">
<section class="lp-hero">
  {b.img(path, p['img'], lang, eager=True)}
  <div class="wrap">
    <div>
      <span class="eyebrow light">{cfg['eyebrow']}</span>
      <h1>{cfg['h1']}</h1>
      <p class="lead">{cfg['lead']}</p>
      <div class="lp-chips">{chips}</div>
      <div class="hero-ctas">
        <a class="btn btn-sun" href="{wa}" target="_blank" rel="noopener" data-cta="lp-hero-whatsapp">{ICONS['wa']}Hablar por WhatsApp</a>
        <a class="btn btn-ghost" href="#detalle" data-cta="lp-hero-ver-precios">Ver parcelas y precios</a>
      </div>
    </div>
    {form}
  </div>
</section>
<section>
  <div class="wrap"><div class="lp-benefits">{bens}</div></div>
</section>
<div id="detalle"></div>
{detalle}
{b.gallery_section(path, p, lang)}
{b.map_section(path, p, lang)}
<section class="lp-cta">
  <div class="wrap">
    <h2>Quedan pocas parcelas disponibles</h2>
    <p>Escríbenos y te enviamos el plano, la disponibilidad actualizada y te ayudamos a coordinar una visita al terreno.</p>
    <div class="hero-ctas">
      <a class="btn btn-sun" href="{wa}" target="_blank" rel="noopener" data-cta="lp-final-whatsapp">{ICONS['wa']}WhatsApp {WA_TXT}</a>
      <a class="btn btn-ghost" href="#formulario" data-cta="lp-final-formulario">Dejar mis datos</a>
    </div>
  </div>
</section>
</main>
<footer class="lp-foot">
  <div class="wrap"><span>© 2026 Inmobiliaria El Roble · <a href="{r}">parcelasconrio.cl</a></span><span><a href="{r}privacidad">Política de privacidad</a> · <a href="mailto:{MAIL}">{MAIL}</a></span></div>
</footer>
<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp" data-cta="lp-flotante-whatsapp">{ICONS['wa']}</a>
<script src="{r}assets/js/main.js?v={b_asset('assets/js/main.js')}" defer></script>
</body>
</html>
"""
    write(path, html + body)


def b_asset(p):
    from common import asset_version
    return asset_version(p)


PRIVACY = {
    "es": ("Política de privacidad", [
        ("Quién es responsable de tus datos", "Inmobiliaria El Roble, que comercializa los proyectos publicados en parcelasconrio.cl y terrazasdelfraile.cl. Para cualquier consulta sobre tus datos escríbenos a <a href=\"mailto:{mail}\">{mail}</a> o por WhatsApp al {wa}."),
        ("Qué datos recogemos", "Los que nos entregas en los formularios del sitio o de nuestros anuncios en Facebook e Instagram: nombre, correo, teléfono o WhatsApp, ciudad, proyecto de interés, mensaje y, si usas el simulador, la simulación de crédito."),
        ("Para qué los usamos", "Para responder tu consulta, enviarte precios, planos y disponibilidad y coordinar visitas. Solo si lo autorizas expresamente (la casilla es opcional y viene sin marcar) te enviaremos novedades, nuevos proyectos y promociones. No vendemos ni cedemos tus datos a terceros."),
        ("Herramientas de medición y publicidad", "El sitio usa el píxel de Meta para medir visitas y consultas y para mostrar anuncios de nuestros proyectos a personas que ya visitaron el sitio. Meta puede usar cookies o identificadores del navegador para esto. Puedes limitarlo desde la configuración de anuncios de tu cuenta de Facebook o Instagram, o bloqueando cookies de terceros en tu navegador."),
        ("Servicios que usamos", "Los formularios se envían por correo mediante FormSubmit. Los formularios instantáneos de Facebook e Instagram son gestionados por Meta Platforms. Ambos tratan los datos solo para entregárnoslos."),
        ("Cuánto tiempo los guardamos", "Mientras dure la atención de tu consulta y la relación comercial, y luego por el plazo que exija la ley. Si autorizaste promociones, hasta que te des de baja."),
        ("Tus derechos", "Puedes pedir acceso, rectificación, eliminación u oposición al uso de tus datos, y retirar la autorización de promociones cuando quieras, escribiendo a <a href=\"mailto:{mail}\">{mail}</a>. Respondemos conforme a la Ley 19.628 sobre protección de la vida privada y sus modificaciones."),
    ]),
    "en": ("Privacy policy", [
        ("Who is responsible for your data", "Inmobiliaria El Roble, which sells the projects published on parcelasconrio.cl and terrazasdelfraile.cl. For any question about your data, write to <a href=\"mailto:{mail}\">{mail}</a> or on WhatsApp at {wa}."),
        ("What data we collect", "The data you give us in the forms on this site or in our Facebook and Instagram ads: name, email, phone or WhatsApp, city, project of interest, message and, if you use the simulator, your financing simulation."),
        ("What we use it for", "To answer your inquiry, send you prices, plans and availability, and arrange visits. Only if you expressly agree (the box is optional and unticked) will we send you news, new projects and offers. We do not sell or transfer your data to third parties."),
        ("Measurement and advertising tools", "The site uses the Meta pixel to measure visits and inquiries and to show ads for our projects to people who have visited the site. Meta may use cookies or browser identifiers for this. You can limit it in the ad settings of your Facebook or Instagram account, or by blocking third-party cookies in your browser."),
        ("Services we use", "Forms are sent by email through FormSubmit. Facebook and Instagram instant forms are handled by Meta Platforms. Both process the data only to deliver it to us."),
        ("How long we keep it", "For as long as we handle your inquiry and the commercial relationship, and then for the period required by law. If you agreed to offers, until you unsubscribe."),
        ("Your rights", "You can request access, correction, deletion or objection to the use of your data, and withdraw your consent to offers at any time, by writing to <a href=\"mailto:{mail}\">{mail}</a>. We respond in accordance with Chilean Law 19,628 on the protection of private life and its amendments."),
    ]),
}


def privacy(b, lang):
    title, items = PRIVACY[lang]
    secs = "".join(f"<h2 style=\"font-size:1.5rem;margin-top:36px\">{h}</h2><p>{t.format(mail=MAIL, wa=WA_TXT)}</p>" for h, t in items)

    def body(path):
        return f"""<section style="padding-top:150px">
  <div class="wrap" style="max-width:820px">
    <span class="eyebrow">Inmobiliaria El Roble</span>
    <h1 style="font-size:clamp(2.2rem,4vw,3rem)">{title}</h1>
    <p class="lead" style="margin-top:12px">{'Última actualización: noviembre de 2026.' if lang == 'es' else 'Last updated: November 2026.'}</p>
    {secs}
  </div>
</section>"""
    b.page(lang, ("privacidad.html", "en/privacy.html"), f"{title} | Parcelas con Río",
           title + (" de Inmobiliaria El Roble: qué datos recogemos y cómo los usamos." if lang == "es" else " of Inmobiliaria El Roble: what data we collect and how we use it."),
           "assets/img/marca/logo.png", body, solid=True)


def generate(b):
    for cfg in LANDINGS:
        landing(b, cfg)
    for lang in ("es", "en"):
        privacy(b, lang)
