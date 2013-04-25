# -*- encoding: utf-8 -*-
'''
Created on 10/04/2013

@author: Frederico da Silva Santos
@email: fredsilva.sistemas@gmail.com
 
'''
from controller import pgdasd
import platform
import os
#import commands 
import shutil
from pgdasd import *


class File():
    
    def __init__(self):
        self.pgdasdControl = pgdasd.PgdasdController()
        
    
    def sizeFile(self, url):
        '''
        Descobre o tamanho em Kbytes de um arquivo ou diretório
        '''
        so = platform.system()
        if so == 'Linux':
            '''command = commands.getoutput("du -hs "+url)
            size = float(command.split("K")[0].replace(',', '.'))'''            
            size = os.stat(url).st_size            
        if so == 'Windows':
            size = os.stat(url).st_size        
        return size
    
    def hasNewFile(self, url):
        '''
        Verifica se existem arquivos no diretório, se houver realiza a importação
        '''        
        '''if self.sizeFile(url) > 0:
            print (self.sizeFile(url))
            return True
        else:
            print (self.sizeFile(url))
            return False'''
        
        for (path, dirs, files) in os.walk(url):
            for file in files:
                arquivo = File()
                arquivo.importFile(url+"/"+file)
        
    def moveImportedFile(self, src, dst):
        '''
        Move o arquivo após importação
        '''
        shutil.move(src, dst)

    
    def importFile(self, url):   
        #try:           
            fileImport = open(url, 'r')
            lines = fileImport.readlines()
            fileImport.close()                
            pgdasd = Pgdasd()  
            pgdasd_01000 = Pgdasd_01000()   
            pgdasd_01500 = Pgdasd_01500()
            pgdasd_01501 = Pgdasd_01501()
            pgdasd_01502 = Pgdasd_01502()
            pgdasd_02000 = Pgdasd_02000()
            pgdasd_03000 = Pgdasd_03000()     
            pgdasd_03100 = Pgdasd_03100()
            pgdasd_03110 = Pgdasd_03110()
            pgdasd_03111 = Pgdasd_03111()
            pgdasd_03112 = Pgdasd_03112()
            pgdasd_03120 = Pgdasd_03120()
            pgdasd_03121 = Pgdasd_03121()
            pgdasd_03122 = Pgdasd_03122()
            pgdasd_03130 = Pgdasd_03130()
            pgdasd_03131 = Pgdasd_03131()
            pgdasd_03132 = Pgdasd_03132()
            pgdasd_03500 = Pgdasd_03500()
            pgdasd_04000 = Pgdasd_04000()            
            
            i = 0                      
            while i < len(lines):                        
                line = lines[i].replace("\n","").replace(",",".").split("|") # ler a linha do arquivo, retira os \n e troca , por .
                   
                if line[0] == '00000':                
                    pgdasd = pgdasd.setPgdasd_00000(line)                                                           
                if line[0] == '01000':
                    pgdasd.Pgdasd_01000 = pgdasd_01000.setPgdasd_01000(line)                                                                                            
                if line[0] == '01500':
                    pgdasd_01500.setPgdasd_01500(line)
                    pgdasd.Pgdasd_01500.append({'rbsn_PA': pgdasd_01500.rbsn_PA, 'rbsn_valor': pgdasd_01500.rbsn_valor})                                                  
                if line[0] == '01501':
                    pgdasd_01501.setPgdasd_01501(line)
                    pgdasd.Pgdasd_01501.append({'rbsn_PA': pgdasd_01501.rbsn_PA, 'rbsn_valor': pgdasd_01501.rbsn_valor})                                              
                if line[0] == '01502':
                    pgdasd_01502.setPgdasd_01502(line)
                    pgdasd.Pgdasd_01502.append({'Rbsn_Ext_PA': pgdasd_01502.Rbsn_Ext_PA, 'Rbsn_Ext_valor': pgdasd_01502.Rbsn_Ext_valor})                                
                if line[0] == '02000':
                    pgdasd.Pgdasd_02000 = pgdasd_02000.setPgdasd_02000(line)                
                if line[0] == '03000':
                    pgdasd_03000.setPgdasd_03000(line)
                    pgdasd.Pgdasd_03000.append({'CNPJ': pgdasd_03000.CNPJ, 'Uf': pgdasd_03000.Uf, 'Cod_TOM': pgdasd_03000.Cod_TOM, 'Vltotal': pgdasd_03000.Vltotal, 'IME': pgdasd_03000.IME, 'Limite': pgdasd_03000.Limite, 'LimUltrapassadoPA': pgdasd_03000.LimUltrapassadoPA, 'prex1': pgdasd_03000.prex1, 'prex2': pgdasd_03000.prex2})                    
                if line[0] == '03100':
                    pgdasd_03100.setPgdasd_03100(line)  
                    pgdasd.Pgdasd_03100.append({'Tipo': pgdasd_03100.Tipo, 'Vltotal':pgdasd_03100.Vltotal})                                                                                       
                if line[0] == '03110':
                    pgdasd_03110.setPgdasd_03110(line)
                    pgdasd.Pgdasd_03110.append({
                                                'Id'              : pgdasd_03110.Id,
                                                 'UF'             :pgdasd_03110.UF,
                                                 'Cod_TOM'        : pgdasd_03110.Cod_TOM,
                                                 'Valor'          : pgdasd_03110.Valor,
                                                 'COFINS'         : pgdasd_03110.COFINS,
                                                 'CSLL'           : pgdasd_03110.CSLL,
                                                 'ICMS'           : pgdasd_03110.ICMS,
                                                 'INSS'           : pgdasd_03110.INSS,
                                                 'IPI'            : pgdasd_03110.IPI,
                                                 'IRPJ'           : pgdasd_03110.IRPJ,
                                                 'ISS'            : pgdasd_03110.ISS,
                                                 'PIS'            : pgdasd_03110.PIS,
                                                 'Aliqapur'       : pgdasd_03110.Aliqapur,
                                                 'Vlimposto'      : pgdasd_03110.Vlimposto,
                                                 'Aliquota_COFINS': pgdasd_03110.Aliquota_COFINS,
                                                 'Valor_COFINS'   : pgdasd_03110.Valor_COFINS,
                                                 'Aliquota_CSLL'  : pgdasd_03110.Aliquota_CSLL,
                                                 'Valor_CSLL'     : pgdasd_03110.Valor_CSLL,
                                                 'Aliquota_ICMS'  : pgdasd_03110.Aliquota_ICMS,
                                                 'Valor_ICMS'     : pgdasd_03110.Valor_ICMS,
                                                 'Aliquota_INSS'  : pgdasd_03110.Aliquota_INSS,
                                                 'Valor_INSS'     : pgdasd_03110.Valor_INSS,
                                                 'Aliquota_IPI'   : pgdasd_03110.Aliquota_IPI,                     
                                                 'Valor_IPI'      : pgdasd_03110.Valor_IPI,
                                                 'Aliquota_IRPJ'  : pgdasd_03110.Aliquota_IRPJ,
                                                 'Valor_IRPJ'     : pgdasd_03110.Valor_IRPJ,
                                                 'Aliquota_ISS'   : pgdasd_03110.Aliquota_ISS,                                          
                                                 'Valor_ISS'      : pgdasd_03110.Valor_ISS,
                                                 'Aliquota_PIS'   : pgdasd_03110.Aliquota_PIS,
                                                 'Valor_PIS'      : pgdasd_03110.Valor_PIS,
                                                 'Diferenca'      : pgdasd_03110.Diferenca,
                                                 'Maiortributo'   : pgdasd_03110.Maiortributo
                                                 })                                                                      
                if line[0] == '03111': 
                    pgdasd.Pgdasd_03111 = pgdasd_03111.setPgdasd_03111(line)                                                   
                if line[0] == '03112':
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03110.Pgdasd_03112 = pgdasd_03000.Pgdasd_03100.Pgdasd_03110.Pgdasd_03112.setPgdasd_03112(line)
                if line[0] == '03120':
                    pgdasd_03120.setPgdasd_03120(line)
                    pgdasd.Pgdasd_03120.append({
                                                'Id'              : pgdasd_03120.Id,                                                 
                                                 'Aliqapur'       : pgdasd_03120.Aliqapur,                                                 
                                                 'Aliquota_COFINS': pgdasd_03120.Aliquota_COFINS,
                                                 'Valor_COFINS'   : pgdasd_03120.Valor_COFINS,
                                                 'Aliquota_CSLL'  : pgdasd_03120.Aliquota_CSLL,
                                                 'Valor_CSLL'     : pgdasd_03120.Valor_CSLL,
                                                 'Aliquota_ICMS'  : pgdasd_03120.Aliquota_ICMS,
                                                 'Valor_ICMS'     : pgdasd_03120.Valor_ICMS,
                                                 'Aliquota_INSS'  : pgdasd_03120.Aliquota_INSS,
                                                 'Valor_INSS'     : pgdasd_03120.Valor_INSS,
                                                 'Aliquota_IPI'   : pgdasd_03120.Aliquota_IPI,                     
                                                 'Valor_IPI'      : pgdasd_03120.Valor_IPI,
                                                 'Aliquota_IRPJ'  : pgdasd_03120.Aliquota_IRPJ,
                                                 'Valor_IRPJ'     : pgdasd_03120.Valor_IRPJ,
                                                 'Aliquota_ISS'   : pgdasd_03120.Aliquota_ISS,                                          
                                                 'Valor_ISS'      : pgdasd_03120.Valor_ISS,
                                                 'Aliquota_PIS'   : pgdasd_03120.Aliquota_PIS,
                                                 'Valor_PIS'      : pgdasd_03120.Valor_PIS,                                                 
                                                })
                if line[0] == '03121':
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03120.Pgdasd_03121 = pgdasd_03000.Pgdasd_03100.Pgdasd_03120.Pgdasd_03121.setPgdasd_03121(line)
                if line[0] == '03122':
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03120.Pgdasd_03122 = pgdasd_03000.Pgdasd_03100.Pgdasd_03120.Pgdasd_03122.setPgdasd_03122(line)
                if line[0] == '03130':
                    pgdasd_03130.setPgdasd_03130(line)
                    pgdasd.Pgdasd_03130.append({
                                                'Id'              : pgdasd_03130.Id,                                                 
                                                 'Aliqapur'       : pgdasd_03130.Aliqapur,                                                 
                                                 'Aliquota_COFINS': pgdasd_03130.Aliquota_COFINS,
                                                 'Valor_COFINS'   : pgdasd_03130.Valor_COFINS,
                                                 'Aliquota_CSLL'  : pgdasd_03130.Aliquota_CSLL,
                                                 'Valor_CSLL'     : pgdasd_03130.Valor_CSLL,
                                                 'Aliquota_ICMS'  : pgdasd_03130.Aliquota_ICMS,
                                                 'Valor_ICMS'     : pgdasd_03130.Valor_ICMS,
                                                 'Aliquota_INSS'  : pgdasd_03130.Aliquota_INSS,
                                                 'Valor_INSS'     : pgdasd_03130.Valor_INSS,
                                                 'Aliquota_IPI'   : pgdasd_03130.Aliquota_IPI,                     
                                                 'Valor_IPI'      : pgdasd_03130.Valor_IPI,
                                                 'Aliquota_IRPJ'  : pgdasd_03130.Aliquota_IRPJ,
                                                 'Valor_IRPJ'     : pgdasd_03130.Valor_IRPJ,
                                                 'Aliquota_ISS'   : pgdasd_03130.Aliquota_ISS,                                          
                                                 'Valor_ISS'      : pgdasd_03130.Valor_ISS,
                                                 'Aliquota_PIS'   : pgdasd_03130.Aliquota_PIS,
                                                 'Valor_PIS'      : pgdasd_03130.Valor_PIS,                                                 
                                                })
                if line[0] == '03131':
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03130.Pgdasd_03131 = pgdasd_03000.Pgdasd_03100.Pgdasd_03130.Pgdasd_03131.setPgdasd_03131(line)
                if line[0] == '03132':
                    pgdasd.Pgdasd_03000.Pgdasd_03100.Pgdasd_03130.Pgdasd_03132 = pgdasd_03000.Pgdasd_03100.Pgdasd_03130.Pgdasd_03132.setPgdasd_03132(line)                                            
                if line[0] == '03500':
                    pgdasd.Pgdasd_03500 = pgdasd_03500.setPgdasd_03500(line)
                if line[0] == '04000':
                    pgdasd.Pgdasd_04000 = pgdasd_04000.setPgdasd_04000(line)                   
                if line[0] == '99999': # Fim do registro  
                    #print(pgdasd.Pgdasd_03000.Pgdasd_03100)                                                                 
                    self.pgdasdControl.insert(pgdasd)                                                                                       
                                                                            
                i = i + 1  
            
            #self.moveImportedFile(url, "importados")
        #except: 
        #    print ('Erro ao abrir o arquivo')   
        #    print ('Enviar email para o Gestor')                                      
                                
        
if __name__ == "__main__":    
    arquivo = File()    
    url = "arquivos"    
    arquivo.hasNewFile(url)    
    #arquivo.importFile(url)    
    