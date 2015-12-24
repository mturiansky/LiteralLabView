'''
auth.py
routes for /api/auth
'''

from flask import request, redirect, url_for
from flask_login import login_user, logout_user
from configuration import APP as app
from configuration import LM as lm
from models.User import verify_user, get_user

@app.route('/api/auth', methods=['POST'])
def auth_post():
    ''' route for logging in a user '''
    user = verify_user(request.json['username'], request.json['password'])
    if user:
        login_user(user)
        return 'OK'
    else:
        return 'ERROR'

@app.route('/api/auth', methods=['DELETE'])
def logout():
    ''' logs out a user '''
    logout_user()
    return 'OK'

@lm.user_loader
def load_user(id):
    ''' login manager needs this to load the user '''
    return get_user(id)
