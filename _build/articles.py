"""Artículos del blog (metadatos). Los cuerpos se cargan desde _build/posts/<key>_<lang>.html."""
import json
import os

POSTS_DIR = os.path.join(os.path.dirname(__file__), "posts")

ARTICLES = [
    {
        "key": "aeropuerto", "slug_es": "como-llegar-a-coyhaique", "slug_en": "how-to-get-to-coyhaique", "img": "coyhaique",
        "cat_es": "Cómo llegar", "cat_en": "Getting there",
        "title_es": "Cómo llegar a Coyhaique: vuelos, aeropuerto y rutas", "title_en": "How to get to Coyhaique: flights, airport and roads",
        "seo_es": "Cómo llegar a Coyhaique en avión o por tierra (guía 2026) | Parcelas con Río", "seo_en": "How to get to Coyhaique by plane or road (2026 guide) | Parcelas con Río",
        "desc_es": "Vuelos a Balmaceda, el nuevo terminal del aeropuerto (octubre de 2026), distancias y rutas para llegar a la capital de la Patagonia de Aysén.",
        "desc_en": "Flights to Balmaceda, the new airport terminal (October 2026), distances and routes to reach the capital of Aysén Patagonia.",
        "tile_es": "Coyhaique, cada vez más cerca", "tile_en": "Coyhaique, closer than ever",
        "tilep_es": "Nuevo terminal del Aeropuerto Balmaceda desde octubre de 2026.", "tilep_en": "New Balmaceda Airport terminal since October 2026.",
        "near": [
            ("Oct 2026", "Nuevo terminal Balmaceda", "New Balmaceda terminal", "Cinco veces más grande, para más de 1 millón de pasajeros al año.", "Five times larger, for over 1 million passengers a year."),
            ("2 h 20", "Vuelo desde Santiago", "Flight from Santiago", "Directo a Balmaceda con LATAM y Sky.", "Direct to Balmaceda with LATAM and Sky."),
            ("1 h 20", "Vuelo desde Puerto Montt", "Flight from Puerto Montt", "Con Sky, JetSMART y LATAM.", "With Sky, JetSMART and LATAM."),
            ("55 km", "Balmaceda – Coyhaique", "Balmaceda – Coyhaique", "Cerca de una hora por tierra hasta la ciudad.", "About an hour by road to town."),
        ],
        "hub_es": "Desde el 5 de octubre de 2026 el Aeropuerto Balmaceda opera con un terminal nuevo: cinco veces más grande, con cinco puentes de embarque y capacidad para más de un millón de pasajeros al año. Desde Santiago son unas 2 h 20 min de vuelo directo, y luego unos 55 km hasta Coyhaique.", "hub_en": "Since 5 October 2026 Balmaceda Airport has operated a brand-new terminal: five times larger, with five jet bridges and capacity for over one million passengers a year. It is a direct flight of about 2 h 20 min from Santiago, then some 55 km by road to Coyhaique.",
    },
    {
        "key": "marmol", "slug_es": "catedrales-de-marmol", "slug_en": "marble-caves-chile", "img": "marmol3",
        "cat_es": "Imperdibles", "cat_en": "Must see",
        "title_es": "Catedrales de Mármol: guía para visitarlas", "title_en": "Marble Caves of Chile: how to visit them",
        "seo_es": "Catedrales de Mármol: cómo llegar, tours y mejor época | Parcelas con Río", "seo_en": "Marble Caves Chile: how to get there, tours and best season | Parcelas con Río",
        "desc_es": "Cómo llegar a las Capillas de Mármol del Lago General Carrera, tours en bote y kayak, mejor época y consejos.",
        "desc_en": "How to reach the Marble Chapels on Lake General Carrera, boat and kayak tours, best season and tips.",
        "tile_es": "Catedrales de Mármol", "tile_en": "The Marble Caves",
        "tilep_es": "Cavernas de mármol esculpidas por el lago más grande de Chile.", "tilep_en": "Marble caverns carved by Chile's largest lake.",
        "hub_es": "A unos 220 km al sur de Coyhaique, en Puerto Río Tranquilo, el Lago General Carrera esculpió cavernas en mármol de unos 300 millones de años. Se recorren en lancha o en kayak, y son Santuario de la Naturaleza desde 1994.", "hub_en": "About 220 km south of Coyhaique, at Puerto Río Tranquilo, Lake General Carrera has carved caves into marble some 300 million years old. You explore them by boat or kayak, and they have been a protected Nature Sanctuary since 1994.",
    },
    {
        "key": "carretera", "slug_es": "carretera-austral", "slug_en": "carretera-austral-road-trip", "img": "ruta2",
        "cat_es": "Ruta escénica", "cat_en": "Scenic route",
        "title_es": "Carretera Austral: la ruta más bella de Chile", "title_en": "Carretera Austral: Chile's most beautiful road trip",
        "seo_es": "Carretera Austral: tramos, imperdibles y mejor época | Parcelas con Río", "seo_en": "Carretera Austral road trip: sections, highlights and best time | Parcelas con Río",
        "desc_es": "Tramos, imperdibles cerca de Coyhaique, estado del camino y consejos para recorrer la Ruta 7.",
        "desc_en": "Sections, highlights near Coyhaique, road conditions and tips for driving Route 7.",
        "tile_es": "Carretera Austral", "tile_en": "Carretera Austral",
        "tilep_es": "Una de las rutas escénicas más famosas del mundo.", "tilep_en": "One of the world's most famous scenic roads.",
        "hub_es": "La Ruta 7 une pueblos, glaciares, lagos y bosques a lo largo de la Patagonia chilena. En 2026 el MOP anunció un plan de unos $800 mil millones para seguir pavimentándola hasta 2030.", "hub_en": "Route 7 links villages, glaciers, lakes and forests across Chilean Patagonia. In 2026 the Ministry of Public Works announced a plan of around CLP 800 billion to keep paving it through 2030.",
    },
    {
        "key": "ski", "slug_es": "centro-de-ski-el-fraile", "slug_en": "el-fraile-ski-coyhaique", "img": "ski",
        "cat_es": "Invierno", "cat_en": "Winter",
        "title_es": "Centro de ski El Fraile: nieve a minutos de Coyhaique", "title_en": "El Fraile ski area: snow minutes from Coyhaique",
        "seo_es": "Centro de ski El Fraile Coyhaique: temporada y cómo llegar | Parcelas con Río", "seo_en": "El Fraile ski area in Coyhaique: season and access | Parcelas con Río",
        "desc_es": "Temporada, pistas y cómo llegar al centro de ski de Coyhaique, rodeado de bosque de lengas.",
        "desc_en": "Season, runs and how to reach Coyhaique's ski area, surrounded by lenga forest.",
        "tile_es": "Nieve en El Fraile", "tile_en": "Snow at El Fraile",
        "tilep_es": "Esquí entre bosques de lenga, cerca de la ciudad.", "tilep_en": "Skiing among lenga forests, close to town.",
        "hub_es": "A 29 km de Coyhaique, el centro de ski El Fraile ofrece nieve entre bosques de lenga, en general de junio a septiembre. Para esquiar o caminar con raquetas sin salir de la región.", "hub_en": "Just 29 km from Coyhaique, the El Fraile ski area offers snow among lenga forests, usually from June to September. Ski or go snowshoeing without leaving the region.",
    },
    {
        "key": "pesca", "slug_es": "pesca-con-mosca-en-aysen", "slug_en": "fly-fishing-aysen-patagonia", "img": "lago_frio_pesca_embarcacion",
        "cat_es": "Pesca", "cat_en": "Fishing",
        "title_es": "Pesca con mosca en Aysén: ríos, temporada y licencia", "title_en": "Fly fishing in Aysén: rivers, season and licence",
        "seo_es": "Pesca con mosca en Aysén: mejores ríos y temporada | Parcelas con Río", "seo_en": "Fly fishing in Aysén, Chilean Patagonia: rivers and season | Parcelas con Río",
        "desc_es": "Los mejores ríos de Aysén para pescar truchas, fechas de la temporada y cómo sacar la licencia de pesca.",
        "desc_en": "The best Aysén rivers for trout, season dates and how to get a fishing licence.",
        "tile_es": "Pesca con mosca", "tile_en": "Fly fishing",
        "tilep_es": "Ríos de clase mundial para truchas.", "tilep_en": "World-class trout rivers.",
        "hub_es": "La temporada de pesca recreativa 2026–2027 en Aysén va del 12 de octubre al 6 de mayo. Ríos como el Simpson, el Mañihuales y el Emperador Guillermo son famosos por sus truchas arcoíris y café.", "hub_en": "Aysén’s 2026–2027 recreational fishing season runs from 12 October to 6 May. Rivers such as the Simpson, the Mañihuales and the Emperador Guillermo are famous for their rainbow and brown trout.",
    },
    {
        "key": "castillo", "slug_es": "trekking-en-aysen-cerro-castillo", "slug_en": "hiking-aysen-cerro-castillo", "img": "ccastillo1",
        "cat_es": "Trekking", "cat_en": "Hiking",
        "title_es": "Trekking en Aysén: Cerro Castillo, Queulat y más", "title_en": "Hiking in Aysén: Cerro Castillo, Queulat and more",
        "seo_es": "Trekking Cerro Castillo y parques de Aysén: guía | Parcelas con Río", "seo_en": "Cerro Castillo trek and Aysén national parks: guide | Parcelas con Río",
        "desc_es": "Circuito Cerro Castillo, Ventisquero Colgante de Queulat y senderos cerca de Coyhaique: temporadas y reservas.",
        "desc_en": "Cerro Castillo circuit, Queulat Hanging Glacier and trails near Coyhaique: seasons and bookings.",
        "tile_es": "Trekking y glaciares", "tile_en": "Trekking and glaciers",
        "tilep_es": "Cerro Castillo y el Ventisquero Colgante.", "tilep_en": "Cerro Castillo and the Hanging Glacier.",
        "hub_es": "En el Parque Nacional Cerro Castillo, al sur de Coyhaique, está la travesía Las Horquetas: 53,5 km en 3 a 5 días. Más al norte, el Ventisquero Colgante del Parque Nacional Queulat cae sobre la Laguna Témpanos.", "hub_en": "Cerro Castillo National Park, south of Coyhaique, is home to the Las Horquetas trek: 53.5 km over 3 to 5 days. Further north, the Hanging Glacier of Queulat National Park drops towards Laguna Témpanos.",
    },
    {
        "key": "vivir", "slug_es": "vivir-en-coyhaique", "slug_en": "living-in-coyhaique-patagonia", "img": "coy1",
        "cat_es": "Vivir en la Patagonia", "cat_en": "Living in Patagonia",
        "title_es": "Vivir en Coyhaique: calidad de vida en la Patagonia", "title_en": "Living in Coyhaique: quality of life in Patagonia",
        "seo_es": "Vivir en Coyhaique: clima, servicios y calidad de vida | Parcelas con Río", "seo_en": "Living in Coyhaique, Chile: climate, services and lifestyle | Parcelas con Río",
        "desc_es": "Clima por estación, servicios, conectividad y estilo de vida en la capital de Aysén.",
        "desc_en": "Seasonal climate, services, connectivity and lifestyle in the capital of Aysén.",
        "tile_es": "Vivir en Coyhaique", "tile_en": "Living in Coyhaique",
        "tilep_es": "Ciudad con servicios, rodeada de naturaleza.", "tilep_en": "A town with services, surrounded by nature.",
        "hub_es": "Coyhaique tiene 57.823 habitantes (Censo 2024), hospital regional, universidades y un comercio en crecimiento, rodeada de reservas naturales. Una ciudad con servicios y la naturaleza a minutos.", "hub_en": "Coyhaique has 57,823 residents (2024 Census), a regional hospital, universities and growing retail, surrounded by nature reserves. A town with services and the wild just minutes away.",
    },
    {
        "key": "comprar", "slug_es": "comprar-parcela-en-la-patagonia", "slug_en": "buying-land-in-chilean-patagonia", "img": "pradera",
        "cat_es": "Guía de compra", "cat_en": "Buyer's guide",
        "title_es": "Cómo comprar una parcela en la Patagonia chilena", "title_en": "How to buy land in Chilean Patagonia",
        "seo_es": "Comprar parcela en la Patagonia: guía legal y práctica | Parcelas con Río", "seo_en": "Buying land in Chilean Patagonia: legal and practical guide | Parcelas con Río",
        "desc_es": "Rol propio, subdivisión de predios rústicos, qué revisar antes de comprar y si los extranjeros pueden comprar en Chile.",
        "desc_en": "Property titles, rural subdivisions, what to check before buying and whether foreigners can buy land in Chile.",
        "tile_es": "Comprar tu parcela", "tile_en": "Buying your plot",
        "tilep_es": "Todo lo que debes revisar antes de firmar.", "tilep_en": "Everything to check before you sign.",
        "hub_es": "Antes de comprar conviene revisar el rol, los certificados del Conservador, las servidumbres y los derechos de agua. Los extranjeros pueden comprar con RUT, sin necesidad de residencia.", "hub_en": "Before buying, check the property roll, the Land Registry certificates, rights-of-way and water rights. Foreigners can buy with a Chilean tax ID (RUT), without residency.",
    },
]

for _a in ARTICLES:
    _a.setdefault("updated", "15-11-2026")
    _a.setdefault("updated_iso", "2026-11-15")
    for _lang in ("es", "en"):
        _f = os.path.join(POSTS_DIR, f"{_a['key']}_{_lang}.html")
        _a[f"body_{_lang}"] = open(_f, encoding="utf-8").read() if os.path.exists(_f) else "<p>…</p>"
    # Índice y tiempo de lectura: posts/<key>.json -> {"toc_es": [[id, título], ...], "toc_en": [...], "read": 8}
    _j = os.path.join(POSTS_DIR, f"{_a['key']}.json")
    if os.path.exists(_j):
        _a.update(json.load(open(_j, encoding="utf-8")))
