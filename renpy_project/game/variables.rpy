# Chronicle of Ash — estado persistente y medidores.
default suspicion = 12
default police_trust = 38
default kira_devotion = 18
default public_fear = 12
default sanity = 82
default notebook_power = 55
default evidence = 0
default relationships = {"Iris": 0, "Nera": 0, "Vela": 0, "Ciro": 0}
default flags = {"path": "undecided", "face_known": False, "real_name_known": False, "witness": False, "idol": False, "mistakes": 0, "new_game_plus": False}
default notebook_name = ""
default notebook_cause = ""
default notebook_hour = ""
default unlocked_endings = list(getattr(persistent, "ash_endings", []))
default unlocked_clues = []
default achievements = []
default quick_menu = True

init python:
    if not hasattr(persistent, "ash_completed"):
        persistent.ash_completed = False
    if not hasattr(persistent, "ash_endings"):
        persistent.ash_endings = []

init python:
    def clamp_stats():
        global suspicion, police_trust, kira_devotion, public_fear, sanity, notebook_power, evidence
        suspicion = max(0, min(100, suspicion))
        police_trust = max(0, min(100, police_trust))
        kira_devotion = max(0, min(100, kira_devotion))
        public_fear = max(0, min(100, public_fear))
        sanity = max(0, min(100, sanity))
        notebook_power = max(0, min(100, notebook_power))
        evidence = max(0, min(10, evidence))

    def clue(name):
        if name not in unlocked_clues:
            unlocked_clues.append(name)
            renpy.notify("Pista añadida: " + name)

    def adjust(key, delta):
        store.__dict__[key] = store.__dict__.get(key, 0) + delta
        clamp_stats()
