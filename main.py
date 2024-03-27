import keyboard

def shiftl():
    keyboard.call_later(lambda: keyboard.send("shift+l"), delay=0.25)

def l():
    keyboard.call_later(lambda: keyboard.send("l"), delay=0.25)

def colon():
    keyboard.call_later(lambda: keyboard.send("shift+;"), delay=0.25)

def semicolon():
    keyboard.call_later(lambda: keyboard.send(";"), delay=0.25)
    

keyboard.add_hotkey("shift+alt+k", shiftl)
keyboard.add_hotkey("alt+k", l)
keyboard.add_hotkey("shift+alt+'", colon)
keyboard.add_hotkey("alt+'", semicolon)

keyboard.wait()
