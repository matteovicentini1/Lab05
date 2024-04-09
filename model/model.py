import database.corso_DAO as dc


class Model:
    def __init__(self):
        self.corsi = dc.getesami()
        self.studenti = dc.getstudenti()
        self.accoppiamenti = dc.getcoppie()


    def gets(self,esame):
        cod = esame.split(" ")[-1]
        final=[]
        mat=[]
        for i in self.accoppiamenti:
            if f'({i[1]})' == cod:
                mat.append(int(i[0]))
        for i in self.studenti:
            if int(i.matricola) in mat:
                final.append(i)
        return final

    def searchstudent(self,mat):
        for i in self.studenti:
            if int(i.matricola) == int(mat):
                return i.nome,i.cognome

