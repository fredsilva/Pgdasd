'''
Created on 25/04/2013

@author: 8620016
'''
# Conectando `a um banco de dados sqllite tempor´ario,
# na memoria do computador.
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer
from sqlalchemy import String, MetaData, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker


class User(object):
    def __init__(self, user_id, name, fullname):
        self.user_id = user_id
        self.name = name
        self.fullname = fullname        
    
    def __repr__(self):
        return "<User('%d','%s', '%s')>" % (self.user_id, self.name, self.fullname)

engine = create_engine('oracle://siatdesv:desenvolvimento@dbserver')

#Cria tabela
metadata = MetaData()
users = Table('fred', metadata,
               Column('user_id', Integer, primary_key=True),
               Column('name', String(50)), 
               Column('fullname', String((50))),               
)

metadata.create_all(engine)

mapper(User, users)

Session = sessionmaker(bind=engine)
session = Session()

# Para persistir o objeto ed_user, adicionamos `a sess˜ao.
# Assim que for necess´ario o comando INSERT ser´a executado.
usuario = User(15, 'samuel', 'Samuel Guimaraes Silva')
session.add(usuario)
session.commit()

