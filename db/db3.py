'''
Created on 16/04/2013

@author: Frederico da Silva Santos
@email: fredsilva.sistemas@gmail.com
'''

import cx_Oracle

class ConnectionOracle():
    '''
    Realiza conexão com o banco de dados Oracle
    '''    
   
    def connect(self):
        self.uid = "siatdesv"    # usuário
        self.pwd = "desenvolvimento"   # senha
        self.db = "dbserver"  # string de conexão do Oracle, configurado no cliente Oracle, arquivo tnsnames.ora
        conn = cx_Oracle.connect(self.uid + "/" + self.pwd + "@" + self.db) #cria a conexão        
        return conn
        '''
        cursor = conn.cursor() # cria um cursor
        cursor.execute("select * from siatdesv.pgdasd where pgdasd_00000_id_declaracao = '02242675201203001'") # consulta sql
        result = cursor.fetchone()  # busca o resultado da consulta
        if result == None: 
                print ("Nenhum Resultado")
                exit
        else:
                while result:   
                        print (result)
                        result = cursor.fetchone()
        cursor.close()
        conn.close()'''    
        
