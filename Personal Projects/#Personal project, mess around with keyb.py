#Personal project, mess around with keyboard module
import time
import keyboard
def hello():
    time.sleep(10)
    print("Going")
    keyboard.send('ctrl+t')
    keyboard.send('menu')
    time.sleep(10)
    return
hello()