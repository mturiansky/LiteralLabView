'''
DataSet.py
Database model for screenshots and webcam images
'''

from datetime import datetime
from sqlalchemy import Column, Integer, String
from configuration import DB as db
from configuration import gen_secret_key

class DataSet(db.Model):
    ''' DataSet model which wraps screenshots and webcam images '''
    id = Column(Integer, primary_key=True)
    tag = Column(String(64), unique=True)
    date = Column(String(80))
    project_name = Column(String(80))

    def __init__(self, proj_name):
        ''' initialization function '''
        self.tag = gen_secret_key()
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.project_name = proj_name

    def __repr__(self):
        ''' representation function '''
        return '<DataSet %s-%s>' % (self.project_name, self.tag)

def add_data(pname):
    ''' wrapper for the dataset model to create a new one '''
    temp_data = DataSet(pname)
    db.session.add(temp_data)
    db.session.commit()
    return temp_data.tag
