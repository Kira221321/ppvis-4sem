from file_manager.file_manager import FileManager
from Field.field import Field

a = FileManager('bla')
environment = Field()
a.upload_data(environment)

if __name__ == '__main__':
    print('How would you like to start: ')
    print('1: Simulation from template field')
    print('2: Previous simulation.')
    while True:
        choice = input('Youre choice:')
        match choice:
            case '1':
                file_manager = FileManager('Field/environment.txt')
                environment = file_manager.load_data_from_template_file()
                break
            case '2':
                file_manager = FileManager('Field/field.txt')
                environment = file_manager.load_data_from_previous_simulation()
                break
            case _:
                print('Try to choose once again)')

