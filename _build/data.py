"""Datos del sitio: proyectos, imágenes y artículos del blog (metadatos)."""

# Imágenes. "credit" se muestra sobre la foto cuando la licencia lo exige.
# Las fotos de paisajes provienen del material del cliente (Terrazas del Fraile)
# y se usan como referencia del territorio, nunca como foto de un lote.
IMG = {
    "hero_poster": {"src": "assets/img/bienvenida/home-v2-poster-1280.jpg"},
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
    "plano_manihuales": {"src": "assets/img/proyectos/plano-horizontes-manihuales-v2.jpg", "w": 760, "h": 1141, "alt_es": "Plano aéreo de los cuatro lotes de Horizontes de Mañihuales", "alt_en": "Aerial plan of the four lots at Horizontes de Mañihuales"},
    "plano_dc_disponibles": {"src": "assets/img/proyectos/plano-dona-cecilia-disponibles.webp", "w": 1920, "h": 1080, "alt_es": "Plano de subdivisión de Parcelación Doña Cecilia: en verde las parcelas disponibles 6, 8, 14, 15, 16 y 17; en rojo las vendidas y en azul la reservada", "alt_en": "Parcelación Doña Cecilia subdivision plan: available plots 6, 8, 14, 15, 16 and 17 in green, sold in red and reserved in blue"},
    "plano_dc_disponibles_movil": {"src": "assets/img/proyectos/plano-dona-cecilia-disponibles-movil.webp", "w": 1040, "h": 1080, "alt_es": "Plano de Parcelación Doña Cecilia con las parcelas disponibles en verde", "alt_en": "Parcelación Doña Cecilia plan with available plots in green"},
    "plano_dc_lotes": {"src": "assets/img/proyectos/plano-dona-cecilia-lotes.webp", "w": 1010, "h": 962, "alt_es": "Plano general de Parcelación Doña Cecilia con los deslindes, el camino interior y la superficie de cada lote", "alt_en": "General plan of Parcelación Doña Cecilia with boundaries, internal road and the area of each lot"},
    **{f"rofuco_{i}": {"src": f"assets/img/proyectos/rofuco-bajo/rofuco-bajo-{i}.webp", "w": 1280, "h": 716, "alt_es": a_es, "alt_en": a_en} for i, a_es, a_en in [
        (1, "Pradera y camino interior en Parcelas Rofuco Bajo", "Meadow and internal road at Parcelas Rofuco Bajo"),
        (2, "Praderas abiertas con árboles nativos en Rofuco Bajo", "Open meadows with native trees at Rofuco Bajo"),
        (3, "Gran árbol nativo sobre la pradera de Rofuco Bajo", "Large native tree over the Rofuco Bajo meadow"),
        (4, "Borde de bosque junto a la pradera en Rofuco Bajo", "Forest edge next to the meadow at Rofuco Bajo"),
        (5, "Árboles altos y pradera en Rofuco Bajo", "Tall trees and meadow at Rofuco Bajo"),
        (6, "Vista amplia de praderas y bosque en Rofuco Bajo", "Wide view of meadows and forest at Rofuco Bajo"),
        (7, "Construcciones en el sector de acceso de Rofuco Bajo", "Buildings at the entrance area of Rofuco Bajo")]},
    "rofuco_8": {"src": "assets/img/proyectos/rofuco-bajo/rofuco-bajo-8.webp", "w": 716, "h": 479, "alt_es": "Copas de los árboles del bosque de Rofuco Bajo vistas desde abajo", "alt_en": "Tree canopy of the Rofuco Bajo forest seen from below"},
    "paisaje_lago": {"src": "assets/img/proyectos/paisaje-lago.jpg", "alt_es": "Lago y cerros del sur de Chile con álamos", "alt_en": "Lake and hills in southern Chile with poplars"},
}

# Proyectos. "img" es referencial del territorio (se rotula así en el sitio).
PROJECTS = [
    {
        "slug": "horizontes-de-manihuales", "name": "Horizontes de Mañihuales", "r": "XI",
        "region_es": "Región de Aysén · Villa Mañihuales", "region_en": "Aysén Region · Villa Mañihuales",
        "status_es": "3 de 4 disponibles", "status_en": "3 of 4 available", "badge_es": "En verde", "badge_en": "Off-plan", "sold": False, "pct": 25,
        "short_es": "4 parcelas de 0,53 a 1 ha frente al río Mañihuales, con acceso por camino público. Desde $28.000.000.",
        "short_en": "4 plots of 0.53 to 1 ha facing the Mañihuales River, with public road access. From CLP 28,000,000.",
        "img": "rio_manihuales_meandro", "real": True, "detail": True, "sim": True,
        "river_es": "Frente al río Mañihuales", "river_en": "Facing the Mañihuales River",
        "map": (-45.069827, -72.161309),
        "gallery": ["rio_manihuales_meandro", "rio_manihuales_ribera", "manihuales_entorno_verde", "manihuales_vista_horizontal"],
        "video": "assets/video/proyectos/horizontes-de-manihuales.mp4",
    },
    {
        "slug": "don-guillermo", "name": "Parcelas Don Guillermo", "r": "XI",
        "region_es": "Región de Aysén · Carretera Austral", "region_en": "Aysén Region · Carretera Austral",
        "status_es": "Única disponible: B11", "status_en": "Only plot left: B11", "badge_es": "Última", "badge_en": "Last one", "sold": False, "pct": 95,
        "short_es": "Frente al río Emperador Guillermo, en plena Carretera Austral. Queda solo la parcela B11, de 9.500 m².",
        "short_en": "Facing the Emperador Guillermo River, right on the Carretera Austral. Only plot B11 (9,500 m²) is left.",
        "img": "carretera2", "detail": True,
        "river_es": "Frente al río Emperador Guillermo", "river_en": "Facing the Emperador Guillermo River",
        "map": (-45.2840594, -72.1713018),
        "plan": "plano_don_guillermo",
    },
    {
        "slug": "rofuco-bajo", "name": "Parcelas Rofuco Bajo", "r": "XIV",
        "region_es": "Región de Los Ríos", "region_en": "Los Ríos Region",
        "status_es": "22 disponibles · 63% vendido", "status_en": "22 available · 63% sold", "badge_es": "En venta", "badge_en": "For sale", "sold": False, "pct": 63,
        "short_es": "Parcelación de praderas en la Región de Los Ríos, con acceso desde la Ruta 5 Sur. Desde $24.500.000 hasta $28.000.000.",
        "short_en": "Meadow plots in the Los Ríos Region, with access from Route 5 South. From CLP 24,500,000 to 28,000,000.",
        "img": "rofuco_2", "real": True, "detail": True,
        "masterplan": "https://virtualplan360.cl/masterplan/parcelas_rofuco_bajo/index.html",
        "map": (-40.2555457, -72.9079419),
        "directions": "https://maps.app.goo.gl/xWtajy56t5PBxSAa8",
        "facts": ["sag", "rol"],
        "gallery": ["rofuco_1", "rofuco_2", "rofuco_3", "rofuco_4", "rofuco_5", "rofuco_6", "rofuco_7", "rofuco_8"],
    },
    {
        "slug": "dona-cecilia", "name": "Parcelación Doña Cecilia", "r": "VII",
        "region_es": "Región del Maule · San Clemente", "region_en": "Maule Region · San Clemente",
        "status_es": "Últimas 6 parcelas", "status_en": "Last 6 plots", "badge_es": "Últimas", "badge_en": "Last plots", "sold": False, "pct": 85,
        "short_es": "Últimas 6 parcelas de 5.000 m² entre praderas y cerros en San Clemente, Región del Maule. $19.500.000 al contado.",
        "short_en": "Last 6 plots of 5,000 m² among meadows and hills in San Clemente, Maule Region. CLP 19,500,000 cash price.",
        "img": "dona_cecilia_panorama_rural", "real": True, "detail": True, "sim": True,
        "map": (-35.4731667, -71.2953611),
        "directions": "https://maps.app.goo.gl/EXbZFjXgswrzoDWf6",
        "masterplan": "https://www.helisterra.com/proyectos_helisterra/Do%C3%B1aCecilia/",
        "facts": ["sag", "rol", "luz"],
        "gallery": ["dona_cecilia_panorama_rural", "dona_cecilia_camino_de_acceso", "dona_cecilia_camino_y_caballos", "dona_cecilia_campo_y_cerros", "dona_cecilia_terrenos_planos", "dona_cecilia_valle_aereo", "dona_cecilia_camino_aereo", "dona_cecilia_trazado_aereo"],
        "gallery2": ["maule_cascada_y_poza", "maule_embalse_vista_aerea", "maule_embalse_y_montanas"],
    },
    {
        "slug": "altos-de-villa-medina", "name": "Altos de Villa Medina", "r": "XI",
        "region_es": "Región de Aysén · Coyhaique", "region_en": "Aysén Region · Coyhaique",
        "status_es": "100% vendido", "status_en": "100% sold", "badge_es": "Vendido", "badge_en": "Sold out", "sold": True, "pct": 100,
        "short_es": "A menos de 20 minutos de Coyhaique y a 1 km de la Carretera Austral.",
        "short_en": "Less than 20 minutes from Coyhaique and 1 km from the Carretera Austral.",
        "img": "villa_medina_valle_aereo", "real": True, "detail": False,
    },
    {
        "slug": "rio-simpson", "name": "Parcelas Río Simpson", "r": "XI",
        "region_es": "Región de Aysén", "region_en": "Aysén Region",
        "status_es": "100% vendido · 2022", "status_en": "100% sold · 2022", "badge_es": "Vendido", "badge_en": "Sold out", "sold": True, "pct": 100,
        "short_es": "Proyecto junto al río Simpson, vendido completamente en 2022.",
        "short_en": "Project next to the Simpson River, completely sold out in 2022.",
        "img": "simpson3", "detail": False,
    },
]

# Horizontes de Mañihuales: (n, total, servidumbre, útil, precio CLP, reservada)
MANIHUALES_LOTS = [
    ("1", "0,610 ha", "0,110 ha", "0,50 ha", 28000000, False),
    ("2", "0,529 ha", "0,029 ha", "0,50 ha", 28000000, False),
    ("3", "0,861 ha", "0,031 ha", "0,830 ha", 33000000, True),
    ("4", "1,00 ha", "—", "1,00 ha", 38000000, False),
]

# Simulador de crédito directo por proyecto (solo proyectos con condiciones confirmadas)
# San Clemente (Parcelación Doña Cecilia): parcelas disponibles, todas de 5.000 m².
# Precio de lista $21.000.000; beneficio por pago al contado $1.500.000; precio al contado $19.500.000.
# Validado con el cliente (22-nov-2026): el crédito directo se calcula sobre el precio de lista; los $19.500.000 son solo
# el precio al contado. Todos los montos del simulador se muestran en pesos.
SAN_CLEMENTE_LOTS = ["6", "8", "14", "15", "16", "17"]

SIMULATOR = {
    "Horizontes de Mañihuales": {"plans": [(50, 24)], "lots": [(f"Parcela {n}", price) for n, _, _, _, price, res in MANIHUALES_LOTS if not res]},
    "San Clemente · Parcelación Doña Cecilia": {
        "plans": [(50, 24)],
        "lots": [(f"Parcela {n} · 5.000 m²", 21000000) for n in SAN_CLEMENTE_LOTS],
        "list": 21000000, "discount": 1500000,
        "note_es": "Crédito directo con 50% de pie y saldo en 24 cuotas en UF, sin intereses. Cuota referencial equivalente a $437.500 mensuales. Su valor en pesos varía según la UF aplicable.",
        "note_en": "Direct financing with 50% down and the balance in 24 instalments set in UF, with no interest. Reference instalment equivalent to CLP 437,500 per month. Its value in pesos varies with the applicable UF.",
    },
}

# Fotos de Wikimedia Commons (licencias CC; requieren crédito). Generado desde el manifiesto.
IMG.update({
    'marmol1': {"src": "assets/img/libres/catedrales-de-marmol-1.jpg", "alt_es": 'Catedral de Mármol', "alt_en": 'Catedral de Mármol', "credit": 'Jpmorenosanchez / <a href="https://commons.wikimedia.org/wiki/File:Lago_General_Carrera_-_Capillas_de_M%C3%A1rmol.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Catedral de Mármol (islote principal) sobre el Lago General Carrera, con cordillera nevada al fondo; día nublado: Jpmorenosanchez / <a href="https://commons.wikimedia.org/wiki/File:Lago_General_Carrera_-_Capillas_de_M%C3%A1rmol.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'marmol2': {"src": "assets/img/libres/catedrales-de-marmol-2.jpg", "alt_es": 'Interior de las cavernas de mármol', "alt_en": 'Interior de las cavernas de mármol', "credit": 'Nicolás Lara / <a href="https://commons.wikimedia.org/wiki/File:Catedral_de_M%C3%A1rmol_en_Lago_General_Carrera.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>', "credit_full": 'Interior de las cavernas de mármol (Capillas de Mármol) con agua turquesa del Lago General Carrera, cerca de Puerto Río Tranquilo: Nicolás Lara / <a href="https://commons.wikimedia.org/wiki/File:Catedral_de_M%C3%A1rmol_en_Lago_General_Carrera.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>'},
    'marmol3': {"src": "assets/img/libres/catedrales-de-marmol-3.jpg", "alt_es": 'La Capilla de Mármol', "alt_en": 'La Capilla de Mármol', "credit": 'Sissssou / <a href="https://commons.wikimedia.org/wiki/File:Capilla_de_Marmol_2017.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'La Capilla de Mármol (islote) con cielo azul y agua turquesa, Lago General Carrera, Puerto Río Tranquilo: Sissssou / <a href="https://commons.wikimedia.org/wiki/File:Capilla_de_Marmol_2017.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'marmol4': {"src": "assets/img/libres/catedrales-de-marmol-4.jpg", "alt_es": 'Interior de la Catedral de Mármol: vetas de mármol y agua turquesa', "alt_en": 'Interior de la Catedral de Mármol: vetas de mármol y agua turquesa', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Catedral_de_M%C3%A1rmol_interior.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Interior de la Catedral de Mármol: vetas de mármol y agua turquesa (geolocalizada en las Capillas, Puerto Río Tranquilo): Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Catedral_de_M%C3%A1rmol_interior.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'ruta1': {"src": "assets/img/libres/carretera-austral-1.jpg", "alt_es": 'Carretera Austral', "alt_en": 'Carretera Austral', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Carretera_Austral_al_norte_de_Cerro_Castillo.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Carretera Austral (Ruta 7) pavimentada hacia el sur, al norte de Villa Cerro Castillo, con montañas al fondo: Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Carretera_Austral_al_norte_de_Cerro_Castillo.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'ruta2': {"src": "assets/img/libres/carretera-austral-2.jpg", "alt_es": 'Carretera Austral pavimentada con cerro nevado y señalética vial', "alt_en": 'Carretera Austral pavimentada con cerro nevado y señalética vial', "credit": 'Camila Eyzaguirre / <a href="https://commons.wikimedia.org/wiki/File:Carretera_Austral_(255633637).jpeg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>', "credit_full": 'Carretera Austral pavimentada con cerro nevado y señalética vial (geolocalizada en -46: Camila Eyzaguirre / <a href="https://commons.wikimedia.org/wiki/File:Carretera_Austral_(255633637).jpeg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>'},
    'ruta3': {"src": "assets/img/libres/carretera-austral-3.jpg", "alt_es": 'Tramo de ripio de la Carretera Austral', "alt_en": 'Tramo de ripio de la Carretera Austral', "credit": 'Rakela / <a href="https://commons.wikimedia.org/wiki/File:Carretera_Austral_-_Leones.JPG" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>', "credit_full": 'Tramo de ripio de la Carretera Austral (Ruta 7) en el sector Leones, con macizo nevado (Campo de Hielo Norte) al fondo: Rakela / <a href="https://commons.wikimedia.org/wiki/File:Carretera_Austral_-_Leones.JPG" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>'},
    'ruta4': {"src": "assets/img/libres/carretera-austral-4.jpg", "alt_es": 'Carretera Austral', "alt_en": 'Carretera Austral', "credit": 'Abbagliati / <a href="https://commons.wikimedia.org/wiki/File:Lago_Bertrand.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Carretera Austral (Ruta CH-7) de ripio con vista al Lago Bertrand y Lago General Carrera: Abbagliati / <a href="https://commons.wikimedia.org/wiki/File:Lago_Bertrand.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'ccastillo1': {"src": "assets/img/libres/cerro-castillo-1.jpg", "alt_es": 'Panorámica de la Laguna Cerro Castillo', "alt_en": 'Panorámica de la Laguna Cerro Castillo', "credit": 'Fotogalilea / <a href="https://commons.wikimedia.org/wiki/File:Laguna_Cerro_Castillo.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Panorámica de la Laguna Cerro Castillo (turquesa) bajo las agujas del Cerro Castillo, Reserva/Parque Nacional Cerro Castillo: Fotogalilea / <a href="https://commons.wikimedia.org/wiki/File:Laguna_Cerro_Castillo.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'ccastillo2': {"src": "assets/img/libres/cerro-castillo-2.jpg", "alt_es": 'Cerro Castillo y su glaciar vistos desde la laguna a sus pies', "alt_en": 'Cerro Castillo y su glaciar vistos desde la laguna a sus pies', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Cerro_Castillo_2016.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Cerro Castillo y su glaciar vistos desde la laguna a sus pies (punto clásico del trekking): Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Cerro_Castillo_2016.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'ccastillo3': {"src": "assets/img/libres/cerro-castillo-3.jpg", "alt_es": 'Sendero de trekking en el Parque Nacional Cerro Castillo: valle con bosque de lenga y cumbres nevadas', "alt_en": 'Sendero de trekking en el Parque Nacional Cerro Castillo: valle con bosque de lenga y cumbres nevadas', "credit": 'Natalia Reyes Escobar / <a href="https://commons.wikimedia.org/wiki/File:Sendero_Parque_Nacional_Cerro_Castillo_06.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Sendero de trekking en el Parque Nacional Cerro Castillo: valle con bosque de lenga y cumbres nevadas: Natalia Reyes Escobar / <a href="https://commons.wikimedia.org/wiki/File:Sendero_Parque_Nacional_Cerro_Castillo_06.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'ccastillo4': {"src": "assets/img/libres/cerro-castillo-4.jpg", "alt_es": 'Cerro Castillo y su glaciar, Parque Nacional Cerro Castillo', "alt_en": 'Cerro Castillo y su glaciar, Parque Nacional Cerro Castillo', "credit": 'Natalia Reyes Escobar / <a href="https://commons.wikimedia.org/wiki/File:Cerro_Castillo_y_Glaciar_Parque_Nacional_Cerro_Castillo_16.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Cerro Castillo y su glaciar, Parque Nacional Cerro Castillo: Natalia Reyes Escobar / <a href="https://commons.wikimedia.org/wiki/File:Cerro_Castillo_y_Glaciar_Parque_Nacional_Cerro_Castillo_16.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'queulat1': {"src": "assets/img/libres/queulat-1.jpg", "alt_es": 'Ventisquero Colgante y su cascada enmarcados por bosque, Parque Nacional Queulat', "alt_en": 'Ventisquero Colgante y su cascada enmarcados por bosque, Parque Nacional Queulat', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Ventisquero_Colgante.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Ventisquero Colgante y su cascada enmarcados por bosque, Parque Nacional Queulat: Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Ventisquero_Colgante.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'queulat2': {"src": "assets/img/libres/queulat-2.jpg", "alt_es": 'Panorámica del Ventisquero Colgante, sus cascadas y la Laguna Témpanos, Parque Nacional Queulat', "alt_en": 'Panorámica del Ventisquero Colgante, sus cascadas y la Laguna Témpanos, Parque Nacional Queulat', "credit": 'Jdzip / <a href="https://commons.wikimedia.org/wiki/File:Panoramica_Glaciar_Ventisquero_Colgante.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Panorámica del Ventisquero Colgante, sus cascadas y la Laguna Témpanos, Parque Nacional Queulat: Jdzip / <a href="https://commons.wikimedia.org/wiki/File:Panoramica_Glaciar_Ventisquero_Colgante.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'queulat3': {"src": "assets/img/libres/queulat-3.jpg", "alt_es": 'Laguna Témpanos con el Ventisquero Colgante al fondo, día despejado, Parque Nacional Queulat', "alt_en": 'Laguna Témpanos con el Ventisquero Colgante al fondo, día despejado, Parque Nacional Queulat', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Laguna_T%C3%A9mpanos.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Laguna Témpanos con el Ventisquero Colgante al fondo, día despejado, Parque Nacional Queulat: Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Laguna_T%C3%A9mpanos.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'queulat4': {"src": "assets/img/libres/queulat-4.jpg", "alt_es": 'Ventisquero Colgante visto desde la Laguna Témpanos, con nubes bajas, Parque Nacional Queulat', "alt_en": 'Ventisquero Colgante visto desde la Laguna Témpanos, con nubes bajas, Parque Nacional Queulat', "credit": 'Lin linao / <a href="https://commons.wikimedia.org/wiki/File:Ventisquero_Queulat_desde_la_laguna_T%C3%A9mpanos.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Ventisquero Colgante visto desde la Laguna Témpanos, con nubes bajas, Parque Nacional Queulat: Lin linao / <a href="https://commons.wikimedia.org/wiki/File:Ventisquero_Queulat_desde_la_laguna_T%C3%A9mpanos.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'coy1': {"src": "assets/img/libres/coyhaique-1.jpg", "alt_es": 'Cerro Mackay con nubes, bosque y río', "alt_en": 'Cerro Mackay con nubes, bosque y río', "credit": 'Jorge Pacheco / <a href="https://commons.wikimedia.org/wiki/File:Coyhaique_(25591820638).jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/2.0" target="_blank" rel="noopener nofollow">CC BY-SA 2.0</a>', "credit_full": 'Cerro Mackay con nubes, bosque y río (Simpson) con puente, en Coyhaique: Jorge Pacheco / <a href="https://commons.wikimedia.org/wiki/File:Coyhaique_(25591820638).jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/2.0" target="_blank" rel="noopener nofollow">CC BY-SA 2.0</a>'},
    'coy2': {"src": "assets/img/libres/coyhaique-2.jpg", "alt_es": 'Vista panorámica de la ciudad de Coyhaique y el Cerro Mackay desde la Reserva Nacional Coyhaique, con Andes nevados al fondo', "alt_en": 'Vista panorámica de la ciudad de Coyhaique y el Cerro Mackay desde la Reserva Nacional Coyhaique, con Andes nevados al fondo', "credit": 'Rakela / <a href="https://commons.wikimedia.org/wiki/File:Coyhaique_desde_la_RNC.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>', "credit_full": 'Vista panorámica de la ciudad de Coyhaique y el Cerro Mackay desde la Reserva Nacional Coyhaique, con Andes nevados al fondo (lleva marca de agua \'RHK\' en la esquina): Rakela / <a href="https://commons.wikimedia.org/wiki/File:Coyhaique_desde_la_RNC.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>'},
    'coy3': {"src": "assets/img/libres/coyhaique-3.jpg", "alt_es": 'Cerro Mackay visto desde la Carretera Austral en Coyhaique, con locomóvil antiguo en primer plano', "alt_en": 'Cerro Mackay visto desde la Carretera Austral en Coyhaique, con locomóvil antiguo en primer plano', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Cerro_Mackay.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Cerro Mackay visto desde la Carretera Austral en Coyhaique, con locomóvil antiguo en primer plano: Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Cerro_Mackay.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'coy4': {"src": "assets/img/libres/coyhaique-4.jpg", "alt_es": 'Laguna Verde rodeada de bosque, Reserva Nacional Coyhaique', "alt_en": 'Laguna Verde rodeada de bosque, Reserva Nacional Coyhaique', "credit": 'Natalia Reyes Escobar / <a href="https://commons.wikimedia.org/wiki/File:Laguna_Verde_Reserva_Nacional_Coyhaique_08.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Laguna Verde rodeada de bosque, Reserva Nacional Coyhaique: Natalia Reyes Escobar / <a href="https://commons.wikimedia.org/wiki/File:Laguna_Verde_Reserva_Nacional_Coyhaique_08.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'baker1': {"src": "assets/img/libres/rio-baker-1.jpg", "alt_es": 'Confluencia del Río Baker con el Río Nef: aguas turquesa y rápidos', "alt_en": 'Confluencia del Río Baker con el Río Nef: aguas turquesa y rápidos', "credit": 'Abbagliati / <a href="https://commons.wikimedia.org/wiki/File:R%C3%ADo_Baker.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Confluencia del Río Baker con el Río Nef: aguas turquesa y rápidos: Abbagliati / <a href="https://commons.wikimedia.org/wiki/File:R%C3%ADo_Baker.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'baker2': {"src": "assets/img/libres/rio-baker-2.jpg", "alt_es": 'Confluencia del Río Baker y el Río Chacabuco', "alt_en": 'Confluencia del Río Baker y el Río Chacabuco', "credit": 'Jason Hollinger / <a href="https://commons.wikimedia.org/wiki/File:Confluence_of_Rio_Baker_and_Rio_Chacobuco_(3260733282).jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/2.0" target="_blank" rel="noopener nofollow">CC BY 2.0</a>', "credit_full": 'Confluencia del Río Baker y el Río Chacabuco (cerca de Cochrane), valle con montañas: Jason Hollinger / <a href="https://commons.wikimedia.org/wiki/File:Confluence_of_Rio_Baker_and_Rio_Chacobuco_(3260733282).jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/2.0" target="_blank" rel="noopener nofollow">CC BY 2.0</a>'},
    'gcarrera1': {"src": "assets/img/libres/lago-general-carrera-1.jpg", "alt_es": 'Lago General Carrera desde el sector de las Capillas de Mármol, con lanchas turísticas y agua turquesa', "alt_en": 'Lago General Carrera desde el sector de las Capillas de Mármol, con lanchas turísticas y agua turquesa', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Lago_General_Carrera_2016.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Lago General Carrera desde el sector de las Capillas de Mármol, con lanchas turísticas y agua turquesa: Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Lago_General_Carrera_2016.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'gcarrera2': {"src": "assets/img/libres/lago-general-carrera-2.jpg", "alt_es": 'Lago General Carrera turquesa desde la Carretera Austral, sector Lago Bertrand, con cumbres nevadas', "alt_en": 'Lago General Carrera turquesa desde la Carretera Austral, sector Lago Bertrand, con cumbres nevadas', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Lago_General_Carrera_desde_Bertrand.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Lago General Carrera turquesa desde la Carretera Austral, sector Lago Bertrand, con cumbres nevadas: Manxuc / <a href="https://commons.wikimedia.org/wiki/File:Lago_General_Carrera_desde_Bertrand.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'simpson1': {"src": "assets/img/libres/rio-simpson-1.jpg", "alt_es": 'Cascada en la Reserva Nacional Río Simpson', "alt_en": 'Cascada en la Reserva Nacional Río Simpson', "credit": 'W. Bulach / <a href="https://commons.wikimedia.org/wiki/File:00_1615_Reserva_Nacional_R%C3%ADo_Simpson.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Cascada en la Reserva Nacional Río Simpson (geolocalizada en la reserva, camino Coyhaique-Puerto Aysén): W. Bulach / <a href="https://commons.wikimedia.org/wiki/File:00_1615_Reserva_Nacional_R%C3%ADo_Simpson.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'simpson2': {"src": "assets/img/libres/rio-simpson-2.jpg", "alt_es": 'Río Simpson a su paso por la ciudad de Coyhaique, valle verde', "alt_en": 'Río Simpson a su paso por la ciudad de Coyhaique, valle verde', "credit": 'Manxuc / <a href="https://commons.wikimedia.org/wiki/File:R%C3%ADo_Simpson_por_Coyhaique.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Río Simpson a su paso por la ciudad de Coyhaique, valle verde (no es dentro de la Reserva): Manxuc / <a href="https://commons.wikimedia.org/wiki/File:R%C3%ADo_Simpson_por_Coyhaique.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'simpson3': {"src": "assets/img/libres/rio-simpson-3.jpg", "alt_es": 'Río Simpson en Coyhaique con el Cerro Mackay al fondo, otoño', "alt_en": 'Río Simpson en Coyhaique con el Cerro Mackay al fondo, otoño', "credit": 'Lin linao / <a href="https://commons.wikimedia.org/wiki/File:R%C3%ADo_Simpson_en_Coyhaique.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>', "credit_full": 'Río Simpson en Coyhaique con el Cerro Mackay al fondo, otoño (no es dentro de la Reserva): Lin linao / <a href="https://commons.wikimedia.org/wiki/File:R%C3%ADo_Simpson_en_Coyhaique.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>'},
    'simpson4': {"src": "assets/img/libres/rio-simpson-4.jpg", "alt_es": 'Paredón rocoso y bosque dentro de la Reserva Nacional Río Simpson', "alt_en": 'Paredón rocoso y bosque dentro de la Reserva Nacional Río Simpson', "credit": 'Maokru / <a href="https://commons.wikimedia.org/wiki/File:Cerro_y_arboles_ubicados_en_la_Reserva_Nacional_del_Rio_Simpson.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Paredón rocoso y bosque dentro de la Reserva Nacional Río Simpson: Maokru / <a href="https://commons.wikimedia.org/wiki/File:Cerro_y_arboles_ubicados_en_la_Reserva_Nacional_del_Rio_Simpson.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
    'fraile_nieve1': {"src": "assets/img/libres/nieve-camino-el-fraile-1.jpg", "alt_es": 'Camino nevado entre bosque de lengas, en la ruta al centro de ski El Fraile, Coyhaique', "alt_en": 'Camino nevado entre bosque de lengas, en la ruta al centro de ski El Fraile, Coyhaique', "credit": 'Hayleen E. Cid A / <a href="https://commons.wikimedia.org/wiki/File:Camino_al_centro_de_Ski_%22El_Fraile%22_en_Coyhaique.JPG" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>', "credit_full": 'Camino nevado entre bosque de lengas, en la ruta al centro de ski El Fraile, Coyhaique (solo 1600x1200): Hayleen E. Cid A / <a href="https://commons.wikimedia.org/wiki/File:Camino_al_centro_de_Ski_%22El_Fraile%22_en_Coyhaique.JPG" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener nofollow">CC BY-SA 3.0</a>'},
    'cinchao1': {"src": "assets/img/libres/nieve-coyhaique-1.jpg", "alt_es": 'Cerro Cinchao con algo de nieve, Reserva Nacional Coyhaique', "alt_en": 'Cerro Cinchao con algo de nieve, Reserva Nacional Coyhaique', "credit": 'Lin linao / <a href="https://commons.wikimedia.org/wiki/File:Cinchao_con_algo_de_nieve.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>', "credit_full": 'Cerro Cinchao con algo de nieve, Reserva Nacional Coyhaique (nieve ligera, foto algo oscura): Lin linao / <a href="https://commons.wikimedia.org/wiki/File:Cinchao_con_algo_de_nieve.jpg" target="_blank" rel="noopener nofollow">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener nofollow">CC BY-SA 4.0</a>'},
})

# Textos alternativos en inglés para las fotos de Commons
for _k, _en in {
    "marmol1": "Marble Cathedral islet on Lake General Carrera with snowy mountains, Puerto Río Tranquilo",
    "marmol2": "Inside the Marble Caves with turquoise water, Lake General Carrera",
    "marmol3": "The Marble Chapel islet under a blue sky on turquoise Lake General Carrera",
    "marmol4": "Marble veins and turquoise water inside the Marble Cathedral",
    "ruta1": "Paved Carretera Austral heading south, north of Villa Cerro Castillo",
    "ruta2": "Carretera Austral with a snowy peak between Villa Cerro Castillo and Bahía Murta",
    "ruta3": "Gravel section of the Carretera Austral near Leones with icefield peaks",
    "ruta4": "Gravel Carretera Austral overlooking Lake Bertrand",
    "ccastillo1": "Turquoise Laguna Cerro Castillo beneath the spires of Cerro Castillo",
    "ccastillo2": "Cerro Castillo and its glacier seen from the lagoon at its foot",
    "ccastillo3": "Hiking trail in Cerro Castillo National Park with lenga forest and snowy peaks",
    "ccastillo4": "Cerro Castillo and its glacier, Cerro Castillo National Park",
    "queulat1": "The Hanging Glacier and waterfall framed by forest, Queulat National Park",
    "queulat2": "Panorama of the Hanging Glacier, waterfalls and Laguna Témpanos, Queulat",
    "queulat3": "Laguna Témpanos with the Hanging Glacier behind, Queulat National Park",
    "queulat4": "The Hanging Glacier seen from Laguna Témpanos under low clouds",
    "coy1": "Cerro Mackay with forest and the Simpson River in Coyhaique",
    "coy2": "Coyhaique and Cerro Mackay seen from Coyhaique National Reserve",
    "coy3": "Cerro Mackay seen from the Carretera Austral in Coyhaique",
    "coy4": "Laguna Verde surrounded by forest, Coyhaique National Reserve",
    "baker1": "Turquoise rapids at the confluence of the Baker and Nef rivers",
    "baker2": "Confluence of the Baker and Chacabuco rivers near Cochrane",
    "gcarrera1": "Turquoise Lake General Carrera near the Marble Caves with tour boats",
    "gcarrera2": "Turquoise Lake General Carrera from the Carretera Austral near Lake Bertrand",
    "simpson1": "Waterfall in Río Simpson National Reserve",
    "simpson2": "The Simpson River flowing through a green valley in Coyhaique",
    "simpson3": "The Simpson River in Coyhaique with Cerro Mackay in autumn",
    "simpson4": "Rock wall and forest in Río Simpson National Reserve",
    "fraile_nieve1": "Snowy road through lenga forest to El Fraile ski area, Coyhaique",
    "cinchao1": "Cerro Cinchao with some snow, Coyhaique National Reserve",
}.items():
    IMG[_k]["alt_en"] = _en

# Fotos reales de proyectos de Inmobiliaria El Roble (carpeta Fotos_proyectos_optimizadas_web)
IMG.update({
    'manihuales_entorno_verde': {"src": "assets/img/proyectos/manihuales/manihuales-entorno-verde.webp", "w": 900, "h": 1600, "alt_es": 'Terreno verde con vegetación en el entorno de Mañihuales', "alt_en": 'Green land with vegetation at Horizontes de Mañihuales'},
    'manihuales_vista_horizontal': {"src": "assets/img/proyectos/manihuales/manihuales-vista-horizontal.webp", "w": 900, "h": 1600, "alt_es": 'Vista horizontal del entorno fluvial de Horizontes de Mañihuales', "alt_en": 'River surroundings of Horizontes de Mañihuales'},
    'rio_manihuales_meandro': {"src": "assets/img/proyectos/manihuales/rio-manihuales-meandro.webp", "w": 900, "h": 1600, "alt_es": 'Meandro del río Mañihuales visto desde el aire', "alt_en": 'Aerial view of a bend in the Mañihuales River'},
    'rio_manihuales_ribera': {"src": "assets/img/proyectos/manihuales/rio-manihuales-ribera.webp", "w": 900, "h": 1600, "alt_es": 'Ribera y bancos de grava del río Mañihuales', "alt_en": 'Riverbank and gravel bars of the Mañihuales River'},
    'dona_cecilia_panorama_rural': {"src": "assets/img/proyectos/dona-cecilia/dona-cecilia-panorama-rural.webp", "w": 1422, "h": 800, "alt_es": 'Panorama rural con praderas y montañas', "alt_en": 'Rural panorama with meadows and mountains'},
    'dona_cecilia_camino_de_acceso': {"src": "assets/img/proyectos/dona-cecilia/dona-cecilia-camino-de-acceso.webp", "w": 1422, "h": 800, "alt_es": 'Camino de ripio entre terrenos del proyecto', "alt_en": 'Gravel road between the project plots'},
    'dona_cecilia_camino_y_caballos': {"src": "assets/img/proyectos/dona-cecilia/dona-cecilia-camino-y-caballos.webp", "w": 1422, "h": 800, "alt_es": 'Camino rural con caballos a un costado', "alt_en": 'Country road with horses alongside'},
    'dona_cecilia_campo_y_cerros': {"src": "assets/img/proyectos/dona-cecilia/dona-cecilia-campo-y-cerros.webp", "w": 1422, "h": 800, "alt_es": 'Campo abierto con cerros y árboles al fondo', "alt_en": 'Open field with hills and trees'},
    'dona_cecilia_terrenos_planos': {"src": "assets/img/proyectos/dona-cecilia/dona-cecilia-terrenos-planos.webp", "w": 1422, "h": 800, "alt_es": 'Pradera abierta con arbolado lateral', "alt_en": 'Open meadow lined with trees'},
    'dona_cecilia_camino_aereo': {"src": "assets/img/proyectos/dona-cecilia/dona-cecilia-camino-aereo.webp", "w": 1422, "h": 800, "alt_es": 'Camino interior visto desde el aire entre praderas', "alt_en": 'Aerial view of the internal road between meadows'},
    'dona_cecilia_trazado_aereo': {"src": "assets/img/proyectos/dona-cecilia/dona-cecilia-trazado-aereo.webp", "w": 1422, "h": 800, "alt_es": 'Vista aérea sobre el trazado del camino y los terrenos', "alt_en": 'Aerial view of the road layout and plots'},
    'dona_cecilia_valle_aereo': {"src": "assets/img/proyectos/dona-cecilia/dona-cecilia-valle-aereo.webp", "w": 1422, "h": 800, "alt_es": 'Vista aérea del proyecto y campos de San Clemente', "alt_en": 'Aerial view of the project and San Clemente fields'},
    'maule_cascada_y_poza': {"src": "assets/img/proyectos/dona-cecilia/maule-cascada-y-poza.webp", "w": 1203, "h": 799, "alt_es": 'Cascada que cae hacia una poza entre paredes rocosas (entorno regional del Maule)', "alt_en": 'Waterfall into a pool between rock walls, Maule Region'},
    'maule_embalse_vista_aerea': {"src": "assets/img/proyectos/dona-cecilia/maule-embalse-vista-aerea.webp", "w": 1422, "h": 800, "alt_es": 'Vista aérea de una península arbolada rodeada de agua (entorno regional del Maule)', "alt_en": 'Aerial view of a wooded peninsula surrounded by water, Maule Region'},
    'maule_embalse_y_montanas': {"src": "assets/img/proyectos/dona-cecilia/maule-embalse-y-montanas.webp", "w": 1422, "h": 800, "alt_es": 'Pasarela junto al agua con montañas al fondo (entorno regional del Maule)', "alt_en": 'Walkway by the water with mountains, Maule Region'},
    'villa_medina_valle_aereo': {"src": "assets/img/proyectos/villa-medina/villa-medina-valle-aereo.webp", "w": 1920, "h": 1080, "alt_es": 'Vista aérea del valle y de los caminos entre parcelas', "alt_en": 'Aerial view of the valley and roads between plots'},
    'villa_medina_cabana_aerea': {"src": "assets/img/proyectos/villa-medina/villa-medina-cabana-aerea.webp", "w": 1920, "h": 1080, "alt_es": 'Vista aérea de una cabaña sobre una pradera', "alt_en": 'Aerial view of a cabin on a meadow'},
    'villa_medina_cabana_y_valle': {"src": "assets/img/proyectos/villa-medina/villa-medina-cabana-y-valle.webp", "w": 1920, "h": 1080, "alt_es": 'Cabaña en primer plano con un valle abierto al fondo', "alt_en": 'Cabin with an open valley behind'},
    'villa_medina_rio_y_valle': {"src": "assets/img/proyectos/villa-medina/villa-medina-rio-y-valle.webp", "w": 1920, "h": 1080, "alt_es": 'Río que atraviesa un valle al pie de las montañas', "alt_en": 'River crossing a valley at the foot of the mountains'},
    'villa_medina_relieve_y_valle': {"src": "assets/img/proyectos/villa-medina/villa-medina-relieve-y-valle.webp", "w": 1920, "h": 1080, "alt_es": 'Laderas y caminos rurales vistos desde el aire', "alt_en": 'Slopes and rural roads from the air'},
    'villa_medina_pradera_y_cerros': {"src": "assets/img/proyectos/villa-medina/villa-medina-pradera-y-cerros.webp", "w": 1920, "h": 1080, "alt_es": 'Pradera seca y cordón de cerros bajo cielo azul', "alt_en": 'Dry meadow and hills under blue sky'},
    'villa_medina_cascada': {"src": "assets/img/proyectos/villa-medina/villa-medina-cascada.webp", "w": 1920, "h": 1080, "alt_es": 'Cascada entre laderas verdes del entorno del proyecto', "alt_en": 'Waterfall between green slopes near the project'},
    'villa_medina_bosque_con_nieve': {"src": "assets/img/proyectos/villa-medina/villa-medina-bosque-con-nieve.webp", "w": 1920, "h": 1080, "alt_es": 'Bosque y sendero nevados en el entorno del proyecto', "alt_en": 'Snowy forest and trail near the project'},
    'lago_frio_pesca_embarcacion': {"src": "assets/img/proyectos/pesca/lago-frio-pesca-embarcacion.webp", "w": 1920, "h": 1080, "alt_es": 'Dos personas pescando desde una embarcación en un lago de Aysén', "alt_en": 'Two people fishing from a boat on a lake in Aysén'},
    'lago_frio_pesca_panorama': {"src": "assets/img/proyectos/pesca/lago-frio-pesca-panorama.webp", "w": 1920, "h": 1080, "alt_es": 'Embarcación de pesca sobre las aguas tranquilas de Aysén', "alt_en": 'Fishing boat on the calm waters of a lake in Aysén'},
})


# Fotogramas de videos propios de Inmobiliaria El Roble (Videos para web)
for _k, _f, _es, _en in [
    ("v_carretera", "carretera-austral", "Carretera Austral entre matorrales y cerros, con un lago al fondo", "Carretera Austral through scrubland and hills, with a lake behind"),
    ("v_simpson", "valle-simpson", "Praderas del sector Valle Simpson con cordillera al fondo", "Meadows in the Valle Simpson area with mountains behind"),
    ("v_simpson2", "valle-simpson-cordillera", "Vista aérea de praderas y bosquetes con cordillera nevada", "Aerial view of meadows and woods with snowy mountains"),
    ("v_mirador", "mirador-cerro-castillo", "Vista desde el mirador de la Cuesta del Diablo sobre las curvas de la Carretera Austral", "View from the Cuesta del Diablo lookout over the Carretera Austral switchbacks"),
    ("v_elizalde_muelle", "lago-elizalde-muelle", "Muelle de madera y botes en el Lago Elizalde, vista aérea", "Wooden pier and boats on Lake Elizalde, aerial view"),
    ("v_elizalde_botes", "lago-elizalde-botes", "Botes en un muelle del Lago Elizalde", "Boats at a pier on Lake Elizalde"),
    ("v_elizalde_lancha", "lago-elizalde-lancha", "Lancha navegando en el Lago Elizalde", "Boat cruising on Lake Elizalde"),
    ("v_elizalde_orilla", "lago-elizalde-orilla", "Orilla turquesa y bosque del Lago Elizalde", "Turquoise shore and forest at Lake Elizalde"),
    ("v_lago_verde", "lago-verde", "Lago Verde, de aguas turquesa, a 15 minutos de Villa Cerro Castillo", "Lago Verde, with turquoise water, 15 minutes from Villa Cerro Castillo"),
    ("v_ibanez", "puerto-ibanez", "Vista aérea de Puerto Ingeniero Ibáñez y el Lago General Carrera", "Aerial view of Puerto Ingeniero Ibáñez and Lake General Carrera"),
    ("v_ibanez_muelle", "puerto-ibanez-muelle", "Antiguo muelle de madera en Puerto Ingeniero Ibáñez", "Old wooden pier in Puerto Ingeniero Ibáñez"),
    ("v_salto", "salto-rio-ibanez", "Salto del Río Ibáñez entre paredes de roca, vista aérea", "Ibáñez River falls between rock walls, aerial view"),
    ("v_salto2", "salto-rio-ibanez-cerca", "Aguas blancas del Salto del Río Ibáñez", "White water at the Ibáñez River falls"),
]:
    IMG[_k] = {"src": f"assets/img/videos/{_f}.jpg", "w": 1600, "h": 900, "alt_es": _es, "alt_en": _en}

# Videos propios para la página "La Patagonia en video" (art = clave del artículo relacionado)
VIDEOS = [
    {"file": "salto-rio-ibanez", "poster": "v_salto", "art": "ibanez", "es": "Salto del Río Ibáñez", "en": "Ibáñez River falls"},
    {"file": "lago-elizalde-lancha", "poster": "v_elizalde_lancha", "art": "elizalde", "es": "Navegando el Lago Elizalde", "en": "Boating on Lake Elizalde"},
    {"file": "carretera-austral", "poster": "v_carretera", "art": "carretera", "es": "Carretera Austral", "en": "Carretera Austral"},
    {"file": "mirador-cerro-castillo", "poster": "v_mirador", "art": "castillo", "es": "Mirador de la Cuesta del Diablo", "en": "Cuesta del Diablo lookout"},
    {"file": "puerto-ibanez", "poster": "v_ibanez", "art": "ibanez", "es": "Puerto Ingeniero Ibáñez", "en": "Puerto Ingeniero Ibáñez"},
    {"file": "lago-elizalde-muelle", "poster": "v_elizalde_muelle", "art": "elizalde", "es": "Muelle del Lago Elizalde", "en": "Lake Elizalde pier"},
    {"file": "valle-simpson", "poster": "v_simpson", "art": "rutasur", "es": "Praderas del Valle Simpson", "en": "Valle Simpson meadows"},
    {"file": "lago-verde", "poster": "v_lago_verde", "art": "rutasur", "es": "Lago Verde", "en": "Lago Verde"},
    {"file": "salto-rio-ibanez-cerca", "poster": "v_salto2", "art": "ibanez", "es": "Aguas del Río Ibáñez", "en": "Ibáñez River white water"},
    {"file": "lago-elizalde-orilla", "poster": "v_elizalde_orilla", "art": "elizalde", "es": "Orillas del Lago Elizalde", "en": "Lake Elizalde shoreline"},
    {"file": "puerto-ibanez-muelle", "poster": "v_ibanez_muelle", "art": "ibanez", "es": "Antiguo muelle de Puerto Ibáñez", "en": "Old pier at Puerto Ibáñez"},
]

IMG["plano_don_guillermo"] = {"src": "assets/img/proyectos/plano-don-guillermo.jpg", "w": 1600, "h": 900,
    "alt_es": "Masterplan de Parcelas Don Guillermo junto al río Emperador Guillermo: todas las parcelas vendidas salvo la B11",
    "alt_en": "Parcelas Don Guillermo masterplan by the Emperador Guillermo River: all plots sold except B11"}
