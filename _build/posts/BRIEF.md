# Instrucciones para redactar los artículos del blog de Parcelas con Río

## Contexto
- Sitio: www.parcelasconrio.cl, de **Inmobiliaria El Roble**. Vende parcelas con rol propio frente a ríos en la Región de Aysén (Patagonia chilena), Los Ríos y el Maule, con crédito directo.
- Objetivo del blog: **SEO**. Guías útiles para turistas chilenos y extranjeros que despierten el deseo de vivir o tener un refugio en la Patagonia. El tono es evocador y cálido, pero práctico y preciso. Es contenido de guía turística de calidad, no un folleto de venta.
- Única fuente de datos: `/private/tmp/claude-501/-Users-mac/6e7298ff-05ed-4006-81ad-674a22b9ee29/scratchpad/investigacion-patagonia.md`. Léela entera antes de escribir.

## Reglas estrictas
1. **No inventes ningún dato** (cifras, fechas, precios, nombres, distancias). Usa solo lo que está en la investigación. Cuando las fuentes difieren, da el rango ("entre 215 y 233 km, unos 220 km") o atribuye ("según el MOP, abril de 2026").
2. Los precios y tarifas que la investigación marca como no oficiales o no confirmados se presentan como **referenciales** y con la recomendación de confirmarlos (en pasesparques.cl, con el operador, etc.).
3. **Aeropuerto:** la formulación correcta es que Coyhaique **estrenó el 5 de octubre de 2026 el nuevo terminal del Aeropuerto Balmaceda**, a unos 55 km de la ciudad. No digas que se construirá un aeropuerto nuevo en otro lugar. No afirmes que hay vuelos internacionales: el terminal tiene categoría internacional, pero no hay rutas internacionales confirmadas.
4. **Afirmaciones promocionales de terceros** ("el Simpson es el cuarto mejor río del mundo para la pesca con mosca") van atribuidas: "según CONAF".
5. **Honestidad:** en "vivir en Coyhaique" menciona con naturalidad que la ciudad es zona saturada por MP2,5 en invierno por la calefacción a leña, y que hay un plan de descontaminación. Puedes señalar que vivir en una parcela fuera del área urbana y usar calefacción eficiente ayuda. No lo escondas ni lo dramatices.
6. **Compra de parcelas:** cierra con una nota: "Esta guía es informativa y no reemplaza la asesoría de un abogado." No afirmes lo que la investigación marca como no verificado (pozo sin derecho de agua, comunas fronterizas, estado del proyecto de ley). Puedes decir que hay un proyecto de ley en trámite y que conviene revisar su estado.
7. **Las parcelas de El Roble:** cada artículo termina con un párrafo breve y natural que conecte con tener un refugio propio en Aysén y enlace a los proyectos. No inventes características de los proyectos. Solo puedes usar estas:
   - Horizontes de Mañihuales: 4 parcelas de 0,53 a 1 ha frente al río Mañihuales, Región de Aysén, con acceso por servidumbre de tránsito y factibilidad eléctrica; 3 de 4 disponibles.
   - Parcelas Don Guillermo: frente al río Emperador Guillermo, en plena Carretera Austral; queda 1 parcela.
   - Todas con rol propio y opción de crédito directo.
   - No digas a cuántos km o minutos está un proyecto de ningún lugar (no está verificado).
8. No uses "auténtico", "inolvidable" ni frases de relleno vacías. Escribe con oraciones claras y concretas. Español de Chile neutro (tú). En inglés, inglés internacional natural (no una traducción literal) y montos en pesos chilenos con su equivalencia en USD solo si la investigación la da.

## Formato de entrega (por cada artículo)
Escribe tres archivos en `/Users/mac/Documents/GitHub/parcelasconrio/_build/posts/`:
- `<key>_es.html` y `<key>_en.html`: **solo el fragmento HTML del cuerpo** (sin `<html>`, `<head>`, `<body>` ni `<h1>`). Va dentro de `<article class="prose">`.
- `<key>.json`: `{"toc_es": [["id", "Título del h2"], ...], "toc_en": [[...]], "read": N}`. N son los minutos de lectura (unas 200 palabras por minuto, redondeado).

Estructura del fragmento:
- Empieza con 1–2 párrafos de entrada evocadores (sin título).
- De 4 a 7 secciones `<h2 id="...">` con ids en minúsculas sin tildes (ej. `id="como-llegar"`). Los ids son los mismos en ES y EN para facilitar el mantenimiento. El json `toc` lista exactamente esos h2 (sin el de fuentes).
- Usa `<h3>`, `<p>`, `<ul>`, `<ol>`, `<table>` (con `<thead>`), `<blockquote>` y `<p class="note">` para consejos o advertencias, según convenga.
- Puedes incluir 1 o 2 imágenes de esta lista, con `<figure><img src="RUTA" alt="..." loading="lazy" width="1200" height="800"><figcaption>...</figcaption></figure>`. Usa solo estas, y solo si representan bien el tema (son paisajes de Aysén; no las presentes como un lugar específico que no muestran):
  - `assets/img/patagonia/coyhaique-1200.webp`: vista aérea de Coyhaique con cerros nevados.
  - `assets/img/patagonia/hero-carretera-austral.webp`: camino entre paredes de roca en Aysén.
  - `assets/img/patagonia/carretera-austral-1200.webp`: valle y camino en Aysén.
  - `assets/img/patagonia/cerro-castillo-1200.webp`: cumbres nevadas sobre bosques en Aysén (no afirmes que es Cerro Castillo; di "cumbres nevadas de Aysén").
  - `assets/img/patagonia/centro-ski-invierno.webp` y `centro-ski-otono.webp`: pistas de esquí del centro El Fraile.
  - `assets/img/patagonia/el-salto-1200.webp`: pueblo entre colinas en otoño, Aysén.
  - `assets/img/paisajes/lago-bote.webp`: bote en un lago calmo de Aysén.
  - `assets/img/paisajes/lago-reflejo.webp`: lago con reflejo de montañas.
  - `assets/img/paisajes/lengas-otono.webp`: bosque de lengas rojas en otoño.
  - `assets/img/paisajes/valle-primavera.webp`: valle verde con bosque nativo.
  - **Prefijo de ruta:** en ES (archivo publicado en `blog/`) usa `../assets/...`. En EN (publicado en `en/blog/`) usa `../../assets/...`.
- **Enlaces internos** (al menos 2 por artículo hacia otras guías, más 1 a proyectos):
  - ES (desde `blog/`): a otra guía, `slug.html`; a los proyectos, `../proyectos/index.html`; a Mañihuales, `../proyectos/horizontes-de-manihuales.html`; a Don Guillermo, `../proyectos/don-guillermo.html`; a contacto, `../contacto.html`.
  - EN (desde `en/blog/`): a otra guía, `slug-en.html`; a los proyectos, `../projects/index.html`; a Mañihuales, `../projects/horizontes-de-manihuales.html`; a Don Guillermo, `../projects/don-guillermo.html`; a contacto, `../contact.html`.
  - Slugs (clave: ES / EN): aeropuerto `como-llegar-a-coyhaique` / `how-to-get-to-coyhaique`; marmol `catedrales-de-marmol` / `marble-caves-chile`; carretera `carretera-austral` / `carretera-austral-road-trip`; ski `centro-de-ski-el-fraile` / `el-fraile-ski-coyhaique`; pesca `pesca-con-mosca-en-aysen` / `fly-fishing-aysen-patagonia`; castillo `trekking-en-aysen-cerro-castillo` / `hiking-aysen-cerro-castillo`; vivir `vivir-en-coyhaique` / `living-in-coyhaique-patagonia`; comprar `comprar-parcela-en-la-patagonia` / `buying-land-in-chilean-patagonia`.
- **Fuentes:** al final, `<h2 id="fuentes">Fuentes</h2>` (EN: `Sources`) con `<ul class="sources">` y los enlaces de la investigación usados (`<a href="URL" target="_blank" rel="noopener nofollow">Nombre, fecha</a>`).
- **Largo:** entre 900 y 1.400 palabras por artículo en español; el inglés es equivalente.
- **SEO:** el primer párrafo y algún h2 incluyen de forma natural la búsqueda principal (ej. "cómo llegar a Coyhaique", "Catedrales de Mármol", "Marble Caves Chile", "fly fishing Patagonia"). Incluye una sección de preguntas frecuentes `<h2 id="preguntas-frecuentes">` con 3–4 `<h3>` de pregunta y su respuesta.

## Fotos libres adicionales (Wikimedia Commons, requieren crédito)
Estas fotos muestran el lugar real. Si usas una, el `<figcaption>` **debe** terminar con el crédito exacto que figura en `/Users/mac/Documents/GitHub/parcelasconrio/_build/data.py` (campo `credit` de la clave). Copia el HTML del crédito tal cual: "Foto: " + credit (en inglés, "Photo: " + credit). La ruta es `assets/img/libres/<archivo>`, con el mismo prefijo `../` o `../../` según el idioma.
- `catedrales-de-marmol-1..4.jpg` (claves marmol1..4): 1 y 3 el islote sobre el lago; 2 y 4 el interior de las cavernas turquesa.
- `cerro-castillo-1..4.jpg` (ccastillo1..4): Laguna Cerro Castillo, el cerro con su glaciar y un sendero del parque.
- `queulat-1..4.jpg` (queulat1..4): Ventisquero Colgante y Laguna Témpanos.
- `coyhaique-1..4.jpg` (coy1..4): Cerro Mackay, la ciudad desde la Reserva Nacional Coyhaique (coy2) y la Laguna Verde de la Reserva (coy4).
- `lago-general-carrera-1..2.jpg` (gcarrera1..2), `rio-baker-1..2.jpg` (baker1..2).
- `rio-simpson-1..4.jpg` (simpson1..4): 1 es una cascada en la Reserva; 2 y 3 son el río a su paso por Coyhaique (no en la reserva); 4 es un paredón en la reserva.
- `carretera-austral-1..4.jpg` (ruta1..4): Ruta 7 al norte de Villa Cerro Castillo, tramo hacia Bahía Murta, sector Leones con ripio y vista al Lago Bertrand.
- `nieve-camino-el-fraile-1.jpg` (fraile_nieve1): camino nevado al centro de ski El Fraile.
