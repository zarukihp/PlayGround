# Chronicle of Ash — novela visual de misterio sobrenatural. Todas las personas/casos son ficticios.
label start:
    $ flags["new_game_plus"] = bool(getattr(persistent, "ash_completed", False))
    if flags["new_game_plus"]:
        $ notebook_power = min(100, notebook_power + 10)
        $ unlocked_clues.append("Recuerdo de otra vuelta")
    scene bg alley with dissolve
    # Audio opcional omitido: el proyecto funciona sin archivos externos de sonido.
    show cg discovery with dissolve
    p "La lluvia dejó el callejón sin testigos. Casi sin testigos."
    hide cg discovery with dissolve
    show noa tense
    noa "No estaba aquí cuando salí de la universidad. Tiene mi nombre escrito en la tapa… aunque la letra no es mía."
    p "El cuaderno negro está seco. En la primera hoja, una frase: «Lo que se entrega a la noche siempre cobra una respuesta»."
    show noa suspicious
    noa "¿Quién dejaría algo así en un callejón?"
    menu:
        "Llevarlo a la comisaría y declarar dónde apareció":
            $ flags["path"] = "detective"
            $ police_trust += 12
            $ suspicion -= 5
            $ relationships["Ciro"] += 1
            $ clue("Cuaderno hallado en el callejón; origen incierto")
            p "Noa fotografió el objeto sin abrirlo y llamó a su padre, el comisario Ciro."
        "Guardarlo y estudiar primero las páginas":
            $ flags["path"] = "kira"
            $ kira_devotion += 8
            $ sanity -= 3
            $ clue("Tapa sin huellas legibles bajo la lluvia")
            p "La curiosidad ganó por un instante. Noa lo guardó dentro de la mochila."
        "No tocarlo; buscar cámaras y preguntar al quiosquero":
            $ flags["path"] = "ally"
            $ evidence += 1
            $ police_trust += 5
            $ suspicion -= 3
            $ flags["witness"] = True
            $ clue("Un quiosquero vio una silueta dejar el cuaderno")
            p "Una cámara municipal apuntaba al callejón. El quiosquero recordaba una gabardina clara, no un rostro."
    scene bg apartment with dissolve
    show nera neutral
    nera "Buenas. ¿Tienes una manzana? No, claro que no. La gente cree que los muertos necesitan modales."
    show noa surprise
    noa "¿Quién eres? ¿Cómo has entrado?"
    nera "Nera. Vigía de la última tinta. Y sí, ese cuaderno puede escribir una muerte. Nombre auténtico y rostro conocido. Nada de apodos."
    p "Nera bosteza y se sienta en el suelo, como si anunciar lo imposible fuera una tarea doméstica."
    menu:
        "Pedir las reglas completas, sin aceptar nada":
            $ sanity += 4
            $ relationships["Nera"] += 1
            $ clue("Regla declarada: nombre auténtico + rostro reconocido")
            nera "Causa y hora son opcionales; el efecto no puede superar lo posible. Un nombre equivocado no hace nada."
        "Exigir que se marche y cerrar el cuaderno":
            $ sanity += 2
            $ notebook_power -= 4
            $ relationships["Nera"] -= 1
            nera "Qué falta de hospitalidad. Te lo explicaré desde el pasillo."
        "Preguntar qué gana ella":
            $ suspicion += 3
            $ relationships["Nera"] += 2
            nera "Yo gano una manzana. La eternidad es larga y la fruta siempre está demasiado lejos."
    scene bg tv with dissolve
    # El boletín de radio se presenta mediante diálogo; no requiere un archivo de audio.
    radio "La ciudad debate la muerte de tres criminales condenados. En redes, una firma anónima ya tiene nombre: Kira. La policía no confirma relación entre los casos."
    p "El presentador no mostró imágenes explícitas; sí mostró portadas, horarios y el miedo creciendo en comentarios."
    show noa tense
    noa "Si alguien usa el cuaderno, ¿la ciudad lo llamará justicia?"
    menu:
        "La opinión pública no convierte sospechas en pruebas":
            $ suspicion -= 2
            $ police_trust += 4
            $ clue("Las tres muertes compartían cobertura mediática, no causa confirmada")
            p "Noa anotó hechos observables y dejó las conclusiones en blanco."
        "La gente puede apoyar una idea y temer a quien la encarna":
            $ kira_devotion += 6
            $ public_fear += 3
            $ relationships["Vela"] += 1
            p "Una voz del canal de espectáculos interrumpió: Vela Lune había defendido públicamente al justiciero."
        "Desconectar la pantalla":
            $ sanity += 3
            $ public_fear += 1
            p "La habitación quedó en silencio, aunque el resplandor de la pantalla tardó en irse."
    scene bg university with dissolve
    show iris suspicious
    iris "Soy Iris Vale. Asesoro al equipo de investigación. ¿Por qué una estudiante de criminología preguntó por los horarios de los fallecimientos?"
    noa "Porque los horarios son públicos y no prueban nada por sí solos."
    iris "Buena respuesta. ¿Y cuál es tu hipótesis que más te incomoda?"
    menu:
        "Un imitador puede estar copiando el patrón de los medios":
            $ evidence += 1
            $ relationships["Iris"] += 1
            $ police_trust += 3
            $ clue("Hipótesis de imitación mediática; requiere contraste")
            iris "Es comprobable. No significa que sea cierta."
        "Que la investigación confirme primero cronología y coartadas":
            $ evidence += 2
            $ relationships["Iris"] += 2
            $ suspicion -= 2
            $ clue("Cronología verificada; faltan coartadas independientes")
            iris "Exacto. Una coartada se comprueba; no se adivina."
        "Que la propia policía filtre información sin querer":
            $ suspicion += 4
            $ police_trust -= 3
            $ clue("Posible filtración institucional aún no corroborada")
            iris "Esa hipótesis también se investiga con registros, no con intuición."
    scene bg cafe with dissolve
    show vela smile
    vela "Noa, ¿verdad? Soy Vela. Yo creo que la ciudad merece menos impunidad. No significa que confíe en cualquier desconocido."
    menu:
        "Escuchar su motivo sin prometer lealtad":
            $ relationships["Vela"] += 2
            $ kira_devotion += 2
            vela "Gracias. La gente oye una canción y se inventa una persona detrás."
        "Discrepar: el miedo no es justicia":
            $ relationships["Vela"] -= 1
            $ police_trust += 2
            $ public_fear -= 2
            vela "Puede que tengas razón. No me gusta que la respuesta sea tan sencilla."
        "Preguntar qué fuentes tiene, no qué siente":
            $ evidence += 1
            $ relationships["Vela"] += 1
            $ clue("Vela solo conoce rumores públicos; no es testigo de los casos")
            vela "Ninguna fuente privada. No confundas mi fama con acceso a la verdad."
    scene bg police with dissolve
    show chief neutral
    ciro "El detective extranjero usa el nombre Iris Vale. Es brillante, excéntrica y detesta las afirmaciones que no puede verificar."
    ciro "Noa, si viste algo en ese callejón, dilo. La confianza sirve cuando también admite dudas."
    menu:
        "Entregar el cuaderno y contar toda la verdad":
            $ flags["path"] = "detective"
            $ police_trust += 12
            $ suspicion -= 4
            $ evidence += 1
            $ relationships["Ciro"] += 2
            $ clue("Declaración íntegra de Noa registrada")
            p "Ciro no dijo que el objeto fuera inofensivo. Lo puso bajo custodia y llamó a dos testigos."
        "Ocultar el cuaderno, pero ofrecer ayudar con las pistas":
            $ flags["path"] = "ally"
            $ police_trust += 3
            $ suspicion += 3
            $ relationships["Ciro"] -= 1
            p "La omisión pesó más que la mentira: Noa no podía olvidar que había elegido callar."
        "Negarlo todo y pedir que dejen a la familia fuera":
            $ flags["path"] = "kira"
            $ police_trust -= 8
            $ suspicion += 8
            $ sanity -= 4
            $ flags["mistakes"] += 1
            p "Ciro no levantó la voz. Su silencio hizo más daño que una acusación."
    $ clamp_stats()
    scene bg rooftop with dissolve
    show iris tense
    iris "Las páginas públicas no bastan para atribuir un patrón a una persona. Tendremos que separar hechos, fuentes y coincidencias."
    p "La lluvia se alejó. En las pantallas de la ciudad, el nombre Kira seguía creciendo sin que nadie pudiera probar quién lo había escrito."
    centered "CAPÍTULO 1 · El margen de la noche" with dissolve
    jump chapter_two

label chapter_two:
    scene bg interrogation with dissolve
    show iris neutral
    iris "Ruta inicial: [flags['path']]. Evidencia: [evidence]. Confianza policial: [police_trust]. ¿Qué haces ahora?"
    menu:
        "Ruta detective: auditar horarios, fuentes y coartadas":
            $ flags["path"] = "detective"
            jump route_detective
        "Ruta aliada: colaborar sin entregar todas tus dudas":
            $ flags["path"] = "ally"
            jump route_ally
        "Ruta Kira: usar el poder en una decisión de alto riesgo":
            $ flags["path"] = "kira"
            jump route_kira
        "Ruta mártir: cortar la cadena exponiéndote":
            $ flags["path"] = "martyr"
            $ sanity -= 8
            jump ending
        "Ruta traidor: vender información a Nera por manzanas":
            $ flags["path"] = "traitor"
            $ relationships["Nera"] += 3
            jump ending
        "Renunciar al cuaderno y entregarlo":
            $ flags["path"] = "renounce"
            $ notebook_power = 0
            $ flags["face_known"] = False
            jump ending

label route_detective:
    scene bg police with dissolve
    show iris suspicious
    iris "La vigilancia solo se autoriza con hechos y alcance limitado. Podemos revisar el registro público de cámaras, entrevistar testigos o comparar coartadas."
    menu:
        "Verificar dos fuentes independientes y preservar el registro":
            $ evidence += 4
            $ police_trust += 12
            $ suspicion -= 7
            $ relationships["Iris"] += 2
            $ clue("Dos fuentes independientes corroboran la cronología")
        "Cotejar coartadas y descartar una coincidencia":
            $ evidence += 3
            $ police_trust += 7
            $ suspicion -= 5
            $ relationships["Iris"] += 1
            $ clue("Coartada comprobada mediante registro público")
        "Filtrar una sospecha sin verificar para acelerar el caso":
            $ evidence = max(0, evidence - 2)
            $ police_trust -= 15
            $ suspicion += 18
            $ sanity -= 5
            p "El rumor llevó a un testigo inocente a abandonar la ciudad. La pista quedó contaminada."
    $ clamp_stats()
    menu:
        "Construir una conclusión que sobreviva a una refutación":
            $ evidence += 2
            $ police_trust += 7
            $ suspicion -= 4
            $ relationships["Iris"] += 1
        "Proteger a un informante aunque el informe quede incompleto":
            $ evidence += 1
            $ police_trust += 2
            $ relationships["Ciro"] += 2
        "Revisar el tablón de pistas y decidir":
            call screen board_screen(called=True)
            $ evidence += 1
    $ clamp_stats()
    jump ending

label route_ally:
    scene bg cafe with dissolve
    show vela neutral
    vela "Puedo poner mi plataforma al servicio de una corrección pública. Iris puede compartir el método, no sus expedientes. ¿A quién priorizamos?"
    menu:
        "Compartir incertidumbre con Iris y contrastar el registro":
            $ relationships["Iris"] += 3
            $ police_trust += 12
            $ evidence += 2
            $ suspicion -= 4
        "Ayudar a Vela a separar admiración de obediencia":
            $ relationships["Vela"] += 3
            $ kira_devotion += 12
            $ public_fear -= 7
        "Proteger a Ciro del escándalo y aportar una pista":
            $ relationships["Ciro"] += 2
            $ police_trust += 6
            $ evidence += 4
        "Abrir el cuaderno y fingir que fue un accidente":
            $ flags["path"] = "kira"
            $ flags["mistakes"] += 1
            $ sanity -= 15
            jump route_kira
    $ clamp_stats()
    jump ending

label route_kira:
    scene bg apartment with dissolve
    show nera suspicious
    nera "Las reglas no son una recomendación. Y una página no demuestra nada sobre una persona real. No uses nombres de gente real: esto es un drama ficticio."
    menu:
        "Anotar en la página de prueba un alias inventado, no una persona":
            $ flags["real_name_known"] = True
            $ flags["face_known"] = True
            $ notebook_name = "Rival ficticio: Eco"
            $ notebook_cause = "Silencio"
            $ notebook_hour = "03:00"
            $ sanity -= 5
            $ kira_devotion += 14
            call screen notebook_screen(called=True)
        "Destruir tu copia de la llave y no volver a escribir":
            $ flags["path"] = "renounce"
            $ notebook_power = 0
            jump ending
        "Preguntar a Nera si el poder tiene un límite":
            $ relationships["Nera"] += 2
            $ notebook_power -= 3
            nera "Sí. La voluntad no puede torcer lo físicamente imposible. Tampoco puede volver inocente una decisión."
    menu:
        "Mantener la calma y dejar de buscar aprobación":
            $ sanity += 6
            $ kira_devotion += 4
            $ public_fear -= 3
        "Usar el cuaderno otra vez: la doble entrada revela tu patrón":
            $ flags["mistakes"] += 1
            $ notebook_power -= 12
            $ sanity -= 15
            $ public_fear += 18
            $ suspicion += 8
        "Provocar pánico para forzar una respuesta pública":
            $ public_fear += 38
            $ kira_devotion += 8
            $ sanity -= 8
        "Aislarte y dejar que la culpa erosione tu cordura":
            $ sanity -= 32
    $ clamp_stats()
    jump ending
