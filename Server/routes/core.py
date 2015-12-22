'''
core.py
contains the routes for the core system
'''

from configuration import APP as app

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'
