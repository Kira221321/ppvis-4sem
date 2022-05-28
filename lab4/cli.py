from utility.file_manager import FileManager
from model.field import Field
from view.field_interface import FieldInterface
from controller.life_cycle import Cycle


if __name__ == '__main__':
    print('How would you like to start: ')
    print('1: Simulation from template field')
    print('2: Previous simulation.')
    while True:
        choice = input('Youre choice:')
        environment: list
        match choice:
            case '1':
                file_manager = FileManager()
                environment = file_manager.load_data_from_template_file()
                field = Field(environment)
                break
            case '2':
                file_manager = FileManager()
                field = file_manager.load_data_from_previous_simulation()
                break
            case _:
                print('Try to choose once again)')
    field_interface = FieldInterface(field)
    field_interface.show_field()
    cycle = Cycle(field)
    while True:
        cycle.life()
        field_interface.show_field()
        exit_check = input("ENTER q TO EXIT")
        if exit_check == 'q':
            file_manager.upload_data(field)
            raise SystemExit
