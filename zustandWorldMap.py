import pyautogui
import math
import time
from pynput import keyboard
import threading
from pynput import keyboard
from pynput.keyboard import Controller, Key
from PIL import ImageChops, ImageStat


attack_start_no_need_to_move = False
# Bilddatei, die gesucht werden soll

# Bildschirmgröße ermitteln, um die Mitte zu berechnen
screen_width, screen_height = pyautogui.size()
screen_center = (screen_width // 2, screen_height // 2)

# Variable, um den Zustand des Programms zu verfolgen
running = True

# Funktion zur Berechnung der Entfernung zur Bildschirmmitte
def distance_to_center(point):
    x, y = point
    return math.sqrt((x - screen_center[0])**2 + (y - screen_center[1])**2)

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

attack_found = False




# Funktion, um das obere rechte 10% des Bildschirms zu berechnen
screen_width, screen_height = pyautogui.size()

# Größe des Mittelteils (z.B. 200x200 px)
middle_width = 200
middle_height = 200

# Berechne die Koordinaten für die Mitte des Bildschirms
x = (screen_width // 2) - (middle_width // 2)
y = (screen_height // 2) - (middle_height // 2)

# Erstelle das neue Region-Quadrat in der Bildschirmmitte
region = (x, y, middle_width, middle_height)

# Funktion, um einen Screenshot von einem bestimmten Bereich zu machen
def take_screenshot(region):
    return pyautogui.screenshot(region=region)

# Funktion, um den Unterschied zwischen zwei Bildern zu berechnen
def calculate_image_difference(img1, img2):
    # Berechnet den Unterschied zwischen den Bildern
    diff = ImageChops.difference(img1, img2)
    
    # Summiere die Pixelunterschiede und normalisiere sie
    stat = ImageStat.Stat(diff)
    diff_sum = sum(stat.sum)
    
    # Die maximale Differenz (RGB 255 * 3 pro Pixel)
    max_diff = 255 * 3 * img1.size[0] * img1.size[1]
    
    # Prozentuale Differenz
    diff_percentage = diff_sum / max_diff
    return diff_percentage

# Bereich für die obere rechte 10% des Bildschirms

def am_i_moving():
# Mache einen Screenshot des Bereichs
    first_screenshot = take_screenshot(region)

    # Warte 2 Sekunden
    time.sleep(1)

    # Mache erneut einen Screenshot
    second_screenshot = take_screenshot(region)

    # Berechne den Unterschied zwischen den beiden Screenshots
    difference = calculate_image_difference(first_screenshot, second_screenshot)

    # Wenn die Differenz größer als 5% ist (0.05), betrachte das Bild als geändert
    if difference > 0.03:
        print(f"Es hat sich etwas geändert! Unterschied: {difference * 100:.2f}%")
        return True

    else:
        print(f"Keine signifikante Änderung erkannt. Unterschied: {difference * 100:.2f}%")
        return False

attack = "attack.png"
def try_click_attack():
    try:
        position = pyautogui.locateOnScreen(attack, confidence=0.90)
        for _ in range(5):
            pyautogui.click(position)
            time.sleep(0.1)
            pyautogui.click(position)


        print("Attack gefunden und geklickt")
        return True
    except:
        return False
        pass

def check_am_I_still_on_worldmap():
    try:
        position = pyautogui.locateOnScreen("main_menu.png", confidence=0.90)
        print("Bin noch auf der Worldmap")
        return True
    except:
        print("Bin nicht mehr auf der Worldmap")
        return False

def world_map():
    if am_i_moving() == True:
        try_click_attack()
    else:
        find_and_click_nearest_occurrence("looters.png")
        try_click_attack()
    still_map = check_am_I_still_on_worldmap()
    time.sleep(0.5)
    try_click_attack()
    return still_map
