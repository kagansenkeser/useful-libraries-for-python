from pynput.mouse import Button, Controller
import time
mouse = Controller()
mouse.position = (1920, 1050)
time.sleep(1)
mouse.click(Button.left, 1)
time.sleep(1)
mouse.position = (1856, 54)
mouse.click(Button.left, 1)
