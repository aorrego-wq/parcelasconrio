"""Textos de páginas: Vivir la Patagonia, Nosotros, Contacto e historias de proyectos."""
from common import ICONS, MAIL, WA, WA_TXT, IG, wa_link


def _L(lang):
    return lambda es, en: es if lang == "es" else en


# Texto adicional por proyecto (sección bajo la portada de cada proyecto)
def _story(lang, eyebrow, title, paras, img_key=None):
    L = _L(lang)
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f"""<section class="statement">
  <div class="wrap grid">
    <div class="reveal"><span class="eyebrow">{eyebrow}</span><p class="big">{title}</p></div>
    <div class="side reveal">{ps}</div>
  </div>
</section>"""


PROJECT_STORY = {
    "horizontes-de-manihuales": {
        "es": _story("es", "El proyecto", "Despierta frente al <em>río Mañihuales</em>, en el corazón verde de Aysén.", [
            "Horizontes de Mañihuales son cuatro parcelas de entre 0,53 y 1 hectárea con frente al río, en Villa Mañihuales, Región de Aysén, rodeadas de bosque nativo.",
            "Un lugar para construir tu casa, una cabaña para escapar o simplemente guardar un pedazo de Patagonia: con acceso por servidumbre de tránsito, factibilidad eléctrica, rol propio y crédito directo."]),
        "en": _story("en", "The project", "Wake up facing the <em>Mañihuales River</em>, in the green heart of Aysén.", [
            "Horizontes de Mañihuales offers four plots of 0.53 to 1 hectare facing the river in Villa Mañihuales, Aysén Region, surrounded by native forest.",
            "A place to build your home, a getaway cabin or simply keep your own piece of Patagonia: right-of-way access, electricity feasibility, own title and direct financing."]),
    },
    "don-guillermo": {
        "es": _story("es", "El proyecto", "Frente al <em>río Emperador Guillermo</em>, sobre la mítica Carretera Austral.", [
            "Parcelas Don Guillermo está junto al río Emperador Guillermo, en plena Carretera Austral, una de las rutas escénicas más famosas del mundo.",
            "Queda una sola parcela disponible. Escríbenos para conocer su superficie, precio y opciones de crédito directo."]),
        "en": _story("en", "The project", "Facing the <em>Emperador Guillermo River</em>, on the legendary Carretera Austral.", [
            "Parcelas Don Guillermo sits next to the Emperador Guillermo River, right on the Carretera Austral, one of the world's most famous scenic routes.",
            "Only one plot is left. Write to us for its size, price and direct financing options."]),
    },
    "rofuco-bajo": {
        "es": _story("es", "El proyecto", "Naturaleza del sur en la <em>Región de Los Ríos</em>.", [
            "Parcelas Rofuco Bajo está en la Región de Los Ríos, tierra de bosques húmedos, ríos y lagos del sur de Chile.",
            "El proyecto ya vendió el 57% de sus parcelas. Pide la disponibilidad actual, superficies y precios por WhatsApp o con el formulario."]),
        "en": _story("en", "The project", "Southern nature in the <em>Los Ríos Region</em>.", [
            "Parcelas Rofuco Bajo is in the Los Ríos Region, a land of rainforests, rivers and lakes in southern Chile.",
            "57% of the plots are already sold. Ask for current availability, sizes and prices on WhatsApp or using the form."]),
    },
    "dona-cecilia": {
        "es": _story("es", "El proyecto", "Las <em>últimas parcelas</em> en San Clemente, Región del Maule.", [
            "Parcelación Doña Cecilia está en la comuna de San Clemente, en la Región del Maule: praderas abiertas, caminos de ripio entre los terrenos y cerros en el horizonte.",
            "Quedan las últimas 6 parcelas. Escríbenos para conocer su ubicación exacta, superficies, precios y opciones de crédito directo."]),
        "en": _story("en", "The project", "The <em>last plots</em> in San Clemente, Maule Region.", [
            "Parcelación Doña Cecilia is in the San Clemente district of the Maule Region: open meadows, gravel roads between the plots and hills on the horizon.",
            "Only the last 6 plots remain. Write to us for the exact location, sizes, prices and direct financing options."]),
    },
}


def patagonia(lang, page, img, L, rel, PATHS, ARTICLES, art_path, post_cards, contact_section):
    from data import IMG
    by = {a["key"]: a for a in ARTICLES}
    blocks = [
        ("aeropuerto", "coyhaique", False), ("marmol", "marmol2", True), ("carretera", "carretera2", False),
        ("ski", "ski", True), ("pesca", "simpson3", False), ("castillo", "ccastillo4", True), ("vivir", "coy2", False),
    ]

    def body(path):
        secs = []
        for k, ikey, rev in blocks:
            a = by[k]
            key = ikey or a["img"]
            cr = IMG[key].get("credit")
            secs.append(f"""<section class="split{' rev' if rev else ''}">
  <div class="wrap">
    <figure class="reveal">{img(path, key, lang)}{('<figcaption>' + L(lang, 'Foto', 'Photo') + ': ' + cr + '</figcaption>') if cr else ''}</figure>
    <div class="reveal">
      <span class="eyebrow">{a['cat_' + lang]}</span>
      <h2>{a['tile_' + lang]}</h2>
      <p>{a['hub_' + lang]}</p>
      <a class="link-arrow" href="{rel(path, art_path(a, lang))}">{L(lang, 'Leer la guía completa', 'Read the full guide')} {ICONS['arrow']}</a>
    </div>
  </div>
</section>""")
        return f"""<section class="page-hero">
  {img(path, 'ccastillo1', lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span>{L(lang, 'Vivir la Patagonia', 'Patagonia')}</nav>
    <span class="eyebrow light">{L(lang, 'Región de Aysén · Patagonia chilena', 'Aysén Region · Chilean Patagonia')}</span>
    <h1>{L(lang, 'Un territorio para enamorarse cada estación', 'A land to fall in love with every season')}</h1>
    <p class="lead">{L(lang, 'Glaciares, lagos turquesa, ríos de pesca de clase mundial, nieve y bosques infinitos. Esto es lo que te espera en la Región de Aysén.', 'Glaciers, turquoise lakes, world-class fishing rivers, snow and endless forests. This is what awaits you in the Aysén Region.')}</p>
  </div>
</section>
{''.join(secs[:3])}
<section class="band">
  {img(path, 'ruta3', lang)}
  <div class="wrap">
    <span class="eyebrow light">{L(lang, 'Tu lugar en el sur', 'Your place in the south')}</span>
    <h2>{L(lang, 'Imagina volver aquí cada fin de semana', 'Imagine coming back here every weekend')}</h2>
    <p>{L(lang, 'Parcelas con rol propio frente a ríos de Aysén, con crédito directo sin interés.', 'Plots with their own title facing rivers in Aysén, with interest-free direct financing.')}</p>
    <div class="hero-ctas"><a class="btn btn-sun" href="{rel(path, PATHS['projects'][0 if lang == 'es' else 1])}">{L(lang, 'Ver parcelas', 'See plots')}</a></div>
  </div>
</section>
{''.join(secs[3:])}
{contact_section(path, lang)}"""
    page(lang, "patagonia", L(lang, "Vivir la Patagonia: Coyhaique, Catedrales de Mármol, pesca, ski y trekking | Parcelas con Río", "Living in Patagonia: Coyhaique, Marble Caves, fishing, skiing and trekking | Parcelas con Río"),
         L(lang, "Todo lo que ofrece la Región de Aysén: cómo llegar a Coyhaique, Catedrales de Mármol, Carretera Austral, centro de ski El Fraile, pesca con mosca y trekking.",
           "Everything the Aysén Region offers: getting to Coyhaique, the Marble Caves, Carretera Austral, El Fraile ski area, fly fishing and trekking."),
         IMG["ccastillo1"]["src"], body, current="patagonia")


def about(lang, page, img, L, rel, PATHS, IMG):
    def body(path):
        credits = "".join(f"<li>{v['credit_full']}</li>" for v in IMG.values() if v.get("credit_full"))
        return f"""<section class="page-hero">
  {img(path, 'lengas', lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span>{L(lang, 'Nosotros', 'About us')}</nav>
    <h1>{L(lang, 'Inmobiliaria El Roble', 'Inmobiliaria El Roble')}</h1>
    <p class="lead">{L(lang, 'Buscamos los mejores rincones del sur de Chile para que tengas tu propio pedazo de naturaleza.', 'We find the best corners of southern Chile so you can own your piece of nature.')}</p>
  </div>
</section>
<section class="split">
  <div class="wrap">
    <figure class="reveal">{img(path, 'valle', lang)}<figcaption>{L(lang, 'Imagen referencial del territorio de Aysén', 'Illustrative image of the Aysén region')}</figcaption></figure>
    <div class="reveal">
      <span class="eyebrow">{L(lang, 'Cómo trabajamos', 'How we work')}</span>
      <h2>{L(lang, 'Terrenos con agua, acceso y todo en regla', 'Land with water, access and everything in order')}</h2>
      <p>{L(lang, 'Inmobiliaria El Roble selecciona terrenos con agua, acceso y entorno natural en las regiones de Aysén, Los Ríos y el Maule, y acompaña cada compra hasta la escritura.', 'Inmobiliaria El Roble selects land with water, access and natural surroundings in the Aysén, Los Ríos and Maule regions, and supports every purchase through to the deed.')}</p>
      <ul class="ticks">
        <li>{L(lang, 'Parcelas con rol propio, listas para escriturar', 'Plots with their own property title, ready for the deed')}</li>
        <li>{L(lang, 'Crédito directo con la inmobiliaria', 'Direct financing with the developer')}</li>
        <li>{L(lang, 'Acceso por caminos y servidumbres de tránsito', 'Access by roads and rights-of-way')}</li>
        <li>{L(lang, 'Visitas al terreno coordinadas contigo', 'Site visits arranged with you')}</li>
      </ul>
      <a class="btn btn-night" href="{rel(path, PATHS['projects'][0 if lang == 'es' else 1])}">{L(lang, 'Ver proyectos', 'See projects')}</a>
    </div>
  </div>
</section>
<section style="background:var(--cream)">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">{L(lang, 'Cómo comprar', 'How to buy')}</span><h2>{L(lang, 'Del primer mensaje a tu escritura', 'From first message to your deed')}</h2></div>
    <ol class="steps">
      <li><strong>{L(lang, 'Elige tu proyecto', 'Choose your project')}</strong><span>{L(lang, 'Revisa los proyectos y escríbenos para recibir precios, planos y disponibilidad.', 'Browse the projects and write to us for prices, plans and availability.')}</span></li>
      <li><strong>{L(lang, 'Visita el terreno', 'Visit the land')}</strong><span>{L(lang, 'Coordinamos contigo una visita para que conozcas la parcela y su entorno.', 'We arrange a visit so you can see the plot and its surroundings.')}</span></li>
      <li><strong>{L(lang, 'Elige cómo pagar', 'Choose how to pay')}</strong><span>{L(lang, 'Al contado o con crédito directo sin interés. Simula tu plan en línea.', 'Cash or interest-free direct financing. Simulate your plan online.')}</span></li>
      <li><strong>{L(lang, 'Firma y escritura', 'Sign and deed')}</strong><span>{L(lang, 'Te acompañamos en la firma ante notario y la inscripción de tu parcela.', 'We guide you through signing before a notary and registering your plot.')}</span></li>
    </ol>
  </div>
</section>
<section id="creditos" style="padding-block:40px">
  <div class="wrap">
    <details class="credits"><summary>{L(lang, 'Créditos de fotografías', 'Photo credits')}</summary>
    <p style="color:var(--muted);margin-bottom:14px">{L(lang, 'Las fotografías de paisajes de Aysén son referenciales del territorio y no corresponden necesariamente a los terrenos en venta. Las fotos de terceros se usan según su licencia:', 'Aysén landscape photos are illustrative of the region and do not necessarily show the land for sale. Third-party photos are used under their licenses:')}</p>
    <ul style="color:var(--muted);font-size:.9rem">{credits}</ul>
    </details>
  </div>
</section>"""
    page(lang, "about", L(lang, "Nosotros · Inmobiliaria El Roble | Parcelas con Río", "About us · Inmobiliaria El Roble | Parcelas con Río"),
         L(lang, "Inmobiliaria El Roble vende parcelas con rol propio frente a ríos en Aysén, Los Ríos y el Maule, con crédito directo y acompañamiento hasta la escritura.",
           "Inmobiliaria El Roble sells riverside plots with their own title in Aysén, Los Ríos and Maule, with direct financing and support through to the deed."),
         IMG["lengas"]["src"], body, current="about")


def contact(lang, page, img, L, contact_section):
    from data import IMG
    from common import rel
    from common import PATHS

    def body(path):
        return f"""<section class="page-hero" style="min-height:52svh">
  {img(path, 'lago_bote', lang, eager=True)}
  <div class="wrap">
    <nav class="crumbs"><a href="{rel(path, PATHS['home'][0 if lang == 'es' else 1])}">{L(lang, 'Inicio', 'Home')}</a><span>/</span>{L(lang, 'Contacto', 'Contact')}</nav>
    <h1>{L(lang, 'Hablemos de tu refugio', "Let's talk about your refuge")}</h1>
  </div>
</section>
{contact_section(path, lang)}"""
    page(lang, "contact", L(lang, "Contacto | Parcelas con Río · Inmobiliaria El Roble", "Contact | Parcelas con Río · Inmobiliaria El Roble"),
         L(lang, "Escríbenos por WhatsApp al +56 9 7889 3044 o con el formulario para recibir precios, planos y agendar una visita a las parcelas.",
           "Write to us on WhatsApp at +56 9 7889 3044 or use the form to get prices, plans and book a visit to the plots."),
         IMG["lago_bote"]["src"], body, current="contact")
