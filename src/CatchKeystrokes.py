'''
Created on 20 janv. 2018

@author: Lionel
'''

import evdev
from RFSignals import affich
from bottle import route, run, template

device = evdev.InputDevice('/dev/input/event2')

# Key state
# Released
KEY_UP = 0
# Pressed
KEY_DOWN = 1
# Held
KEY_HOLD = 2

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        keyEvent = evdev.categorize(event)
        if keyEvent.keystate == KEY_DOWN:
            keyCode = keyEvent.keycode
            if keyCode == "KEY_2":
                print("Salut 2")
            elif keyCode == "KEY_Q":
                print("Salut Q")
            elif keyCode == "KEY_3":
                affich()

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/testlionel/<machin>/<truc>')
def bidule(machin, truc):
    return template('{{bonjour}} et {{what}}', bonjour=machin, what=truc)

@route('/affichage')
def affichage():
    affich()

run(host='localhost', port=8080)