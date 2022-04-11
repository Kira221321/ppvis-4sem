from .dinosaur_factories import Dinosaur


class Predator(Dinosaur):
    def __init__(self):
        super().__init__()
        self.type = 'predator'
        self.hunger = 20
    
    def hunt(self):
        pass


class Trex(Predator):
    def __init__(self):
        super().__init__()
        self.type = 'trex'
        self.health = 70








