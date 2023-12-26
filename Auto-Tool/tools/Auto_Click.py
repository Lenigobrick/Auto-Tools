from pynput.mouse import Controller, Button
mouse = Controller()

def auto_click_function():
    mouse.click(Button.left, 1)