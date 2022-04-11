from .dinosaur_factories import Dinosaur


class Herbivore(Dinosaur):
    def __init__(self):
        super().__init__()
        self.type = 'herbivore'

    
    def plants_searching(self):
        pass


class Brontosaurus(Herbivore):
    def __init__(self):
        super().__init__()
        self.type = 'brontosaurus'
        self.health = 50




class Stegosaurus(Herbivore):
    def __init__(self):
        super().__init__()
        self.type = 'stegosaurus'
        self.health = 40

