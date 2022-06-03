from View.view import ProgramScreenManager, MenuScreen, AddScreen, RemoveScreen, ShowScreen, ChooseFile
from kivy.app import App
from kivy.lang import Builder
import os

from Controller.controller import DataBaseController


print(os.getcwd())


Builder.load_file("./View/view.kv")
screen_manager = ProgramScreenManager()

class TheLabApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.db_controller = DataBaseController()
        self.screen_manager.add_widget(MenuScreen(self.db_controller, './1.xml', name="menu"))
        self.screen_manager.add_widget(AddScreen(self.db_controller, name="add"))
        self.screen_manager.add_widget(RemoveScreen(self.db_controller, name="remove"))
        self.screen_manager.add_widget(ShowScreen(self.db_controller, name="show"))

    def build(self):
        return screen_manager

    def exit_program(self):
        raise SystemExit


if __name__ == '__main__':
    TheLabApp().run()
