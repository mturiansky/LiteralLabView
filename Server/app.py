#!/usr/bin/env python2.7

'''
app.py
This file is used to run the development server.
'''

from argparse import ArgumentParser as AP
from configuration import APP as app
from routes.core import *

def add_arguments(parser):
    ''' used to add options to the arg parser '''
    parser.add_argument('-n', '--nodebug',
                        help='disable the debug information', action='store_true')
    parser.add_argument('-p', '--port', type=int, help='set the port',
                        default=5000)

def main(args):
    ''' main function to run the app '''
    app.run(debug=(not args.nodebug), port=args.port)

if __name__ == '__main__':
    PARSER = AP(description='Used to run the development server')
    add_arguments(PARSER)
    ARGS = PARSER.parse_args()
    main(ARGS)
