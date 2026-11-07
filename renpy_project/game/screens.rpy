# Pantallas mínimas para ejecutar el proyecto sin depender de una plantilla externa.

style ash_text:
    color "#eee8df"
    size 24

style ash_button_text:
    color "#eee8df"
    hover_color "#efcf9d"
    size 22

screen say(who, what):
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xsize 1180
        background Solid("#101626e8")
        padding (34, 24)
        vbox:
            spacing 10
            if who:
                text who id "who" color "#95d8e6" size 25
            text what id "what" style "ash_text"
            hbox:
                spacing 18
                textbutton "Historial" action ShowMenu("history")
                textbutton "Guardar" action ShowMenu("save")
                textbutton "Auto" action Preference("auto-forward", "toggle")
                textbutton "Saltar" action Skip()
                textbutton "Pistas" action Show("board_screen")
                textbutton "Estado" action Show("meters_screen")
                textbutton "Cuaderno" action Show("notebook_screen")

screen choice(items):
    modal True
    frame:
        xalign 0.5
        yalign 0.70
        xsize 1040
        background Solid("#101626eF")
        padding (28, 22)
        vbox:
            spacing 12
            for item in items:
                textbutton item.caption action item.action xfill True

screen input(prompt):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 24)
        vbox:
            spacing 14
            text prompt
            input id "input"

screen main_menu():
    tag menu
    add Solid("#101626")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 850
        background Solid("#182238ee")
        padding (48, 42)
        vbox:
            spacing 18
            text "CHRONICLE OF ASH" size 42 color "#efcf9d" xalign 0.5
            text "LA CIUDAD DE CENIZA · NOVELA VISUAL" size 22 xalign 0.5
            textbutton "Comenzar" action Start() xalign 0.5
            textbutton "Cargar partida" action ShowMenu("load") xalign 0.5
            textbutton "Preferencias" action ShowMenu("preferences") xalign 0.5
            textbutton "Salir" action Quit(confirm=True) xalign 0.5

screen navigation():
    vbox:
        spacing 8
        textbutton "Volver" action Return()
        textbutton "Guardar" action ShowMenu("save")
        textbutton "Cargar" action ShowMenu("load")
        textbutton "Preferencias" action ShowMenu("preferences")
        textbutton "Menú principal" action MainMenu()

screen game_menu(title="Menú"):
    tag menu
    add Solid("#080d19ee")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1120
        ysize 650
        background Solid("#202a3bee")
        padding (30, 26)
        hbox:
            spacing 30
            use navigation
            vbox:
                spacing 14
                text title size 34 color "#efcf9d"
                transclude

screen save():
    use game_menu("Guardar"):
        vbox:
            spacing 12
            text "Selecciona una ranura para guardar la partida." size 20
            grid 4 3:
                spacing 10
                for slot in range(1, 13):
                    textbutton "Ranura [slot] · [FileTime(slot, format='%Y-%m-%d %H:%M') or 'vacía']" action FileSave(slot)

screen load():
    use game_menu("Cargar"):
        vbox:
            spacing 12
            text "Selecciona una partida guardada." size 20
            grid 4 3:
                spacing 10
                for slot in range(1, 13):
                    textbutton "Ranura [slot] · [FileTime(slot, format='%Y-%m-%d %H:%M') or 'vacía']" action FileLoad(slot)

screen preferences():
    use game_menu("Preferencias"):
        vbox:
            spacing 16
            textbutton "Velocidad de texto: normal" action Preference("text speed", 30)
            textbutton "Avance automático: cambiar" action Preference("auto-forward", "toggle")
            textbutton "Modo de pantalla: cambiar" action Preference("display", "toggle")

screen history():
    use game_menu("Historial"):
        viewport:
            draggable True
            mousewheel True
            ysize 530
            vbox:
                spacing 8
                for entry in _history_list:
                    if entry.who:
                        text "[entry.who]: [entry.what]" size 18
                    else:
                        text entry.what size 18

screen confirm(message, yes_action, no_action):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        background Solid("#202a3bee")
        padding (32, 28)
        vbox:
            spacing 18
            text message
            hbox:
                spacing 20
                textbutton "Sí" action yes_action
                textbutton "No" action no_action

screen notify(message):
    frame:
        xalign 0.98
        yalign 0.05
        background Solid("#202a3bee")
        padding (18, 12)
        text message size 18

screen skip_indicator():
    text "SALTANDO" xalign 0.98 yalign 0.02 size 16 color "#efcf9d"
