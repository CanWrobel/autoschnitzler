import pyautogui
import time
from PIL import ImageChops, ImageStat




def loot_bildschirm():

    drück_di_loot = "loot.png"
    try:
        position_loot = pyautogui.locateOnScreen(drück_di_loot, confidence=0.90)
        print("DEBUG: Loot-Bild gefunden")
        for _ in range(5):
            pyautogui.click(position_loot)
            time.sleep(0.1)
            pyautogui.click(position_loot)        
    except:
        pass
        

    done_looting = "done.png"
    
    # Sucht das "Done"-Bild und klickt darauf
    try:        
        done_position = pyautogui.locateOnScreen(done_looting, confidence=0.90)

        for _ in range(5):
            pyautogui.click(done_position)
            time.sleep(0.1)
        print("DEBUG: Looten abgeschlossen (Done-Bild gefunden und geklickt).")
    except:
        pass
    # Sobald das "Done"-Bild gefunden und geklickt wurde, setze die Variable und beende die Suche
    global attack_start_no_need_to_move
    attack_start_no_need_to_move = False  # Diese Variable wird hier korrekt auf False gesetzt

    print("DEBUG: Suche nach Loot-Bild beendet.")
    

