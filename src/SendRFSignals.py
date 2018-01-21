'''
Created on 20 janv. 2018

@author: Lionel
'''

from bottle import Bottle, run, template
from RFSignals import affich

app = Bottle()

@app.route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@app.route('/testlionel/<machin>/<truc>')
def bidule(machin, truc):
    return template('{{bonjour}} et {{what}}', bonjour=machin, what=truc)

@app.route('/affichage')
def affichage():
    affich()
    
def get_app():
    return app

run(app, host='localhost', port=8080)
