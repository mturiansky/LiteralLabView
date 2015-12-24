'''
core.py
contains the routes for the core system
'''

from flask import render_template, redirect, url_for
from configuration import APP as app
from flask_login import login_required, current_user

@app.route('/')
@login_required
def home():
    ''' route for the landing page '''
    return render_template('index.html')

@app.route('/login')
def login():
    ''' route for logging in '''
    if current_user.username != 'Anonymous':
        return redirect(url_for('home'))
    return render_template('login.html')
