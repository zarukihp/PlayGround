screen notebook_screen(called=False):
    modal True
    add Solid("#050912dd")
    frame:
        xalign .5 yalign .5 xsize 980 ysize 610 padding (38,32) background "#182238ee"
        vbox:
            spacing 14
            text "CUADERNO DE CENIZA" size 34 color "#eecb91"
            text "REGLA 01 · El nombre auténtico y un rostro reconocido son necesarios." size 19
            text "Un nombre falso no activa la página. Nunca se muestran instrucciones para identificar personas reales." size 17 color "#b8c5d8"
            hbox:
                spacing 12
                vbox:
                    text "Nombre (ficción)" size 18
                    input value VariableInputValue("notebook_name") length 36
                vbox:
                    text "Causa (opcional)" size 18
                    input value VariableInputValue("notebook_cause") length 36
                vbox:
                    text "Hora (opcional)" size 18
                    input value VariableInputValue("notebook_hour") length 10
            text "Rostro reconocido: [ 'SÍ' if flags['face_known'] else 'NO' ]   ·   Poder: [notebook_power]" size 18 color "#b8c5d8"
            if flags["real_name_known"] and flags["face_known"] and notebook_name.strip():
                textbutton "Confirmar entrada ficticia" action [Function(use_notebook), If(called, Return(), Hide("notebook_screen"))]
            else:
                text "Entrada bloqueada: falta nombre confirmado y/o rostro conocido." size 18 color "#df9b9b"
            textbutton "Cerrar sin escribir" action If(called, Return(), Hide("notebook_screen"))
    key "K_ESCAPE" action If(called, Return(), Hide("notebook_screen"))

screen board_screen(called=False):
    modal True
    add Solid("#080d19dd")
    frame:
        xalign .5 yalign .5 xsize 1050 ysize 600 padding (32,28) background "#202a3bee"
        vbox:
            spacing 12
            text "TABLÓN · Hechos comprobables" size 32 color "#efcf9d"
            text "Pistas: [', '.join(unlocked_clues) if unlocked_clues else 'Ninguna confirmada']" size 20
            text "HIPÓTESIS (no equivalen a prueba): muertes nocturnas · informativos públicos · sesgo de selección." size 18
            text "Evidencia [evidence]/10 · Testigo: [ 'sí' if flags['witness'] else 'no' ] · Vigilancia: [ 'activa' if evidence >= 3 else 'sin base suficiente' ]" size 18 color "#bfd4df"
            textbutton "Volver" action If(called, Return(), Hide("board_screen"))
    key "K_ESCAPE" action If(called, Return(), Hide("board_screen"))

screen meters_screen():
    modal True
    add Solid("#080d19dd")
    frame:
        xalign .5 yalign .5 xsize 820 ysize 560 padding (32,28) background "#202a3bee"
        vbox:
            spacing 10
            text "ESTADO · Relaciones y medidores" size 30 color "#efcf9d"
            text "Sospecha detective [suspicion]  |  Confianza policial [police_trust]" size 19
            text "Devoción Kira [kira_devotion]  |  Miedo público [public_fear]" size 19
            text "Cordura [sanity]  |  Poder cuaderno [notebook_power]  |  Evidencia [evidence]" size 19
            text "Iris [relationships['Iris']] · Nera [relationships['Nera']] · Vela [relationships['Vela']] · Ciro [relationships['Ciro']]" size 18
            textbutton "Cerrar" action Hide("meters_screen")
    key "K_ESCAPE" action Hide("meters_screen")

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign .985 yalign .018 spacing 8
            textbutton "Historial" action ShowMenu("history")
            textbutton "Guardar" action ShowMenu("save")
            textbutton "Auto" action Preference("auto-forward", "toggle")
            textbutton "Saltar" action Skip()
            textbutton "Cuaderno" action Show("notebook_screen")
            textbutton "Pistas" action Show("board_screen")
            textbutton "Estado" action Show("meters_screen")

init python:
    def use_notebook():
        if not flags["real_name_known"] or not flags["face_known"] or not notebook_name.strip():
            flags["mistakes"] += 1
            renpy.notify("La página permanece vacía. Faltan condiciones verificables.")
            return
        flags["mistakes"] += 1
        adjust("notebook_power", -7)
        adjust("sanity", -9)
        adjust("public_fear", 4)
        clue("Una entrada ficticia comprobada por el sistema")
        renpy.notify("Ensayo narrativo registrado. No hay personas reales en esta simulación.")
