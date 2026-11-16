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
            "Horizontes de Mañihuales son cuatro parcelas de entre 0,53 y 1 hectárea frente al río Mañihuales, con acceso por camino público, hermosos árboles nativos y un entorno natural de gran belleza.",
            "Está a 1 hora y 10 minutos al norte de Coyhaique y a 10 minutos de Villa Mañihuales. El proyecto está en venta en verde mientras se obtiene la aprobación del SAG."]),
        "en": _story("en", "The project", "Wake up facing the <em>Mañihuales River</em>, in the green heart of Aysén.", [
            "Horizontes de Mañihuales offers four plots of 0.53 to 1 hectare facing the Mañihuales River, with public road access, beautiful native trees and stunning natural surroundings.",
            "It is 1 hour 10 minutes north of Coyhaique and 10 minutes from Villa Mañihuales. The project is sold off-plan while SAG approval is obtained."]),
    },
    "don-guillermo": {
        "es": _story("es", "El proyecto", "Frente al <em>río Emperador Guillermo</em>, sobre la mítica Carretera Austral.", [
            "Parcelas Don Guillermo está junto al río Emperador Guillermo, en plena Carretera Austral, una de las rutas escénicas más famosas del mundo.",
            "La única parcela disponible es la B11, de 9.500 m². Escríbenos para conocer su precio y formas de pago."]),
        "en": _story("en", "The project", "Facing the <em>Emperador Guillermo River</em>, on the legendary Carretera Austral.", [
            "Parcelas Don Guillermo sits next to the Emperador Guillermo River, right on the Carretera Austral, one of the world's most famous scenic routes.",
            "The only plot left is B11, with 9,500 m². Write to us for its price and payment options."]),
    },
    "rofuco-bajo": {
        "es": _story("es", "El proyecto", "Naturaleza del sur en la <em>Región de Los Ríos</em>.", [
            "Parcelas Rofuco Bajo está en la Región de Los Ríos, tierra de bosques húmedos, ríos y lagos del sur de Chile.",
            "Ya se vendieron 38 de sus 60 parcelas y quedan 22 disponibles, con precios desde $24.500.000 hasta $28.000.000. Consulta precios por WhatsApp o con el formulario, y recorre el proyecto en el Masterplan 360."]),
        "en": _story("en", "The project", "Southern nature in the <em>Los Ríos Region</em>.", [
            "Parcelas Rofuco Bajo is in the Los Ríos Region, a land of rainforests, rivers and lakes in southern Chile.",
            "38 of its 60 plots are already sold and 22 remain, priced from CLP 24,500,000 to 28,000,000. Ask for prices on WhatsApp or via the form, and explore the project in the 360 Masterplan."]),
    },
    "dona-cecilia": {
        "es": _story("es", "El proyecto", "Las <em>últimas parcelas</em> en San Clemente, Región del Maule.", [
            "Parcelación Doña Cecilia está en la comuna de San Clemente, en la Región del Maule: praderas abiertas, caminos de ripio entre los terrenos y cerros en el horizonte.",
            "Quedan las últimas 6 parcelas. Escríbenos para conocer su ubicación exacta, superficies, precios y formas de pago."]),
        "en": _story("en", "The project", "The <em>last plots</em> in San Clemente, Maule Region.", [
            "Parcelación Doña Cecilia is in the San Clemente district of the Maule Region: open meadows, gravel roads between the plots and hills on the horizon.",
            "Only the last 6 plots remain. Write to us for the exact location, sizes, prices and payment options."]),
    },
}


def patagonia(lang, page, img, L, rel, PATHS, ARTICLES, art_path, post_cards, contact_section, video_card=None, VIDEOS=()):
    from data import IMG
    by = {a["key"]: a for a in ARTICLES}
    blocks = [
        ("aeropuerto", "coyhaique", False), ("marmol", "marmol2", True), ("carretera", "carretera2", False),
        ("ski", "ski", True), ("pesca", "simpson3", False), ("castillo", "ccastillo4", True), ("rutasur", "v_mirador", False), ("elizalde", "v_elizalde_lancha", True), ("ibanez", "v_salto", False), ("vivir", "coy2", True),
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
    <p>{L(lang, 'Parcelas frente a ríos de Aysén, con crédito directo sin interés y asesoría legal.', 'Plots facing rivers in Aysén, with interest-free direct financing and legal support.')}</p>
    <div class="hero-ctas"><a class="btn btn-sun" href="{rel(path, PATHS['projects'][0 if lang == 'es' else 1])}">{L(lang, 'Ver parcelas', 'See plots')}</a></div>
  </div>
</section>
{''.join(secs[3:])}
<section class="experiences">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow light">{L(lang, 'Filmado por Inmobiliaria El Roble', 'Filmed by Inmobiliaria El Roble')}</span>
      <h2>{L(lang, 'La Patagonia en video', 'Patagonia on video')}</h2>
      <p class="lead">{L(lang, 'Mira desde el aire algunos de los lugares que te esperan en Aysén.', 'See from above some of the places waiting for you in Aysén.')}</p>
    </div>
    <div class="vgrid">{''.join(video_card(path, v, lang, by) for v in VIDEOS[:3]) if video_card else ''}</div>
    <p class="center" style="margin-top:34px"><a class="btn btn-sun" href="{rel(path, PATHS['videos'][0 if lang == 'es' else 1])}">{L(lang, 'Ver todos los videos', 'Watch all videos')}</a></p>
  </div>
</section>
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
      <p class="legal-note">{L(lang, 'Te guiaremos y asesoraremos legalmente durante todo el proceso de compra, con el apoyo de nuestro staff de abogados.', 'We will guide you and provide legal advice throughout the entire purchase, with the support of our team of lawyers.')}</p>
      <ul class="ticks">
        <li>{L(lang, 'Asesoría legal con nuestro staff de abogados', 'Legal advice from our team of lawyers')}</li>
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
      <li><strong>{L(lang, 'Elige cómo pagar', 'Choose how to pay')}</strong><span>{L(lang, 'Al contado, con crédito bancario o con crédito directo sin interés, según el proyecto.', 'Cash, bank loan or interest-free direct financing, depending on the project.')}</span></li>
      <li><strong>{L(lang, 'Firma y escritura', 'Sign and deed')}</strong><span>{L(lang, 'Te guiamos y asesoramos legalmente, con nuestro staff de abogados, en la firma ante notario y la inscripción de tu parcela.', 'Our team of lawyers guides you through signing before a notary and registering your plot.')}</span></li>
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
         L(lang, "Inmobiliaria El Roble vende parcelas frente a ríos en Aysén, Los Ríos y el Maule, con crédito directo y asesoría legal durante todo el proceso de compra.",
           "Inmobiliaria El Roble sells riverside plots in Aysén, Los Ríos and Maule, with direct financing and legal support throughout the purchase."),
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
