from abc import ABC, abstractmethod
from random import choice


class DinosaurFactory(ABC):

    @abstractmethod
    def factory_method(self):
        pass


class Dinosaur(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def dying(self):
        pass
