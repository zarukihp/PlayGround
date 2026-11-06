# Documento de diseño (GDD)

## 1. Ficha del proyecto

- **Título de trabajo:** *Cuaderno & Cosecha*.
- **Género:** simulación de granja y vida social con misterio sobrenatural y thriller narrativo.
- **Formato:** prototipo web de un jugador, HTML/CSS/JavaScript sin framework ni servidor.
- **Público:** personas que disfrutan de rutinas acogedoras y decisiones narrativas con consecuencias.
- **Tono:** cotidiano, melancólico y sobrenatural; sin gore ni representación gráfica de violencia.
- **Ambientación:** Valle Manzano, una comunidad rural ficticia. La granja, sus habitantes y el cuaderno son propiedad creativa original de este prototipo.

## 2. Premisa y fantasía del jugador

El jugador hereda una granja en Valle Manzano. Entre tareas, amistades y rumores encuentra un cuaderno sobrenatural, custodiado por Bruma. Sus páginas permiten causar la desaparición ficticia de una persona cuyo nombre y rostro se conocen. El cuaderno no revela culpables ni garantiza justicia: cada uso altera el miedo, la confianza comunitaria y la atención del detective Sael.

La fantasía central consiste en **cultivar una vida cotidiana y decidir qué hacer con un poder que no ofrece respuestas morales fáciles**. El jugador puede investigar, construir vínculos, ignorar el cuaderno o usarlo; nunca recibe dinero, objetos ni ventajas de granja por escribir un nombre.

## 3. Pilares de diseño

1. **Rutina acogedora y legible:** sembrar, regar, cosechar, vender, explorar y conversar con acciones cortas.
2. **Personajes con matices:** cada pista puede ser incompleta; los secretos no equivalen automáticamente a culpabilidad.
3. **Consecuencias sin recompensa violenta:** usar el cuaderno reduce energía y confianza, aumenta miedo y sospecha, y puede afectar relaciones y finales.
4. **Investigación responsable:** identidad confirmada no equivale a culpabilidad demostrada. La interfaz recuerda que una pista no es una prueba.
5. **Ficción segura y original:** sucesos fuera de escena, sin gore, y sin presentar instrucciones para dañar a personas reales.

## 4. Bucle de juego

### Bucle diario
1. Leer la nota, el clima y la noticia de la mañana.
2. Elegir cómo gastar el tiempo y la energía entre la granja y el pueblo.
3. Cuidar cultivos, buscar recursos, conversar, regalar o investigar.
4. Revisar dinero, objetivos, relaciones, pistas y nivel de sospecha.
5. Terminar el día: los cultivos regados progresan, la lluvia puede regar el campo y se recupera la energía.

### Bucle de temporada
- La primavera dura 28 días.
- Hay seis cultivos, seis parcelas, compra de semillas, recolección y venta.
- El día 7 se celebra el mercado de primavera al visitar la plaza ese día.
- El día 14, desde las 19:00, se activa una escena interactiva de la noche de faroles en la plaza. Una de tres respuestas modifica vínculos, bienestar comunitario o evidencia; el evento solo puede resolverse una vez.
- La temporada concluye con un epílogo determinado por las decisiones y la investigación.

### Decisión del cuaderno
Para habilitar una entrada se debe conocer una identidad entre los cinco objetivos narrativos, seleccionar a la persona y confirmar la decisión. Cada identidad solo puede recibir una entrada. La elección deja un registro permanente en la partida y produce cambios sociales y de investigación; no se concede una recompensa material.

## 5. Sistemas y reglas

### Granja y economía
- Seis parcelas y seis cultivos: nabo, judía, patata, fresa, flor y calabaza.
- Las semillas se compran en La Despensa o se adquieren como compra directa desde el selector de siembra. Si ya hay semillas de esa variedad en la bolsa, se consume una y no se vuelve a cobrar.
- Regar cuesta energía y hace avanzar el cultivo al dormir; la lluvia riega automáticamente.
- Cosechar añade una unidad al inventario. Se pueden vender cosechas, setas silvestres y piedra lisa.
- Las semillas no son artículos vendibles ni regalables.
- La cesta de Mara requiere dos nabos y entrega 40 ₲, amistad y una pequeña mejora comunitaria. Es una recompensa social/económica ordinaria, independiente del thriller.

### Tiempo y energía
- El día comienza a las 06:00. Las acciones avanzan el reloj y consumen energía; los menús y diálogos no lo hacen avanzar por sí solos.
- Dormir restaura la energía y resuelve el crecimiento de cultivos.
- Las tiendas tienen horarios visibles. El clima varía y la jornada lluviosa favorece los cultivos.

### Relaciones
- Ocho habitantes locales: Mara, Teo, Iris, Darío, Nerea, Basil, Luz y Elia. El personaje jugador no se cuenta como NPC. Sael es un detective visitante adicional, no parte del grupo de ocho habitantes.
- Conversar, regalar y participar en el festival de faroles aumenta relaciones; cada NPC tiene un gusto. El juego muestra corazones y amistades cercanas.
- Las relaciones pueden reiniciarse al escribir el nombre de esa persona; la ausencia afecta al tejido comunitario.

### Investigación
- Cinco objetivos: Darío, Basil, Nerea, Iris y Luz.
- Fuentes: radio/Canal Valle, comisaría, santuario, café y pistas ambiguas de Bruma.
- La lista del cuaderno solo muestra identidades desbloqueadas. El tablón diferencia evidencia observada de conclusiones.
- Sael observa rutinas y patrones; la sospecha aumenta con ciertas decisiones y puede activar una advertencia y el final de descubrimiento.

### Variables narrativas
- `fear`: inquietud pública; aumenta con las entradas y cambia las noticias y la descripción del festival.
- `suspicion`: atención de Sael; determina su escalada narrativa y puede activar el final de descubrimiento.
- `community`: confianza colectiva; baja especialmente tras entradas sin sustento.
- `justice`: valoración narrativa del resultado; los datos sólidos y los falsos positivos tienen consecuencias diferentes.
- `devotion` y `stability`: medidores del vínculo con el cuaderno y del deterioro del entorno, respectivamente.
- `relationships`: afinidad individual con personajes.

### Finales
- **La paciencia también es justicia:** temporada sin entradas.
- **Una primavera imperfecta:** uso limitado del cuaderno sin llegar a otro umbral dominante.
- **El valle bajo una sola sombra:** tres o más entradas y miedo alto.
- **La verdad sale a la luz:** sospecha alta del detective al concluir la temporada.
- **Devolver lo imposible:** final voluntario al devolver el cuaderno desde el perfil.

Los finales describen consecuencias sociales; no son premios por causar daño. Los umbrales son prototípicos y pueden ajustarse tras pruebas de balance.

## 6. Personajes

| Personaje | Función | Matiz narrativo / pista |
|---|---|---|
| Mara Solís | Tendera y vínculo de bienvenida | Pide dos nabos; conserva cartas relacionadas con una deuda ajena. |
| Teo Luján | Carpintero | Oyó una discusión, pero no se atreve a contarla. |
| Iris Vega | Locutora | Editó una entrevista para proteger a alguien; una grabación parcial no basta para condenarla. |
| Darío Castañeda | Concejal y objetivo | La auditoría ofrece evidencia de fondos desviados y presión sobre un testigo. |
| Nerea Vidal | Voluntaria de clínica y objetivo | Ocultó medicinas para mantener abierta la clínica; el rumor contra ella no está verificado. |
| Basil Roca | Guardabosques y objetivo | Su coartada es incompleta, pero no demuestra violencia. |
| Luz Paredes | Agente y objetivo | Compartió información para contrastar una pista; el caso sigue abierto. |
| Elia Robles | Apicultora | Cuida el colmenar y conserva un archivo vecinal de cartas y favores; organiza los faroles. |
| Sael | Detective visitante | Contrasta horarios y patrones, no lee la mente ni conoce automáticamente la verdad. |
| Bruma | Testigo sobrenatural | Comentario atmosférico y pista deliberadamente ambigua; no dicta culpabilidad. |

## 7. Lugares

La granja, La Despensa, comisaría, Canal Valle, santuario, bosque norte, Café del puente, plaza central y cantera vieja. El prototipo presenta los ocho destinos del pueblo como tarjetas interactivas y la granja como vista propia.

## 8. Interfaz y accesibilidad funcional

- Navegación por cinco vistas, atajos de teclado 1–5 y cierre de modal con Escape.
- Indicadores de día, hora, energía, dinero, clima, miedo y sospecha.
- Confirmaciones en modal para decisiones narrativas y mensajes breves para acciones rutinarias.
- Maquetación responsive y controles HTML semánticos. Recomendación pendiente: revisión completa de contraste, foco visible, lectores de pantalla y reducción de movimiento.

## 9. Audio y arte

El prototipo utiliza ilustración CSS, iconos Unicode/emoji y tipografías web enlazadas; no contiene escenas gráficas ni assets de personajes de terceros. El botón de sonido es actualmente una señal visual de interfaz, no una mezcla de audio implementada. Para publicación debe preferirse audio original o con licencia documentada.

## 10. Alcance actual y límites conocidos

Este entregable es un vertical slice funcional, no un juego comercial terminado. Las conversaciones usan líneas rotativas breves; algunas variables narrativas se registran aunque todavía no alteren todos los sistemas. El evento del día 14 tiene una escena interactiva con tres respuestas y consecuencias limitadas. No hay combate, multijugador, servidor, sincronización entre dispositivos ni garantía anti-manipulación del guardado local.
