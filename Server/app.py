#!/usr/bin/env python2.7

'''
app.py
This file is used to run the development server.
'''

import os
import atexit
from argparse import ArgumentParser as AP
from configuration import APP as app
from routes.core import home

def add_arguments(parser):
    ''' used to add options to the arg parser '''
    parser.add_argument('-n', '--nodebug',
                        help='disable the debug information', action='store_true')
    parser.add_argument('-p', '--port', type=int, help='set the port',
                        default=5000)
    parser.add_argument('-c', '--cleanup',
                        help='delete database and uploads on exit', action='store_true')

def clean_exit():
    ''' function to cleanup database and uploads on exit '''
    if os.path.exists(os.path.realpath(app.config['UPLOADS_FOLDER'])):
        print '[*] Removing uploads folder...'
        os.rmdir(app.config['UPLOADS_FOLDER'])
        print '[+] Uploads folder removed'

    if os.path.exists(os.path.realpath(app.config['SQLALCHEMY_DATABASE_URI'][10:])):
        print '[*] Removing database...'
        os.remove(app.config['SQLALCHEMY_DATABASE_URI'][10:])
        print '[+] Database removed'

def main(args):
    ''' main function to run the app '''
    if args.cleanup:
        atexit.register(clean_exit)
    app.run(debug=(not args.nodebug), port=args.port)

if __name__ == '__main__':
    PARSER = AP(description='Used to run the development server')
    add_arguments(PARSER)
    ARGS = PARSER.parse_args()
    main(ARGS)
