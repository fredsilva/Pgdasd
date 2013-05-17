'''
Created on 15/05/2013

@author: 8620016
'''

if __name__ == '__main__':
    '''url = "recebidos/"   
    file = open(url+"file.txt",'r')
    newFile = open(url+"newFile.txt","w")    
    content = file.readlines()
    file.close()
    newFile.writelines(filter(lambda x:x.startswith("03000") and "TO" in x,content))'''
    
    import re

    pat = ('^00000\|\d+\|\d+.*\n'
           '^03000\|TO\|\d+.*\n'
           '^99999\|\d+\|\d+.*\n'
           '|'
           '^AAAAA\|\d+\|\d+.*\n'
           '|'
           '^ZZZZZ\|\d+\|\d+.*')
    rag = re.compile(pat,re.MULTILINE)
    
    with open('recebidos/file.txt','r') as f,\
         open('recebidos/newfile.txt','w') as g:
        g.write(''.join(rag.findall(f.read())))