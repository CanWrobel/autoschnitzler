import pyautogui
import time

# Endlosschleife zum kontinuierlichen Ausdrucken der Mausposition
while True:
    # Aktuelle Mausposition abfragen
    x, y = pyautogui.position()
    
    # Position ausdrucken
    print(f"Mausposition: X={x}, Y={y}")
    
    # Kleiner Sleep, um die Ausgabe lesbar zu machen
    time.sleep(0.1)  # Alle 100 ms die Position aktualisieren
