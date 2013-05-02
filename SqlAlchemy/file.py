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
        #try:           
            url = url+"/"+file            
            fileImport = open(url, 'r')
            lines = fileImport.readlines()
            fileImport.close()                                   
            pgdasd = Pgdasd()                                                                   
            i = 0                      
            while i < len(lines):                                                    
                line = lines[i].replace("\n","").replace(",",".").split("|") # ler a linha do arquivo, retira os \n e troca , por .                
                if line[0] == '00000':                
                    pgdasd = pgdasd.setPgdasd_00000(line)      
                    print(pgdasd.PGDASD_00000_ID_DECLARACAO)                                                         
                if line[0] == '01000':
                    pgdasd.Pgdasd_01000 = pgdasd.Pgdasd_01000.setPgdasd_01000(line)                    
                if line[0] == '01500':#Se repete
                    pgdasd.Pgdasd_01500 = pgdasd.Pgdasd_01500.setPgdasd_01500(line)                                                                        
                if line[0] == '01501':#Se repete
                    pgdasd.Pgdasd_01501 = pgdasd.Pgdasd_01501.setPgdasd_01501(line)                    
                if line[0] == '01502':#Se repete
                    pgdasd.Pgdasd_01502 = pgdasd.Pgdasd_01502.setPgdasd_01502(line)
                if line[0] == '02000':
                    pgdasd.Pgdasd_02000 = pgdasd.Pgdasd_02000.setPgdasd_02000(line)
                if line[0] == '03000':#Pode repetir
                    pgdasd.Pgdasd_03000 = pgdasd.Pgdasd_03000.setPgdasd_03000(line)
                if line[0] == '03100':#Se repete
                    pgdasd.Pgdasd_03000.Pgdasd_03100 = pgdasd.Pgdasd_03000.Pgdasd_03100.setPgdasd_03100(line)                    
                if line[0] == '03110':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03110 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03110.setPgdasd_03110(line)
                if line[0] == '03111':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03110.Pgdasd_03111 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03110.Pgdasd_03111.setPgdasd_03111(line)
                if line[0] == '03112':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03110.Pgdasd_03112 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03110.Pgdasd_03112.setPgdasd_03112(line)
                if line[0] == '03120':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03120 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03120.setPgdasd_03120(line)                                    
                if line[0] == '03121':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03120.Pgdasd_031121 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03120.Pgdasd_031121.setPgdasd_03121(line)
                if line[0] == '03122':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03120.Pgdasd_031122 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03120.Pgdasd_031122.setPgdasd_03122(line)
                if line[0] == '03130':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03130 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03130.setPgdasd_03130(line)                                    
                if line[0] == '03131':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03130.Pgdasd_031131 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03130.Pgdasd_031131.setPgdasd_03131(line)
                if line[0] == '03132':#Se repete                    
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03130.Pgdasd_031132 = pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03130.Pgdasd_031132.setPgdasd_03132(line)
                if line[0] == '03500':#Se repete                
                    pgdasd.Pgdasd_03500 = pgdasd.Pgdasd_03500.setPgdasd_03500(line)
                if line[0] == '04000': #Se repete
                    pgdasd.Pgdasd_04000 = pgdasd.Pgdasd_04000.setPgdasd_04000(line)                       
                if line[0] == '99999':    
                    pass                                                                                                                                                                                                     
                i = i + 1   
            shutil.copy2(url, "importados/"+file) # Copia arquivo para o diretório importados                                    
        #except: 
            #print ('Erro ao abrir o arquivo')   
        #    print ('Enviar email para o Gestor')                                      
                                

class Banco():
    
    def insere(self, pgdasd):
        try:
            engine = create_engine('oracle://siatdesv:desenvolvimento@dbserver')            
            Session = sessionmaker(bind=engine)
            session = Session()
            session.add(pgdasd)
            session.commit()
            print("Commit")
        except:        
            session.roolback()
            print("Rollback")
    
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
    #arquivo.deleteImportedFile(url)    
    