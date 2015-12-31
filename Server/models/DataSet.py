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
    experiment_name = Column(String(80))

    def __init__(self, proj_name, exp_name):
        ''' initialization function '''
        self.tag = gen_secret_key()
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.project_name = proj_name
        self.experiment_name = exp_name

    def __repr__(self):
        ''' representation function '''
        return '<DataSet %s-%s>' % (self.project_name, self.tag)

def add_data(pname, ename):
    ''' wrapper for the dataset model to create a new one '''
    temp_data = DataSet(pname, ename)
    db.session.add(temp_data)
    db.session.commit()
    return temp_data

def last_data():
    ''' finds the most recent data set '''
    count = DataSet.query.count()
    return DataSet.query.get(count)

def find_data(to_find):
    ''' basic string based search '''
    results = []
    for data in DataSet.query.all():
        if to_find in data.tag or to_find in data.date or to_find in data.project_name or to_find in data.experiment_name:
            if data not in results:
                results.append(data)
    return results

def get_by_tag(tag_to_find):
    ''' returns the data item with the correct tag '''
    return DataSet.query.filter_by(tag=tag_to_find).first() is not None
