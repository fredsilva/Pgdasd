'''
Created on 31/05/2013

@author: 8620016
'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import mapper, Session, relationship


class Group(object):
    def __init__(self, name):
        self.name = name

class User(object):
    def __init__(self, name, password, group):
        self.name = name
        self.password = password
        self.group = group

    group = relationship(Group)

def connect(url):
    engine = create_engine(url, echo=True)
    metadata = MetaData(engine, reflect=True)

    # Do this for each table
    mapper(User, metadata.tables['group'])
    mapper(Group, metadata.tables['user'])


    session = Session(bind=engine)
    return session


session = connect('oracle://siatdesv:desenvolvimento@dbserver')
finance_group = Group('finance')
session.add(finance_group)