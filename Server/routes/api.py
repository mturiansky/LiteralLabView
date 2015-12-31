'''
api.py
routes for the api backend
'''

import os
from flask import jsonify, send_from_directory, abort, request
from flask_login import login_required
from configuration import APP as app
from models.DataSet import last_data, get_by_tag, add_data

@app.route('/api/data/upload', methods=['POST'])
def upload():
    ''' route for uploading images '''
    print '[+] request received'
    if 'secret_key' in request.json and request.json['secret_key'] == app.config['COMMUNICATION_KEY']:
        print '[+] secret_key verified'
        if 'project_name' in request.json and 'experiment_name' in request.json and 'screenshot' in request.files and 'camera' in request.files:
            print '[+] filds verified'
            temp_data = add_data(request.json['project_name'], request.json['experiment_name'])
            request.files['screenshot'].save(os.path.join(app.config['UPLOADS_FOLDER'], 's' + temp_data.tag + '.png'))
            request.files['camera'].save(os.path.join(app.config['UPLOADS_FOLDER'], 'c' + temp_data.tag + '.png'))
            print '[+] files saved'
            return 'OK'
    return 'ERROR'

@app.route('/api/data/recent')
@login_required
def get_recent():
    ''' route to retrieve most recent data '''
    recent_data = last_data()
    return jsonify(projectName=recent_data.project_name, experimentName=recent_data.experiment_name, screenshotImage=('/api/img/s/' + recent_data.tag), cameraImage=('/api/img/c/' + recent_data.tag))

@app.route('/api/img/<sorc>/<tag>')
@login_required
def img_route(sorc, tag):
    ''' route to send the correct image back '''
    if sorc != 's' and sorc != 'c':
        return abort(404)
    if not get_by_tag(tag):
        return abort(404)
    return send_from_directory(app.config['UPLOADS_FOLDER'], sorc + tag + '.png')
