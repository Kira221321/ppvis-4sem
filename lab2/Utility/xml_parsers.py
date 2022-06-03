import xml.dom.minidom as minidom
import xml.sax


class Reader(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.data_table = []
        self.student_data = []
        self.parser = xml.sax.make_parser()

    def startElement(self, name, attrs):
        self.current = name
        if name == "student":
            pass

    def characters(self, content):
        if self.current == "student_name":
            self.student_name = content
        elif self.current == "student_last_name":
            self.student_last_name = content
        elif self.current == "student_patronymic":
            self.student_patronymic = content
        elif self.current == "group":
            self.group = content
        elif self.current == "sem_1":
            self.sem_1 = content
        elif self.current == "sem_2":
            self.sem_2 = content
        elif self.current == "sem_3":
            self.sem_3 = content
        elif self.current == "sem_4":
            self.sem_4 = content
        elif self.current == "sem_5":
            self.sem_5 = content
        elif self.current == "sem_6":
            self.sem_6 = content
        elif self.current == "sem_7":
            self.sem_7 = content
        elif self.current == "sem_8":
            self.sem_8 = content
        elif self.current == "sem_9":
            self.sem_9 = content
        elif self.current == "sem_10":
            self.sem_10 = content

    def endElement(self, name):
        if self.current == "student_name":
            self.student_data.append(self.student_name)
        elif self.current == "student_last_name":
            self.student_data.append(self.student_last_name)
        elif self.current == "student_patronymic":
            self.student_data.append(self.student_patronymic)
        elif self.current == "group":
            self.student_data.append(self.group)
        elif self.current == "sem_1":
            self.student_data.append(self.sem_1)
        elif self.current == "sem_2":
            self.student_data.append(self.sem_2)
        elif self.current == "sem_3":
            self.student_data.append(self.sem_3)
        elif self.current == "sem_4":
            self.student_data.append(self.sem_4)
        elif self.current == "sem_5":
            self.student_data.append(self.sem_5)
        elif self.current == "sem_6":
            self.student_data.append(self.sem_6)
        elif self.current == "sem_7":
            self.student_data.append(self.sem_7)
        elif self.current == "sem_8":
            self.student_data.append(self.sem_8)
        elif self.current == "sem_9":
            self.student_data.append(self.sem_9)
        elif self.current == "sem_10":
            self.student_data.append(self.sem_10)
        if len(self.student_data) == 14:
            self.data_table.append(tuple(self.student_data))
            self.student_data = []
        self.current = ""


class Writer:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.dom_tree = minidom.Document()
        self.rows = []

    def create_xml_student(self, data):
        student = self.dom_tree.createElement("student")

        for value in data:
            temp_child = self.dom_tree.createElement(value)
            student.appendChild(temp_child)

            node_text = self.dom_tree.createTextNode(str(data[value]))
            temp_child.appendChild(node_text)

        self.rows.append(student)

    def create_xml_file(self):
        pass_table = self.dom_tree.createElement("pass_table")

        for student in self.rows:
            pass_table.appendChild(student)

        self.dom_tree.appendChild(pass_table)

        self.dom_tree.writexml(open(self.file_name, 'w'),
                               indent="  ",
                               addindent="  ",
                               newl='\n')
        self.dom_tree.unlink()

