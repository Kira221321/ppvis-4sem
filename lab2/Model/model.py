from dataclasses import dataclass


@dataclass
class Student:
    student_name: str = 'name'
    student_last_name: str = 'last_name'
    student_patronymic: str = 'patronymic'
    group: str = '0'
    sem_1: int = 0
    sem_2: int = 0
    sem_3: int = 0
    sem_4: int = 0
    sem_5: int = 0
    sem_6: int = 0
    sem_7: int = 0
    sem_8: int = 0
    sem_9: int = 0
    sem_10: int = 0


class StudentsStorage:
    def __init__(self):
        self.storage = list()

    def add(self, student):
        self.storage.append(student)

    def search_by_student_last_name(self, student_last_name):
        found_students = list()
        for student in self.storage:
            if student.student_last_name == student_last_name:
                found_students.append(student)
        return found_students

    def search_by_group(self, group):
        found_students = list()
        for student in self.storage:
            if student.group == group:
                found_students.append(student)
        return found_students

    def search_by_student_and_work_amount(self, student, min_amount_of_work, max_amount_of_work):
        found_students = list()
        for student_ in self.storage:
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
        for student_ in self.storage:
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
        for _ in range(len(self.storage)):
            if self.storage[index].student_last_name == input_:
                self.storage.remove(self.storage[index])
                counter += 1
            else:
                index += 1
        return counter if counter > 0 else False

    def delete_by_group(self, delete_group):
        counter = 0
        index = 0
        for _ in range(len(self.storage)):
            if self.storage[index].group == delete_group:
                self.storage.remove(self.storage[index])
                counter += 1
            else:
                index += 1
        return counter if counter > 0 else False

    def delete_by_student_and_work_amount(self, student, min_amount_of_work, max_amount_of_work):
        counter = 0
        index = 0
        for _ in range(len(self.storage)):
            student_ = self.storage[index]
            work_amount = int(student_.sem_1) + int(student_.sem_2) \
                          + int(student_.sem_3) + int(student_.sem_4) \
                          + int(student_.sem_5) + int(student_.sem_6) \
                          + int(student_.sem_7) + int(student_.sem_8) \
                          + int(student_.sem_9) + int(student_.sem_10)
            if self.storage[index].student_last_name == student \
                    and int(max_amount_of_work) > work_amount > int(min_amount_of_work):
                self.storage.remove(self.storage[index])
                counter += 1
            else:
                index += 1
        return counter if counter > 0 else False

    def delete_by_group_and_work_amount(self, group, min_amount_of_work, max_amount_of_work):
        counter = 0
        index = 0
        for _ in range(len(self.storage)):
            student = self.storage[index]
            work_amount = int(student.sem_1) + int(student.sem_2) \
                          + int(student.sem_3) + int(student.sem_4) \
                          + int(student.sem_5) + int(student.sem_6) \
                          + int(student.sem_7) + int(student.sem_8) \
                          + int(student.sem_9) + int(student.sem_10)
            if self.storage[index].group == group \
                    and int(max_amount_of_work) > work_amount > int(min_amount_of_work):
                self.storage.remove(self.storage[index])
                counter += 1
            else:
                index += 1
        return counter if counter > 0 else False

