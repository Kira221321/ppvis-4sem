import pickle


class FileManager:
    def __init__(self, my_file):
        self.file = my_file

    def load_data_from_template_file(self):
        try:
            data_saver = list()
            with open(self.file, 'r') as file:
                for line in file:
                    data_saver.append(line.split())
            return data_saver
        except FileNotFoundError:
            print("There is no such file!")

    def load_data_from_previous_simulation(self):
        try:
            with open('Field/field.pickle', 'rb') as file:
                pickle.load(file)
        except FileNotFoundError:
            print('There is no such file!')

    def upload_data(self, field):
        with open('Field/field.pickle', 'wb') as file:
            pickle.dump(field, file)
