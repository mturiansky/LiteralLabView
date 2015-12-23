'''
core.py
contains the routes for the core system
'''

from flask import render_template
from configuration import APP as app
from flask_login import login_required

@app.route('/')
@login_required
def home():
    ''' route for the landing page '''
    return render_template('index.html')

@app.route('/login')
def login():
    ''' route for logging in '''
    return render_template('login.html')
