"""Datos del sitio: proyectos, imágenes y artículos del blog (metadatos)."""

# Imágenes. "credit" se muestra sobre la foto cuando la licencia lo exige.
# Las fotos de paisajes provienen del material del cliente (Terrazas del Fraile)
# y se usan como referencia del territorio, nunca como foto de un lote.
IMG = {
    "hero_poster": {"src": "assets/img/hero/desktop/primavera.webp"},
    "coyhaique": {"src": "assets/img/patagonia/coyhaique-1200.webp", "alt_es": "Vista aérea de Coyhaique con cerros nevados", "alt_en": "Aerial view of Coyhaique with snowy peaks"},
    "carretera": {"src": "assets/img/patagonia/hero-carretera-austral.webp", "alt_es": "Carretera Austral entre paredes de roca en Aysén", "alt_en": "Carretera Austral between rock walls in Aysén"},
    "carretera2": {"src": "assets/img/patagonia/carretera-austral-1200.webp", "alt_es": "Valle y camino en la Región de Aysén", "alt_en": "Valley and road in the Aysén Region"},
    "castillo": {"src": "assets/img/patagonia/cerro-castillo-1200.webp", "alt_es": "Cumbres nevadas sobre bosques en Aysén", "alt_en": "Snowy peaks above forests in Aysén"},
    "ski": {"src": "assets/img/patagonia/centro-ski-invierno.webp", "alt_es": "Pistas de esquí nevadas entre bosques cerca de Coyhaique", "alt_en": "Snowy ski runs among forests near Coyhaique"},
    "ski_otono": {"src": "assets/img/patagonia/centro-ski-otono.webp", "alt_es": "Centro de ski con nieve y sol", "alt_en": "Ski area with snow and sun"},
    "salto": {"src": "assets/img/patagonia/el-salto-1200.webp", "alt_es": "Pueblo entre colinas con colores de otoño en Aysén", "alt_en": "Village among hills in autumn colours, Aysén"},
    "lago": {"src": "assets/img/paisajes/lago-azul.webp", "alt_es": "Lago azul rodeado de colinas en la Patagonia", "alt_en": "Blue lake surrounded by hills in Patagonia"},
    "lago_bote": {"src": "assets/img/paisajes/lago-bote.webp", "alt_es": "Bote de pesca en un lago calmo de Aysén", "alt_en": "Fishing boat on a calm lake in Aysén"},
    "lago_reflejo": {"src": "assets/img/paisajes/lago-reflejo.webp", "alt_es": "Lago con reflejo de montañas nevadas", "alt_en": "Lake reflecting snowy mountains"},
    "lengas": {"src": "assets/img/paisajes/lengas-otono.webp", "alt_es": "Bosque de lengas rojas en otoño", "alt_en": "Red lenga forest in autumn"},
    "lenga_roja": {"src": "assets/img/paisajes/lenga-roja.webp", "alt_es": "Lenga roja en otoño patagónico", "alt_en": "Red lenga tree in Patagonian autumn"},
    "hojas": {"src": "assets/img/paisajes/hojas-lenga.webp", "alt_es": "Hojas de lenga en otoño", "alt_en": "Lenga leaves in autumn"},
    "pradera": {"src": "assets/img/paisajes/pradera-primavera.webp", "alt_es": "Pradera y bosque nativo en primavera", "alt_en": "Meadow and native forest in spring"},
    "valle": {"src": "assets/img/paisajes/valle-primavera.webp", "alt_es": "Valle verde con bosque nativo en Aysén", "alt_en": "Green valley with native forest in Aysén"},
    "bosque_aereo": {"src": "assets/img/paisajes/bosque-aereo.webp", "alt_es": "Vista aérea de bosque nativo", "alt_en": "Aerial view of native forest"},
    "bosque": {"src": "assets/img/paisajes/bosque-interior.webp", "alt_es": "Interior de bosque nativo", "alt_en": "Inside a native forest"},
    "plano_manihuales": {"src": "assets/img/proyectos/plano-horizontes-manihuales.jpg", "alt_es": "Plano aéreo de los cuatro lotes de Horizontes de Mañihuales", "alt_en": "Aerial plan of the four lots at Horizontes de Mañihuales"},
    "paisaje_lago": {"src": "assets/img/proyectos/paisaje-lago.jpg", "alt_es": "Lago y cerros del sur de Chile con álamos", "alt_en": "Lake and hills in southern Chile with poplars"},
}

# Proyectos. "img" es referencial del territorio (se rotula así en el sitio).
PROJECTS = [
    {
        "slug": "horizontes-de-manihuales", "name": "Horizontes de Mañihuales", "r": "XI",
        "region_es": "Región de Aysén · Patagonia", "region_en": "Aysén Region · Patagonia",
        "status_es": "3 de 4 disponibles", "status_en": "3 of 4 available", "badge_es": "Nuevo", "badge_en": "New", "sold": False, "pct": 25,
        "short_es": "4 parcelas de 0,53 a 1 ha frente al río Mañihuales, con acceso por servidumbre y factibilidad eléctrica.",
        "short_en": "4 plots of 0.53 to 1 ha facing the Mañihuales River, with right-of-way access and electricity feasibility.",
        "img": "valle", "detail": True,
    },
    {
        "slug": "don-guillermo", "name": "Parcelas Don Guillermo", "r": "XI",
        "region_es": "Región de Aysén · Carretera Austral", "region_en": "Aysén Region · Carretera Austral",
        "status_es": "Queda 1 parcela", "status_en": "1 plot left", "badge_es": "Última", "badge_en": "Last one", "sold": False, "pct": 95,
        "short_es": "Frente al río Emperador Guillermo, en plena Carretera Austral.",
        "short_en": "Facing the Emperador Guillermo River, right on the Carretera Austral.",
        "img": "carretera2", "detail": True,
    },
    {
        "slug": "rofuco-bajo", "name": "Parcelas Rofuco Bajo", "r": "XIV",
        "region_es": "Región de Los Ríos", "region_en": "Los Ríos Region",
        "status_es": "57% vendido", "status_en": "57% sold", "badge_es": "En venta", "badge_en": "For sale", "sold": False, "pct": 57,
        "short_es": "Parcelas en el sector de Rofuco Bajo, en la Región de Los Ríos.",
        "short_en": "Plots in the Rofuco Bajo area, Los Ríos Region.",
        "img": "paisaje_lago", "detail": True,
    },
    {
        "slug": "dona-cecilia", "name": "Parcelación Doña Cecilia", "r": "VII",
        "region_es": "Región del Maule", "region_en": "Maule Region",
        "status_es": "Últimas 6 parcelas", "status_en": "Last 6 plots", "badge_es": "Últimas", "badge_en": "Last plots", "sold": False, "pct": 85,
        "short_es": "Últimas parcelas disponibles en la Región del Maule.",
        "short_en": "Last plots available in the Maule Region.",
        "img": "pradera", "detail": True,
    },
    {
        "slug": "altos-de-villa-medina", "name": "Altos de Villa Medina", "r": "XI",
        "region_es": "Región de Aysén · Coyhaique", "region_en": "Aysén Region · Coyhaique",
        "status_es": "100% vendido", "status_en": "100% sold", "badge_es": "Vendido", "badge_en": "Sold out", "sold": True, "pct": 100,
        "short_es": "A menos de 20 minutos de Coyhaique y a 1 km de la Carretera Austral.",
        "short_en": "Less than 20 minutes from Coyhaique and 1 km from the Carretera Austral.",
        "img": "salto", "detail": False,
    },
]

MANIHUALES_LOTS = [
    ("1", "0,610 ha · 6.100 m²", "0.610 ha · 6,100 m²", False),
    ("2", "0,529 ha · 5.290 m²", "0.529 ha · 5,290 m²", False),
    ("3", "0,861 ha · 8.610 m²", "0.861 ha · 8,610 m²", True),
    ("4", "1 ha · 10.000 m²", "1 ha · 10,000 m²", False),
]
