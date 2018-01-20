'''
Created on 20 janv. 2018

@author: Lionel
'''

import evdev

device = evdev.InputDevice('/dev/input/event2')

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))