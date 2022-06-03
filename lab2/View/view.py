from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '720')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import os
import re
import xml.dom.minidom as minidom

from Controller.controller import DataBaseController
from Model.model import Student


RED = [1, 0, 0, 1]
GREEN = [0, 1, 0, 1]
BLUE = [0, 0, 1, 1]
WHITE_BLUE = [0, 1, 1, 1]
GRAY = [1, 1, 1, 1]


class MenuScreen(Screen):
    def __init__(self, db_controller, file, **kw):
        super(MenuScreen, self).__init__(**kw)
        self._controller = db_controller
        self.file = file

    def exit_program(self):
        self._controller.write_data_into_file(self.file)
        raise SystemExit


class AddScreen(Screen):
    def __init__(self, db_controller, **kw):
        super(AddScreen, self).__init__(**kw)

        self._controller = db_controller

    def is_not_empty(self, input_):
        if input_.text == '':
            input_.background_color = RED
            return False
        else:
            input_.background_color = GRAY
            return True

    def is_type_is_int(self, input_):
        try:
            int(input_.text)
            return True
        except Exception:
            input_.background_color = RED
            return False

    def check(self):
        if all((self.is_not_empty(self.name_student_input),
                self.is_not_empty(self.surname_student_input),
                self.is_not_empty(self.patronymic_student_input),
                self.is_not_empty(self.group_input),
                self.is_not_empty(self.sem_1_input),
                self.is_not_empty(self.sem_2_input),
                self.is_not_empty(self.sem_3_input),
                self.is_not_empty(self.sem_4_input),
                self.is_not_empty(self.sem_5_input),
                self.is_not_empty(self.sem_6_input),
                self.is_not_empty(self.sem_7_input),
                self.is_not_empty(self.sem_8_input),
                self.is_not_empty(self.sem_9_input),
                self.is_not_empty(self.sem_10_input),
                self.is_type_is_int(self.sem_1_input),
                self.is_type_is_int(self.sem_2_input),
                self.is_type_is_int(self.sem_3_input),
                self.is_type_is_int(self.sem_4_input),
                self.is_type_is_int(self.sem_5_input),
                self.is_type_is_int(self.sem_6_input),
                self.is_type_is_int(self.sem_7_input),
                self.is_type_is_int(self.sem_8_input),
                self.is_type_is_int(self.sem_9_input),
                self.is_type_is_int(self.sem_10_input))):
            return True

    def create_field(self):
        if self.check():
            student = Student(
                self.name_student_input.text,
                self.surname_student_input.text,
                self.patronymic_student_input.text,
                self.group_input.text,
                self.sem_1_input.text,
                self.sem_2_input.text,
                self.sem_3_input.text,
                self.sem_4_input.text,
                self.sem_5_input.text,
                self.sem_6_input.text,
                self.sem_7_input.text,
                self.sem_8_input.text,
                self.sem_9_input.text,
                self.sem_10_input.text,
            )
            self._controller.add_student(student)
            self.clear_all_fields()
            self.status_of_process.background_color = GREEN
            self.status_of_process.text = 'Completed'
        else:
            self.status_of_process.background_color = RED
            self.status_of_process.text = 'Error!!!'


class RemoveScreen(Screen):
    def __init__(self, db_controller, **kw):
        super(RemoveScreen, self).__init__(**kw)
        self._controller = db_controller
        self.choice = 0

    def set_choice(self, choice, choice_button):
        self.choice = choice
        for button in self.choice_buttons:
            button.background_color = GRAY
        choice_button.background_color = GREEN

    def is_type_is_int(self, input_):
        try:
            int(input_)
            return True
        except Exception:
            return False

    def remove_field(self):
        is_removed = False
        if 0 < self.choice < 5:
            if self.remove_input.text == "":
                self.remove_input.background_color = RED
            else:
                match self.choice:
                    case 1:
                        is_removed = self._controller.delete(
                            "delete_by_student_last_name",
                            student_last_name=self.remove_input.text
                        )
                    case 2:
                        is_removed = self._controller.delete(
                            "delete_by_group", group=self.remove_input.text
                        )
                    case 3:
                        try:
                            student, min_amount_of_work, max_amount_of_work = self.remove_input.text.split()
                            if self.is_type_is_int(min_amount_of_work) and self.is_type_is_int(max_amount_of_work):
                                is_removed = self._controller.delete(
                                    "delete_by_student_and_work_amount",
                                    student=student, min_amount_of_work=min_amount_of_work,
                                    max_amount_of_work=max_amount_of_work
                                )
                        except Exception:
                            self.massage_wrong_input()
                            self.remove_input.background_color = RED
                            return
                    case 4:
                        try:
                            group, min_amount_of_work, max_amount_of_work = self.remove_input.text.split()
                            if self.is_type_is_int(min_amount_of_work) and self.is_type_is_int(max_amount_of_work):
                                is_removed = self._controller.delete_by_group_and_work_amount(
                                    "delete_by_group_and_work_amount",
                                    group=group, min_amount_of_work=min_amount_of_work,
                                    max_amount_of_work=max_amount_of_work
                                )
                        except Exception:
                            self.massage_wrong_input()
                            self.remove_input.background_color = RED
                            return
                if is_removed:
                    self.menu_label.text = f"Remove complete! {is_removed} student was deleted"
                else:
                    self.menu_label.text = "No such records!"
                self.remove_input.background_color = GRAY
        else:
            self.menu_label.text = "Choice way of remove!"

    def massage_wrong_input(self):
        self.menu_label.text = "Invalid input!"

class ShowScreen(Screen):
    fields_on_screens = 5

    def __init__(self, db_controller, **kw):
        super(ShowScreen, self).__init__(**kw)
        self.list_of_screens = []
        self.index_of_screen = 0
        self.choice = 0
        self.present_fields_screen = None
        self._controller = db_controller

    def set_search(self, search, choice_button):
        self.choice = search
        for button in self.search_buttons:
            button.background_color = GRAY
        choice_button.background_color = GREEN

    def is_type_is_int(self, input_):
        try:
            int(input_)
            return True
        except Exception:
            return False

    def search(self):
        if 0 < self.choice < 5:
            match self.choice:
                case 1:
                    student_last_name = self.student_surname_input.text
                    if student_last_name == '':
                        self.student_surname_input.background_color = RED
                    else:
                        self.student_surname_input.background_color = GRAY
                        found_books = self._controller.search("search_by_student_last_name", student_last_name=student_last_name)
                        self.show(found_books)
                        self.clear_search_fields()
                case 2:
                    group = self.group_input.text
                    if self.group_input.text == '':
                        self.group_input.background_color = RED
                    else:
                        self.group_input.background_color = GRAY
                        found_books = self._controller.search("search_by_group", group=group)
                        self.show(found_books)
                        self.clear_search_fields()
                case 3:
                    if self.student_surname_and_work_input.text == '':
                        self.student_surname_and_work_input.background_color = RED
                    else:
                        try:
                            student, min_amount_of_work, max_amount_of_work = self.student_surname_and_work_input.text.split()
                            if self.is_type_is_int(min_amount_of_work) and self.is_type_is_int(max_amount_of_work):
                                self.group_input.background_color = GRAY
                                found_books = self._controller.search(
                                    "search_by_student_and_work_amount",
                                    student=student, min_amount_of_work=int(min_amount_of_work),
                                    max_amount_of_work=int(max_amount_of_work)
                                )
                                self.show(found_books)
                                self.clear_search_fields()
                        except Exception:
                            self.massage_wrong_input()
                case 4:
                    if self.group_and_work_input.text == '':
                        self.group_and_work_input.background_color = RED
                    else:
                        try:
                            group, min_amount_of_work, max_amount_of_work = self.group_and_work_input.text.split()
                            if self.is_type_is_int(min_amount_of_work) and self.is_type_is_int(max_amount_of_work):
                                self.group_input.background_color = GRAY
                                found_books = self._controller.search(
                                    "search_by_group_and_work_amount",
                                    group=group, min_amount_of_work=int(min_amount_of_work),
                                    max_amount_of_work=int(max_amount_of_work)
                                )
                                self.show(found_books)
                                self.clear_search_fields()
                        except Exception:
                            self.massage_wrong_input()
        else:
            if self.present_fields_screen:
                self.remove_widget(self.present_fields_screen)
            self.present_fields_screen = GridLayout(
                cols=5, padding=[0, 360, 0, 80],
                row_force_default=True,
                row_default_height=100)
            not_found = Button(text="Choose variant of searching")
            self.present_fields_screen.add_widget(not_found)
            self.add_widget(self.present_fields_screen)

    def massage_wrong_input(self):
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)
        self.present_fields_screen = GridLayout(
            cols=1, padding=[0, 360, 0, 80],
            row_force_default=True,
            row_default_height=100)
        not_found = Button(text="Invalid input")
        self.present_fields_screen.add_widget(not_found)
        self.add_widget(self.present_fields_screen)

    def show(self, list_of_fields):
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)
        if not list_of_fields:
            self.present_fields_screen = GridLayout(
                cols=1, padding=[0, 360, 0, 80],
                row_force_default=True,
                row_default_height=100)
            not_found = Button(text="Nothing found")
            self.present_fields_screen.add_widget(not_found)
            self.add_widget(self.present_fields_screen)
            return
        self.list_of_screens = []
        self.index_of_screen = 0
        self.number_of_elements_text.text = str(len(list_of_fields))
        if self.amount_of_pages_input.text:
            if self.is_type_is_int(self.amount_of_pages_input.text):
                ShowScreen.fields_on_screens = int(self.amount_of_pages_input.text)
        counter_of_screens = ShowScreen.fields_on_screens
        number_of_screens = 0
        for field in list_of_fields:
            if ShowScreen.fields_on_screens == counter_of_screens:
                counter_of_screens = 0
                student_record = GridLayout(cols=12, padding=[0, 360, 0, 80], row_force_default=True,
                                         row_default_height=(360 - 80) / ShowScreen.fields_on_screens)
                self.list_of_screens.append(student_record)
                number_of_screens += 1
            student = f"{field.student_name} {field.student_last_name} {field.student_patronymic}"
            student_record.add_widget(Button(text=student, size_hint_x=None, width=200, font_size=12))
            student_record.add_widget(Button(text=field.group, size_hint_x=None, width=100, font_size=12))
            student_record.add_widget(Button(text=str(field.sem_1), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_2), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_3), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_4), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_5), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_6), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_7), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_8), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_9), font_size=12))
            student_record.add_widget(Button(text=str(field.sem_10), font_size=12))
            counter_of_screens += 1

        self.present_fields_screen = self.list_of_screens[self.index_of_screen]
        self.number_of_page_text.text = str(self.index_of_screen + 1)
        self.index_of_page_text.text = str(len(self.list_of_screens))
        self.add_widget(self.present_fields_screen)

    def set_present_fields_screen(self, index_of_screen):
        if -1 < index_of_screen < len(self.list_of_screens):
            self.index_of_screen = index_of_screen
            self.remove_widget(self.present_fields_screen)
            self.present_fields_screen = self.list_of_screens[index_of_screen]
            self.add_widget(self.present_fields_screen)
            self.number_of_page_text.text = str(self.index_of_screen + 1)

    def clear_search_fields(self):
        self.student_surname_input.text = ''
        self.group_input.text = ''
        self.student_surname_and_work_input.text = ''
        self.group_and_work_input.text = ''
        self.student_surname_input.background_color = GRAY
        self.group_input.background_color = GRAY
        self.student_surname_and_work_input.background_color = GRAY
        self.group_and_work_input.background_color = GRAY

class ChooseFile(Screen):

    def __init__(self, **kw):
        super(ChooseFile, self).__init__(**kw)
        self.file = ""
        self.lib_was_chosen = False

    def create_file(self, file, create_button):
        self.lib_was_chosen = False
        for button in self.file_buttons:
            button.background_color = GRAY
        pattern = re.compile("\w+.xml")
        if re.match(pattern, file):
            if file not in os.listdir("."):
                create_button.disabled = True
                dom_tree = minidom.Document()
                pass_table = dom_tree.createElement("pass_table")
                dom_tree.appendChild(pass_table)
                dom_tree.writexml(open(file, 'w'),
                                       indent="  ",
                                       addindent="  ",
                                       newl='\n')
                dom_tree.unlink()
                self.lib_was_chosen = True
                self.db_controller = DataBaseController()
                self.db_controller.read_from_file(file)
                self.file = file

                create_button.background_color = GREEN
                create_button.text = "Library selected"
            else:
                create_button.background_color = RED
                create_button.text = "This lib already exists"
        else:
            create_button.background_color = RED
            create_button.text = "Invalid input"

    def input_library(self, file, choice_button):
        self.lib_was_chosen = False
        for button in self.file_buttons:
            button.background_color = GRAY
        if self.file_search_input.text in os.listdir("."):
            self.lib_was_chosen = True
            self.db_controller = DataBaseController(file)
            choice_button.background_color = GREEN
            choice_button.text = "Library selected"
        else:
            choice_button.background_color = RED
            choice_button.text = "No such library"

    def set_library(self, choice_button):
        self.lib_was_chosen = True
        for button in self.file_buttons:
            button.background_color = GRAY
        self.file = "./" + choice_button.text
        self.db_controller = DataBaseController()
        self.db_controller.read_from_file(self.file)
        choice_button.background_color = GREEN

    def create_menu(self):
        if self.lib_was_chosen:
            screen_manager.add_widget(MenuScreen(self.db_controller, self.file, name="menu"))
            screen_manager.add_widget(AddScreen(self.db_controller, name="add"))
            screen_manager.add_widget(RemoveScreen(self.db_controller, name="remove"))
            screen_manager.add_widget(ShowScreen(self.db_controller, name="show"))
            set_screen("menu")


class ProgramScreenManager(ScreenManager):
    def __init__(self) -> None:
        super().__init__()
        self.db_controller = DataBaseController()
        self.db_controller.read_from_file('./1.xml')
        self.add_widget(MenuScreen(self.db_controller, './1.xml', name="menu"))


def set_screen(screen_name):
    screen_manager.current = screen_name
