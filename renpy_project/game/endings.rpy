# Árbitro exclusivo: siempre resuelve un único final; los umbrales se documentan en LEEME.txt.
def ending_id():
    if flags["path"] == "renounce": return "E15"
    if flags["path"] == "martyr": return "E14"
    if flags["path"] == "traitor": return "E13"
    if flags["path"] == "detective":
        if evidence >= 6 and police_trust >= 65: return "E01"
        if evidence >= 4 and suspicion < 45: return "E02"
        if evidence < 2: return "E09"
        return "E03"
    if flags["path"] == "ally":
        if relationships["Iris"] >= 3 and police_trust >= 55: return "E04"
        if relationships["Vela"] >= 3 and kira_devotion >= 38: return "E05"
        if evidence >= 4: return "E06"
        return "E07"
    if flags["path"] == "kira":
        if flags["mistakes"] >= 2: return "E10"
        if sanity < 55: return "E11"
        if kira_devotion >= 75 and public_fear < 60: return "E08"
        if public_fear >= 50: return "E12"
        return "E08"
    return "E15"

label ending:
    $ result = ending_id()
    if result not in unlocked_endings:
        $ unlocked_endings.append(result)
    if result not in persistent.ash_endings:
        $ persistent.ash_endings.append(result)
    $ persistent.ash_completed = True
    $ renpy.save_persistent()
    scene bg rooftop with dissolve
    if result == "E01":
        show iris smile
        iris "La cadena de pruebas se sostiene. No porque confiáramos ciegamente: cada dato sobrevivió a una comprobación." 
        p "La verdad no devuelve a nadie, pero evita que el siguiente caso se pierda."
    elif result == "E02":
        show iris neutral
        iris "La ciudad conocerá la verdad. Mi nombre no aparecerá en el informe."
        p "Una victoria sin aplausos, y sin certezas cómodas."
    elif result == "E03":
        show iris sad
        iris "Llegamos tarde para reparar el daño. Aun así, el cuaderno ya no decidirá el próximo caso."
        p "La justicia sobrevivió; la confianza, no."
    elif result == "E04":
        show iris smile
        iris "Gracias por compartir tus dudas antes de convertirlas en certezas."
        p "La investigación y la amistad siguieron rutas paralelas, por fin con el mismo destino."
    elif result == "E05":
        show vela smile
        vela "No te pediré que adores a nadie. Quiero que me escuches a mí."
        p "La devoción se transformó en una conversación imperfecta, pero humana."
    elif result == "E06":
        show chief neutral
        ciro "Entregaremos la evidencia completa. Sin escoger qué parte merece existir."
        p "Una alianza incómoda cerró el caso sin borrar las preguntas."
    elif result == "E07":
        show nera suspicious
        nera "Pensaste que ayudar era lo mismo que obedecer. Ahora ya sabes la diferencia."
        p "Te apartaste del tablero antes de que alguien más moviera tu pieza."
    elif result == "E08":
        show noa neutral
        noa "El miedo tenía una fecha de caducidad. Yo no quise leerla."
        p "La ciudad se acostumbró a la calma; nadie se puso de acuerdo sobre su precio."
    elif result == "E09":
        show iris suspicious
        iris "Tu sospecha no produjo una sola prueba verificable. No es lo mismo que resolver el caso."
        p "El detective se marchó con una pregunta más y una respuesta menos."
    elif result == "E10":
        show noa fear
        noa "Me equivoqué al creer que una página podía ocultar todas mis huellas."
        p "Dos errores públicos bastaron para que la investigación encontrara un patrón."
    elif result == "E11":
        show noa sad
        noa "Ya no sé si estoy escribiendo para cambiar el mundo o para acallar mi propia cabeza."
        p "El cuaderno quedó cerrado. La habitación, no."
    elif result == "E12":
        show iris sad
        iris "El miedo no es consentimiento. La ciudad te teme, pero no te pertenece."
        p "La falsa paz se agrietó desde dentro."
    elif result == "E13":
        show nera smile
        nera "Una manzana por la información. No, no acepto pagos en efectivo."
        p "Traicionaste a ambos bandos; el único beneficiario pidió una siesta."
    elif result == "E14":
        show noa sad
        noa "Que el final de mi historia impida el principio de otra."
        p "Tu sacrificio puso fin al vínculo, no a todas las dudas."
    else:
        show noa smile
        noa "Cerré el cuaderno. Nera sigue exigiendo alquiler por vivir en mi armario."
        p "Nera aceptó una manzana como depósito. La humanidad conservó una deuda absurda."
    centered "[result] — [ending_title(result)]" with dissolve
    call screen ending_replay
    return

init python:
    def ending_title(code):
        names={"E01":"Archivo de la verdad","E02":"Sombra útil","E03":"La verdad incompleta","E04":"Dos métodos, una promesa","E05":"Fuera del altar","E06":"La alianza incómoda","E07":"La puerta entreabierta","E08":"La quietud prestada","E09":"Caso sin prueba","E10":"La firma del error","E11":"La tinta interior","E12":"Ciudad bajo cristal","E13":"El precio de una siesta","E14":"La última hoja","E15":"No escribir"}
        return names.get(code,"Final oculto")

screen ending_replay():
    modal True
    frame:
        xalign .5 yalign .5 padding (35,30) background "#111aee"
        vbox:
            spacing 14
            text "ARCHIVO DE FINALES — [len(persistent.ash_endings)] / 15" size 30 color "#f3d9bd"
            for code in sorted(persistent.ash_endings):
                text "[code] · [ending_title(code)]" size 20
            textbutton "Nueva ruta" action [Hide("ending_replay"), Jump("chapter_two")]
            textbutton "Menú principal" action [Hide("ending_replay"), MainMenu()]
