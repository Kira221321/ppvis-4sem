import xml.sax

from Utility.xml_parsers import Reader, Writer
from Model.model import Student


class DataBaseController:

    def __init__(self, file):
        self._reader = Reader()
        self._writer = Writer(file)
        self._list_of_students = list()
        self.read_from_file(file)

    def add_student(self, student):
        self._list_of_students.append(student)

    def get_all_students(self):
        return self._list_of_students

    def search_by_student_last_name(self, student_last_name):
        found_students = list()
        for student in self._list_of_students:
            if student.student_last_name == student_last_name:
                found_students.append(student)
        return found_students

    def search_by_group(self, group):
        found_students = list()
        for student in self._list_of_students:
            if student.group == group:
                found_students.append(student)
        return found_students

    def search_by_student_and_work_amount(self, student, min_amount_of_work, max_amount_of_work):
        found_students = list()
        for student_ in self._list_of_students:
            work_amount = int(student_.sem_1) + int(student_.sem_2) \
                          + int(student_.sem_3) + int(student_.sem_4) \
                          + int(student_.sem_5) + int(student_.sem_6) \
                          + int(student_.sem_7) + int(student_.sem_8) \
                          + int(student_.sem_9) + int(student_.sem_10)
            if student_.student_last_name == student and\
                    min_amount_of_work < work_amount < max_amount_of_work:
                found_students.append(student_)
        return found_students

    def search_by_group_and_work_amount(self, group, min_amount_of_work, max_amount_of_work):
        found_students = list()
        for student_ in self._list_of_students:
            work_amount = int(student_.sem_1) + int(student_.sem_2) \
                          + int(student_.sem_3) + int(student_.sem_4) \
                          + int(student_.sem_5) + int(student_.sem_6) \
                          + int(student_.sem_7) + int(student_.sem_8) \
                          + int(student_.sem_9) + int(student_.sem_10)
            if student_.group == group and\
                    min_amount_of_work < work_amount < max_amount_of_work:
                found_students.append(student_)
        return found_students


    def delete_by_student_last_name(self, input_):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_students)):
            if self._list_of_students[index].student_last_name == input_:
                self._list_of_students.remove(self._list_of_students[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_by_group(self, input_):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_students)):
            if self._list_of_students[index].group == input_:
                self._list_of_students.remove(self._list_of_students[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_by_student_and_work_amount(self, student, min_amount_of_work, max_amount_of_work):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_students)):
            student_ = self._list_of_students[index]
            work_amount = int(student_.sem_1) + int(student_.sem_2) \
                          + int(student_.sem_3) + int(student_.sem_4) \
                          + int(student_.sem_5) + int(student_.sem_6) \
                          + int(student_.sem_7) + int(student_.sem_8) \
                          + int(student_.sem_9) + int(student_.sem_10)
            if self._list_of_students[index].student_last_name == student \
                    and int(max_amount_of_work) > work_amount > int(min_amount_of_work):
                self._list_of_students.remove(self._list_of_students[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_by_group_and_work_amount(self, group, min_amount_of_work, max_amount_of_work):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_students)):
            student = self._list_of_students[index]
            work_amount = int(student.sem_1) + int(student.sem_2) \
                          + int(student.sem_3) + int(student.sem_4) \
                          + int(student.sem_5) + int(student.sem_6) \
                          + int(student.sem_7) + int(student.sem_8) \
                          + int(student.sem_9) + int(student.sem_10)
            if self._list_of_students[index].group == group \
                    and int(max_amount_of_work) > work_amount > int(min_amount_of_work):
                self._list_of_students.remove(self._list_of_students[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def write_data_into_file(self):
        for student in self._list_of_students:
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
            self._list_of_students.append(Student(
                student[0], student[1], student[2], student[3], student[4],
                student[5], student[6], student[7], student[8], student[9],
                student[10], student[11], student[12], student[13]
            ))
