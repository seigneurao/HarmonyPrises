'''
Created on 21 janv. 2018

@author: Lionel
'''

import os, sys

# Make sure the harmonyprises module is in the PYTHON_PATH and importable
HARMONYPRISES_PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, HARMONYPRISES_PARENT_DIR) 

# Create the wsgi application
from src.SendRFSignals import get_app
application = get_app()