import keyboard
import time
time.sleep(5)
tim = 0
while tim < 100:
    time.sleep(0.1)
    keyboard.press('k')
    tim += 0.1