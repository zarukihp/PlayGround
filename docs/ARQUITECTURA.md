# Arquitectura, datos y lógica

## Estructura del prototipo

```text
.
├── index.html              # Interfaz, vistas, controles y modales
├── style.css               # Presentación responsive
├── game.js                 # Datos, estado, reglas, renderizado y eventos
├── docs/
│   ├── GDD.md               # Diseño y comportamiento esperado
│   ├── ALCANCE.md           # Límites y hoja de ruta
│   ├── ARQUITECTURA.md      # Este documento
│   ├── QA.md                # Casos de prueba y criterios de salida
│   ├── LEGAL.md             # Supuestos y riesgos de publicación
│   └── schemas/             # Contratos de datos JSON
└── README.md                # Entrada del proyecto y documentación
```

No hay backend, dependencias de ejecución ni empaquetador. `game.js` se carga al final de `index.html`; `setup()` conecta eventos y el renderizado inicial. El estado vive en el objeto `S`, se guarda como JSON en `localStorage` con la clave `cuadernoCosechaSave` y se vuelve a leer al cargar. El guardado es local, editable por el usuario y no está versionado ni validado en tiempo de ejecución.

## Módulos lógicos (dentro de `game.js`)

- **Catálogos:** `PEOPLE`, `TARGETS`, `CROPS`, `PLACES`, `WEATHER` y `WEEKDAYS`.
- **Estado y persistencia:** `defaultState()`, `loadState()` y `save()`.
- **Vistas:** `render()`, `renderStats()`, `renderPlots()`, `renderTown()`, `renderNotebook()`, `renderBoard()`, `renderPeople()` y `renderNews()`.
- **Acciones de granja/economía:** `plotAction()`, `plantCrop()`, `buySeed()`, `sellHarvest()` y `deliverTurnips()`.
- **Pueblo y relaciones:** `visitPlace()`, `talk()`, `gift()` y `talkDetective()`.
- **Narrativa:** `listenRadio()`, `askBruma()`, `writeEntry()`, `festival()`, `lanternFestival()`, `lanternChoice()`, `sleep()` y finales.
- **Interfaz:** `modal()`, `closeModal()`, `toast()`, `help()`, `calendar()` y `setup()`.

Los esquemas en [`schemas/partida.schema.json`](schemas/partida.schema.json) y [`schemas/contenido.schema.json`](schemas/contenido.schema.json) documentan la forma esperada de los datos. Son contratos de referencia: actualmente el juego no ejecuta un validador JSON Schema.

## Contrato de estado

El esquema de partida describe los campos que inicializa `defaultState()`: calendario, economía, energía, parcelas, inventario, afinidad, identidades conocidas, entradas, evidencia, variables narrativas, objetivos, banderas, noticias y preferencias de interfaz. Los rangos reflejan límites de juego donde son conocidos. `entries` guarda la identidad, el motivo elegido y el día; la partida no guarda secretos de plataforma ni datos personales.

El guardado actual carece de `schemaVersion`. Una futura migración debería añadir una versión explícita y validar/normalizar el JSON antes de usarlo, conservando valores válidos y restaurando los campos ausentes desde los valores predeterminados.

## Pseudocódigo del bucle principal

```text
al iniciar:
  intentar leer la partida local
  combinar campos conocidos con valores predeterminados
  conectar controles y atajos
  renderizar todas las vistas
  si es el primer día y falta la introducción: mostrar bienvenida

al realizar una acción con coste:
  comprobar requisitos (energía, horario, inventario y estado de la parcela)
  si falla un requisito: informar y no aplicar cambios
  aplicar coste de energía/tiempo
  aplicar el efecto de la acción
  actualizar nota o noticia cuando corresponda
  renderizar y guardar

al visitar un lugar:
  comprobar horario y energía
  registrar la visita y avanzar el reloj
  según el lugar:
    ofrecer tienda, pista, personaje, recolección o evento
  guardar el estado actualizado

al terminar el día:
  si ya se alcanzó el día 28: elegir final por umbrales y mostrar epílogo
  si no:
    avanzar los cultivos regados
    pasar al día siguiente, restaurar energía y establecer clima
    aplicar lluvia y preparar noticia/notificación
    renderizar, guardar y mostrar resumen de mañana

al confirmar una entrada del cuaderno:
  exigir objetivo conocido, no usado y energía suficiente
  registrar una sola entrada para esa identidad
  actualizar miedo, sospecha, confianza, justicia, devoción y estabilidad
  reiniciar afinidad de esa persona; publicar noticia ficticia
  no entregar dinero, objetos ni ventajas de granja
  renderizar, guardar y explicar consecuencias

al resolver el festival de faroles:
  elegir una respuesta disponible
  comprobar energía solo para ayudar a encenderlos
  aplicar una consecuencia social/narrativa distinta
  marcar el evento como resuelto y guardar
```

## Reglas y umbrales observables en código

- Las relaciones se limitan a 0–100; los medidores de miedo, sospecha, comunidad, justicia, devoción y estabilidad también usan límites de 0–100.
- El día inicia a las 06:00. Las acciones avanzan el reloj; dormir lo reinicia y restaura energía. El día 28 es el último día jugable antes del cierre de temporada.
- La tienda cierra a las 17:00, la comisaría a las 19:00 y Canal Valle a las 21:00.
- El final de descubrimiento tiene prioridad con sospecha ≥75; de otro modo, cero entradas conduce al final de paciencia. Tres o más entradas y miedo >65 conducen al final de miedo; los demás casos llegan al final intermedio.
- La renuncia voluntaria muestra el final correspondiente desde el perfil.

## Aspectos conocidos para una siguiente iteración

- `loadState()` combina algunos objetos con defaults, pero no valida tipos, rangos ni versiones.
- Las acciones de obtención de evidencia y varios flags narrativos son irrepetibles o acumulativos de forma desigual; deben mantenerse cubiertos por pruebas.
- El guardado automático ocurre durante el renderizado. Si el almacenamiento está bloqueado o lleno, la partida continúa en memoria y el indicador avisa.
- Los textos y datos se mantienen en el mismo archivo que la lógica; convendría separarlos si crece el contenido.
