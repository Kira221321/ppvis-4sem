from abc import ABC, abstractmethod
from random import choice

from .dinosaurs import Trex, Brontosaurus, Stegosaurus


class DinosaurFactory(ABC):

    @abstractmethod
    def factory_method(self):
        pass


class BrontosaurusFactory(DinosaurFactory):

    def factory_method(self):
        brontosaurus = Brontosaurus()
        brontosaurus._type = 'brontosaurus'
        brontosaurus._health = 70
        brontosaurus._hunger = 0
        brontosaurus._sex = choice(['male', 'female'])
        return brontosaurus


class StegosaurusFactory(DinosaurFactory):

    def factory_method(self):
        stegosaurus = Stegosaurus()
        stegosaurus._type = 'stegosaurus'
        stegosaurus._health = 70
        stegosaurus._hunger = 0
        stegosaurus._sex = choice(['male', 'female'])
        return stegosaurus


class TrexFactory(DinosaurFactory):

    def factory_method(self):
        trex = Trex()
        trex._type = 'trex'
        trex._health = 70
        trex._hunger = 0
        trex._sex = choice(['male', 'female'])
        return trex
