'''
core.py
contains the routes for the core system
'''

from flask import render_template
from configuration import APP as app

@app.route('/')
def home():
    ''' route for the landing page '''
    return render_template('index.html')
