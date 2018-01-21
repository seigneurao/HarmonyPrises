'''
Created on 20 janv. 2018

@author: Lionel
'''

from bottle import Bottle
from RFSignals import affich

app = Bottle()

@app.route('/hello/<name>')
def index(name):
    return app.template('<b>Hello {{name}}</b>!', name=name)

@app.route('/testlionel/<machin>/<truc>')
def bidule(machin, truc):
    return app.template('{{bonjour}} et {{what}}', bonjour=machin, what=truc)

@app.route('/affichage')
def affichage():
    affich()
    
def get_app():
    return app
