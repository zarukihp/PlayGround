# QA y criterios de aceptación

## Entorno y preparación

- Abrir `index.html` en un navegador de escritorio actual o iniciar el servidor local con `./start.sh`.
- Revisar la consola del navegador durante los recorridos; no se requiere cuenta ni servicio externo.
- Cada caso que necesite partida limpia empieza con **Perfil → Reiniciar partida**. Para probar persistencia, recargar la misma pestaña/navegador sin limpiar `localStorage`.
- Los esquemas JSON de `schemas/` son contratos de referencia; el juego no los valida automáticamente.

## Casos manuales de aceptación

| ID | Recorrido | Resultado esperado |
|---|---|---|
| QA-01 | Abrir una partida nueva y recorrer Granja, Pueblo, Cuaderno, Tablón y Gente; usar los atajos 1–5 y Escape en un modal. | Se muestra la bienvenida inicial, las vistas cambian, los controles conservan su función y los modales pueden cerrarse sin errores de consola. |
| QA-02 | Sembrar una parcela sin semillas, repetir con una semilla comprada y después regar/cosechar. | La primera siembra cobra una vez; una semilla en bolsa se consume sin nuevo cargo; la parcela progresa al dormir tras ser regada, la cosecha se añade al inventario. |
| QA-03 | Comprar semillas y usar vender cosecha / regalar; probar también con cosecha y recursos. | Las semillas nunca se venden ni se regalan. Cosechas y recursos admitidos sí pueden venderse/regalarse; inventario y saldo se actualizan correctamente. |
| QA-04 | Conseguir dos nabos y entregar la cesta de Mara; intentar repetir la entrega. | La primera entrega consume dos nabos, da 40 ₲, afinidad y mejora comunitaria; la segunda no vuelve a pagar ni consumir. |
| QA-05 | Visitar tienda, comisaría y Canal Valle al límite y después del cierre. | Tienda cierra a las 17:00, comisaría a las 19:00 y Canal Valle a las 21:00; una visita rechazada no produce los efectos del lugar. |
| QA-06 | Visitar Canal Valle, comisaría, santuario y café; revisar objetivos conocidos y tablón. | Se desbloquean las identidades previstas y aparecen las pistas con fuente; los rumores y las pistas ambiguas no se presentan como prueba concluyente. |
| QA-07 | Seleccionar un objetivo sin conocerlo y luego uno conocido; confirmar entrada. | Un objetivo no conocido no se puede escribir; una entrada válida consume energía, queda registrada, altera variables sociales/investigativas y no concede recompensa material. La identidad no puede repetirse. |
| QA-08 | Interactuar con Bruma sin setas y luego con una seta; revisar inventario y evidencia. | Sin recurso no se consume nada; con seta se consume una y se registra una pista ambigua, sin declarar culpabilidad. |
| QA-09 | Dormir en días consecutivos con cultivos regados y sin regar; llegar al día 28. | Crecimiento y lluvia respetan el estado de parcela, energía y reloj se reinician al comenzar el día; el último día lleva al cierre de temporada y el epílogo correspondiente. |
| QA-10 | Visitar la plaza el día 7 y resolver el mercado; volver a visitar. | El mercado ocurre una sola vez por partida. |
| QA-11 | Llegar al día 14, visitar la plaza antes de las 19:00 y después desde las 19:00; resolver faroles y volver. | Antes de la hora no se presenta la escena; desde las 19:00 ofrece tres elecciones con efectos distintos; solo se puede resolver una vez. La opción de ayuda respeta el coste de energía. |
| QA-12 | Guardar, recargar y continuar; después elegir reiniciar desde el perfil. | La partida normal se recupera del almacenamiento local; reiniciar la elimina y devuelve los valores iniciales. No se promete sincronización ni resistencia a edición manual. |
| QA-13 | Abrir Perfil y elegir devolver el cuaderno. Abrir la guía con `?`. | La renuncia termina la partida con el final voluntario. La guía señala correctamente que se renuncia desde el perfil o se llega al día 28. |
| QA-14 | Probar en ventana estrecha y navegar los controles con teclado. | No hay desbordamiento que impida jugar; controles HTML reciben foco y se pueden activar por teclado. Esta prueba funcional no sustituye una auditoría formal de accesibilidad. |

## Revisión técnica

Comprobaciones ejecutables desde la raíz del proyecto:

```sh
node --check game.js
python3 -m json.tool docs/schemas/partida.schema.json >/dev/null
python3 -m json.tool docs/schemas/contenido.schema.json >/dev/null
```

La validación de sintaxis/JSON no reemplaza los recorridos manuales de navegador. No hay suite automatizada ni dependencia de test configurada actualmente.

## Criterios de salida del vertical slice

- Los casos de aceptación críticos QA-01 a QA-13 se completan sin errores de consola ni bloqueo del progreso.
- Compras, consumo, ventas y regalos respetan las reglas de semillas y recursos; los eventos únicos no se duplican al volver a visitar.
- Las decisiones del misterio persisten al recargar y muestran consecuencias coherentes con la ficción y con la documentación.
- Se anotan por separado las limitaciones visuales, de accesibilidad y de compatibilidad que queden pendientes; no se declara certificación formal.
