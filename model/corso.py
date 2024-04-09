class Corso:
    def __init__(self,nome,c,crediti,pd):
        self.nome=nome
        self.codice=c
        self.crediti=crediti
        self.pd=pd


    def __str__(self):
        return f'{self.nome} ({self.codice})'