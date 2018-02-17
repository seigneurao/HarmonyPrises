'''
Created on 20 janv. 2018

@author: Lionel
'''

import time
import sys
import RPi.GPIO as GPIO

'''
1 : short on, long off
0 : long on, short off
'''
OUTLET1_ON_SIGNAL = "1110101011101010110011001"
OUTLET1_OFF_SIGNAL = "1110101011101010110000111"
OUTLET2_ON_SIGNAL = "1110101011101010001111001"
OUTLET2_OFF_SIGNAL = "1110101011101010001100111"
OUTLET3_ON_SIGNAL = ""
OUTLET3_OFF_SIGNAL = ""

one_short_delay = 0.00009
one_long_delay = 0.00055
zero_short_delay = 0.00020
zero_long_delay = 0.00045
extended_delay = 0.00481

NUM_ATTEMPTS = 10
TRANSMIT_PIN = 2

def switchOnOutlet1():
    emitRFSignal(OUTLET1_ON_SIGNAL)
    
def switchOffOutlet1():
    emitRFSignal(OUTLET1_OFF_SIGNAL)

def switchOnOutlet2():
    emitRFSignal(OUTLET2_ON_SIGNAL)

def switchOffOutlet2():
    emitRFSignal(OUTLET2_OFF_SIGNAL)
    
def switchOnOutlet3():
    emitRFSignal(OUTLET3_ON_SIGNAL)

def switchOffOutlet3():
    emitRFSignal(OUTLET3_OFF_SIGNAL)

def emitRFSignal(signalCode):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(NUM_ATTEMPTS):
        for i in signalCode:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(one_short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(one_long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(zero_long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(zero_short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.cleanup()
