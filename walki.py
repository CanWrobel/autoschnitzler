from pynput import keyboard
from pynput.keyboard import Controller
import threading
import time

# Create a keyboard controller to simulate key presses
kb_controller = Controller()

# Variable to track if 'w' is being held down
is_w_held = False

# Function to hold down 'w' every 1 ms
def hold_w():
    global is_w_held
    while is_w_held:
        kb_controller.press('w')  # Press and hold 'w'
        time.sleep(0.001)  # Sleep for 1 ms
        kb_controller.press('f')  # Press and hold 'w'
        time.sleep(0.001)  # Sleep for 1 ms
        kb_controller.release('w')  # Release 'w' after each cycle
        time.sleep(0.001)  # Sleep for 1 ms
        kb_controller.release('f')  # Release 'w' after each cycle



def spam_f():
    global is_f_held
    while is_f_held:
        time.sleep(0.001)  # Sleep for 1 ms

# Function to handle key press events
def on_press(key):
    global is_w_held
    try:
        if key.char == '9':  # Check if '9' is pressed
            if not is_w_held:
                is_w_held = True
                print("Started holding 'w'.")
                # Start a separate thread to press 'w' every 1 ms
                threading.Thread(target=hold_w, daemon=True).start()
            else:
                is_w_held = False
                print("Stopped holding 'w'.")
    except AttributeError:
        pass  # Ignore special key presses

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when 'esc' is pressed
        return False

# Start the listener
print("Press '9' to toggle walking (holding 'w'). Press 'esc' to exit.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
