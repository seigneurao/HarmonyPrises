'''
Created on 20 janv. 2018

@author: Lionel
'''

import evdev
import RFSignals

device = evdev.InputDevice('/dev/input/event2')

# Key state
# Released
KEY_UP = 0
# Pressed
KEY_DOWN = 1
# Held
KEY_HOLD = 2

keyMapping = {}
keyMapping["KEY_1"] = "switchOnOutlet1"
keyMapping["KEY_2"] = "switchOffOutlet1"
keyMapping["KEY_3"] = "switchOnOutlet2"
keyMapping["KEY_4"] = "switchOffOutlet2"
keyMapping["KEY_5"] = "switchOnOutlet3"
keyMapping["KEY_6"] = "switchOffOutlet3"


for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        keyEvent = evdev.categorize(event)
        if keyEvent.keystate == KEY_DOWN:
            keyCode = keyEvent.keycode
            targetMethod = getattr(RFSignals, keyMapping[keyCode])
            targetMethod()
