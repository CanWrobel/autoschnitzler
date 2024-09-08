import time
import pyautogui
from pynput import keyboard
import threading
from pynput import keyboard
from pynput.keyboard import Controller, Key


def detect_we_are_in_fight():
        try:
            pyautogui.locateOnScreen("in_fight.png", confidence=0.85)
            return True
        except:
            return False


def charge():
        kb_controller = Controller()

        # F2 drücken und loslassen
        kb_controller.press(Key.f2)  # Verwende Key.f2 für F2
        time.sleep(0.1)
        kb_controller.release(Key.f2)
        print("F1 gedrückt")

        # F1 drücken und loslassen
        kb_controller.press(Key.f1)  # Verwende Key.f1 für F1
        time.sleep(0.1)
        kb_controller.release(Key.f1)
        print("F3 gedrückt")


def press_tab():
    kb_controller = Controller()
    kb_controller.press(Key.tab)  # Verwende Key.f1 für F1
    time.sleep(0.5)
    kb_controller.release(Key.tab)

def check_donelinski():
    try:
        position = pyautogui.locateOnScreen("done_with_battle.png", confidence=0.85)
        for _ in range(5):
            pyautogui.click(position)
            time.sleep(0.1)
            pyautogui.click(position)
        print("DEBUG: Done with battle gefunden und geklickt")
    except:
        return False

def in_fight():
    weAreInFight = detect_we_are_in_fight()
    if weAreInFight:
#        charge()
#        press_tab()
        time.sleep(1)
        check_donelinski()
    

    return weAreInFight



 