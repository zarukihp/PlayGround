# Alcance y hoja de ruta

## Resumen

**Cuaderno & Cosecha** es un vertical slice web local para un jugador. Combina una rutina de granja con ocho habitantes locales, investigación narrativa y un misterio sobrenatural. El propósito de esta entrega es demostrar un ciclo jugable completo de primavera, no ofrecer un producto comercial terminado.

## Alcance implementado

- Primavera de 28 días, reloj diario, energía, clima, guardado local y cinco vistas principales.
- Seis parcelas y seis cultivos, compra/consumo de semillas, riego, crecimiento, cosecha, venta y recursos recolectables.
- La Despensa, comisaría, Canal Valle/radio, santuario, bosque, café, plaza y cantera.
- Ocho habitantes locales y Sael como visitante; conversaciones, regalos, afinidad y cesta de bienvenida de Mara.
- Cinco objetivos narrativos, pistas y entradas irreversibles en el cuaderno. La identidad confirmada no se presenta como prueba de culpabilidad.
- Mercado de primavera (día 7) y escena interactiva de faroles (día 14, desde las 19:00), ambos con activación única por partida.
- Noticias, advertencias de sospecha, opción voluntaria de renunciar al cuaderno y finales de temporada.
- Interfaz responsive, ayuda, calendario, modales y guardado automático en el almacenamiento local del navegador.

## Fuera de alcance

- Servidor, cuentas, sincronización entre dispositivos, multijugador o copias de seguridad remotas.
- Combate, contenido gráfico de violencia, instrucciones de daño real o simulación forense.
- Economía de temporada completa, recetas, construcción avanzada, más estaciones, misiones extensas o diálogos con ramas profundas.
- Audio ambiental funcional, localización a otros idiomas, sistema de mods, analítica o telemetría.
- Protección contra edición/manipulación del guardado en el navegador.

## Hoja de ruta sugerida

### Fase 0 — Vertical slice actual

Contenido listado arriba. Criterio de salida: los recorridos principales pueden completarse sin errores de consola, las decisiones se guardan y la documentación refleja el comportamiento real.

### Fase 1 — Estabilidad y accesibilidad

- Validación en navegadores de escritorio y móvil; corrección de foco, contraste, etiquetas y navegación por teclado.
- Pruebas automatizadas de economía, calendario, límites de estadísticas y migración de partidas guardadas.
- Mejoras de feedback para energía, horarios, errores y estados de objetivos.

### Fase 2 — Profundidad narrativa

- Revisar cada pista y su procedencia; separar explícitamente observación, rumor e inferencia.
- Añadir escenas y respuestas de personajes que reaccionen a la confianza comunitaria sin premiar daño.
- Balancear finales y ofrecer resúmenes de decisiones comprensibles.

### Fase 3 — Preparación de publicación

- Auditoría de marca, título, historia, assets, fuentes tipográficas y licencias.
- Sustituir/autorizar recursos externos según la estrategia de distribución; añadir avisos de privacidad y soporte.
- Pruebas de rendimiento, empaquetado, compatibilidad y revisión legal en los territorios de publicación.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Las pistas ambiguas se leen como prueba | Rotular cada pista por fuente y reforzar en UI que identidad no equivale a culpabilidad. |
| La mecánica del cuaderno recuerda obras existentes | Mantener nombres, arte, texto, personajes, mundo y presentación propios; revisar el concepto completo antes de publicar y pedir asesoría legal si hay dudas. |
| El guardado del navegador se pierde o se manipula | Informar que el guardado es local; no usarlo como almacenamiento de datos sensibles ni como sistema competitivo. |
| Una acción rutinaria deja estados incoherentes | Cubrir límites, eventos de un solo uso, recarga y final de temporada con QA manual y automatizado. |
