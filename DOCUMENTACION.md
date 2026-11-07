# Chronicle of Ash: La ciudad de ceniza

## Resumen ejecutivo
Novela visual original de misterio sobrenatural y thriller psicológico. Noa Senda, estudiante de criminología, encuentra un cuaderno inexplicable y debe decidir qué hacer con un poder capaz de alterar vidas. La historia pone el foco en evidencia, consentimiento, confianza y responsabilidad; la violencia se mantiene sugerida, sin gore. El paquete contiene una apertura jugable y rutas que conducen a quince desenlaces.

## GDD · Documento de diseño

### Formato y público
- Género: novela visual, misterio, thriller sobrenatural.
- Plataformas: navegador de escritorio/móvil moderno (HTML local) y Ren'Py 8.x.
- Idioma: español.
- Presentación: ilustración anime 2D original, retratos estáticos con expresiones intercambiables, fondos, CGs y UI de novela visual.
- Experiencia: lectura guiada con elecciones explícitas; no hay combate ni reflejos necesarios.

### Premisa y tono
Una cadena de muertes ficticias se convierte en conversación pública antes de ser evidencia. Noa encuentra un cuaderno asociado a ese rumor. La aparición de Nera, una vigía sobrenatural, confirma que el objeto tiene reglas, pero no ofrece certezas morales. El tono alterna inquietud, investigación y humor seco; la violencia no se representa gráficamente.

### Personajes
- **Noa Senda:** protagonista, estudiante de criminología. Sus elecciones determinan la ruta.
- **Iris Vale:** investigadora metódica; exige contrastar fuentes y distinguir hipótesis de hechos.
- **Nera:** vigía sobrenatural, irónica y observadora; explica los límites del cuaderno.
- **Vela Lune:** figura pública cuya relación con la devoción colectiva se explora desde la autonomía.
- **Ciro Senda:** responsable policial y familiar de Noa; representa confianza institucional imperfecta.
- **Radio Ciudad:** voz del debate público, no narrador omnisciente.

### Bucle de juego
1. Leer escena y diálogo.
2. Elegir entre respuestas con consecuencias narrativas y cambios de estado.
3. Consultar opcionalmente medidores, tablón de pistas y cuaderno ficticio.
4. Al cerrar el capítulo 1, escoger ruta investigadora, aliada, Kira, mártir, traidor o renuncia.
5. El árbitro evalúa la ruta, evidencia, confianza, sospecha, relaciones, devoción, miedo, cordura y errores, y resuelve exactamente un final.
6. Repetir rutas para completar el archivo de finales.

### Sistemas
- **Medidores (0–100):** sospecha, confianza policial, devoción, miedo público, cordura y poder del cuaderno. La evidencia está limitada a 0–10.
- **Relaciones:** Iris, Nera, Vela y Ciro; aumentan o bajan por elecciones.
- **Pistas:** registro de información textual. El tablón diferencia hechos de hipótesis.
- **Cuaderno:** campos de nombre ficticio, causa y hora. La entrada se bloquea mientras no haya nombre y rostro ficticios reconocidos; nunca solicita ni procesa identidad real como mecánica válida.
- **Archivo:** registra finales descubiertos. Ren'Py conserva el archivo entre sesiones mediante `persistent`; HTML usa el guardado local del navegador.
- **New Game+:** en HTML se habilita tras un final y da bonificación inicial. Ren'Py conserva la marca de partida completada y activa un recuerdo/bonificación al comenzar otra partida.
- **Guardado:** localStorage en HTML; sistema estándar de ranuras/autoguardado de Ren'Py.
- **Accesibilidad básica:** texto legible, botones explícitos, navegación por clic/teclado de motor y sin información transmitida solo por audio.

### Progresión y alcance
El capítulo 1 cubre el hallazgo del cuaderno, la aparición de Nera, el debate mediático, los primeros contactos con Iris y Vela y una conversación en la comisaría. Es el prólogo jugable del arco. El capítulo 2 ofrece las rutas y condiciones del árbitro de finales. Las implementaciones comparten premisa, variables, decisiones principales y finales.

## Diagrama de flujo

```text
Inicio / New Game+
        |
Hallazgo del cuaderno en el callejón
  | entregar       | investigar        | no tocar
  +----------------+-------------------+
        |
Nera explica reglas → debate público → Iris → Vela → Ciro
        |
     Cierre del capítulo 1
        |
Selección del capítulo 2
  | detective | aliada | Kira | mártir | traidor | renuncia
  |           |       |      |        |          |
  +-----------+-------+------+--------+----------+
                        |
         Árbitro de condiciones E01–E15
                        |
           Archivo persistente / Nueva ruta
```

## Tabla de finales
Las condiciones se evalúan en orden; se aplica el primer caso coincidente. Los umbrales son inclusivos salvo cuando se indica `<`.

| Código | Nombre | Condición exacta del árbitro |
|---|---|---|
| E01 | Archivo de la verdad | Ruta detective; evidencia ≥ 6 y confianza policial ≥ 65. |
| E02 | Sombra útil | Ruta detective; si no se activó E01, evidencia ≥ 4 y sospecha < 45. |
| E03 | La verdad incompleta | Ruta detective; si no se activó E01/E02 y evidencia ≥ 2. |
| E09 | Caso sin prueba | Ruta detective; evidencia < 2 (se evalúa antes del E03). |
| E04 | Dos métodos, una promesa | Ruta aliada; relación Iris ≥ 3 y confianza policial ≥ 55. |
| E05 | Fuera del altar | Ruta aliada; si no se activó E04, relación Vela ≥ 3 y devoción ≥ 38. |
| E06 | La alianza incómoda | Ruta aliada; si no se activó E04/E05, evidencia ≥ 4. |
| E07 | La puerta entreabierta | Ruta aliada; condición de respaldo. |
| E10 | La firma del error | Ruta Kira; errores ≥ 2. |
| E11 | La tinta interior | Ruta Kira; si no se activó E10, cordura < 55. |
| E08 | La quietud prestada | Ruta Kira; si no se activó E10/E11 y devoción ≥ 75 con miedo < 60, o si no se cumple ningún otro caso Kira (respaldo). |
| E12 | Ciudad bajo cristal | Ruta Kira; si no se activó E10/E11/E08 por la condición de devoción, miedo ≥ 50. |
| E13 | El precio de una siesta | Ruta traidor, sin más condiciones. |
| E14 | La última hoja | Ruta mártir, sin más condiciones. |
| E15 | No escribir | Ruta renuncia, ruta sin definir (respaldo), o decisión de renuncia desde ruta Kira. |

**Prioridad importante Kira:** tras E10 y E11, el chequeo E08 por devoción ocurre antes que E12 por miedo. Si se busca E12, debe evitarse devoción ≥75 junto con miedo <60; elevar miedo a ≥50 sin satisfacer el E08 prioritario. E08 también es el resultado de respaldo si no hay otra condición.

**Nota de alcanzabilidad:** las seis rutas están disponibles en el menú del capítulo 2, y el árbitro define condiciones para E01–E15. Sin embargo, la prueba automatizada de navegador ejecutada en este entorno solo confirmó E01, E04, E10, E13, E14 y E15; E09 terminó en timeout y los demás objetivos no coincidieron con el resultado esperado. Por ello, las condiciones que siguen describen la lógica del árbitro, no una alcanzabilidad jugable ya certificada. La prueba debe repetirse una vez corregido su selector de decisiones y diagnosticadas las discrepancias.

**Condiciones que el árbitro evalúa:** Detective: E01 requiere evidencia ≥6 y confianza ≥65; E02 evidencia ≥4 y sospecha <45 si no se activa E01; E03 corresponde a evidencia ≥2 como resultado posterior; E09 a evidencia <2. Aliada: E04 prioriza relación Iris ≥3 y confianza ≥55; E05 relación Vela ≥3 y devoción ≥38; E06 evidencia ≥4; E07 es el caso restante. Kira: E10 se prioriza con dos errores; E11 si la cordura cae por debajo de 55 y no se activa E10; después se evalúa E08 por devoción ≥75 y miedo <60, E12 por miedo ≥50, y E08 funciona además como respaldo. Traidor, mártir y renuncia se asignan directamente desde la selección. Los efectos de decisiones concretas pueden cambiar estos valores; comprueba el estado final antes de interpretar una ruta como validada.

## Estructura del proyecto
```text
index.html                 entrada HTML
style.css                  estilo de interfaz web
game.js                    diálogo, elecciones, estados y árbitro HTML
assets/images/             ilustraciones de la versión HTML
renpy_project/game/        proyecto fuente para Ren'Py
  options.rpy               configuración
  screens.rpy               menú, diálogo, guardado y preferencias
  screens_custom.rpy        cuaderno, tablón, medidores y menú rápido
  variables.rpy             estado, límites y persistencia
  characters.rpy            personajes y definiciones de imágenes
  script.rpy                capítulo 1 y rutas
  endings.rpy               árbitro y presentación E01–E15
  images/                   ilustraciones Ren'Py
LEEME.txt                   instrucciones de ejecución
GUION_CAPITULO_1.md         guion resumido del capítulo inicial
INVENTARIO_ASSETS.md        detalle de recursos
QA.md                       checklist de control
```

## Ejecución
Consultar `LEEME.txt` para instrucciones completas de HTML y Ren'Py. La versión web funciona offline después de extraer el paquete. Ren'Py requiere instalar el SDK oficial 8.x. No se distribuye audio ni se necesitan dependencias de runtime.
