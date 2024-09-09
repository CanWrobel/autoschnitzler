import pyautogui
import pytesseract

from pynput.mouse import Button, Controller
import time

# Erstelle einen Mauscontroller
mouse = Controller()

# Bewege die Maus an eine Position (x=500, y=500)
mouse.position = (1500, 1000)

# Warte kurz
time.sleep(1)

# Führe einen Linksklick aus
mouse.click(Button.left, 1)

# Optional: Führe einen Doppelklick aus
mouse.click(Button.left, 2)

# Optional: Führe einen Rechtsklick aus
mouse.click(Button.right, 1)
