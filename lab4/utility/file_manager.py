import pickle


class FileManager:

    def load_data_from_template_file(self):
        try:
            data_saver = list()
            with open('model/environment.txt', 'r') as file:
                for line in file:
                    data_saver.append(line.split())
            return data_saver
        except FileNotFoundError:
            print("There is no such file!")

    def load_data_from_previous_simulation(self):
        try:
            with open('model/field.pickle', 'rb') as file:
                environment = pickle.load(file)
                print(environment)
                return environment
        except FileNotFoundError:
            print('There is no such file!')

    def upload_data(self, field):
        with open('model/field.pickle', 'wb') as file:
            pickle.dump(field, file)
