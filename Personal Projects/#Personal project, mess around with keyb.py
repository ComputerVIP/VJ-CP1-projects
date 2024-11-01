#Personal project, mess around with keyboard module
import time
import keyboard


def hello():
    time.sleep(5)
    keyboard.send("windows + s")
    time.sleep(0.5)
    keyboard.write("Microsoft Edge")
    time.sleep(0.5)
    keyboard.send("enter")
    time.sleep(1)
    keyboard.send("ctrl + t")
    time.sleep(1)
    keyboard.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(0.5)
    keyboard.send("enter")
    time.sleep(10)
    return

hello()