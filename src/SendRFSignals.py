'''
Created on 20 janv. 2018

@author: Lionel
'''

import RFSignals
from bottle import Bottle

app = Bottle()

@app.route('/outlet1/on')
def switchOnOutlet1():
    RFSignals.switchOnOutlet1()

@app.route('/outlet1/off')
def switchOffOutlet1():
    RFSignals.switchOffOutlet1()

@app.route('/outlet2/on')
def switchOnOutlet2():
    RFSignals.switchOnOutlet2()

@app.route('/outlet2/off')
def switchOffOutlet2():
    RFSignals.switchOffOutlet2()
    
def get_app():
    return app
