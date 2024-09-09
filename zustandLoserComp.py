import pyautogui
import time

def detect_loser_comp():
    loser_comp = "fucking_loser_comp.png"
    
    try:
        # Prüfe auf den Loser-Comp-Bildschirm
        if pyautogui.locateOnScreen(loser_comp, confidence=0.95):
            print("DEBUG: Loser Comp gefunden")
             # Schleife verlassen, da "Loser Comp" gefunden wurde
            return True
    except:
        pass
from pynput.mouse import Button, Controller
import time
def klick_loser_comp_weg():
    


    # Erstelle einen Mauscontroller
    mouse = Controller()

    # Bewege die Maus an eine Position (x=500, y=500)
    mouse.position = (1500, 1000)

    for _ in range(3):
        # Warte kurz
        time.sleep(0.5)

        # Führe einen Linksklick aus
        mouse.click(Button.left, 1)




def losercomp():
    if detect_loser_comp():
        klick_loser_comp_weg()
        return False