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

OUTLET1_ON_KEY = "KEY_1"
OUTLET1_OFF_KEY = "KEY_2"
OUTLET2_ON_KEY = "KEY_3"
OUTLET2_OFF_KEY = "KEY_4"

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        keyEvent = evdev.categorize(event)
        if keyEvent.keystate == KEY_DOWN:
            keyCode = keyEvent.keycode
            if keyCode == OUTLET1_ON_KEY:
                RFSignals.switchOnOutlet1()
            elif keyCode == OUTLET1_OFF_KEY:
                RFSignals.switchOffOutlet1()
            elif keyCode == OUTLET2_ON_KEY:
                RFSignals.switchOnOutlet2()
            elif keyCode == OUTLET2_OFF_KEY:
                RFSignals.switchOffOutlet2()
