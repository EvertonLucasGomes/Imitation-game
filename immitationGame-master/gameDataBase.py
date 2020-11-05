import sqlite3
import os
from random import sample

class bd:

    def __init__(self):

        caminhoAtual = os.getcwd()

        #INCIA CONEXÃO COM O BANDO DE DADOS
        self.conection = sqlite3.connect('{}/dataBase.db'.format(caminhoAtual))
        self.cur = self.conection.cursor()

    def insertSubtitle(self,s):
        #INSERIR DADOS NA TABELA Legendas
        command = f'INSERT INTO Legendas (subtitle) VALUES("{s}")'
        
        self.cur.execute(command)
        self.conection.commit()

    def getSubtitles(self):

        command = 'SELECT * FROM Legendas'

        self.cur.execute(command)
        legendas = self.cur.fetchall()

        #RETORNA AS TUPLAS DE DADOS
        return legendas

a = bd()
#INSERI OS DADOS NO BANCO DE DADOS
#a.insertSubtitle('Era uma vez')
#a.insertSubtitle('End Game')

#RETORNA UMA LISTA DE DADOS
#print(a.getSubtitles())