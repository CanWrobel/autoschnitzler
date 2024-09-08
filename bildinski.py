import pyautogui
import math
import time
from pynput import keyboard
import threading
from pynput import keyboard
from pynput.keyboard import Controller, Key

attack_start_no_need_to_move = False
# Bilddatei, die gesucht werden soll

attack_found = False
# Bildschirmgröße ermitteln, um die Mitte zu berechnen
screen_width, screen_height = pyautogui.size()
screen_center = (screen_width // 2, screen_height // 2)

# Variable, um den Zustand des Programms zu verfolgen
running = True

# Funktion zur Berechnung der Entfernung zur Bildschirmmitte
def distance_to_center(point):
    x, y = point
    return math.sqrt((x - screen_center[0])**2 + (y - screen_center[1])**2)


def in_position_bringen():
    # Tastatur-Controller initialisieren
    kb_controller = Controller()

    # F2 drücken und loslassen
    time.sleep(3)
    kb_controller.press(Key.f1)  # Verwende Key.f2 für F2
    time.sleep(1)
    kb_controller.release(Key.f1)
    print("F2 gedrückt")

    # F1 drücken und loslassen
    time.sleep(1)
    kb_controller.press(Key.f3)  # Verwende Key.f1 für F1
    time.sleep(1)
    kb_controller.release(Key.f3)
    print("F1 gedrückt")

attack = "attack.png"
def try_click_attack():
    try:
        position = pyautogui.locateOnScreen(attack, confidence=0.90)
        pyautogui.click(position)
        time.sleep(0.5)
        pyautogui.click(position)


        print("Attack gefunden und geklickt")
        kb_controller = Controller()

        # F2 drücken und loslassen
        time.sleep(3)
        kb_controller.press(Key.f1)  # Verwende Key.f2 für F2
        time.sleep(1)
        kb_controller.release(Key.f1)
        print("F1 gedrückt")

        # F1 drücken und loslassen
        time.sleep(1)
        kb_controller.press(Key.f3)  # Verwende Key.f1 für F1
        time.sleep(1)
        kb_controller.release(Key.f3)
        print("F1 gedrückt")

        kb_controller.press(Key.tab)  # Verwende Key.f1 für F1


        adolf = True
        while adolf:
            #print("DEBUG: Sucke das Loot-Bild")
            drück_di_loot = "loot.png"
            try:
                position_loot = pyautogui.locateOnScreen(drück_di_loot, confidence=0.90)
                print("DEBUG: Loot-Bild gefunden")
                for _ in range(5):
                    pyautogui.click(position_loot)
                    time.sleep(0.1)
                    pyautogui.click(position_loot)
                adolf = False
                loot_bildschirm()
                return True
                
            except:
                pass
        

    except:
        pass


# Zähle, wie oft das Bild auf dem Bildschirm gefunden wird und klicke auf das nächste zur Mitte (5 Pixel höher)
def find_and_click_nearest_occurrence(image):
    try:
        occurrences = list(pyautogui.locateAllOnScreen(image, confidence=0.90))
        if not occurrences:
            print(f"Keine Vorkommen von '{image}' gefunden.")
            

            return

        # Berechne die Mittelpunkte aller gefundenen Bilder
        centers = [pyautogui.center(occurrence) for occurrence in occurrences]

        # Finde das Zentrum, das der Bildschirmmitte am nächsten ist
        nearest_center = min(centers, key=distance_to_center)

        # Klicke auf die Position, aber 5 Pixel höher
        click_position = (nearest_center.x, nearest_center.y - 5)
        pyautogui.click(click_position)
        print(f"Bild '{image}' gefunden und auf die Position {click_position} geklickt (5 Pixel höher).")
    except Exception as e:
        print(f"Fehler beim Suchen oder Klicken auf das Bild: {e}")

# Endlosschleife für die Bildsuche mit 30-Sekunden-Intervall
def image_search_loop_and_click_it(bild):
        for _ in range(2):
            find_and_click_nearest_occurrence(bild)
        sekunden_warten= 10
        for _ in range(sekunden_warten):
            raus_aus_schleifinski = try_click_attack()
            time.sleep(1)
            if raus_aus_schleifinski:
                break

# Funktion zur Behandlung von Tastendruck-Ereignissen
def on_press(key):
    pass  # Keine spezifische Aktion bei Tastendruck benötigt

# Funktion zur Behandlung von Tastenfreigabe-Ereignissen
def on_release(key):
    pass

# Startet den Listener in einem separaten Thread
def start_keyboard_listener():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()  # Startet den Listener in einem separaten Thread

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
    done_position = pyautogui.locateOnScreen(done_looting, confidence=0.90)

    for _ in range(5):
        pyautogui.click(done_position)
        time.sleep(0.1)
    print("DEBUG: Looten abgeschlossen (Done-Bild gefunden und geklickt).")

    # Sobald das "Done"-Bild gefunden und geklickt wurde, setze die Variable und beende die Suche
    global attack_start_no_need_to_move
    attack_start_no_need_to_move = False  # Diese Variable wird hier korrekt auf False gesetzt

    print("DEBUG: Suche nach Loot-Bild beendet.")
    

    adolf = True
    # Überprüfen, ob der "Loser Comp"-Bildschirm auftaucht oder ins Hauptmenü wechselt
    
    time.sleep(4)
    while adolf:  # Verwende eine unendliche Schleife, da die Bedingungen innerhalb der Schleife entscheiden, wann sie beendet wird
        loser_comp = "fucking_loser_comp.png"
        main_menu = "main_menu.png"
        
        try:
            # Prüfe auf den Loser-Comp-Bildschirm
            if pyautogui.locateOnScreen(loser_comp, confidence=0.90):
                print("DEBUG: Loser Comp gefunden")
                losercomp()
                break  # Schleife verlassen, da "Loser Comp" gefunden wurde
        except:
            pass
        
        try:
            # Prüfe auf das Hauptmenü
            if pyautogui.locateOnScreen(main_menu, confidence=0.90):
                adolf  = False
                print("DEBUG: Hauptmenü gefunden")
                attack_start_no_need_to_move = False  # Hier setze die Variable auf False, um die    zu stoppen
                break  # Beende die Schleife, sobald das Hauptmenü gefunden wurde
        except:
            pass




def losercomp():
    for _ in range(5):

        time.sleep(1)
        pyautogui.click(1500,1000)





start_loot = False

attack_angefangen = False

looters = './looters.png'
loot_abgeschlossen = False
# Programm starten
if __name__ == "__main__":
    print("Drücke ESC, um das Programm zu beenden.")

    # Startet den Tastatur-Listener
    start_keyboard_listener()



    while True:
        #große schleife
        while not attack_start_no_need_to_move:
            image_search_loop_and_click_it(looters)


        

    # Startet die Bildsuche
