# Inventario de assets · Chronicle of Ash

## Resumen

El arte se generó específicamente para este proyecto mediante `tools_generate_art.py`. Son ilustraciones 2D originales de estética anime; no se usan imágenes descargadas, fuentes externas, personajes ni marcas de terceros. Los recursos son PNG y no dependen de conexión o licencias externas para ejecutarse.

| Grupo | Cantidad | Tamaño | Uso |
|---|---:|---|---|
| Fondos | 8 | 1280 × 720 px | Escenarios de la novela visual. |
| CG | 3 | 1280 × 720 px | Ilustraciones de momentos clave y galería. |
| Retratos | 40 | PNG con transparencia | 5 personajes × 8 expresiones intercambiables. |
| **Total por versión** | **51** | **3,3 MiB aprox.** | Recursos del juego. |

Cada versión incluye una copia de los 51 PNG: `assets/images/` para HTML y `renpy_project/game/images/` para Ren'Py. El tamaño total de las dos copias es aproximadamente 6,4 MiB (3.319.949 bytes por carpeta de imágenes).

## Fondos

| Archivo web | Nombre en Ren'Py | Escena |
|---|---|---|
| `bg_alley.png` | `bg/alley.png` | Callejón lluvioso; hallazgo inicial. |
| `bg_apartment.png` | `bg/apartment.png` | Apartamento de Noa; ruta del cuaderno. |
| `bg_cafe.png` | `bg/cafe.png` | Encuentro y conversación con Vela. |
| `bg_interrogation.png` | `bg/interrogation.png` | Pantalla de decisión de rutas. |
| `bg_police.png` | `bg/police.png` | Comisaría e investigación. |
| `bg_rooftop.png` | `bg/rooftop.png` | Azotea y epílogos. |
| `bg_tv.png` | `bg/tv.png` | Debate público y medios. |
| `bg_university.png` | `bg/university.png` | Universidad y entorno de Noa. |

## CG (ilustraciones de escena)

| Archivo web | Nombre en Ren'Py | Uso |
|---|---|---|
| `cg_discovery.png` | `cg/discovery.png` | Descubrimiento del cuaderno. |
| `cg_lastpage.png` | `cg/lastpage.png` | Página final y recurso de archivo. |
| `cg_revelation.png` | `cg/revelation.png` | Revelación narrativa y recurso de archivo. |

## Retratos y expresiones

Los nombres de archivo web usan el patrón `<personaje>_<expresión>.png`; en Ren'Py se encuentran bajo `images/chars/` con el mismo nombre. Cada personaje cuenta con `anger`, `fear`, `neutral`, `sad`, `smile`, `surprise`, `suspicious` y `tense`.

| Personaje | Prefijo | Cantidad |
|---|---|---:|
| Noa Senda | `noa_` | 8 |
| Iris Vale | `iris_` | 8 |
| Nera | `nera_` | 8 |
| Vela Lune | `vela_` | 8 |
| Ciro Senda (alias de sprite: `chief`) | `chief_` | 8 |
| **Total** |  | **40** |

Ejemplos: `noa_neutral.png`, `noa_fear.png`, `iris_suspicious.png`, `nera_smile.png`, `vela_tense.png` y `chief_sad.png`.

## Correspondencia y atribución

- HTML carga `assets/images/bg_<escena>.png`, `assets/images/cg_<escena>.png` y `assets/images/<personaje>_<expresión>.png` desde `game.js`.
- Ren'Py carga las copias bajo `renpy_project/game/images/`; las etiquetas y nombres de display están declarados en `renpy_project/game/characters.rpy`.
- El generador opcional es `tools_generate_art.py`. Para regenerar los PNG hacen falta Pillow y CairoSVG; no son dependencias necesarias para jugar.
- Créditos: arte original generado para este proyecto; no hay atribuciones externas pendientes.
