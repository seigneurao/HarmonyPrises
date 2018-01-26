'''
Created on 20 janv. 2018

@author: Lionel
'''

import RFSignals
from bottle import Bottle

app = Bottle()

@app.route('/switch/<outletNumber>/<outletState>')
def switchOutlet(outletNumber, outletState):
    targetMethodName = "switch" + str.capitalize(outletState) + "Outlet" + outletNumber
    targetMethod = getattr(RFSignals, targetMethodName)
    targetMethod()
    
def get_app():
    return app
