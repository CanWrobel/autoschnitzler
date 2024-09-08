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

def klick_loser_comp_weg():
    for _ in range(5):
        time.sleep(0.1)
        pyautogui.click(1500,1030)

def losercomp():
    if detect_loser_comp():
        klick_loser_comp_weg()
        return False