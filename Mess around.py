import keyboard
while True:
    try:
        if keyboard.is_pressed('caps lock'):
            keyboard.press('caps lock')
            pass
    except:
        pass