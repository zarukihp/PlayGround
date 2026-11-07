# QA · Chronicle of Ash

## Alcance de la revisión

Se realizaron comprobaciones estáticas y una carga local de la versión HTML. Ren'Py no está instalado en este entorno, por lo que la ejecución desde el motor queda pendiente. La suite automatizada de rutas todavía no valida todos los finales; no se considera aprobada la alcanzabilidad completa.

## Lista de control

| Área | Estado | Evidencia / nota |
|---|---|---|
| JavaScript | ✅ | `node --check game.js` sin errores de sintaxis. |
| Recursos gráficos | ✅ | 51 PNG por versión: 8 fondos, 3 CG y 40 retratos. Ambas carpetas contienen 51 archivos. |
| HTML y carga inicial | ✅ | Cargado en Chromium headless desde servidor local; comprobados título y estado inicial. |
| Flujo HTML | ⚠️ Parcial | La prueba automatizada no termina correctamente para todos los objetivos; los resultados actuales confirman E01, E04, E10, E13, E14 y E15. Las discrepancias de los demás códigos requieren separar fallos del selector de pruebas de posibles problemas de flujo. |
| Guardado HTML | ✅ Estático | La partida se serializa en `localStorage`, incluido el archivo de finales y el estado New Game+. No se realizó una prueba integral de restauración en navegador. |
| Protección del cuaderno | ✅ Revisión de código | La entrada exige los indicadores narrativos de nombre y rostro ficticios. El relato no incorpora una función de búsqueda o validación de identidades reales. |
| Condiciones de finales | ⚠️ Revisión estática | El árbitro declara 15 códigos; no se ha demostrado todavía en navegador la alcanzabilidad de cada uno. |
| Guion, diseño y documentación | ✅ | Incluye `DOCUMENTACION.md`, `GUION_CAPITULO_1.md`, `INVENTARIO_ASSETS.md` y `LEEME.txt`. |
| Ren'Py: sintaxis y lanzamiento | ⚠️ Pendiente | No se encontró una instalación de Ren'Py/SDK. Ejecutar `Lint` y `Launch Project` con Ren'Py 8.x antes de distribuir un build. |
| Empaquetado ZIP | ✅ | Se creó `Chronicle_of_Ash.zip`; la tabla del archivo y la comprobación `unzip -t` no reportaron errores. |
| Audio y accesibilidad | ⚠️ Parcial | No se requieren archivos de audio. No se ha realizado una auditoría formal de accesibilidad. |

## Resultados de prueba de finales HTML

La última ejecución automatizada obtuvo estos resultados:

| Objetivo | Resultado observado |
|---|---|
| E01 | E01 — pasa |
| E02, E03, E05, E06, E07, E08, E11, E12 | Código distinto al objetivo — pendiente de diagnóstico |
| E04 | E04 — pasa |
| E09 | Timeout — pendiente de diagnóstico |
| E10 | E10 — pasa |
| E13 | E13 — pasa |
| E14 | E14 — pasa |
| E15 | E15 — pasa |

La discrepancia puede proceder de las políticas de selección/interacción de la prueba; aún no se ha determinado si también hay defectos de alcanzabilidad. Por tanto, las condiciones documentadas en `DOCUMENTACION.md` describen el árbitro del código, pero no equivalen a una certificación de rutas jugables.

## Pendiente antes de una distribución comercial

1. Corregir el selector de decisiones de la prueba de navegador y repetir cada ruta con almacenamiento aislado.
2. Abrir `renpy_project` con Ren'Py 8.x y ejecutar **Lint**.
3. Lanzar el proyecto y verificar menús, guardado/carga, pantallas modales, archivo de finales y New Game+.
4. Probar una compilación generada por el Launcher en cada plataforma objetivo.
5. Realizar una revisión manual de legibilidad y accesibilidad en móvil y escritorio.

## Reproducción de las comprobaciones básicas

Desde la carpeta del proyecto:

```sh
node --check game.js
python3 -m http.server 8000
```

Después, abre `http://localhost:8000` en el navegador. El proyecto Ren'Py requiere instalar el SDK oficial Ren'Py 8.x y seleccionar la carpeta `renpy_project` desde el Launcher.
