from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.mouse import Button, Controller
import time
x=1
while x<5:
    mouse = Controller()
    mouse.position = (1500, 500)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(1)

    keyboard.press("h")
    keyboard.release("h")
    keyboard.press("i")
    keyboard.release("i")
    time.sleep(2)

    mouse.position = (337, 385)
    mouse.click(Button.left, 1)
    time.sleep(1)
    x=x+1


