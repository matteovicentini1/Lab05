import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.studenti = None


    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        self._view.txt_name.value = None
        if name is None or name == "":
            self._view.create_alert("Selezionare un corso")
            return
        else:
            studenti = self._model.gets(name)
            self._view.txt_result.controls.append(ft.Text(f'Ci sono {len(studenti)} al corso:',color='red',size=20))
            for i in studenti:
                self._view.txt_result.controls.append(ft.Text(i))
        self._view.update_page()


    def cercastudente(self,e):
        matricola = self._view.matricola.value
        try:
            int(matricola)
            if matricola is None or matricola == "":
                self._view.create_alert("scrivere una matricola")
                return
            else:
                b,n,c = self._model.searchstudent(matricola)
                if b==True:
                    self._view.nome.value=n
                    self._view.cognome.value=c
                else:
                    self._view.txt_result.controls.append(ft.Text(f'Matricola Inesistente', color='red',size=15))
            self._view.update_page()
        except ValueError:
            self._view.matricola.value = None
            self._view.txt_result.controls.append(ft.Text(f'Inserire una matricola numerica', color='red', size=15))
            self._view.update_page()

    def cercacorso(self,e):
        matricola = self._view.matricola.value
        self._view.matricola.value=None
        try:
            int(matricola)
            b,corsi = self._model.inside(int(matricola))
            if b ==True:
                self._view.txt_result.controls.append(ft.Text(f'Studente con matricola {matricola} presente ed iscritto a tali corsi:'))
                for i in corsi:
                    self._view.txt_result.controls.append(ft.Text(i))
            else:
                self._view.txt_result.controls.append(ft.Text(f'Studente con matricola {matricola} non presente'))
            self._view.update_page()

        except ValueError:
            self._view.matricola.value = None
            self._view.txt_result.controls.append(ft.Text(f'Inserire una matricola numerica', color='red', size=15))
            self._view.update_page()

    def iscrivi(self,e):
        matricola = self._view.matricola.value
        cod = self._view.txt_name.value.split(" ")[-1]
        try:
            b = self._model.controlloesistenza(int(matricola))
            b2 = self._model.controlloacoppiamento(int(matricola))
            if b==True and b2 ==True:
                self._model.put(matricola,cod)
                self._view.txt_result.controls.append(ft.Text(f'Matricola aggiunta al corso', color='red', size=15))
            elif b==True and b2==False:
                self._view.txt_result.controls.append(ft.Text(f'Matricola già appartenente al corso', color='red', size=15))
            elif b == False and b2 == True:
                self._view.txt_result.controls.append(ft.Text(f'Matricola Inesistente', color='red', size=15))
            self._view.update_page()

        except ValueError:
            self._view.matricola.value = None
            self._view.txt_result.controls.append(ft.Text(f'Inserire una matricola numerica', color='red', size=15))
            self._view.update_page()


