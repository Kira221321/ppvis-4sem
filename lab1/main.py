import argparse
from file_manager.file_manager import FileManager
from Dinosaurs.dinosaur_factories import TrexFactory, BrontosaurusFactory, StegosaurusFactory
from Plants.plants import Plant
from Field.field import Field
from Interface.field_interface import FieldInterface
from Cycle.life_cycle import Cycle


parser = argparse.ArgumentParser("Choose type of the interface")
parser.add_argument("-p", "--previous", action="store_true", help="Continue previous simulation")
parser.add_argument("-t", "--template", action="store_true", help="Start simulation using template")
parser.add_argument("-a", "--add", help="add a chosen animal in random place")
parser.add_argument("-x", "--x_coord", help="if this attribute is specified, then animal will be added to chosen x coordinate")
parser.add_argument("-y", "--y_coord", help="if this attribute is specified, then animal will be added to chosen y coordinate")
args = parser.parse_args()


def add_creature(forest):
    if args.add:
        match args.add:
            case 'trex':
                creature = 'trex'
            case 'brontosaurus':
                creature = 'brontosaurus'
            case 'stegosaurus':
                creature = 'stegosaurus'
            case 'plant':
                creature = 'plant'
            case _:
                print('Wrong creature input')
                return
        if args.x_coord and args.y_coord:
            try:
                x_coord = int(args.x_coord)
                y_coord = int(args.y_coord)
                forest.append_creature(creature, x_coord, y_coord)
            except TypeError:
                print("Wrong coordinates input")
        else:
            print("You didn't set coordinates")


if __name__ == '__main__':
    if args.template:
        file_manager = FileManager()
        environment = file_manager.load_data_from_template_file()
        field = Field(environment)
    elif args.previous:
        file_manager = FileManager()
        field = file_manager.load_data_from_previous_simulation()
    else:
        print("You didn't enter type of simulation")
        raise SystemExit
    add_creature(field)
    field_interface = FieldInterface(field)
    field_interface.show_field()
    cycle = Cycle(field)
    cycle.life()
    field_interface.show_field()
    file_manager.upload_data(field)
