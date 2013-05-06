# -*- encoding: utf-8 -*-
'''
Created on 10/04/2013

@author: Frederico da Silva Santos
@email: fredsilva.sistemas@gmail.com
 
'''
import platform
import os 
import shutil
from pgdasd import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class File():
    
    def __init__(self):
        pass
        #self.pgdasdControl = pgdasd.PgdasdController()
        
    
    def hasNewFile(self, url):
        '''
        Verifica se existem arquivos no diretório, se houver realiza a importação
        '''        
        for (path, dirs, files) in os.walk(url):
            for file in files:
                arquivo = File()                
                arquivo.importFile(url, file)
        
    def deleteImportedFile(self, url):
        '''
        Exclui todos os arquivos do diretório após a importação
        '''
        for (path, dirs, files) in os.walk(url):
            for file in files:                
                os.remove(os.path.join(path, file))

    
    def importFile(self, url, file):   
        try:           
            url = url+"/"+file            
            fileImport = open(url, 'r')
            lines = fileImport.readlines()
            fileImport.close()                                                                                                               
            i = 0                    
            while i < len(lines):                                                                
                line = lines[i].replace("\n","").replace(",",".").split("|") # ler a linha do arquivo, retira os \n e troca , por .                
                if line[0] == '00000':                                    
                    id_04000 = 0 
                    id_02000 = 0
                    id_03110 = 0
                    id_03111 = 0
                    id_03112 = 0
                    id_03120 = 0
                    id_03121 = 0
                    id_03122 = 0
                    id_03130 = 0
                    id_03131 = 0
                    id_03132 = 0
                    pgdasd = Pgdasd()
                    pgdasd = pgdasd.setPgdasd_00000(line)      
                    banco = Banco()
                    banco.insere(pgdasd)                                                         
                if line[0] == '01000':
                    pgdasd.Pgdasd_01000 = pgdasd.Pgdasd_01000.setPgdasd_01000(line, pgdasd)
                    #pgdasd_01000 = Pgdasd_01000()
                    #pgdasd_01000.setPgdasd_01000(line, pgdasd)
                    banco = Banco()
                    banco.insere(pgdasd.Pgdasd_01000)                    
                if line[0] == '01500':#Se repete
                    #pgdasd.Pgdasd_01500 = pgdasd.Pgdasd_01500.setPgdasd_01500(line)
                    pgdasd_01500 = Pgdasd_01500()
                    pgdasd_01500.setPgdasd_01500(line, pgdasd)
                    banco = Banco()
                    banco.insere(pgdasd_01500)                                                                        
                if line[0] == '01501':#Se repete
                    #pgdasd.Pgdasd_01501 = pgdasd.Pgdasd_01501.setPgdasd_01501(line)
                    pgdasd_01501 = Pgdasd_01501()
                    pgdasd_01501.setPgdasd_01501(line, pgdasd)
                    banco = Banco()
                    banco.insere(pgdasd_01501)
                if line[0] == '01502':#Se repete
                    #pgdasd.Pgdasd_01502 = pgdasd.Pgdasd_01502.setPgdasd_01502(line)
                    pgdasd_01502 = Pgdasd_01502()
                    pgdasd_01502.setPgdasd_01502(line, pgdasd)
                    banco = Banco()
                    banco.insere(pgdasd_01502)
                if line[0] == '02000':
                    id_02000 = id_02000+1 
                    pgdasd_02000 = Pgdasd_02000()
                    pgdasd_02000.setPgdasd_02000(line, pgdasd, id_02000)
                    banco = Banco()
                    banco.insere(pgdasd_02000)
                if line[0] == '03000':#Pode repetir
                    #pgdasd.Pgdasd_03000 = pgdasd.Pgdasd_03000.setPgdasd_03000(line)
                    pgdasd_03000 = Pgdasd_03000()
                    pgdasd_03000.setPgdasd_03000(line, pgdasd)
                    banco = Banco()
                    banco.insere(pgdasd_03000)
                if line[0] == '03100':#Se repete
                    #pgdasd.Pgdasd_03000.Pgdasd_03100 = pgdasd.Pgdasd_03000.Pgdasd_03100.setPgdasd_03100(line)
                    pgdasd_03100 = Pgdasd_03100()
                    pgdasd_03100.setPgdasd_03100(line, pgdasd, pgdasd_03000)
                    banco = Banco()
                    banco.insere(pgdasd_03100)                                        
                if line[0] == '03110':#Se repete                    
                    id_03110 = id_03110+1
                    pgdasd_03110 = Pgdasd_03110()
                    pgdasd_03110.setPgdasd_03110(line, pgdasd, pgdasd_03000, pgdasd_03100, id_03110)
                    banco = Banco()
                    banco.insere(pgdasd_03110)
                if line[0] == '03111':#Se repete                    
                    id_03111 = id_03111+1
                    pgdasd_03111 = Pgdasd_03111()
                    pgdasd_03111.setPgdasd_03111(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03110, id_03111)
                    banco = Banco()
                    banco.insere(pgdasd_03111)
                if line[0] == '03112':#Se repete                    
                    id_03112 = id_03112+1
                    pgdasd_03112 = Pgdasd_03112()
                    pgdasd_03112.setPgdasd_03112(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03110, id_03112)
                    banco = Banco()
                    banco.insere(pgdasd_03112)
                if line[0] == '03120':#Se repete                    
                    id_03120 = id_03120+1
                    pgdasd_03120 = Pgdasd_03120()
                    pgdasd_03120.setPgdasd_03120(line, pgdasd, pgdasd_03000, pgdasd_03100, id_03120)
                    banco = Banco()
                    banco.insere(pgdasd_03120)
                if line[0] == '03121':#Se repete                    
                    id_03121 = id_03121+1
                    pgdasd_03121 = Pgdasd_03121()
                    pgdasd_03121.setPgdasd_03121(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03120, id_03121)
                    banco = Banco()
                    banco.insere(pgdasd_03121)
                if line[0] == '03122':#Se repete                    
                    id_03122 = id_03122+1
                    pgdasd_03122 = Pgdasd_03122()
                    pgdasd_03122.setPgdasd_03122(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03120, id_03122)
                    banco = Banco()
                    banco.insere(pgdasd_03122)
                if line[0] == '03130':#Se repete                    
                    id_03130 = id_03130+1
                    pgdasd_03130 = Pgdasd_03130()
                    pgdasd_03130.setPgdasd_03130(line, pgdasd, pgdasd_03000, pgdasd_03100, id_03130)
                    banco = Banco()
                    banco.insere(pgdasd_03130)                                    
                if line[0] == '03131':#Se repete                    
                    id_03131 = id_03131+1
                    pgdasd_03131 = Pgdasd_03131()
                    pgdasd_03131.setPgdasd_03131(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03130, id_03132)
                    banco = Banco()
                    banco.insere(pgdasd_03131)
                if line[0] == '03132':#Se repete                    
                    id_03132 = id_03132+1
                    pgdasd_03132 = Pgdasd_03132()
                    pgdasd_03132.setPgdasd_03132(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03130, id_03132)
                    banco = Banco()
                    banco.insere(pgdasd_03132)
                if line[0] == '03500':#Se repete                
                    #pgdasd.Pgdasd_03500 = pgdasd.Pgdasd_03500.setPgdasd_03500(line)
                    pgdasd_03500 = Pgdasd_03500()
                    pgdasd_03500.setPgdasd_03500(line, pgdasd)
                    banco = Banco()
                    banco.insere(pgdasd_03500)
                if line[0] == '04000': #Se repete
                    id_04000 = id_04000+1
                    pgdasd_04000 = Pgdasd_04000()
                    pgdasd_04000.setPgdasd_04000(line, pgdasd, id_04000)
                    banco = Banco()
                    banco.insere(pgdasd_04000)
                if line[0] == '99999':    
                    pass                                                                                                                                                                                                     
                i = i + 1   
            print("Arquivo "+url+" importado com sucesso")    
            shutil.copy2(url, "importados/"+file) # Copia arquivo para o diretório importados                                    
        except: 
            print ('Erro ao abrir o arquivo')   
            #print ('Enviar email para o Gestor')                                      
                                

class Banco():
    
    def insere(self, pgdasd):
        try:
            engine = create_engine('oracle://siatdesv:desenvolvimento@dbserver')            
            Session = sessionmaker(bind=engine)
            session = Session()
            session.add(pgdasd)
            session.commit()
            print("Gravando "+pgdasd.__tablename__)                    
        except:        
            session.roolback()                
    
    def insereLista(self, pgdasd):    
        engine = create_engine('oracle://siatdesv:desenvolvimento@dbserver')            
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add_all(pgdasd)
        session.commit()   
        
if __name__ == "__main__":    
    arquivo = File()    
    url = "arquivos"    
    arquivo.hasNewFile(url)    
    arquivo.deleteImportedFile(url)    
    