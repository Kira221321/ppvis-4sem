from model.dinosaur_factories import TrexFactory, BrontosaurusFactory, StegosaurusFactory
from model.plants import Plant


class Field:

    def __init__(self, environment: list):
        self._environment = []
        self.trex_creator = TrexFactory()
        self.brontosaurus_creator = BrontosaurusFactory()
        self.stegosaurus_creator = StegosaurusFactory()
        line_num = 0
        for line in environment:
            list_of_creatures = []
            column_num = 0
            for creature in line:
                match creature:
                    case 'T':
                        trex = self.trex_creator.factory_method(
                            self, line_num, column_num
                        )
                        list_of_creatures.append(trex)
                        column_num += 1
                    case 'S':
                        stegosaurus = self.stegosaurus_creator.factory_method(
                            self, line_num, column_num
                        )
                        list_of_creatures.append(stegosaurus)
                        column_num += 1
                    case 'B':
                        brontosaurus = self.brontosaurus_creator.factory_method(
                            self, line_num, column_num
                        )
                        list_of_creatures.append(brontosaurus)
                        column_num += 1
                    case 'P':
                        plant = Plant(
                            self, line_num, column_num
                        )
                        list_of_creatures.append(plant)
                        column_num += 1
                    case 'None':
                        list_of_creatures.append(None)
                        column_num += 1
            line_num += 1
            self._environment.append(list_of_creatures)

    @property
    def environment(self):
        return self._environment

    def get_creatures_around(self):
        pass

    def is_place_empty(self, x, y):
        return self._environment[x][y] is None

    def are_coords_valid(self, x, y):
        return -1 < x < 10 and -1 < y < 15

    def append_creature(self, creature_type, x, y):
        match creature_type:
            case "trex":
                trex = self.trex_creator.factory_method(self, x, y)
                self._environment[x][y] = trex
            case "brontosaurus":
                brontosaurus = self.brontosaurus_creator.factory_method(self, x, y)
                self._environment[x][y] = brontosaurus
            case "stegosaurus":
                stegosaurus = self.stegosaurus_creator.factory_method(self, x, y)
                self._environment[x][y] = stegosaurus
            case "plant":
                plant = Plant(self, x, y)
                self._environment[x][y] = plant

    def get_empty_place_near(self, x, y):
        if self.are_coords_valid(x - 1, y - 1):
            if self.is_place_empty(x - 1, y - 1):
                return {"x_pos": x - 1, "y_pos": y - 1}
        if self.are_coords_valid(x - 1, y):
            if self.is_place_empty(x - 1, y):
                return {"x_pos": x - 1, "y_pos": y}
        if self.are_coords_valid(x - 1, y + 1):
            if self.is_place_empty(x - 1, y + 1):
                return {"x_pos": x - 1, "y_pos": y + 1}
        if self.are_coords_valid(x, y - 1):
            if self.is_place_empty(x, y - 1):
                return {"x_pos": x, "y_pos": y - 1}
        if self.are_coords_valid(x, y + 1):
            if self.is_place_empty(x, y + 1):
                return {"x_pos": x, "y_pos": y + 1}
        if self.are_coords_valid(x + 1, y - 1):
            if self.is_place_empty(x + 1, y - 1):
                return {"x_pos": x + 1, "y_pos": y - 1}
        if self.are_coords_valid(x + 1, y):
            if self.is_place_empty(x + 1, y):
                return {"x_pos": x + 1, "y_pos": y}
        if self.are_coords_valid(x + 1, y + 1):
            if self.is_place_empty(x + 1, y + 1):
                return {"x_pos": x + 1, "y_pos": y + 1}
