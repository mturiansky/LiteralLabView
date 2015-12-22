'''
User.py
Database model for users
'''

from sqlalchemy import Column, Integer, String
from configuration import DB as db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    ''' User model for storing users in the database '''
    id = Column(Integer, primary_key=True)

    def __init__(self):
        ''' initialization function '''
        pass
