from signal import set_wakeup_fd
import xml.sax

from Utility.xml_parsers import Reader, Writer
from Model.model import Student, StudentsStorage


class DataBaseController:

    def __init__(self):
        self._reader = Reader()
        self._list_of_students = StudentsStorage()

    def add_student(self, student):
        self._list_of_students.add(student)

    def get_all_students(self):
        return self._list_of_students.storage

    def search(self, search_type, **kwargs):
        match search_type:
            case "search_by_student_last_name":
                return self._list_of_students.search_by_student_last_name(kwargs["student_last_name"])
            case "search_by_group":
                return self._list_of_students.search_by_group(kwargs["group"])
            case "search_by_student_and_work_amount":
                return self._list_of_students.search_by_student_and_work_amount(
                    kwargs["sudent"],
                    kwargs["min_amount_of_work"],
                    kwargs["max_amount_of_work"],
                )
            case "search_by_group_and_work_amount":
                return self._list_of_students.search_by_group_and_work_amount(
                    kwargs["group"],
                    kwargs["min_amount_of_work"],
                    kwargs["max_amount_of_work"],
                )

    def delete(self, delete_type, **kwargs):
        match delete_type:
            case "delete_by_student_last_name":
                return self._list_of_students.delete_by_student_last_name(kwargs["student_last_name"])
            case "delete_by_group":
                return self._list_of_students.delete_by_group(kwargs["group"])
            case "delete_by_student_and_work_amount":
                return self._list_of_students.delete_by_student_and_work_amount(
                    kwargs["sudent"],
                    kwargs["min_amount_of_work"],
                    kwargs["max_amount_of_work"],
                )
            case "delete_by_group_and_work_amount":
                return self._list_of_students.delete_by_group_and_work_amount(
                    kwargs["group"],
                    kwargs["min_amount_of_work"],
                    kwargs["max_amount_of_work"],
                )

    def write_data_into_file(self, file):
        self._writer = Writer(file)
        for student in self._list_of_students.storage:
            self._writer.create_xml_student({
                "student_name": student.student_name,
                "student_last_name": student.student_last_name,
                "student_patronymic": student.student_patronymic,
                "group": student.group,
                "sem_1": student.sem_1,
                "sem_2": student.sem_2,
                "sem_3": student.sem_3,
                "sem_4": student.sem_4,
                "sem_5": student.sem_5,
                "sem_6": student.sem_6,
                "sem_7": student.sem_7,
                "sem_8": student.sem_8,
                "sem_9": student.sem_9,
                "sem_10": student.sem_10,
            })
        self._writer.create_xml_file()

    def read_from_file(self, file):
        parser = xml.sax.make_parser()
        parser.setContentHandler(self._reader)
        parser.parse(file)
        for student in self._reader.data_table:
            self._list_of_students.add(Student(
                student[0], student[1], student[2], student[3], student[4],
                student[5], student[6], student[7], student[8], student[9],
                student[10], student[11], student[12], student[13]
            ))
