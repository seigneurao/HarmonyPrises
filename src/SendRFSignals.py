'''
Created on 20 janv. 2018

@author: Lionel
'''

from src.RFSignals import RFSignals
from bottle import Bottle

app = Bottle()

@app.route('/switch/<outletNumber>/<outletState>')
def switchOutlet(outletNumber, outletState):
    targetMethodName = "switch" + str.capitalize(outletState) + "Outlet" + outletNumber
    targetMethod = getattr(RFSignals, targetMethodName)
    targetMethod()
    
@app.route('/health') 
def bidule(): 
    return 'Hello world!' 
    
def get_app():
    return app
