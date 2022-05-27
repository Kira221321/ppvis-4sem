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

        box_layout = BoxLayout(orientation="vertical")
        menu_label = Label(text="Menu", font_size=30)
        add_button = Button(text="Add", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                            on_press=lambda x: set_screen("add"), background_color=WHITE_BLUE)
        remove_button = Button(text="Delete", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                               on_press=lambda x: set_screen("remove"), background_color=WHITE_BLUE)
        show_button = Button(text="Show", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                             on_press=lambda x: set_screen("show"), background_color=WHITE_BLUE)
        exit_button = Button(text="Exit", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                             on_press=lambda x: self.exit_program(), background_color=WHITE_BLUE)
        box_layout.add_widget(menu_label)
        box_layout.add_widget(add_button)
        box_layout.add_widget(remove_button)
        box_layout.add_widget(show_button)
        box_layout.add_widget(exit_button)
        self.add_widget(box_layout)

    def exit_program(self):
        self._controller.write_data_into_file(self.file)
        raise SystemExit


class AddScreen(Screen):
    def __init__(self, db_controller, **kw):
        super(AddScreen, self).__init__(**kw)

        self._controller = db_controller

        added_fields = GridLayout(cols=2)

        fio_student_text = Button(text="Student", background_color=WHITE_BLUE)
        fio_student_input = GridLayout(cols=3)
        name_student_text = Button(text="Name", background_color=WHITE_BLUE)
        surname_student_text = Button(text="Last name", background_color=WHITE_BLUE)
        patronymic_student_text = Button(text="Patronymic", background_color=WHITE_BLUE)
        self.name_student_input = TextInput()
        self.surname_student_input = TextInput()
        self.patronymic_student_input = TextInput()
        fio_student_input.add_widget(surname_student_text)
        fio_student_input.add_widget(name_student_text)
        fio_student_input.add_widget(patronymic_student_text)
        fio_student_input.add_widget(self.surname_student_input)
        fio_student_input.add_widget(self.name_student_input)
        fio_student_input.add_widget(self.patronymic_student_input)

        social_work = Button(text="Social work", background_color=WHITE_BLUE)
        social_work_input = GridLayout(cols=10)
        sem_1 = Button(text="sem1", background_color=WHITE_BLUE)
        sem_2 = Button(text="sem2", background_color=WHITE_BLUE)
        sem_3 = Button(text="sem3", background_color=WHITE_BLUE)
        sem_4 = Button(text="sem4", background_color=WHITE_BLUE)
        sem_5 = Button(text="sem5", background_color=WHITE_BLUE)
        sem_6 = Button(text="sem6", background_color=WHITE_BLUE)
        sem_7 = Button(text="sem7", background_color=WHITE_BLUE)
        sem_8 = Button(text="sem8", background_color=WHITE_BLUE)
        sem_9 = Button(text="sem9", background_color=WHITE_BLUE)
        sem_10 = Button(text="sem10", background_color=WHITE_BLUE)
        self.sem_1_input = TextInput()
        self.sem_2_input = TextInput()
        self.sem_3_input = TextInput()
        self.sem_4_input = TextInput()
        self.sem_5_input = TextInput()
        self.sem_6_input = TextInput()
        self.sem_7_input = TextInput()
        self.sem_8_input = TextInput()
        self.sem_9_input = TextInput()
        self.sem_10_input = TextInput()
        social_work_input.add_widget(sem_1)
        social_work_input.add_widget(sem_2)
        social_work_input.add_widget(sem_3)
        social_work_input.add_widget(sem_4)
        social_work_input.add_widget(sem_5)
        social_work_input.add_widget(sem_6)
        social_work_input.add_widget(sem_7)
        social_work_input.add_widget(sem_8)
        social_work_input.add_widget(sem_9)
        social_work_input.add_widget(sem_10)
        social_work_input.add_widget(self.sem_1_input)
        social_work_input.add_widget(self.sem_2_input)
        social_work_input.add_widget(self.sem_3_input)
        social_work_input.add_widget(self.sem_4_input)
        social_work_input.add_widget(self.sem_5_input)
        social_work_input.add_widget(self.sem_6_input)
        social_work_input.add_widget(self.sem_7_input)
        social_work_input.add_widget(self.sem_8_input)
        social_work_input.add_widget(self.sem_9_input)
        social_work_input.add_widget(self.sem_10_input)

        group = Button(text="Group", background_color=WHITE_BLUE)
        self.group_input = TextInput()

        status = Button(text="Status", background_color=WHITE_BLUE)
        self.status_of_process = Button(background_color=GRAY)

        create_button = Button(text="Create ->", on_press=lambda x: self.create_field(),
                               background_color=BLUE)
        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             background_color=BLUE)

        added_fields.add_widget(fio_student_text)
        added_fields.add_widget(fio_student_input)
        added_fields.add_widget(group)
        added_fields.add_widget(self.group_input)
        added_fields.add_widget(social_work)
        added_fields.add_widget(social_work_input)
        added_fields.add_widget(status)
        added_fields.add_widget(self.status_of_process)
        added_fields.add_widget(back_button)
        added_fields.add_widget(create_button)

        self.add_widget(added_fields)

    def clear_all_fields(self):
        self.name_student_input.text = ''
        self.surname_student_input.text = ''
        self.patronymic_student_input.text = ''
        self.group_input.text = ''
        self.sem_1_input.text = ''
        self.sem_2_input.text = ''
        self.sem_3_input.text = ''
        self.sem_4_input.text = ''
        self.sem_5_input.text = ''
        self.sem_6_input.text = ''
        self.sem_7_input.text = ''
        self.sem_8_input.text = ''
        self.sem_9_input.text = ''
        self.sem_10_input.text = ''

        self.name_student_input.background_color = GRAY
        self.surname_student_input.background_color = GRAY
        self.patronymic_student_input.background_color = GRAY
        self.group_input.background_color = GRAY
        self.sem_1_input.background_color = GRAY
        self.sem_2_input.background_color = GRAY
        self.sem_3_input.background_color = GRAY
        self.sem_4_input.background_color = GRAY
        self.sem_5_input.background_color = GRAY
        self.sem_6_input.background_color = GRAY
        self.sem_7_input.background_color = GRAY
        self.sem_8_input.background_color = GRAY
        self.sem_9_input.background_color = GRAY
        self.sem_10_input.background_color = GRAY

    def on_leave(self, *args):
        self.clear_all_fields()
        self.status_of_process.text = ''
        self.status_of_process.background_color = GRAY

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
        select_remove = BoxLayout(orientation="vertical")
        self.menu_label = Label(text="Deleting by:", font_size=30)
        fio_student_remove_button = Button(
            text="Student last name", font_size=30, on_press=lambda x: self.set_choice(1, fio_student_remove_button))
        group_remove_button = Button(
            text="Group", font_size=30,
            on_press=lambda x: self.set_choice(2, group_remove_button))
        student_last_name_and_work_remove_button = Button(
            text="Student last name and work amount", font_size=30,
            on_press=lambda x: self.set_choice(3, student_last_name_and_work_remove_button))
        group_and_work_remove_button = Button(
            text="Group and work amount", font_size=30,
            on_press=lambda x: self.set_choice(3, group_and_work_remove_button))
        self.choice_buttons = list()
        self.choice_buttons.append(fio_student_remove_button)
        self.choice_buttons.append(group_remove_button)
        self.choice_buttons.append(student_last_name_and_work_remove_button)
        self.choice_buttons.append(group_and_work_remove_button)
        self.remove_input = TextInput()
        go_back_buttons = BoxLayout()
        remove_button = Button(text="Remove ->", on_press=lambda x: self.remove_field(),
                               background_color=BLUE)
        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             background_color=BLUE)
        select_remove.add_widget(self.menu_label)
        select_remove.add_widget(fio_student_remove_button)
        select_remove.add_widget(group_remove_button)
        select_remove.add_widget(student_last_name_and_work_remove_button)
        select_remove.add_widget(group_and_work_remove_button)
        select_remove.add_widget(self.remove_input)
        go_back_buttons.add_widget(back_button)
        go_back_buttons.add_widget(remove_button)
        select_remove.add_widget(go_back_buttons)
        self.add_widget(select_remove)

    def on_leave(self, *args):
        self.menu_label.text = "Deleting by:"
        self.choice = 0
        self.remove_input.background_color = GRAY
        self.remove_input.text = ""

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
                        is_removed = self._controller.delete_by_student_last_name(self.remove_input.text)
                    case 2:
                        is_removed = self._controller.delete_by_group(self.remove_input.text)
                    case 3:
                        try:
                            student, min_amount_of_work, max_amount_of_work = self.remove_input.text.split()
                            if self.is_type_is_int(min_amount_of_work) and self.is_type_is_int(max_amount_of_work):
                                is_removed = self._controller.delete_by_student_and_work_amount(
                                    student, min_amount_of_work, max_amount_of_work
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
                                    group, min_amount_of_work, max_amount_of_work
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

        test_layout = GridLayout(cols=5, padding=[0, 300, 0, 80])
        travel_layout = AnchorLayout(anchor_x='left', anchor_y="bottom")
        search_columns = GridLayout(cols=2, padding=[0, 0, 0, 80], row_force_default=True,
                                    row_default_height=(300/6))
        amount_of_pages = Button(text="Amount of records on page", background_color=GRAY)
        self.amount_of_pages_input = TextInput()

        search_student_surname = Button(text="Search by student last name", background_color=GRAY,
                                       on_press=lambda x: self.set_search(1, search_student_surname))
        self.student_surname_input = TextInput()
        search_group = Button(
            text="Search by group",
            background_color=GRAY,
            on_press=lambda x: self.set_search(2, search_group))
        self.group_input = TextInput()
        search_student_surname_and_work = Button(
            text="Search by student surname and work",
            background_color=GRAY,
            on_press=lambda x: self.set_search(3, search_student_surname_and_work)
        )
        self.student_surname_and_work_input = TextInput()
        search_group_and_work = Button(text="Search by group and work", background_color=GRAY,
                                  on_press=lambda x: self.set_search(4, search_group_and_work))
        self.group_and_work_input = TextInput()
        self.search_info = Button(text="SEARCH", background_color=GRAY,
                                  on_press=lambda x: self.search())
        search = Button(text="ALL", background_color=GRAY,
                        on_press=lambda x: self.show(self._controller.get_all_students()))
        self.search_buttons = list()
        self.search_buttons.append(search_student_surname)
        self.search_buttons.append(search_group)
        self.search_buttons.append(search_student_surname_and_work)
        self.search_buttons.append(search_group_and_work)
        search_columns.add_widget(search_student_surname)
        search_columns.add_widget(self.student_surname_input)
        search_columns.add_widget(search_group)
        search_columns.add_widget(self.group_input)
        search_columns.add_widget(search_student_surname_and_work)
        search_columns.add_widget(self.student_surname_and_work_input)
        search_columns.add_widget(search_group_and_work)
        search_columns.add_widget(self.group_and_work_input)
        search_columns.add_widget(search)
        search_columns.add_widget(self.search_info)
        search_columns.add_widget(amount_of_pages)
        search_columns.add_widget(self.amount_of_pages_input)
        columns_names = GridLayout(cols=12)
        student_fio = Button(text="Student", size_hint_x=None, size_hint_y=None, width=200, height=60, background_color=GREEN)
        group = Button(text="group", size_hint_y=None, size_hint_x=None, width=100, height=60, background_color=GREEN)
        sem_1 = Button(text="sem_1", size_hint_y=None, height=60, background_color=GREEN)
        sem_2 = Button(text="sem_2", size_hint_y=None, height=60, background_color=GREEN)
        sem_3 = Button(text="sem_3", size_hint_y=None, height=60, background_color=GREEN)
        sem_4 = Button(text="sem_4", size_hint_y=None, height=60, background_color=GREEN)
        sem_5 = Button(text="sem_5", size_hint_y=None, height=60, background_color=GREEN)
        sem_6 = Button(text="sem_6", size_hint_y=None, height=60, background_color=GREEN)
        sem_7 = Button(text="sem_7", size_hint_y=None, height=60, background_color=GREEN)
        sem_8 = Button(text="sem_8", size_hint_y=None, height=60, background_color=GREEN)
        sem_9 = Button(text="sem_9", size_hint_y=None, height=60, background_color=GREEN)
        sem_10 = Button(text="sem_10", size_hint_y=None, height=60, background_color=GREEN)

        columns_names.add_widget(student_fio)
        columns_names.add_widget(group)
        columns_names.add_widget(sem_1)
        columns_names.add_widget(sem_2)
        columns_names.add_widget(sem_3)
        columns_names.add_widget(sem_4)
        columns_names.add_widget(sem_5)
        columns_names.add_widget(sem_6)
        columns_names.add_widget(sem_7)
        columns_names.add_widget(sem_8)
        columns_names.add_widget(sem_9)
        columns_names.add_widget(sem_10)

        navigation_panel = BoxLayout()
        number_of_page_boxlayout = BoxLayout(orientation="vertical")
        index_of_page_boxlayout = BoxLayout(orientation="vertical")
        number_of_elements_boxlayout = BoxLayout(orientation="vertical")

        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             size_hint_y=None, height=80, background_color=BLUE)
        first_page_button = Button(text="First page", on_press=lambda x: self.set_present_fields_screen(0),
                                   size_hint_y=None, height=80, background_color=BLUE)
        last_page_button = Button(text="Last page",
                                  on_press=lambda x: self.set_present_fields_screen(len(self.list_of_screens) - 1),
                                  size_hint_y=None, height=80, background_color=BLUE)
        next_page_button = Button(text="Next page",
                                  on_press=lambda x: self.set_present_fields_screen(self.index_of_screen + 1),
                                  size_hint_y=None, height=80, background_color=BLUE)
        past_page_button = Button(text="Past page",
                                  on_press=lambda x: self.set_present_fields_screen(self.index_of_screen - 1),
                                  size_hint_y=None, height=80, background_color=BLUE)
        number_of_page_text = Button(text="№ page",
                                     size_hint_y=None, height=40, background_color=BLUE)
        index_of_page_text = Button(text="Count pages",
                                    size_hint_y=None, height=40, background_color=BLUE)
        number_of_elements_text = Button(text="Count el",
                                         size_hint_y=None, height=40, background_color=BLUE)
        self.number_of_page_text = Button(text=str(self.index_of_screen),
                                          size_hint_y=None, height=40, background_color=BLUE)
        self.index_of_page_text = Button(text=str(len(self.list_of_screens)),
                                         size_hint_y=None, height=40, background_color=BLUE)
        self.number_of_elements_text = Button(text=str(len(self._controller.get_all_students())),
                                         size_hint_y=None, height=40, background_color=BLUE)

        number_of_page_boxlayout.add_widget(number_of_page_text)
        number_of_page_boxlayout.add_widget(self.number_of_page_text)

        index_of_page_boxlayout.add_widget(index_of_page_text)
        index_of_page_boxlayout.add_widget(self.index_of_page_text)

        number_of_elements_boxlayout.add_widget(number_of_elements_text)
        number_of_elements_boxlayout.add_widget(self.number_of_elements_text)

        navigation_panel.add_widget(back_button)
        navigation_panel.add_widget(first_page_button)
        navigation_panel.add_widget(past_page_button)
        navigation_panel.add_widget(next_page_button)
        navigation_panel.add_widget(last_page_button)
        navigation_panel.add_widget(number_of_page_boxlayout)
        navigation_panel.add_widget(index_of_page_boxlayout)
        navigation_panel.add_widget(number_of_elements_boxlayout)
        travel_layout.add_widget(navigation_panel)
        test_layout.add_widget(columns_names)
        self.add_widget(search_columns)
        self.add_widget(travel_layout)
        self.add_widget(test_layout)

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
                        found_books = self._controller.search_by_student_last_name(student_last_name)
                        self.show(found_books)
                        self.clear_search_fields()
                case 2:
                    group = self.group_input.text
                    if self.group_input.text == '':
                        self.group_input.background_color = RED
                    else:
                        self.group_input.background_color = GRAY
                        found_books = self._controller.search_by_group(group)
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
                                found_books = self._controller.search_by_student_and_work_amount(
                                    student, int(min_amount_of_work), int(max_amount_of_work)
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
                            student, min_amount_of_work, max_amount_of_work = self.group_and_work_input.text.split()
                            if self.is_type_is_int(min_amount_of_work) and self.is_type_is_int(max_amount_of_work):
                                self.group_input.background_color = GRAY
                                found_books = self._controller.search_by_group_and_work_amount(
                                    student, int(min_amount_of_work), int(max_amount_of_work)
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

    def on_leave(self, *args):
        for button in self.search_buttons:
            button.background_color = GRAY
        self.choice = 0
        self.clear_search_fields()
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)


class ChooseFile(Screen):

    def __init__(self, **kw):
        super(ChooseFile, self).__init__(**kw)
        self.file = ""
        self.lib_was_chosen = False
        choice = BoxLayout(orientation="vertical")

        # find_current_file = BoxLayout()
        # file_search = Button(text="Choose library", font_size=48,
        #                      on_press=lambda x: self.input_library(self.file_search_input.text, file_search))
        # self.file_search_input = TextInput()
        # find_current_file.add_widget(file_search)
        # find_current_file.add_widget(self.file_search_input)

        create_lib_box = BoxLayout()
        create_lib = Button(text="Create library", font_size=48,
                            on_press=lambda x: self.create_file(self.create_lib_input.text, create_lib))
        self.create_lib_input = TextInput()
        create_lib_box.add_widget(create_lib)
        create_lib_box.add_widget(self.create_lib_input)

        self.file_buttons = list()
        # self.file_buttons.append(file_search)
        self.file_buttons.append(create_lib)

        pattern = re.compile("\w+.xml")
        for file in os.listdir("."):
            if re.match(pattern, file):
                new_lib = Button(text=file, font_size=48,
                                 on_press=self.set_library)
                choice.add_widget(new_lib)
                self.file_buttons.append(new_lib)

        menu = Button(text="Set Library", font_size=48,
                      on_press=lambda x: self.create_menu())
        # choice.add_widget(find_current_file)
        choice.add_widget(create_lib_box)

        choice.add_widget(menu)
        self.add_widget(choice)

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


screen_manager = ScreenManager()
screen_manager.add_widget(ChooseFile(name="choice"))


def set_screen(screen_name):
    screen_manager.current = screen_name


class TheLabApp(App):

    def build(self):
        return screen_manager
