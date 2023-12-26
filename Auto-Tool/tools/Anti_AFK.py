from pynput.keyboard import Listener, KeyCode, Key, Controller
import random
import time
keyboard = Controller()

def anti_afk_function():
    delay_before_action = random.uniform(20, 30)
    time.sleep(delay_before_action)
    if random.choice([True, False]):
        keyboard.press('z')
        time.sleep(0.5)
        keyboard.release('z')
        time.sleep(0.2)
        keyboard.press('s')
        time.sleep(0.5)
        keyboard.release('s')
    else:
        keyboard.press('q')
        time.sleep(0.5)
        keyboard.release('q')
        time.sleep(0.2)
        keyboard.press('d')
        time.sleep(0.5)
        keyboard.release('d')

    delay_after_action = random.uniform(2, 5)
    time.sleep(delay_after_action)

    keyboard.press(Key.space)
    time.sleep(0.2)
    keyboard.release(Key.space)