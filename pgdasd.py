#-*- encoding:utf-8 -*-
'''
Created on 11/04/2013

@author: Frederico da Silva Santos
'''

class Pgdasd():
    '''
    Identificação do contribuinte e dados da apuração.
    '''

    def __init__(self):
        # campo 00000
        self.Pgdasd_00000_ID_Declaracao = ""
        self.Pgdasd_00000_Num_Recibo = ""
        self.Pgdasd_00000_Num_Autenticacao = "" 
        self.Pgdasd_00000_Dt_Transmissao = ""
        self.Pgdasd_00000_Versao = ""
        self.Pgdasd_00000_Cnpjmatriz = ""
        self.Pgdasd_00000_Nome = ""
        self.Pgdasd_00000_Cod_TOM = ""
        self.Pgdasd_00000_Optante = ""
        self.Pgdasd_00000_Abertura= ""
        self.Pgdasd_00000_PA = ""
        self.Pgdasd_00000_Rpa = 0.0
        self.Pgdasd_00000_Razao = 0.000
        self.Pgdasd_00000_IM = 0.0
        self.Pgdasd_00000_Operacao = ""
        self.Pgdasd_00000_Regime = ""
        self.Pgdasd_00000_RpaC = 0.0
        self.Pgdasd_00000_Rpa_Int = 0.0         
        self.Pgdasd_00000_Rpa_Ext = 0.0
        self.Pgdasd_ultimo02000 = 0.0
        self.Pgdasd_ultimo04000 = 0.0
                
        # campo 01000
        self.Pgdasd_01000 = Pgdasd_01000()
        
        # campo 01500
        self.Pgdasd_01500 = []        
        
        # campo 01501
        self.Pgdasd_01501 = []
        
        # campo 01502
        self.Pgdasd_01502 = []
        
        # campo 02000
        self.Pgdasd_02000 = Pgdasd_02000()
        
        # campo 03000
        self.Pgdasd_03000 = []
        
        self.Pgdasd_03100 = []
                    
        self.Pgdasd_03110 = []        
        self.Pgdasd_03111 = Pgdasd_03111()        
        self.Pgdasd_03112 = []        
        
        self.Pgdasd_03120 = []
        self.Pgdasd_03121 = []
        self.Pgdasd_03122 = []
        
        self.Pgdasd_03130 = []
        self.Pgdasd_03131 = []
        self.Pgdasd_03132 = []
               
        # campo 03500
        self.Pgdasd_03500 = Pgdasd_03500()
        
        # campo 04000
        self.Pgdasd_04000 = Pgdasd_04000()
        
    def setPgdasd_00000(self, line):
        self.Pgdasd_00000_ID_Declaracao    = line[1]
        self.Pgdasd_00000_Num_Recibo       = line[2]
        self.Pgdasd_00000_Num_Autenticacao = line[3]
        self.Pgdasd_00000_Dt_Transmissao   = line[4]
        self.Pgdasd_00000_Versao           = line[5]
        self.Pgdasd_00000_Cnpjmatriz       = line[6]
        self.Pgdasd_00000_Nome             = line[7]
        self.Pgdasd_00000_Cod_TOM          = line[8]
        self.Pgdasd_00000_Optante          = line[9]
        self.Pgdasd_00000_Abertura         = line[10]
        self.Pgdasd_00000_PA               = line[11]
        self.Pgdasd_00000_Rpa              = line[12]
        self.Pgdasd_00000_Razao            = line[13]
        self.Pgdasd_00000_IM               = line[14]
        self.Pgdasd_00000_Operacao         = line[15]
        self.Pgdasd_00000_Regime           = line[16]
        if line[17] == '':
            self.Pgdasd_00000_RpaC = 0.0
        else:    
            self.Pgdasd_00000_RpaC         = line[17]
        self.Pgdasd_00000_Rpa_Int          = line[18]
        self.Pgdasd_00000_Rpa_Ext          = line[19]        
        return self    
    
class Pgdasd_01000():
    '''
    Informações do valor apurado pelo cálculo.
    '''
    def __init__(self):
        self.Nrpagto   = ""
        self.Princ     = 0.0
        self.Multa     = 0.0
        self.Juros     = 0.0
        self.Tdevido   = 0.0
        self.Dtvenc    = ""
        self.Dtvalcalc = ""
        self.Vdas      = 0.0
        
    def setPgdasd_01000(self, line):
        self.Nrpagto   = line[1]
        self.Princ     = line[2]
        self.Multa     = line[3]
        self.Juros     = line[4]
        self.Tdevido   = line[5]
        self.Dtvenc    = line[6]
        self.Dtvalcalc = line[7]
        self.Vdas      = line[8]        
        return self
    
class Pgdasd_01500():
    '''
    Informações de receitas brutas de períodos anteriores à opção.
    '''
    def __init__(self):
        self.rbsn_PA    = ""
        self.rbsn_valor = 0.0        
        
    def setPgdasd_01500(self, line):
        self.rbsn_PA    = line[1]
        self.rbsn_valor = line[2]        
        return self
    
class Pgdasd_01501():
    '''
    Informações de receitas brutas de períodos anteriores à opção no mercado interno.
    0 a 23 ocorrências - Uma ocorrência por linha
    '''
    def __init__(self):
        self.rbsn_PA    = ""
        self.rbsn_valor = 0.0        
        
    def setPgdasd_01501(self, line):
        self.rbsn_PA    = line[1]
        self.rbsn_valor = line[2]        
        return self

class Pgdasd_01502():
    '''
    Informações de receitas brutas de períodos anteriores à opção no mercado externo.
    0 a 23 ocorrências - Uma ocorrência por linha
    '''
    def __init__(self):
        self.Rbsn_Ext_PA    = ""
        self.Rbsn_Ext_valor = 0.0        
        
    def setPgdasd_01502(self, line):
        self.Rbsn_Ext_PA    = line[1]
        self.Rbsn_Ext_valor = line[2]        
        return self

class Pgdasd_02000():
    '''
    Receitas brutas de períodos anteriores, valor original e tributos fixos.
    1 ocorrência
    '''
    def __init__(self):
        self.Id     = 0
        self.rbt12  = 0.0    
        self.Rbtaa  = 0.0
        self.Rba    = 0.0 
        self.rbt12o = 0.0
        self.Rbtaao = 0.0
        self.ICMS   = 0.0
        self.ISS    = 0.0
        self.Rbtaa_Int = 0.0
        self.Rbtaa_Into = 0.0    
        self.Rbtaa_Ext = 0.0
        self.Rbtaa_Exto = 0.0        
        
    def setPgdasd_02000(self, line):
        #self.Id         = line[1]
        self.rbt12      = line[1]    
        self.Rbtaa      = line[2]
        self.Rba        = line[3]
        self.rbt12o     = line[4]
        self.Rbtaao     = line[5]
        if line[6] == '':
            self.ICMS   = 0.00
        else:
            self.ICMS       = line[6]
        if line[7] == '':
            self.ISS    = 0.00
        else:
            self.ISS    = line[7]
        self.Rbtaa_Int  = line[8]
        self.Rbtaa_Into = line[9]   
        self.Rbtaa_Ext  = line[10] 
        self.Rbtaa_Exto = line[11]        
        return self

class Pgdasd_03000():
    '''
    Informações de cada estabelecimento filial.
    Ocorrência - N:1 – de 1 (apenas a matriz) até o número máximo de estabelecimento (matriz mais as filiais)
    '''
    def __init__(self):
        self.CNPJ              = ""
        self.Uf                = ""    
        self.Cod_TOM           = ""
        self.Vltotal           = 0.0 
        self.IME               = 0.0
        self.Limite            = 0.0
        self.LimUltrapassadoPA = ""
        self.prex1             = 0.0        
        self.prex2             = 0.0
        self.Pgdasd_03100      = []
                
        
    def setPgdasd_03000(self, line):        
        self.CNPJ              = line[1]    
        self.Uf                = line[2]
        self.Cod_TOM           = line[3]
        self.Vltotal           = line[4]
        self.IME               = line[5]
        self.Limite            = line[6]
        self.LimUltrapassadoPA = line[7]
        if line[8] == "":
            self.prex1 = 0.00
        else:
            self.prex1         = line[8]
        if line[9] == "":
            self.prex2 = 0.00
        else:
            self.prex2         = line[9]
                           
        return self
    
class Pgdasd_03100():
    '''
    Informações de cada atividade selecionada para cada estabelecimento.
    Ocorrência - N:1 – de 0 (quando nenhum dado é informado para a filial) até 24.
    '''
    def __init__(self):
        self.Tipo    = ""
        self.Vltotal = 0.0    
        self.Pgdasd_03110 = Pgdasd_03110()
        self.Pgdasd_03120 = Pgdasd_03120()
        self.Pgdasd_03130 = Pgdasd_03130()
        #self.Pgdasd_Ultimo03110             = 0
        #self.Pgdasd_Ultimo03111             = 0 
        #self.Pgdasd_Ultimo03112             = 0
                
        
    def setPgdasd_03100(self, line):        
        self.Tipo    = line[1]    
        self.Vltotal = line[2]                       
        return self
    
class Pgdasd_03110():
    '''
    Informações detalhadas do valor da receita por atividade com percentual (faixa A).
    Ocorrência - N:1
    '''
    def __init__(self):
        self.Id              = 0
        self.UF              = ""
        self.Cod_TOM         = ""    
        self.Valor           = 0.0
        self.COFINS          = "" 
        self.CSLL            = ""
        self.ICMS            = ""
        self.INSS            = ""
        self.IPI             = ""
        self.IRPJ            = ""
        self.ISS             = ""
        self.PIS             = ""
        self.Aliqapur        = 0.0
        self.Vlimposto       = 0.0
        self.Aliquota_COFINS = 0.0
        self.Valor_COFINS    = 0.0
        self.Aliquota_CSLL   = 0.0
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0        
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0
        self.Diferenca       = 0.0
        self.Maiortributo    = 0.0
        self.Pgdasd_03111 = Pgdasd_03111()
        self.Pgdasd_03112 = Pgdasd_03112()        
        #self.Pgdasd_Ultimo03111    = 0.0
        #self.Pgdasd_Ultimo03112    = 0.0
                
        
    def setPgdasd_03110(self, line):        
        self.UF              = line[1]
        self.Cod_TOM         = line[2]    
        self.Valor           = line[3]
        self.COFINS          = line[4]
        self.CSLL            = line[5]
        self.ICMS            = line[6]
        self.INSS            = line[7]
        self.IPI             = line[8]
        self.IRPJ            = line[9]
        self.ISS             = line[10]
        self.PIS             = line[11]
        self.Aliqapur        = line[12]
        self.Vlimposto       = line[13]
        self.Aliquota_COFINS = line[14]
        self.Valor_COFINS    = line[15]
        self.Aliquota_CSLL   = line[16]
        self.Valor_CSLL      = line[17]
        self.Aliquota_ICMS   = line[18]
        self.Valor_ICMS      = line[19]
        self.Aliquota_INSS   = line[20]
        self.Valor_INSS      = line[21]
        self.Aliquota_IPI    = line[22]        
        self.Valor_IPI       = line[23]
        self.Aliquota_IRPJ   = line[24]
        self.Valor_IRPJ      = line[25]
        self.Aliquota_ISS    = line[26]
        self.Valor_ISS       = line[27]
        self.Aliquota_PIS    = line[28]
        self.Valor_PIS       = line[29]
        self.Diferenca       = line[30]
        self.Maiortributo    = line[31]                   
        return self
    
class Pgdasd_03111():
    '''
    Informação do valor de receita com isenção (faixa A).        
    Ocorrência - 1:1 – pode não ocorrer
    '''
    def __init__(self):
        self.Id              = 0
        self.Aliqapur        = 0.0
        self.Vlimposto       = 0.0    
        self.Aliquota_COFINS = 0.0
        self.Valor_COFINS    = 0.0
        self.Aliquota_CSLL   = 0.0
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0
        self.Diferenca       = 0.0
        self.Maiortributo    = 0.0        
                
        
    def setPgdasd_03111(self, line):        
        self.Aliqapur        = line[1]
        self.Vlimposto       = line[2]    
        self.Aliquota_COFINS = line[3]
        self.Valor_COFINS    = line[4]
        self.Aliquota_CSLL   = line[5]
        self.Valor_CSLL      = line[6]
        self.Aliquota_ICMS   = line[7]
        self.Valor_ICMS      = line[8]
        self.Aliquota_INSS   = line[9]
        self.Valor_INSS      = line[10]
        self.Aliquota_IPI    = line[11]
        self.Valor_IPI       = line[12]
        self.Aliquota_IRPJ   = line[13]
        self.Valor_IRPJ      = line[14]
        self.Aliquota_ISS    = line[15]
        self.Valor_ISS       = line[16]
        self.Aliquota_PIS    = line[17]
        self.Valor_PIS       = line[18]
        self.Diferenca       = line[19]
        self.Maiortributo    = line[20]
        return self

class Pgdasd_03112():
    '''
    Informações detalhadas do valor da receita por atividade com percentual (faixa A).        
    Ocorrência - N:1 – pode não ocorrer
    '''
    def __init__(self):
        self.Id              = 0
        self.Valor           = 0.0
        self.Red             = 0.0    
        self.Aliqapur        = 0.0
        self.Vlimposto       = 0.0
        self.Aliquota_COFINS = 0.0
        self.Valor_COFINS    = 0.0
        self.Aliquota_CSLL   = 0.0
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0        
        self.Diferenca       = 0.0
        self.Maiortributo    = 0.0
                
        
    def setPgdasd_03112(self, line):    
        self.Id              = 50            
        self.Valor           = line[1]
        self.Red             = line[2]    
        self.Aliqapur        = line[3]
        self.Vlimposto       = line[4]
        self.Aliquota_COFINS = line[5]
        self.Valor_COFINS    = line[6]
        self.Aliquota_CSLL   = line[7]
        self.Valor_CSLL      = line[8]
        self.Aliquota_ICMS   = line[9]
        self.Valor_ICMS      = line[10]
        self.Aliquota_INSS   = line[11]
        self.Valor_INSS      = line[12]
        self.Aliquota_IPI    = line[13]
        self.Valor_IPI       = line[14]
        self.Aliquota_IRPJ   = line[15]
        self.Valor_IRPJ      = line[16]
        self.Aliquota_ISS    = line[17]
        self.Valor_ISS       = line[18]
        self.Aliquota_PIS    = line[19]
        self.Valor_PIS       = line[20]       
        self.Diferenca       = line[21]
        self.Maiortributo    = line[22]
        return self


class Pgdasd_03120():
    '''
    Informações detalhadas do valor da receita por atividade com percentual (faixa B).
    Ocorrência - N:1
    '''
    def __init__(self):
        self.Id              = 0
        self.Aliqapur        = 0.0
        self.Aliquota_COFINS = 0.0    
        self.Valor_COFINS    = 0.0        
        self.Aliquota_CSLL   = 0.0
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0        
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0        
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0    
        self.Pgdasd_03121 = Pgdasd_03121()
        self.Pgdasd_03122 = Pgdasd_03122()    
        #self.Pgdasd_Ultimo03121    = 0.0
        #self.Pgdasd_Ultimo03122       = 0.0
        
                
        
    def setPgdasd_03120(self, line):        
        self.Aliqapur        = line[1]
        self.Aliquota_COFINS = line[2]    
        self.Valor_COFINS    = line[3]        
        self.Aliquota_CSLL   = line[4]
        self.Valor_CSLL      = line[5]
        self.Aliquota_ICMS   = line[6]
        self.Valor_ICMS      = line[7]
        self.Aliquota_INSS   = line[8]        
        self.Valor_INSS      = line[9]
        self.Aliquota_IPI    = line[10]
        self.Valor_IPI       = line[11]
        self.Aliquota_IRPJ   = line[12]
        self.Valor_IRPJ      = line[13]        
        self.Aliquota_ISS    = line[14]
        self.Valor_ISS       = line[15]
        self.Aliquota_PIS    = line[16]
        self.Valor_PIS       = line[17]                   
        return self
    
class Pgdasd_03121():
    '''
    Informação do valor de receita com isenção (faixa B).        
    Ocorrência - 1:1 – pode não ocorrer
    '''
    def __init__(self):
        self.Id              = 0
        self.Aliqapur        = 0.0
        self.Aliquota_COFINS = 0.0    
        self.Valor_COFINS    = 0.0
        self.Aliquota_CSLL   = 0.0
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0            
                
        
    def setPgdasd_03121(self, line):                
        self.Aliqapur        = line[1]
        self.Aliquota_COFINS = line[2]    
        self.Valor_COFINS    = line[3]
        self.Aliquota_CSLL   = line[4]
        self.Valor_CSLL      = line[5]
        self.Aliquota_ICMS   = line[6]
        self.Valor_ICMS      = line[7]
        self.Aliquota_INSS   = line[8]
        self.Valor_INSS      = line[9]
        self.Aliquota_IPI    = line[10]
        self.Valor_IPI       = line[11]
        self.Aliquota_IRPJ   = line[12]
        self.Valor_IRPJ      = line[13]
        self.Aliquota_ISS    = line[14]
        self.Valor_ISS       = line[15]
        self.Aliquota_PIS    = line[16]
        self.Valor_PIS       = line[17]
        return self
    
class Pgdasd_03122():
    '''
    Informação do valor da receita por atividade com percentual (faixa B).     
    Ocorrência - N:1 – pode não ocorre
    '''
    def __init__(self):
        self.Id              = 0
        self.Aliqapur        = 0.0
        self.Aliquota_COFINS = 0.0    
        self.Valor_COFINS    = 0.0
        self.Aliquota_CSLL   = 0.0
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0            
                
        
    def setPgdasd_03122(self, line):                
        self.Aliqapur        = line[1]
        self.Aliquota_COFINS = line[2]    
        self.Valor_COFINS    = line[3]
        self.Aliquota_CSLL   = line[4]
        self.Valor_CSLL      = line[5]
        self.Aliquota_ICMS   = line[6]
        self.Valor_ICMS      = line[7]
        self.Aliquota_INSS   = line[8]
        self.Valor_INSS      = line[9]
        self.Aliquota_IPI    = line[10]
        self.Valor_IPI       = line[11]
        self.Aliquota_IRPJ   = line[12]
        self.Valor_IRPJ      = line[13]
        self.Aliquota_ISS    = line[14]
        self.Valor_ISS       = line[15]
        self.Aliquota_PIS    = line[16]
        self.Valor_PIS       = line[17]
        return self

    
class Pgdasd_03130():
    '''
    Informações detalhadas do valor da receita por atividade com percentual (faixa C).
    Ocorrência - N:1
    '''
    def __init__(self):
        self.Id              = 0
        self.Aliqapur        = 0.0
        self.Aliquota_COFINS = 0.0    
        self.Valor_COFINS    = 0.0
        self.Aliquota_CSLL   = 0.0         
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0        
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0   
        self.Pgdasd_03131 = Pgdasd_03131()
        self.Pgdasd_03132 = Pgdasd_03132()     
        #self.Pgdasd_Ultimo03131    = 0.0
        #self.Pgdasd_Ultimo03132    = 0.0
                
        
    def setPgdasd_03130(self, line):        
        self.Aliqapur        = line[1]
        self.Aliquota_COFINS = line[2]    
        self.Valor_COFINS    = line[3]
        self.Aliquota_CSLL   = line[4]        
        self.Valor_CSLL      = line[5]
        self.Aliquota_ICMS   = line[6]
        self.Valor_ICMS      = line[7]
        self.Aliquota_INSS   = line[8]
        self.Valor_INSS      = line[9]
        self.Aliquota_IPI    = line[10]
        self.Valor_IPI       = line[11]
        self.Aliquota_IRPJ   = line[12]
        self.Valor_IRPJ      = line[13]
        self.Aliquota_ISS    = line[14]
        self.Valor_ISS       = line[15]      
        self.Aliquota_PIS    = line[16]
        self.Valor_PIS       = line[17]                      
        return self
    
class Pgdasd_03131():
    '''
    Informação do valor de receita com isenção (faixa C).        
    Ocorrência - 1:1 – pode não ocorrer
    '''
    def __init__(self):
        self.Id              = 0
        self.Aliqapur        = 0.0
        self.Aliquota_COFINS = 0.0    
        self.Valor_COFINS    = 0.0
        self.Aliquota_CSLL   = 0.0
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0            
                
        
    def setPgdasd_03131(self, line):                
        self.Aliqapur        = line[1]
        self.Aliquota_COFINS = line[2]    
        self.Valor_COFINS    = line[3]
        self.Aliquota_CSLL   = line[4]
        self.Valor_CSLL      = line[5]
        self.Aliquota_ICMS   = line[6]
        self.Valor_ICMS      = line[7]
        self.Aliquota_INSS   = line[8]
        self.Valor_INSS      = line[9]
        self.Aliquota_IPI    = line[10]
        self.Valor_IPI       = line[11]
        self.Aliquota_IRPJ   = line[12]
        self.Valor_IRPJ      = line[13]
        self.Aliquota_ISS    = line[14]
        self.Valor_ISS       = line[15]
        self.Aliquota_PIS    = line[16]
        self.Valor_PIS       = line[17]
        return self
    
class Pgdasd_03132():
    '''
    Informação do valor da receita por atividade com percentual (faixa C).        
    Ocorrência - 1:1 – pode não ocorrer
    '''
    def __init__(self):
        self.Id              = 0
        self.Aliqapur        = 0.0
        self.Aliquota_COFINS = 0.0    
        self.Valor_COFINS    = 0.0
        self.Aliquota_CSLL   = 0.0
        self.Valor_CSLL      = 0.0
        self.Aliquota_ICMS   = 0.0
        self.Valor_ICMS      = 0.0
        self.Aliquota_INSS   = 0.0
        self.Valor_INSS      = 0.0
        self.Aliquota_IPI    = 0.0
        self.Valor_IPI       = 0.0
        self.Aliquota_IRPJ   = 0.0
        self.Valor_IRPJ      = 0.0
        self.Aliquota_ISS    = 0.0
        self.Valor_ISS       = 0.0
        self.Aliquota_PIS    = 0.0
        self.Valor_PIS       = 0.0            
                
        
    def setPgdasd_03132(self, line):                
        self.Aliqapur        = line[1]
        self.Aliquota_COFINS = line[2]    
        self.Valor_COFINS    = line[3]
        self.Aliquota_CSLL   = line[4]
        self.Valor_CSLL      = line[5]
        self.Aliquota_ICMS   = line[6]
        self.Valor_ICMS      = line[7]
        self.Aliquota_INSS   = line[8]
        self.Valor_INSS      = line[9]
        self.Aliquota_IPI    = line[10]
        self.Valor_IPI       = line[11]
        self.Aliquota_IRPJ   = line[12]
        self.Valor_IRPJ      = line[13]
        self.Aliquota_ISS    = line[14]
        self.Valor_ISS       = line[15]
        self.Aliquota_PIS    = line[16]
        self.Valor_PIS       = line[17]
        return self

class Pgdasd_03500():
    '''
    Informações referentes à folha de salários.
    Ocorrência – zero a 12 ocorrências, uma por linha.
    '''
    def __init__(self):
        self.fssn_PA    = ""        
        self.fssn_valor = 0.0         
                
        
    def setPgdasd_03500(self, line):        
        self.fssn_PA    = line[1]        
        self.fssn_valor = line[2]               
        return self
    
class Pgdasd_04000():
    '''
    Informações do perfil
    Ocorrência – N:1
    '''
    def __init__(self):
        self.Id         = 0        
        self.codrecp    = ""
        self.valorprinc = 0.0
        self.codrecm    = ""
        self.valorm     = 0.0
        self.codrecj    = ""
        self.valorj     = 0.0
        self.uf         = ""
        self.codmunic   = ""         
                
        
    def setPgdasd_04000(self, line):        
        self.codrecp    = line[1]
        self.valorprinc = line[2]
        self.codrecm    = line[3]
        self.valorm     = line[4]
        self.codrecj    = line[5]
        self.valorj     = line[6]
        self.uf         = line[7]
        self.codmunic   = line[8]            
        return self