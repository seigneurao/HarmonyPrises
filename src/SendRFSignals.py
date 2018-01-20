'''
Created on 20 janv. 2018

@author: Lionel
'''

from bottle import route, run, template
from RFSignals import affich

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
