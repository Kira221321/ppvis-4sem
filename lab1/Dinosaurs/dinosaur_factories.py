from abc import ABC, abstractmethod
from random import choice
from .dinosaurs import Trex, Brontosaurus, Stegosaurus
import Field

class DinosaurFactory(ABC):

    @abstractmethod
    def factory_method(self, field: Field, pos_x: int, pos_y: int):
        pass


class BrontosaurusFactory(DinosaurFactory):

    def factory_method(self, field: Field, pos_x: int, pos_y: int) -> Brontosaurus:
        brontosaurus = Brontosaurus()
        brontosaurus._type = 'brontosaurus'
        brontosaurus._life_cycle = False
        brontosaurus._health = 150
        brontosaurus._hunger = 0
        brontosaurus._sex = choice(['male', 'female'])
        brontosaurus._step = 2
        brontosaurus._field = field
        brontosaurus.x_position = pos_x
        brontosaurus.y_position = pos_y
        return brontosaurus


class StegosaurusFactory(DinosaurFactory):

    def factory_method(self, field: Field, pos_x: int, pos_y: int) -> Stegosaurus:
        stegosaurus = Stegosaurus()
        stegosaurus._type = 'stegosaurus'
        stegosaurus._life_cycle = False
        stegosaurus._health = 130
        stegosaurus._hunger = 0
        stegosaurus._sex = choice(['male', 'female'])
        stegosaurus._step = 2
        stegosaurus._field = field
        stegosaurus.x_position = pos_x
        stegosaurus.y_position = pos_y
        return stegosaurus


class TrexFactory(DinosaurFactory):

    def factory_method(self, field: Field, pos_x: int, pos_y: int) -> Trex:
        trex = Trex()
        trex._type = 'trex'
        trex._life_cycle = False
        trex._health = 200
        trex._hunger = 0
        trex._sex = choice(['male', 'female'])
        trex._step = 3
        trex._field = field
        trex.x_position = pos_x
        trex.y_position = pos_y
        return trex
