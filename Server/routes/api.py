'''
api.py
routes for the api backend
'''

from flask import jsonify, send_from_directory, abort
from flask_login import login_required
from configuration import APP as app
from models.DataSet import last_data, get_by_tag

@app.route('/api/data/upload', methods=['POST'])
def upload():
    ''' route for uploading images '''
    return

@app.route('/api/data/recent')
@login_required
def get_recent():
    ''' route to retrieve most recent data '''
    recent_data = last_data()
    return jsonify(screenshotImage=('/api/img/s/' + recent_data.tag), cameraImage=('/api/img/c/' + recent_data.tag))

@app.route('/api/img/<sorc>/<tag>')
@login_required
def img_route(sorc, tag):
    ''' route to send the correct image back '''
    if sorc != 's' and sorc != 'c':
        return abort(404)
    if not get_by_tag(tag):
        return abort(404)
    return send_from_directory(app.config['UPLOADS_FOLDER'], sorc + tag + '.jpg')
