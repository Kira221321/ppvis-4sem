from kivy.config import Config
from kivy.uix.label import Label


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1224')
Config.set('graphics', 'height', '720')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
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
BLACK = [0, 0, 0, 1]
WHITE = []


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
        self.field = field
        self.file_manager = FileManager()
        self.forest_life_cycle = Cycle(field)
        self.list_of_widgets = []
        self.show_simulation()
        self.control_buttons = GridLayout(cols=2, padding=[650, 600, 0, 0])

        self.coords = BoxLayout()
        self.x_coord = TextInput()
        self.y_coord = TextInput()
        self.creature = TextInput()
        self.add_new_animal = Button(text="Add New Animal", background_color=YELLOW,
                                     on_press=lambda x: self.add_animal(self.x_coord, self.y_coord, self.creature))

        self.coords_delete = BoxLayout()
        self.x_coord_delete = TextInput()
        self.y_coord_delete = TextInput()
        self.delete_animal_button = Button(text="Delete Animal", background_color=YELLOW,
                                    on_press=lambda x: self.delete_animal(
                                        self.x_coord_delete, self.y_coord_delete
                                    ))
        self.coords_delete.add_widget(self.x_coord_delete)
        self.coords_delete.add_widget(self.y_coord_delete)

        self.coords.add_widget(self.x_coord)
        self.coords.add_widget(self.y_coord)
        self.coords.add_widget(self.creature)
        exit_ = Button(text="quit", background_color=YELLOW, on_press=lambda x: self.exit_program())
        continue_simulation = Button(text="continue", background_color=YELLOW, on_press=lambda x: self.continue_simulation())
        self.control_buttons.add_widget(self.add_new_animal)
        self.control_buttons.add_widget(self.coords)
        self.control_buttons.add_widget(self.delete_animal_button)
        self.control_buttons.add_widget(self.coords_delete)

        self.control_buttons.add_widget(exit_)
        self.control_buttons.add_widget(continue_simulation)
        self.add_widget(self.control_buttons)

    def is_type_is_int(self, input_):
        try:
            int(input_.text)
            input_.background_color = GRAY
            return True
        except Exception:
            input_.background_color = RED
            return False

    def delete_animal(self, x_coord, y_coord):
        x_coord_check = self.is_type_is_int(x_coord)
        y_coord_check = self.is_type_is_int(y_coord)
        if x_coord_check and y_coord_check:
            if self.field.are_coords_valid(int(x_coord.text), int(y_coord.text)):
                self.field.environment[int(x_coord.text)][int(y_coord.text)] = None
                self.show_simulation()
            else:
                x_coord.background_color = RED
                y_coord.background_color = RED

    def add_animal(self, x_coord, y_coord, creature):
        x_coord_check = self.is_type_is_int(x_coord)
        y_coord_check = self.is_type_is_int(y_coord)
        creature_check = True if creature.text in [
            "brontosaurus", "stegosaurus", "trex", "plant"
        ] else False
        print(x_coord_check, y_coord_check, creature_check)
        if creature_check:
            if x_coord_check and y_coord_check:
                if self.field.are_coords_valid(int(x_coord.text), int(y_coord.text)):
                    creature.background_color = GRAY
                    self.field.append_creature(creature.text, int(x_coord.text), int(y_coord.text))
                    self.show_simulation()
                else:
                    x_coord.background_color = RED
                    y_coord.background_color = RED
        else:
            creature.background_color = RED

    def show_simulation(self):
        field_grid_layout = GridLayout(cols=15, padding=[100, 100, 100, 200])
        for widget in self.list_of_widgets:
            self.remove_widget(widget)
        self.list_of_widgets.append(field_grid_layout)
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
                    empty = Button(background_color=BLACK)
                    field_grid_layout.add_widget(empty)
        self.add_widget(field_grid_layout)

    def continue_simulation(self):
        for widget in self.list_of_widgets:
            self.remove_widget(widget)
        self.forest_life_cycle.life()
        self.show_simulation()


    def exit_program(self):
        print("aaaa")
        self.file_manager.upload_data(self.field)
        raise SystemExit


screen_manager = ScreenManager()
screen_manager.add_widget(MenuScreen(name="menu"))


def set_screen(screen_name):
    screen_manager.current = screen_name


class TheLabApp(App):

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return screen_manager
