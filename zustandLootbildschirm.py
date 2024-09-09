import pyautogui
import time
from PIL import ImageChops, ImageStat
import pytesseract
import request



def schau_ob_uebergewicht():
    # Tesseract-OCR Pfad (nur notwendig, wenn Tesseract nicht im PATH ist)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Definiere den Bereich für den Screenshot
    x1, y1 = 1678, 55
    x2, y2 = 1757, 89

    # Berechne Breite und Höhe
    width = x2 - x1
    height = y2 - y1

    # Erstelle Region für den Screenshot
    region = (x1, y1, width, height)

    # Mache den Screenshot
    screenshot = pyautogui.screenshot(region=region)

    # Speichern des Screenshots (optional)
    screenshot.save("screenshot.png")

    # OCR auf das Bild anwenden
    text = pytesseract.image_to_string(screenshot)

    # Teile den Text bei " / "
    parts = text.split(" / ")

    # Konvertiere die Teile in ganze Zahlen
    def alarm():
        print("⚠️ Alarm! Die erste Zahl ist 1.5-mal größer als die zweite Zahl!")



    # Text in Teile splitten
    parts = text.split("/")

    try:
        # Entferne Leerzeichen und parse in Integer
        number1 = int(parts[0].strip())
        number2 = int(parts[1].strip())

        print(f"Erste Zahl: {number1}")
        print(f"Zweite Zahl: {number2}")

        # Überprüfe die Bedingung
        if number1 >= 1* number2:
            request.alarm()
    except ValueError as e:
        print(f"Fehler beim Parsen der Zahlen: {e}")

    # Ausgabe des erkannten Textes
    print("Erkannter Text:")
    print(text)


def drück_di_done():
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

    

def loot_bildschirm():

    drück_di_loot = "loot.png"
    try:
        position_loot = pyautogui.locateOnScreen(drück_di_loot, confidence=0.90)
        print("DEBUG: Loot-Bild gefunden")
        for _ in range(5):
            pyautogui.click(position_loot)
            time.sleep(0.1)
            pyautogui.click(position_loot)        

        schau_ob_uebergewicht()
    except:
        pass
        
    

    drück_di_done()



