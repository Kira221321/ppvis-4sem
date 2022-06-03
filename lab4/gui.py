from model.field import Field
from view.field_gui_interface import MenuScreen, SimulationInterface, ProgramScreenManager
from kivy.lang import Builder
from kivy.app import App
from utility.file_manager import FileManager


Builder.load_file("./view/field_gui_interface.kv")
screen_manager = ProgramScreenManager()


class TheLabApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.screen_manager.add_widget(MenuScreen(name="menu"))
        # self.screen_manager.add_widget(SimulationInterface(
        #     FileManager().load_data_from_template_file(), name="simulation"
        # ))

    def build(self):
        return screen_manager

    def start_simulation(self):
        self.screen_manager.add_widget(SimulationInterface(
            Field(FileManager().load_data_from_template_file()), name="simulation"
        ))

    def exit_program(self):
        raise SystemExit


if __name__ == '__main__':
    TheLabApp().run()
