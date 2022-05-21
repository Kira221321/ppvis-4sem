from kivy.config import Config
from kivy.uix.label import Label


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1524')
Config.set('graphics', 'height', '920')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from utility.file_manager import FileManager
from controller.life_cycle import Cycle
from model.field import Field


RED = [1, 0, 0, 1]
GREEN = [0, 1, 0, 1]
BLUE = [0, 0, 1, 1]
ORANGE = [0, 1, 1, 1]
YELLOW = [1, 1, 0, 1]
GRAY = [1, 1, 1, 1]


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)

        box_layout = BoxLayout(orientation="vertical")
        add_button = Button(text="Previous simulation", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                            on_press=lambda x: self.choice_simulation("previous", add_button), background_color=ORANGE)
        remove_button = Button(text="Simulation from template", font_size=30, size_hint=(.5, 1),
                               pos_hint={"center_x": .5},
                               on_press=lambda x: self.choice_simulation("template", remove_button),
                               background_color=ORANGE)
        exit_button = Button(text="Exit", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                             on_press=lambda x: self.exit_program(), background_color=ORANGE)
        box_layout.add_widget(add_button)
        box_layout.add_widget(remove_button)
        box_layout.add_widget(exit_button)
        self.add_widget(box_layout)


    def choice_simulation(self, simulation_type, choice_button):
        match simulation_type:
            case "previous":
                file_manager = FileManager()
                forest = file_manager.load_data_from_previous_simulation()
                if not forest:
                    choice_button.disabled = True
                    choice_button.text = "No previous simulation"
                    return
            case "template":
                file_manager = FileManager()
                environment = file_manager.load_data_from_template_file()
                forest = Field(environment)
        screen_manager.add_widget(SimulationInterface(forest, name="simulation"))
        set_screen("simulation")

    def exit_program(self):
        raise SystemExit


class SimulationInterface(Screen):
    def __init__(self, field, **kw):
        super(SimulationInterface, self).__init__(**kw)
        self.north_region = GridLayout(cols=3, padding=[300, 0, 300, 600])
        self.field = field
        self.file_manager = FileManager()
        self.forest_life_cycle = Cycle(field)
        self.list_of_widgets = []
        self.show_simulation()
        self.control_buttons = BoxLayout(padding=[650, 800, 0, 0])
        exit_ = Button(text="quit", background_color=YELLOW, on_press=lambda x: self.exit_program())
        continue_simulation = Button(text="continue", background_color=YELLOW, on_press=lambda x: self.continue_simulation())
        self.control_buttons.add_widget(exit_)
        self.control_buttons.add_widget(continue_simulation)
        self.add_widget(self.control_buttons)

    def show_simulation(self):
        field_grid_layout = GridLayout(cols=15, padding=[100, 100, 300, 300])
        creatures = self.field._environment
        for line in creatures:
            for creature in line:
                if creature:
                    match creature._type:
                        case 'trex':
                            trex = Image(source="view/images/trex.jpg")
                            field_grid_layout.add_widget(trex)
                        case 'brontosaurus':
                            brontosaurus = Image(source="view/images/brontosaurus.jpg")
                            field_grid_layout.add_widget(brontosaurus)
                        case 'stegosaurus':
                            stegosaurus = Image(source="view/images/stegosaurus.jpg")
                            field_grid_layout.add_widget(stegosaurus)
                        case 'plant':
                            plant = Image(source="view/images/bush.jpg")
                            field_grid_layout.add_widget(plant)
                else:
                    empty = Label()
                    field_grid_layout.add_widget(empty)
        self.add_widget(field_grid_layout)


    def fullness_region(self, cell, left_indent, top_indent, right_indent, bottom_indent):
        cell_grid_layout = GridLayout(cols=3, padding=[left_indent, top_indent, right_indent, bottom_indent])
        self.list_of_widgets.append(cell_grid_layout)
        for creature in cell.creatures:
            if creature:
                match creature.type:
                    case 'bear':
                        bear = Image(source="view/images/bear.png")
                        cell_grid_layout.add_widget(bear)
                    case 'dragon':
                        dragon = Image(source="view/images/dragon.png")
                        cell_grid_layout.add_widget(dragon)
                    case 'rabbit':
                        rabbit = Image(source="view/images/rabbit.png")
                        cell_grid_layout.add_widget(rabbit)
                    case 'boar':
                        boar = Image(source="view/images/boar.png")
                        cell_grid_layout.add_widget(boar)
                    case 'bush':
                        bush = Image(source="view/images/bush.png")
                        cell_grid_layout.add_widget(bush)
                    case 'dragon_egg':
                        dragon_egg = Image(source="view/images/dragon_egg.png")
                        cell_grid_layout.add_widget(dragon_egg)
            else:
                empty = Label()
                cell_grid_layout.add_widget(empty)
        self.add_widget(cell_grid_layout)

    def continue_simulation(self):
        for widget in self.list_of_widgets:
            self.remove_widget(widget)
        self.forest_life_cycle.life()
        self.show_simulation()


    def exit_program(self):
        self.file_manager.upload_data(self.field)
        raise SystemExit


screen_manager = ScreenManager()
screen_manager.add_widget(MenuScreen(name="menu"))


def set_screen(screen_name):
    screen_manager.current = screen_name


class TheLabApp(App):

    def build(self):
        Window.clearcolor = (1, .9, .1, .8)
        return screen_manager
