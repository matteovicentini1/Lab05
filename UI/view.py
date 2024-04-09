import flet as ft
import database.corso_DAO as db

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self.txt_name = ft.Dropdown(label="Corso",width=500,hint_text="Inserire un corso")
        self.fillcorso()
        self.btn_hello = ft.ElevatedButton(text="Cerca esame", on_click=self._controller.handle_hello)

        row1 = ft.Row([self.txt_name, self.btn_hello],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.matricola=ft.TextField(label='Matricola')
        self.nome=ft.TextField(label='Nome',read_only=True)
        self.cognome=ft.TextField(label='Cognome',read_only=True)

        r2 = ft.Row([self.matricola,self.nome,self.cognome],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(r2)

        self.btncercast= ft.ElevatedButton(text='Cerca Studente',on_click=self._controller.cercastudente)
        self.btncercacors = ft.ElevatedButton(text='Cerca Corso',on_click=self._controller.cercacorso)
        self.btniscrivi = ft.ElevatedButton(text='Iscrivi',on_click=self._controller.iscrivi)

        r3 = ft.Row([self.btncercast,self.btncercacors, self.btniscrivi],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(r3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def fillcorso(self):
        for i in db.getesami():
            self.txt_name.options.append(ft.dropdown.Option(i))

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
