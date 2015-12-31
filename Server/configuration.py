'''
configuration.py
'''

import os
import random
import string
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sslify import SSLify
from flask_mobility import Mobility
from flask_login import LoginManager, AnonymousUserMixin
from flask_triangle import Triangle

def glob_static():
    ''' a function to glob static and group files '''
    css_files = ['https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css']
    js_files = ['https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js',
                'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js',
                'https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/angular-ui-router/0.2.10/angular-ui-router.js']
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
    for dummy_root, dummy_dirs, files in os.walk(file_path):
        for i in sorted(files):
            if i.endswith('.css'):
                css_files.append('/static/' + i)
            elif i.endswith('.js'):
                js_files.append('/static/' + i)
    return (css_files, js_files)

def get_uploads():
    ''' checks if uploads dir exists, creates it if not '''
    uploads_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')
    if not os.path.isdir(uploads_path):
        print '[-] uploads directory not found, creating...'
        os.mkdir(uploads_path)
        print '[+] uploads directory created'
    return uploads_path

def gen_secret_key():
    ''' generates a 64 character secret key '''
    key = ''
    choices = string.ascii_uppercase + string.ascii_lowercase + string.digits
    for _ in range(64):
        key += random.SystemRandom().choice(choices)
    return key

# initialize app
APP = Flask(__name__)
APP.config['TITLE'] = 'LiteralLabView'

# grab css and js files
(APP.config['CSS'], APP.config['JS']) = glob_static()

# generate secret key
APP.secret_key = gen_secret_key()

# uploads folder
APP.config['UPLOADS_FOLDER'] = get_uploads()

# SQLAlchemy setup
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/llw.db'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)

if not os.path.exists(os.path.realpath('/tmp/llw.db')):
    print '[-] Database not found, creating...'
    from models.User import User
    from models.DataSet import DataSet
    DB.create_all()
    DB.session.add(User('admin', 'admin', in_admin=1))
    DB.session.add(DataSet('test-project'))
    DB.session.commit()
    print '[+] Database created'

# SSLify setup
SSL = SSLify(APP)

# Mobility setup
MOBILE = Mobility(APP)

# Triangle setup
TRI = Triangle(APP)

# Login Manager setup
LM = LoginManager()
LM.login_view = 'login'
LM.session_protection = 'strong'
AnonymousUserMixin.username = u'Anonymous'
LM.anonymous_user = AnonymousUserMixin
LM.init_app(APP)
