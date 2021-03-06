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

    def is_authenticated(self):
        ''' returns true if valid login credentials '''
        return True

    def is_active(self):
        ''' returns true if an account has been activated '''
        return True

    def get_id(self):
        ''' returns the id as a unicode string '''
        return str(self.id).decode('unicode-escape')

    def __repr__(self):
        ''' representation function '''
        return '<User %s>' % self.username

def add_user(uname, passwd):
    ''' function to add user to database '''
    temp_user = User(uname, passwd)
    db.session.add(temp_user)
    db.session.commit()
    return temp_user

def verify_user(uname, passwd):
    ''' verifies the user '''
    user = User.query.filter_by(username=uname).first()
    temp_pass = sha1(passwd).hexdigest()
    return temp_pass == user.password

def get_user(id):
    ''' function to return the user by id '''
    return User.query.get(id)
