from abc import ABC, abstractmethod
from random import choice


class Dinosaur(ABC):

    def __init__(self):
        self._health: int
        self._type: str
        self.sex = choice(['male', 'female'])
        self._hunger = 0

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


class Brontosaurus(Dinosaur):

    def eat(self):
        pass

    def move(self):
        pass

    def reproduce(self):
        pass

    def dying(self):
        pass


class Stegosaurus(Dinosaur):

    def eat(self):
        pass

    def move(self):
        pass

    def reproduce(self):
        pass

    def dying(self):
        pass


class Trex(Dinosaur):

    def eat(self):
        pass

    def move(self):
        pass

    def reproduce(self):
        pass

    def dying(self):
        pass

