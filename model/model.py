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
                return True,i.nome,i.cognome
        return False,'f','f'

    def inside(self,matr):
        mat=[]
        for i in self.accoppiamenti:
            mat.append(int(i[0]))
        if matr in mat:
            corsi=[]
            cod=[]
            for i in self.accoppiamenti:
                if int(i[0])==matr:
                    cod.append(i[1])
            for i in self.corsi:
                if i.codice in cod:
                    corsi.append(i)
            return True, corsi

        else:
            return False,[]

    def controlloesistenza(self,matricola):
        mtot=[]
        for i in self.studenti:
            mtot.append(int(i.matricola))
        if matricola in mtot:
            return True
        else:
            return False

    def controlloacoppiamento(self,matricola):
        mtot = []
        for i in self.accoppiamenti:
            mtot.append(int(i[0]))
        if matricola in mtot:
            return True
        else:
            return False

    def cercacod(self,cod):
        for i in self.corsi:
            if f'({i.codice})' == cod:
                return i

    def cercastudente(self,matricola):
        for i in self.studenti:
            if int(i.matricola)== int(matricola):
                return i


    def put(self,matricola,cod):
        codice = self.cercacod(cod)
        stud = self.cercastudente(matricola)
        dc.putcoppia(stud.matricola,codice.codice)
        self.accoppiamenti.append([stud.matricola,codice.codice])
