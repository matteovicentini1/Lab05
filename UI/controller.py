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
                n,c = self._model.searchstudent(matricola)
                if n != None and c != None:
                    self._view.nome.value=n
                    self._view.cognome.value=c
                else:
                    self._view.txt_result.controls.append(ft.Text(f'Matricola Inesistente', color='red',size=15))
            self._view.update_page()
        except ValueError:
            self._view.matricola.value = None
            self._view.txt_result.controls.append(ft.Text(f'Inserire un numero', color='red', size=15))
            self._view.update_page()