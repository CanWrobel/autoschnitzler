import pyautogui
from PIL import Image
import pytesseract

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

# Erkannten Text
text = "37 / 488"

# Teile den Text bei " / "
parts = text.split(" / ")

# Konvertiere die Teile in ganze Zahlen
try:
    number1 = int(parts[0])
    number2 = int(parts[1])
    print(f"Erste Zahl: {number1}")
    print(f"Zweite Zahl: {number2}")
    if number 
except ValueError as e:
    print(f"Fehler beim Parsen der Zahlen: {e}")

# Ausgabe des erkannten Textes
print("Erkannter Text:")
print(text)
