'''
api.py
routes for the api backend
'''

from configuration import APP as app
from configuration import DB as db

@app.route('/api/data/recent')
def get_recent():
    ''' route to retrieve most recent data '''
    return
