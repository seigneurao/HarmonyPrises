'''
Created on 20 janv. 2018

@author: Lionel
'''

OUTLET1_ON_SIGNAL = "blah"
OUTLET1_OFF_SIGNAL = "bleh"
OUTLET2_ON_SIGNAL = "blih"
OUTLET2_OFF_SIGNAL = "bloh"

def switchOnOutlet1():
    emitRFSignal(OUTLET1_ON_SIGNAL)
    
def switchOffOutlet1():
    emitRFSignal(OUTLET1_OFF_SIGNAL)

def switchOnOutlet2():
    emitRFSignal(OUTLET2_ON_SIGNAL)

def switchOffOutlet2():
    emitRFSignal(OUTLET2_OFF_SIGNAL)

def emitRFSignal(signalCode):
    print(signalCode)
