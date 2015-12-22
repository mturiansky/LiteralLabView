'''
User.py
Database model for users
'''

from hashlib import sha1
from sqlalchemy import Column, Integer, String, Boolean
from configuration import DB as db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    ''' User model for storing users in the database '''
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    password = Column(String(40))
    admin = Column(Boolean)

    def __init__(self, in_username, in_password, in_admin=0):
        ''' initialization function '''
        self.username = in_username
        self.password = sha1(in_password).hexdigest()
        self.admin = in_admin

    def is_anonymous(self):
        ''' returns false always, since a user is not anonymous '''
        return False

    def get_id(self):
        ''' returns the id as a unicode string '''
        return str(self.id).decode()

    def __repr__(self):
        ''' representation function '''
        return '<User %s>' % self.username
