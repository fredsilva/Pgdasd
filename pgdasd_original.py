#encoding:utf-8
'''
Created on 11/04/2013

@author: Frederico da Silva Santos
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey

Base = declarative_base()
SCHEMA = {'schema' : 'SIATTREI'}

class Pgdasd(Base):
    
    __tablename__ = 'PGDASD'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID               = Column(Integer, primary_key = True, autoincrement=True)
    PGDASD_00000_ID_DECLARACAO    = Column(String)
    PGDASD_00000_NUM_RECIBO       = Column(String)
    PGDASD_00000_NUM_AUTENTICACAO = Column(String) 
    PGDASD_00000_DT_TRANSMISSAO   = Column(String)
    PGDASD_00000_VERSAO           = Column(String)
    PGDASD_00000_CNPJMATRIZ       = Column(String)
    PGDASD_00000_NOME             = Column(String)
    PGDASD_00000_COD_TOM          = Column(String)
    PGDASD_00000_OPTANTE          = Column(String)
    PGDASD_00000_ABERTURA         = Column(String)
    PGDASD_00000_PA               = Column(String)
    PGDASD_00000_RPA              = Column(Numeric(15,2))
    PGDASD_00000_RAZAO            = Column(Numeric(15,3))
    PGDASD_00000_IM               = Column(Numeric(15,2))
    PGDASD_00000_OPERACAO         = Column(String)
    PGDASD_00000_REGIME           = Column(String)
    PGDASD_00000_RPAC             = Column(Numeric(15,2))
    PGDASD_00000_RPA_INT          = Column(Numeric(15,2))         
    PGDASD_00000_RPA_EXT          = Column(Numeric(15,2))
        
    
    def setPgdasd_00000(self, line):
        self.PGDASD_00000_ID_DECLARACAO    = line[1]
        self.PGDASD_00000_NUM_RECIBO       = line[2]
        self.PGDASD_00000_NUM_AUTENTICACAO = line[3]
        self.PGDASD_00000_DT_TRANSMISSAO   = line[4]
        self.PGDASD_00000_VERSAO           = line[5]
        self.PGDASD_00000_CNPJMATRIZ       = line[6]
        self.PGDASD_00000_NOME             = line[7]
        self.PGDASD_00000_COD_TOM          = line[8]
        self.PGDASD_00000_OPTANTE          = line[9]
        self.PGDASD_00000_ABERTURA         = line[10]
        self.PGDASD_00000_PA               = line[11]
        self.PGDASD_00000_RPA              = line[12]
        self.PGDASD_00000_RAZAO            = line[13]
        self.PGDASD_00000_IM               = line[14]
        self.PGDASD_00000_OPERACAO         = line[15]
        self.PGDASD_00000_REGIME           = line[16]
        self.PGDASD_00000_RPAC             = line[17]
        self.PGDASD_00000_RPA_INT          = line[18]
        self.PGDASD_00000_RPA_EXT          = line[19]     
                
        return self
    
class Pgdasd_01000(Base):
    __tablename__ = 'pgdasd_01000'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID             = Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))   
    PGDASD_01000_NRPAGTO        = Column(String, primary_key = True)
    PGDASD_01000_PRINC          = Column(Numeric(14,2))
    PGDASD_01000_MULTA          = Column(Numeric(14,2))
    PGDASD_01000_JUROS          = Column(Numeric(14,2))
    PGDASD_01000_TDEVIDO        = Column(Numeric(14,2))
    PGDASD_01000_DTVENC         = Column(String(8))
    PGDASD_01000_DTVALCALC      = Column(String(8))
    PGDASD_01000_VDAS           = Column(Numeric(14,2))
        
    
    def setPgdasd_01000(self, line, pgdasd):                     
        self.PGDASD_00000_ID             = pgdasd.PGDASD_00000_ID
        self.PGDASD_01000_NRPAGTO        = line[1]
        self.PGDASD_01000_PRINC          = line[2]
        self.PGDASD_01000_MULTA          = line[3]
        self.PGDASD_01000_JUROS          = line[4]
        self.PGDASD_01000_TDEVIDO        = line[5]
        self.PGDASD_01000_DTVENC         = line[6]
        self.PGDASD_01000_DTVALCALC      = line[7]
        self.PGDASD_01000_VDAS           = line[8]        
        return self

class Pgdasd_01500(Base):
    __tablename__  = 'pgdasd_01500'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID         =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_01500_RBSN_PA    = Column(String(6), primary_key = True)    
    PGDASD_01500_RBSN_VALOR = Column(Numeric(14,2))
        
    
    def setPgdasd_01500(self, line, pgdasd):             
        self.PGDASD_00000_ID             = pgdasd.PGDASD_00000_ID
        self.PGDASD_00000_DT_TRANSMISSAO = pgdasd.PGDASD_00000_DT_TRANSMISSAO
        self.PGDASD_00000_OPERACAO       = pgdasd.PGDASD_00000_OPERACAO               
        self.PGDASD_01500_RBSN_PA        = line[1]
        self.PGDASD_01500_RBSN_VALOR     = line[2]            
        return self         
    
        
class Pgdasd_01501(Base):
    __tablename__  = 'pgdasd_01501'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID         =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))    
    PGDASD_01501_RBSN_PA    = Column(String(6), primary_key = True)    
    PGDASD_01501_RBSN_VALOR = Column(Numeric(14,2))
        
    
    def setPgdasd_01501(self, line, pgdasd):             
        self.PGDASD_00000_ID         = pgdasd.PGDASD_00000_ID
        self.PGDASD_01501_RBSN_PA    = line[1]
        self.PGDASD_01501_RBSN_VALOR = line[2]            
        return self

class Pgdasd_01502(Base):
    __tablename__  = 'pgdasd_01502'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID             =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_01502_RBSN_EXT_PA    = Column(String(6), primary_key = True)    
    PGDASD_01502_RBSN_EXT_VALOR = Column(Numeric(14,2))
        
    
    def setPgdasd_01502(self, line, pgdasd):                 
        self.PGDASD_00000_ID             = pgdasd.PGDASD_00000_ID
        self.PGDASD_01502_RBSN_EXT_PA    = line[1]
        self.PGDASD_01502_RBSN_EXT_VALOR = line[2]            
        return self
    
class Pgdasd_02000(Base):
    __tablename__  = 'pgdasd_02000'
    __table_args__ = SCHEMA
        
    PGDASD_00000_ID            =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_02000_ID            = Column(Integer, primary_key = True)
    PGDASD_02000_RBT12         = Column(Numeric(14,2))
    PGDASD_02000_RBTAA         = Column(Numeric(14,2))
    PGDASD_02000_RBA           = Column(Numeric(14,2))
    PGDASD_02000_RBT12O        = Column(Numeric(14,2))
    PGDASD_02000_RBTAAO        = Column(String(8))
    PGDASD_02000_ICMS          = Column(String(8))
    PGDASD_02000_ISS           = Column(Numeric(14,2))
    PGDASD_02000_RBTAA_INT     = Column(Numeric(14,2))
    PGDASD_02000_RBTAA_INTO    = Column(Numeric(14,2))
    PGDASD_02000_RBTAA_EXT     = Column(Numeric(14,2))
    PGDASD_02000_RBTAA_EXTO    = Column(Numeric(14,2))
        
    
    def setPgdasd_02000(self, line, pgdasd, id_02000):             
        self.PGDASD_00000_ID            = pgdasd.PGDASD_00000_ID
        self.PGDASD_02000_ID            = id_02000 
        self.PGDASD_02000_RBT12         = line[1]
        self.PGDASD_02000_RBTAA         = line[2]
        self.PGDASD_02000_RBA           = line[3]
        self.PGDASD_02000_RBT12O        = line[4]
        self.PGDASD_02000_RBTAAO        = line[5]
        self.PGDASD_02000_ICMS          = line[6]
        self.PGDASD_02000_ISS           = line[7]        
        self.PGDASD_02000_RBTAA_INT     = line[8]
        self.PGDASD_02000_RBTAA_INTO    = line[9]
        self.PGDASD_02000_RBTAA_EXT     = line[10]
        self.PGDASD_02000_RBTAA_EXTO    = line[11]        
        return self

class Pgdasd_03000(Base):
    __tablename__  = 'pgdasd_03000'
    __table_args__ = SCHEMA
        
    PGDASD_00000_ID                = Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    #PGDASD_03000_ID                = Column(Integer, primary_key = True)
    PGDASD_03000_CNPJ              = Column(String(14), primary_key = True)
    PGDASD_03000_UF                = Column(String(2))
    PGDASD_03000_COD_TOM           = Column(String(4))
    PGDASD_03000_VLTOTAL           = Column(Numeric(14,2))
    PGDASD_03000_IME               = Column(Numeric(14,2))
    PGDASD_03000_LIMITE            = Column(Numeric(14,2))
    PGDASD_03000_LIMULTRAPASSADOPA = Column(String(1))
    PGDASD_03000_PREX1             = Column(Numeric(4,10))
    PGDASD_03000_PREX2             = Column(Numeric(4,10))
            
    
    def setPgdasd_03000(self, line, pgdasd):                             
        self.PGDASD_00000_ID                = pgdasd.PGDASD_00000_ID
        #self.PGDASD_03000_ID                = id_03000
        self.PGDASD_03000_CNPJ              = line[1]
        self.PGDASD_03000_UF                = line[2]
        self.PGDASD_03000_COD_TOM           = line[3]
        self.PGDASD_03000_VLTOTAL           = line[4]
        self.PGDASD_03000_IME               = line[5]
        self.PGDASD_03000_LIMITE            = line[6]
        self.PGDASD_03000_LIMULTRAPASSADOPA = line[7]
        self.PGDASD_03000_PREX1             = line[8]        
        self.PGDASD_03000_PREX2             = line[9]   
                
        #self.Pgdasd_03100.PGDASD_03000_CNPJ   = self.PGDASD_03000_CNPJ #Verificar se vai dar erro aqui
                 
        return self


class Pgdasd_03100(Base):
    __tablename__  = 'pgdasd_03100'
    __table_args__ = SCHEMA
        
    PGDASD_00000_ID      =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ      = Column(String, ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO    = Column(String(2), primary_key = True)
    PGDASD_03100_VLTOTAL = Column(Numeric(14,2))
       
    
    def setPgdasd_03100(self, line, pgdasd, pgdasd_03000):                       
        self.PGDASD_00000_ID      = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ    = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO    = line[1]
        self.PGDASD_03100_VLTOTAL = line[2]   
                  
        return self
        
class Pgdasd_03110(Base):
    __tablename__  = 'pgdasd_03110'
    __table_args__ = SCHEMA
        
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03110_ID              = Column(Integer, primary_key = True)
    PGDASD_03110_UF              = Column(String(2))
    PGDASD_03110_COD_TOM         = Column(String(4))
    PGDASD_03110_VALOR           = Column(Numeric(14,2))
    PGDASD_03110_COFINS          = Column(String(1))
    PGDASD_03110_CSLL            = Column(String(1))
    PGDASD_03110_ICMS            = Column(String(1))
    PGDASD_03110_INSS            = Column(String(1))
    PGDASD_03110_IPI             = Column(String(1))
    PGDASD_03110_IRPJ            = Column(String(1))
    PGDASD_03110_ISS             = Column(String(1))
    PGDASD_03110_PIS             = Column(String(1))
    PGDASD_03110_ALIQAPUR        = Column(Numeric(14,3))
    PGDASD_03110_VLIMPOSTO       = Column(Numeric(14,3))
    PGDASD_03110_ALIQUOTA_COFINS = Column(Numeric(14,3))
    PGDASD_03110_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03110_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03110_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03110_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03110_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03110_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03110_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03110_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03110_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03110_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03110_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03110_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03110_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03110_ALIQUOTA_PIS    = Column(Numeric(14,3))
    PGDASD_03110_VALOR_PIS       = Column(Numeric(14,3))
    PGDASD_03110_DIFERENCA       = Column(Numeric(14,2))
    PGDASD_03110_MAIORTRIBUTO    = Column(Numeric(14,3))
            
    
    def setPgdasd_03110(self, line, pgdasd, pgdasd_03000, pgdasd_03100, id_03110):
        
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        
        self.PGDASD_03110_ID              = id_03110            
        self.PGDASD_03110_UF              = line[1]
        self.PGDASD_03110_COD_TOM         = line[2]
        self.PGDASD_03110_VALOR           = line[3]
        self.PGDASD_03110_COFINS          = line[4]
        self.PGDASD_03110_CSLL            = line[5]
        self.PGDASD_03110_ICMS            = line[6]
        self.PGDASD_03110_INSS            = line[7]
        self.PGDASD_03110_IPI             = line[8]
        self.PGDASD_03110_IRPJ            = line[9]
        self.PGDASD_03110_ISS             = line[10]
        self.PGDASD_03110_PIS             = line[11]
        self.PGDASD_03110_ALIQAPUR        = line[12]
        self.PGDASD_03110_VLIMPOSTO       = line[13]
        self.PGDASD_03110_ALIQUOTA_COFINS = line[14]
        self.PGDASD_03110_VALOR_COFINS    = line[15]
        self.PGDASD_03110_ALIQUOTA_CSLL   = line[16]
        self.PGDASD_03110_VALOR_CSLL      = line[17]
        self.PGDASD_03110_ALIQUOTA_ICMS   = line[18]
        self.PGDASD_03110_VALOR_ICMS      = line[19]
        self.PGDASD_03110_ALIQUOTA_INSS   = line[20]
        self.PGDASD_03110_VALOR_INSS      = line[21]
        self.PGDASD_03110_ALIQUOTA_IPI    = line[22]
        self.PGDASD_03110_VALOR_IPI       = line[23]
        self.PGDASD_03110_ALIQUOTA_IRPJ   = line[24]
        self.PGDASD_03110_VALOR_IRPJ      = line[25]
        self.PGDASD_03110_ALIQUOTA_ISS    = line[26]
        self.PGDASD_03110_VALOR_ISS       = line[27]
        self.PGDASD_03110_ALIQUOTA_PIS    = line[28]
        self.PGDASD_03110_VALOR_PIS       = line[29]
        self.PGDASD_03110_DIFERENCA       = line[30]
        self.PGDASD_03110_MAIORTRIBUTO    = line[31]                
                
        return self
    
class Pgdasd_03111(Base):
    __tablename__  = 'pgdasd_03111'
    __table_args__ = SCHEMA
        
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03110_ID              = Column(Integer, ForeignKey('pgdasd_03110.PGDASD_03110_ID'))
    PGDASD_03111_ID              = Column(Integer, primary_key = True)
    PGDASD_03111_ALIQAPUR        = Column(Numeric(14,2))    
    PGDASD_03111_VLIMPOSTO       = Column(Numeric(14,2))    
    PGDASD_03111_ALIQUOTA_COFINS = Column(Numeric(14,3))
    PGDASD_03111_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03111_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03111_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03111_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03111_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03111_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03111_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03111_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03111_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03111_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03111_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03111_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03111_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03111_ALIQUOTA_PIS    = Column(Numeric(14,3))
    PGDASD_03111_VALOR_PIS       = Column(Numeric(14,3))
    PGDASD_03111_DIFERENCA       = Column(Numeric(14,2))
    PGDASD_03111_MAIORTRIBUTO    = Column(Numeric(14,3))
    
    def setPgdasd_03111(self, line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03110, id_03111):    
                
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        self.PGDASD_03110_ID              = pgdasd_03110.PGDASD_03110_ID
        
        self.PGDASD_03111_ID              = id_03111                 
        self.PGDASD_03111_ALIQAPUR        = line[1]
        self.PGDASD_03111_VLIMPOSTO       = line[2]
        self.PGDASD_03111_ALIQUOTA_COFINS = line[3]
        self.PGDASD_03111_VALOR_COFINS    = line[4]
        self.PGDASD_03111_ALIQUOTA_CSLL   = line[5]
        self.PGDASD_03111_VALOR_CSLL      = line[6]
        self.PGDASD_03111_ALIQUOTA_ICMS   = line[7]
        self.PGDASD_03111_VALOR_ICMS      = line[8]
        self.PGDASD_03111_ALIQUOTA_INSS   = line[9]
        self.PGDASD_03111_VALOR_INSS      = line[10]
        self.PGDASD_03111_ALIQUOTA_IPI    = line[11]
        self.PGDASD_03111_VALOR_IPI       = line[12]
        self.PGDASD_03111_ALIQUOTA_IRPJ   = line[13]
        self.PGDASD_03111_VALOR_IRPJ      = line[14]
        self.PGDASD_03111_ALIQUOTA_ISS    = line[15]
        self.PGDASD_03111_VALOR_ISS       = line[16]
        self.PGDASD_03111_ALIQUOTA_PIS    = line[17]
        self.PGDASD_03111_VALOR_PIS       = line[18]
        self.PGDASD_03111_DIFERENCA       = line[19]
        self.PGDASD_03111_MAIORTRIBUTO    = line[20]        
        
class Pgdasd_03112(Base):
    __tablename__  = 'pgdasd_03112'
    __table_args__ = SCHEMA
        
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03110_ID              = Column(Integer, ForeignKey('pgdasd_03110.PGDASD_03110_ID'))
    PGDASD_03112_ID              = Column(Integer, primary_key = True)
    PGDASD_03112_VALOR           = Column(Numeric(14,2))    
    PGDASD_03112_RED             = Column(Numeric(14,2))    
    PGDASD_03112_ALIQAPUR        = Column(Numeric(14,3))
    PGDASD_03112_VLIMPOSTO       = Column(Numeric(14,3))
    PGDASD_03112_ALIQUOTA_COFINS = Column(Numeric(14,3))
    PGDASD_03112_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03112_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03112_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03112_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03112_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03112_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03112_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03112_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03112_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03112_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03112_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03112_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03112_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03112_DIFERENCA       = Column(Numeric(14,2))
    PGDASD_03112_MAIORTRIBUTO    = Column(Numeric(14,3))
    PGDASD_03112_VALOR_PIS       = Column(Numeric(14,3))
    PGDASD_03112_ALIQUOTA_PIS    = Column(Numeric(14,3))
    
    def setPgdasd_03112(self, line,  pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03110, id_03112): 
                
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        self.PGDASD_03110_ID              = pgdasd_03110.PGDASD_03110_ID
           
        self.PGDASD_03112_ID              = id_03112                  
        self.PGDASD_03112_VALOR           = line[1]
        self.PGDASD_03112_RED             = line[2]
        self.PGDASD_03112_ALIQAPUR        = line[3]
        self.PGDASD_03112_VLIMPOSTO       = line[4]
        self.PGDASD_03112_ALIQUOTA_COFINS = line[5]
        self.PGDASD_03112_VALOR_COFINS    = line[6]
        self.PGDASD_03112_ALIQUOTA_CSLL   = line[7]
        self.PGDASD_03112_VALOR_CSLL      = line[8]
        self.PGDASD_03112_ALIQUOTA_ICMS   = line[9]
        self.PGDASD_03112_VALOR_ICMS      = line[10]
        self.PGDASD_03112_ALIQUOTA_INSS   = line[11]
        self.PGDASD_03112_VALOR_INSS      = line[12]
        self.PGDASD_03112_ALIQUOTA_IPI    = line[13]
        self.PGDASD_03112_VALOR_IPI       = line[14]
        self.PGDASD_03112_ALIQUOTA_IRPJ   = line[15]
        self.PGDASD_03112_VALOR_IRPJ      = line[16]
        self.PGDASD_03112_ALIQUOTA_ISS    = line[17]
        self.PGDASD_03112_VALOR_ISS       = line[18]
        self.PGDASD_03112_ALIQUOTA_PIS    = line[19]
        self.PGDASD_03112_VALOR_PIS       = line[20]
        self.PGDASD_03112_DIFERENCA       = line[21]
        self.PGDASD_03112_MAIORTRIBUTO    = line[22]                
    
class Pgdasd_03120(Base):
    __tablename__  = 'pgdasd_03120'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03120_ID              = Column(Integer, primary_key = True)
    PGDASD_03120_ALIQAPUR        = Column(Numeric(14,2))
    PGDASD_03120_ALIQUOTA_COFINS = Column(Numeric(14,3))
    PGDASD_03120_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03120_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03120_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03120_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03120_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03120_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03120_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03120_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03120_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03120_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03120_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03120_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03120_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03120_ALIQUOTA_PIS    = Column(Numeric(14,3))
    PGDASD_03120_VALOR_PIS       = Column(Numeric(14,3))    
            
    
    def setPgdasd_03120(self, line, pgdasd, pgdasd_03000, pgdasd_03100, id_03120):   
                
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        
        self.PGDASD_03120_ID              = id_03120                  
        self.PGDASD_03120_ALIQAPUR        = line[1]
        self.PGDASD_03120_ALIQUOTA_COFINS = line[2]
        self.PGDASD_03120_VALOR_COFINS    = line[3]
        self.PGDASD_03120_ALIQUOTA_CSLL   = line[4]
        self.PGDASD_03120_VALOR_CSLL      = line[5]
        self.PGDASD_03120_ALIQUOTA_ICMS   = line[6]
        self.PGDASD_03120_VALOR_ICMS      = line[7]
        self.PGDASD_03120_ALIQUOTA_INSS   = line[8]
        self.PGDASD_03120_VALOR_INSS      = line[9]
        self.PGDASD_03120_ALIQUOTA_IPI    = line[10]
        self.PGDASD_03120_VALOR_IPI       = line[11]
        self.PGDASD_03120_ALIQUOTA_IRPJ   = line[12]
        self.PGDASD_03120_VALOR_IRPJ      = line[13]
        self.PGDASD_03120_ALIQUOTA_ISS    = line[14]
        self.PGDASD_03120_VALOR_ISS       = line[15]
        self.PGDASD_03120_ALIQUOTA_PIS    = line[16]
        self.PGDASD_03120_VALOR_PIS       = line[17]      
                                        
        return self
        
class Pgdasd_03121(Base):
    __tablename__  = 'pgdasd_03121'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03120_ID              = Column(Integer, ForeignKey('pgdasd_03120.PGDASD_03120_ID'))
    PGDASD_03121_ID              = Column(Integer, primary_key = True)
    PGDASD_03121_ALIQAPUR        = Column(Numeric(14,2))    
    PGDASD_03121_ALIQUOTA_COFINS = Column(Numeric(14,2))    
    PGDASD_03121_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03121_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03121_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03121_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03121_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03121_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03121_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03121_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03121_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03121_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03121_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03121_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03121_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03121_ALIQUOTA_PIS    = Column(Numeric(14,3))
    PGDASD_03121_VALOR_PIS       = Column(Numeric(14,3))
    
    
    def setPgdasd_03121(self, line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03120, id_03121):  
                
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        self.PGDASD_03120_ID              = pgdasd_03120.PGDASD_03120_ID
         
        self.PGDASD_03121_ID              = id_03121                  
        self.PGDASD_03121_ALIQAPUR        = line[1]
        self.PGDASD_03121_ALIQUOTA_COFINS = line[2]
        self.PGDASD_03121_VALOR_COFINS    = line[3]
        self.PGDASD_03121_ALIQUOTA_CSLL   = line[4]
        self.PGDASD_03121_VALOR_CSLL      = line[5]
        self.PGDASD_03121_ALIQUOTA_ICMS   = line[6]
        self.PGDASD_03121_VALOR_ICMS      = line[7]
        self.PGDASD_03121_ALIQUOTA_INSS   = line[8]
        self.PGDASD_03121_VALOR_INSS      = line[9]
        self.PGDASD_03121_ALIQUOTA_IPI    = line[10]
        self.PGDASD_03121_VALOR_IPI       = line[11]
        self.PGDASD_03121_ALIQUOTA_IRPJ   = line[12]
        self.PGDASD_03121_VALOR_IRPJ      = line[13]
        self.PGDASD_03121_ALIQUOTA_ISS    = line[14]
        self.PGDASD_03121_VALOR_ISS       = line[15]
        self.PGDASD_03121_ALIQUOTA_PIS    = line[16]
        self.PGDASD_03121_VALOR_PIS       = line[17]
        
        
class Pgdasd_03122(Base):
    __tablename__  = 'pgdasd_03122'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03120_ID              = Column(Integer, ForeignKey('pgdasd_03120.PGDASD_03120_ID'))
    PGDASD_03122_ID              = Column(Integer, primary_key = True)
    PGDASD_03122_ALIQAPUR        = Column(Numeric(14,2))    
    PGDASD_03122_ALIQUOTA_COFINS = Column(Numeric(14,2))    
    PGDASD_03122_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03122_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03122_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03122_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03122_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03122_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03122_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03122_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03122_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03122_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03122_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03122_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03122_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03122_ALIQUOTA_PIS    = Column(Numeric(14,3))
    PGDASD_03122_VALOR_PIS       = Column(Numeric(14,3))    
    
    def setPgdasd_03122(self, line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03120, id_03122):    
        
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        self.PGDASD_03120_ID              = pgdasd_03120.PGDASD_03120_ID
        
        self.PGDASD_03122_ID              = id_03122                 
        self.PGDASD_03122_ALIQAPUR        = line[1]
        self.PGDASD_03122_ALIQUOTA_COFINS = line[2]
        self.PGDASD_03122_VALOR_COFINS    = line[3]
        self.PGDASD_03122_ALIQUOTA_CSLL   = line[4]
        self.PGDASD_03122_VALOR_CSLL      = line[5]
        self.PGDASD_03122_ALIQUOTA_ICMS   = line[6]
        self.PGDASD_03122_VALOR_ICMS      = line[7]
        self.PGDASD_03122_ALIQUOTA_INSS   = line[8]
        self.PGDASD_03122_VALOR_INSS      = line[9]
        self.PGDASD_03122_ALIQUOTA_IPI    = line[10]
        self.PGDASD_03122_VALOR_IPI       = line[11]
        self.PGDASD_03122_ALIQUOTA_IRPJ   = line[12]
        self.PGDASD_03122_VALOR_IRPJ      = line[13]
        self.PGDASD_03122_ALIQUOTA_ISS    = line[14]
        self.PGDASD_03122_VALOR_ISS       = line[15]
        self.PGDASD_03122_ALIQUOTA_PIS    = line[16]
        self.PGDASD_03122_VALOR_PIS       = line[17]
    
    
class Pgdasd_03130(Base):
    __tablename__  = 'pgdasd_03130'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03130_ID              = Column(Integer, primary_key = True)
    PGDASD_03130_ALIQAPUR        = Column(Numeric(14,2))
    PGDASD_03130_ALIQUOTA_COFINS = Column(Numeric(14,3))
    PGDASD_03130_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03130_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03130_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03130_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03130_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03130_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03130_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03130_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03130_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03130_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03130_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03130_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03130_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03130_ALIQUOTA_PIS    = Column(Numeric(14,3))
    PGDASD_03130_VALOR_PIS       = Column(Numeric(14,3))
            
    
    def setPgdasd_03130(self, line, pgdasd, pgdasd_03000, pgdasd_03100, id_03130):    
                
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        
        self.PGDASD_03130_ID              = id_03130                 
        self.PGDASD_03130_ALIQAPUR        = line[1]
        self.PGDASD_03130_ALIQUOTA_COFINS = line[2]
        self.PGDASD_03130_VALOR_COFINS    = line[3]
        self.PGDASD_03130_ALIQUOTA_CSLL   = line[4]
        self.PGDASD_03130_VALOR_CSLL      = line[5]
        self.PGDASD_03130_ALIQUOTA_ICMS   = line[6]
        self.PGDASD_03130_VALOR_ICMS      = line[7]
        self.PGDASD_03130_ALIQUOTA_INSS   = line[8]
        self.PGDASD_03130_VALOR_INSS      = line[9]
        self.PGDASD_03130_ALIQUOTA_IPI    = line[10]
        self.PGDASD_03130_VALOR_IPI       = line[11]
        self.PGDASD_03130_ALIQUOTA_IRPJ   = line[12]
        self.PGDASD_03130_VALOR_IRPJ      = line[13]
        self.PGDASD_03130_ALIQUOTA_ISS    = line[14]
        self.PGDASD_03130_VALOR_ISS       = line[15]
        self.PGDASD_03130_ALIQUOTA_PIS    = line[16]
        self.PGDASD_03130_VALOR_PIS       = line[17]         
                
        return self

class Pgdasd_03131(Base):
    __tablename__  = 'pgdasd_03131'
    __table_args__ = SCHEMA
        
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03130_ID              = Column(Integer, ForeignKey('pgdasd_03130.PGDASD_03130_ID'))
    PGDASD_03131_ID              = Column(Integer, primary_key = True)
    PGDASD_03131_ALIQAPUR        = Column(Numeric(14,2))    
    PGDASD_03131_ALIQUOTA_COFINS = Column(Numeric(14,2))    
    PGDASD_03131_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03131_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03131_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03131_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03131_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03131_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03131_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03131_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03131_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03131_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03131_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03131_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03131_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03131_ALIQUOTA_PIS    = Column(Numeric(14,3))
    PGDASD_03131_VALOR_PIS       = Column(Numeric(14,3))
    
    
    def setPgdasd_03131(self, line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03130, id_03131):    
                
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        self.PGDASD_03130_ID              = pgdasd_03130.PGDASD_03130_ID
           
        self.PGDASD_03131_ID              = id_03131              
        self.PGDASD_03131_ALIQAPUR        = line[1]
        self.PGDASD_03131_ALIQUOTA_COFINS = line[2]
        self.PGDASD_03131_VALOR_COFINS    = line[3]
        self.PGDASD_03131_ALIQUOTA_CSLL   = line[4]
        self.PGDASD_03131_VALOR_CSLL      = line[5]
        self.PGDASD_03131_ALIQUOTA_ICMS   = line[6]
        self.PGDASD_03131_VALOR_ICMS      = line[7]
        self.PGDASD_03131_ALIQUOTA_INSS   = line[8]
        self.PGDASD_03131_VALOR_INSS      = line[9]
        self.PGDASD_03131_ALIQUOTA_IPI    = line[10]
        self.PGDASD_03131_VALOR_IPI       = line[11]
        self.PGDASD_03131_ALIQUOTA_IRPJ   = line[12]
        self.PGDASD_03131_VALOR_IRPJ      = line[13]
        self.PGDASD_03131_ALIQUOTA_ISS    = line[14]
        self.PGDASD_03131_VALOR_ISS       = line[15]
        self.PGDASD_03131_ALIQUOTA_PIS    = line[16]
        self.PGDASD_03131_VALOR_PIS       = line[17]        

class Pgdasd_03132(Base):
    __tablename__  = 'pgdasd_03132'
    __table_args__ = SCHEMA
    
    
    PGDASD_00000_ID              =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03000_CNPJ              = Column(String(14), ForeignKey('pgdasd_03000.PGDASD_03000_CNPJ'))    
    PGDASD_03100_TIPO            = Column(String(2), ForeignKey('pgdasd_03100.PGDASD_03100_TIPO'))
    PGDASD_03130_ID              = Column(Integer, ForeignKey('pgdasd_03130.PGDASD_03130_ID'))
    PGDASD_03132_ID              = Column(Integer, primary_key = True)
    PGDASD_03132_ALIQAPUR        = Column(Numeric(14,2))    
    PGDASD_03132_ALIQUOTA_COFINS = Column(Numeric(14,2))    
    PGDASD_03132_VALOR_COFINS    = Column(Numeric(14,3))
    PGDASD_03132_ALIQUOTA_CSLL   = Column(Numeric(14,3))
    PGDASD_03132_VALOR_CSLL      = Column(Numeric(14,3))
    PGDASD_03132_ALIQUOTA_ICMS   = Column(Numeric(14,3))
    PGDASD_03132_VALOR_ICMS      = Column(Numeric(14,3))
    PGDASD_03132_ALIQUOTA_INSS   = Column(Numeric(14,3))
    PGDASD_03132_VALOR_INSS      = Column(Numeric(14,3))
    PGDASD_03132_ALIQUOTA_IPI    = Column(Numeric(14,3))
    PGDASD_03132_VALOR_IPI       = Column(Numeric(14,3))
    PGDASD_03132_ALIQUOTA_IRPJ   = Column(Numeric(14,3))
    PGDASD_03132_VALOR_IRPJ      = Column(Numeric(14,3))
    PGDASD_03132_ALIQUOTA_ISS    = Column(Numeric(14,3))
    PGDASD_03132_VALOR_ISS       = Column(Numeric(14,3))
    PGDASD_03132_ALIQUOTA_PIS    = Column(Numeric(14,3))
    PGDASD_03132_VALOR_PIS       = Column(Numeric(14,3))
    
    
    def setPgdasd_03132(self, line, pgdasd, pgdasd_03000, pgdasd_03100, pgdasd_03130, id_03132):  
        
        self.PGDASD_00000_ID              = pgdasd.PGDASD_00000_ID
        self.PGDASD_03000_CNPJ              = pgdasd_03000.PGDASD_03000_CNPJ 
        self.PGDASD_03100_TIPO            = pgdasd_03100.PGDASD_03100_TIPO
        self.PGDASD_03130_ID              = pgdasd_03130.PGDASD_03130_ID
        
        self.PGDASD_03132_ID              = id_03132                   
        self.PGDASD_03132_ALIQAPUR        = line[1]
        self.PGDASD_03132_ALIQUOTA_COFINS = line[2]
        self.PGDASD_03132_VALOR_COFINS    = line[3]
        self.PGDASD_03132_ALIQUOTA_CSLL   = line[4]
        self.PGDASD_03132_VALOR_CSLL      = line[5]
        self.PGDASD_03132_ALIQUOTA_ICMS   = line[6]
        self.PGDASD_03132_VALOR_ICMS      = line[7]
        self.PGDASD_03132_ALIQUOTA_INSS   = line[8]
        self.PGDASD_03132_VALOR_INSS      = line[9]
        self.PGDASD_03132_ALIQUOTA_IPI    = line[10]
        self.PGDASD_03132_VALOR_IPI       = line[11]
        self.PGDASD_03132_ALIQUOTA_IRPJ   = line[12]
        self.PGDASD_03132_VALOR_IRPJ      = line[13]
        self.PGDASD_03132_ALIQUOTA_ISS    = line[14]
        self.PGDASD_03132_VALOR_ISS       = line[15]
        self.PGDASD_03132_ALIQUOTA_PIS    = line[16]
        self.PGDASD_03132_VALOR_PIS       = line[17]        
                

class Pgdasd_03500(Base):
    __tablename__  = 'pgdasd_03500'
    __table_args__ = SCHEMA
    
    PGDASD_00000_ID         =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_03500_FSSN_PA    = Column(String(6), primary_key = True)
    PGDASD_03500_FSSN_VALOR = Column(Numeric(14,2))
            
    
    def setPgdasd_03500(self, line, pgdasd):                        
        self.PGDASD_00000_ID         = pgdasd.PGDASD_00000_ID
        self.PGDASD_03500_FSSN_PA    = line[1]
        self.PGDASD_03500_FSSN_VALOR = line[2]
                                     
        return self

class Pgdasd_04000(Base):
    __tablename__  = 'pgdasd_04000'
    __table_args__ = SCHEMA
        
    PGDASD_00000_ID            =  Column(Integer, ForeignKey('pgdasd.PGDASD_00000_ID'))
    PGDASD_04000_ID            = Column(Integer, primary_key = True)
    PGDASD_04000_CODRECP       = Column(String(4))
    PGDASD_04000_VALORPRINC    = Column(Numeric(14,2))
    PGDASD_04000_CODRECM       = Column(String(4))
    PGDASD_04000_VALORM        = Column(Numeric(14,2))
    PGDASD_04000_CODRECJ       = Column(String(4))
    PGDASD_04000_VALORJ        = Column(Numeric(14,2))
    PGDASD_04000_UF            = Column(String(2))
    PGDASD_04000_CODMUNIC      = Column(String(4))
            
    
    def setPgdasd_04000(self, line, pgdasd, id_04000):   
          
        self.PGDASD_00000_ID         = pgdasd.PGDASD_00000_ID         
        self.PGDASD_04000_ID         = id_04000                 
        self.PGDASD_04000_CODRECP    = line[1]
        self.PGDASD_04000_VALORPRINC = line[2]
        self.PGDASD_04000_CODRECM    = line[3]
        self.PGDASD_04000_VALORM     = line[4]
        self.PGDASD_04000_CODRECJ    = line[5]
        self.PGDASD_04000_VALORJ     = line[6]
        self.PGDASD_04000_UF         = line[7]
        self.PGDASD_04000_CODMUNIC   = line[8]
                                     
        return self
                