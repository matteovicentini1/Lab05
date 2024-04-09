class Studente:
    def __init__(self,mat,nom,cogn,cds):
        self.matricola=mat
        self.nome=nom
        self.cognome=cogn
        self.cds=cds

    def __str__(self):
        return f'{self.nome}, {self.cognome} ({self.matricola})'