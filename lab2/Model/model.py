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
