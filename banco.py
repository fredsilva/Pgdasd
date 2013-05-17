# -*_ encoding; ytf-8 -*-
'''
Created on 16/04/2013

@author: Frederico da Silva Santos
@email: fredsilva.sistemas@gmail.com
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Banco():
    
    def insere(self, pgdasd):
        engine = create_engine('oracle://siatdesv:desenvolvimento@dbserver')            
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(pgdasd)
        session.commit()