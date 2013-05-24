# -*- encoding: utf-8 -*-
'''
Created on 10/04/2013

@author: Frederico da Silva Santos
@email: fredsilva.sistemas@gmail.com
 
'''
import os 
import shutil
import zipfile
import re
from pgdasd import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class File():        
        
    
    def hasNewFile(self, url):
        '''
        Verifica se existem arquivos no diretório, se houver, descompacta-os e realiza a importação
        '''        
        #self.extractAllFiles(url)
        #self.separatorRegTO(url, 'TO')
        #url = "arquivos/"
        for (path, dirs, files) in os.walk(url):            
            for file in files:                                                                                          
                fileOriginal = File()                            
                fileOriginal.importFile(url, file)
        
    def removeAllFiles(self, url):
        '''
        Remove todos os arquivos do diretório após a importação
        '''
        for (path, dirs, files) in os.walk(url):
            for file in files:                
                os.remove(os.path.join(path, file))
    
    def extractAllFiles(self, url):
        '''
        Descompacta todos os arquivos .zip de um diretório
        '''
        for (path, dirs, files) in os.walk(url):
            for file in files:
                if file.endswith('.zip'):
                    fileOriginal = zipfile.ZipFile(os.path.join(url,file),'r')
                    fileOriginal.extractall(url)
                    fileOriginal.close()
                    shutil.move(os.path.join(url,file), os.path.join("compactados/",file))                    
                                            
    
    def contLinesFile(self, url):
        '''
        Retorna a quantidade de linhas de um fileOriginal
        '''
        file = open(url,'r')
        lines = file.readlines()
        i = 0
        for line in lines:
            i += 1
        return i
    
    def separatorRegTO(self, url, stateReg):
        '''
        Extrai somente os registros do PGDASD referentes a contribuintes do Estado do Tocantins
        
        OBS: O problema está ocorrendo á partir da linha 38020 do fileOriginal: 01-2015-PGDASD-20120312-01-TO.txt 
        '''
        for(path, dirs, files) in os.walk(url):
            for file in files:
                fileOriginal = open(os.path.join(url,file),'r')                
                newFile = open(os.path.join('arquivos/',file),'w')        
                lines = fileOriginal.readlines()        
                
                i = 0
                quantLines = 0
                lineTemp = []                
                foundState03110 = False
                foundState03000 = False
                newFile.write(lines[0])                     
                for line in lines:                     
                    lineTemp.append(line)                               
                    if line[0:5] == '03000':
                        state = line[21:23]
                        if state == stateReg:
                            foundState03000 = True                                    
                    if line[0:5] == '03110' and state != stateReg:                                                                    
                        if line[6:8] == stateReg:
                            foundState03110 = True
                    if line[0:5] == '99999':                
                        if foundState03000 or foundState03110: #Se existe registro TO no campo 03000 ou 03110                     
                            newFile.writelines(lineTemp)
                            quantLines += len(lineTemp)                                                     
                        lineTemp = []   
                        foundState03110 = False             
                        foundState03000 = False                                  
                    i = i+1                            
                newFile.write('ZZZZZ|'+str(quantLines+2))                            
                newFile.write('\n')
                fileOriginal.close()
                newFile.close()                
                                                        
        self.removeAllFiles(url)       
        
        
        
    def separatorRegTO2(self, url):
        '''
        Cópia de segurança do método separatorRegTO
        '''
        for(path, dirs, files) in os.walk(url):
            for file in files:
                fileOriginal = open(os.path.join(url,file),'r')                
                newArquivo = open(os.path.join('arquivos/',file),'w')        
                lines = fileOriginal.readlines()        
                
                i = 0
                quantLines = 0
                linhaTemp = []
                newArquivo.write(lines[0])                     
                for line in lines:                     
                    linhaTemp.append(line)                               
                    if line[0:5] == '03000':
                        state = line[21:23]
                        print(state)                                              
                    if line[0:5] == '99999':                
                        if state == 'TO':                    
                            newArquivo.writelines(linhaTemp)
                            quantLines += len(linhaTemp)                                              
                        else:
                            linhaTemp = []                
                        
                        linhaTemp = []                                                            
                    i = i+1                            
                newArquivo.write('ZZZZZ|'+str(quantLines+2))                            
                newArquivo.write('\n')
                fileOriginal.close()
                newArquivo.close()                
                                                        
        self.removeAllFiles(url)         
                  
    
    def getFileName(self, file):
        '''
        Retorna o nome do fileOriginal sem a extensão
        '''
        fileName = re.split('[/]', file) # Separa a string pelas barras
        fileName = fileName[len(fileName)-1].split('.')[0] # pega o nome do fileOriginal sem a extensão       
        return fileName
    
    def moveAllFiles(self, src, dest, exts):
        '''
        Move todos os arquivos de determinadas extensões para outro diretório
        '''
        for (path, dirs, files) in os.walk(src):
            for file in files:               
                for ext in exts:
                    if file.endswith(ext): 
                        shutil.move(os.path.join(src,file), os.path.join(dest, file))
    
    def importFile(self, url, file):  
            '''
            Grava no banco os registros dos arquivos do PGDASD         
            ''' 
        #try:           
            url = url+"/"+file            
            fileImport = open(url, 'r')
            lines = fileImport.readlines()            
            fileImport.close()         
            banco = Banco()
                                                                                                                  
            i = 0                    
            while i < len(lines):                                                                                
                line = lines[i].replace("\n","").replace(",",".").split("|") # ler a linha do fileOriginal, retira os \n e troca , por .                        
                if line[0] == '00000':                                                        
                    id_02000 = 0
                    #id_03000 = 0
                    id_03110 = 0
                    id_03111 = 0
                    id_03112 = 0
                    id_03120 = 0
                    id_03121 = 0
                    id_03122 = 0
                    id_03130 = 0
                    id_03131 = 0
                    id_03132 = 0
                    id_04000 = 0
                    pgdasd = Pgdasd()
                    pgdasd = pgdasd.setPgdasd_00000(line)                          
                    banco.insere(pgdasd, i+1)                         
                if line[0] == '01000':
                    #pgdasd.Pgdasd_01000 = pgdasd.Pgdasd_01000.setPgdasd_01000(line, pgdasd)
                    pgdasd_01000 = Pgdasd_01000()
                    pgdasd_01000.setPgdasd_01000(line, pgdasd)                                        
                    banco.insere(pgdasd_01000, i+1)                    
                if line[0] == '01500':#Se repete                    
                    pgdasd_01500 = Pgdasd_01500()
                    pgdasd_01500.setPgdasd_01500(line, pgdasd)                    
                    banco.insere(pgdasd_01500, i+1)                                                                        
                if line[0] == '01501':#Se repete                    
                    pgdasd_01501 = Pgdasd_01501()
                    pgdasd_01501.setPgdasd_01501(line, pgdasd)                    
                    banco.insere(pgdasd_01501, i+1)
                if line[0] == '01502':#Se repete                    
                    pgdasd_01502 = Pgdasd_01502()
                    pgdasd_01502.setPgdasd_01502(line, pgdasd)                    
                    banco.insere(pgdasd_01502, i+1)
                if line[0] == '02000':
                    id_02000 = id_02000+1 
                    pgdasd_02000 = Pgdasd_02000()
                    pgdasd_02000.setPgdasd_02000(line, pgdasd, id_02000)                    
                    banco.insere(pgdasd_02000, i+1)
                if line[0] == '03000':#Pode repetir
                    #id_03000 = id_03000+1                    
                    pgdasd_03000 = Pgdasd_03000()
                    pgdasd_03000.setPgdasd_03000(line, pgdasd)                    
                    banco.insere(pgdasd_03000, i+1)
                if line[0] == '03100':#Se repete                    
                    pgdasd_03100 = Pgdasd_03100()

                    pgdasd_03100.setPgdasd_03100(line, pgdasd, pgdasd_03000)                    
                    banco.insere(pgdasd_03100, i+1)                                        
                if line[0] == '03110':#Se repete                    
                    id_03110 = id_03110+1
                    pgdasd_03110 = Pgdasd_03110()
                    pgdasd_03110.setPgdasd_03110(line, pgdasd, pgdasd_03000, pgdasd_03100, id_03110)                    
                    banco.insere(pgdasd_03110, i+1)
                if line[0] == '03111':#Se repete                    
                    id_03111 = id_03111+1
                    pgdasd_03111 = Pgdasd_03111()
                    pgdasd_03111.setPgdasd_03111(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03110, id_03111)                    
                    banco.insere(pgdasd_03111, i+1)
                if line[0] == '03112':#Se repete                    
                    id_03112 = id_03112+1
                    pgdasd_03112 = Pgdasd_03112()
                    pgdasd_03112.setPgdasd_03112(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03110, id_03112)                    
                    banco.insere(pgdasd_03112, i+1)
                if line[0] == '03120':#Se repete                    
                    id_03120 = id_03120+1
                    pgdasd_03120 = Pgdasd_03120()
                    pgdasd_03120.setPgdasd_03120(line, pgdasd, pgdasd_03000, pgdasd_03100, id_03120)                    
                    banco.insere(pgdasd_03120, i+1)
                if line[0] == '03121':#Se repete                    
                    id_03121 = id_03121+1
                    pgdasd_03121 = Pgdasd_03121()
                    pgdasd_03121.setPgdasd_03121(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03120, id_03121)                    
                    banco.insere(pgdasd_03121, i+1)
                if line[0] == '03122':#Se repete                    
                    id_03122 = id_03122+1
                    pgdasd_03122 = Pgdasd_03122()
                    pgdasd_03122.setPgdasd_03122(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03120, id_03122)                    
                    banco.insere(pgdasd_03122, i+1)
                if line[0] == '03130':#Se repete                    
                    id_03130 = id_03130+1
                    pgdasd_03130 = Pgdasd_03130()
                    pgdasd_03130.setPgdasd_03130(line, pgdasd, pgdasd_03000, pgdasd_03100, id_03130)                    
                    banco.insere(pgdasd_03130, i+1)                                    
                if line[0] == '03131':#Se repete                    
                    id_03131 = id_03131+1
                    pgdasd_03131 = Pgdasd_03131()
                    pgdasd_03131.setPgdasd_03131(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03130, id_03132)                    
                    banco.insere(pgdasd_03131, i+1)
                if line[0] == '03132':#Se repete                    
                    id_03132 = id_03132+1
                    pgdasd_03132 = Pgdasd_03132()
                    pgdasd_03132.setPgdasd_03132(line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03130, id_03132)                    
                    banco.insere(pgdasd_03132, i+1)
                if line[0] == '03500':#Se repete                                    
                    pgdasd_03500 = Pgdasd_03500()
                    pgdasd_03500.setPgdasd_03500(line, pgdasd)                    
                    banco.insere(pgdasd_03500, i+1)
                if line[0] == '04000': #Se repete
                    id_04000 = id_04000+1
                    pgdasd_04000 = Pgdasd_04000()
                    pgdasd_04000.setPgdasd_04000(line, pgdasd, id_04000)                    
                    banco.insere(pgdasd_04000, i+1)
                if line[0] == '99999':    
                    pass                                                                                                                                                                                                     
                i = i + 1   
            print("Arquivo "+url+" importado com sucesso") 
            shutil.move(url, os.path.join("importados/",file))                                                       
        #except: 
            #print("Problemas na linha: "+str(i+1))
            #print ('Erro ao abrir o fileOriginal')
            #shutil.move(url, "erro/"+file) # Move fileOriginal para o diretório erro
                                                
                                

class Banco():
    
    def insere(self, pgdasd, linha):   
        
        try:
            engine = create_engine('oracle://siatdesv:desenvolvimento@dbserver')            
            #engine = create_engine('oracle://treina:treinamento@dbserver')
            Session = sessionmaker(bind=engine)
            session = Session()
            session.add(pgdasd)            
            session.commit()            
            print("Gravando "+pgdasd.__tablename__+" - Linha: "+str(linha))                    
        except Exception as e:
            session.rollback()
            print ("Erro: "+str(e)+" na linha "+str(linha))                           
    
if __name__ == "__main__":        
    fileOriginal = File()    
    url = "arquivos/"       
    fileOriginal.hasNewFile(url)      
    