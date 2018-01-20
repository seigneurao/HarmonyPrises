'''
Created on 20 janv. 2018

@author: Lionel
'''

import evdev

device = evdev.InputDevice('/dev/input/event2')

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        keyEvent = evdev.categorize(event)
        if keyEvent.keystate == 1:
            keyCode = keyEvent.keycode
            if keyCode == "KEY_2":
                print("Salut 2")
            elif keyCode == "KEY_Q":
                print("Salut Q")