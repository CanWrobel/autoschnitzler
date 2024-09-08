import pyautogui
import time
import zustandWorldMap
import zustandLootbildschirm
import zustandInFight
import zustandLoserComp

# Definiere die Zustände
STATE_WORLDMAP = "worldmap"
STATE_ATTACKSCREEN = "attackscreen"
STATE_LOOTSCREEN = "lootscreen"
STATE_LOSERCOMP = "losercomp"

# Setze den Anfangszustand
current_state = STATE_WORLDMAP

# Hauptschleife
while True:
    if current_state == STATE_WORLDMAP:
        print("Im Worldmap-Zustand")
        if not zustandWorldMap.world_map():
            print("Wechsel zu Attack-Screen")
            current_state = STATE_ATTACKSCREEN
        else:
            print("Noch in der Worldmap...")

    elif current_state == STATE_ATTACKSCREEN:
        print("Im Attack-Zustand")
        if not zustandInFight.in_fight():
            print("Wechsel zu Loot-Screen")
            time.sleep(2) # Warte kurz, um den Loot-Screen zu erkennen
            current_state = STATE_LOOTSCREEN
        else:
            print("Noch im Kampf...")

    elif current_state == STATE_LOOTSCREEN:
        print("Im Loot-Screen-Zustand")
        if not zustandLootbildschirm.loot_bildschirm():
            print("Wechsel zu Worldmap")
            current_state = STATE_LOSERCOMP

    elif current_state == STATE_LOSERCOMP:
        print("Im Loser Comp-Zustand")
        if not zustandLoserComp.losercomp():
            print("Zurück zur Worldmap")
            current_state = STATE_WORLDMAP
        else:
            print("Immer noch im Loser Comp-Bildschirm...")
    
    # Warte kurz, um den Status nicht zu oft zu prüfen