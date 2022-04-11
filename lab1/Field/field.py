from Dinosaurs.dinosaur_factories import TrexFactory, BrontosaurusFactory, StegosaurusFactory
from Plants.plants import Plant


class Field:

    def __init__(self, environment: list):
        self._field = []
        trex_creator = TrexFactory()
        brontosaurus_creator = BrontosaurusFactory()
        stegosaurus_creator = StegosaurusFactory()
        for line in environment:
            list_of_creatures = []
            for creature in line:
                match creature:
                    case 'T':
                        trex = trex_creator.factory_method()
                        list_of_creatures.append(trex)
                    case 'S':
                        stegosaurus = stegosaurus_creator.factory_method()
                        list_of_creatures.append(stegosaurus)
                    case 'B':
                        brontosaurus = brontosaurus_creator.factory_method()
                        list_of_creatures.append(brontosaurus)
                    case 'P':
                        plant = Plant()
                        list_of_creatures.append(plant)
                    case 'None':
                        list_of_creatures.append(None)
            self._field.append(list_of_creatures)
