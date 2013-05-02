from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'fred'
    
    USER_ID  = Column(Integer, primary_key = True)
    NAME     = Column(String(50))
    FULLNAME = Column(String(50))
    
    def __init__(self, user_id, name, fullname):
        self.USER_ID  = user_id
        self.NAME     = name
        self.FULLNAME = fullname
        
class Banco():    
        
    def insere(self, pgdasd):        
        try:
            engine = create_engine('oracle://siatdesv:desenvolvimento@dbserver')            
            Session = sessionmaker(bind=engine)
            session = Session()
            session.add(pgdasd)
            session.commit()
            print('commit')        
        except:
            session.rollback()
            print('rollback')
            
if __name__ == '__main__':
    banco = Banco()
    user = User(18, "Teste", "Teste da Silva")
    banco.insere(user)