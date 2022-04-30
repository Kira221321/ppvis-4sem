from abc import ABC, abstractmethod
from random import choice
from random import randint

import Field


CHANCE_TO_GO_AWAY = 50
REPRODUCE_CHANCE = 10
DIRECTIONS = [
    "up",
    "down",
    "left",
    "right",
]


class Dinosaur(ABC):

    def __init__(self):
        self._health: int = 0
        self._type: str = "type"
        self._life_cycle: bool = False
        self._sex = choice(['male', 'female'])
        self._hunger = 0
        self._step: int = 0
        self._field: Field = None
        self._x_position: int = 0
        self._y_position: int = 0

    @property
    def life_cycle(self):
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        self._life_cycle = life_cycle

    @property
    def type(self):
        return self._type

    @property
    def sex(self):
        return self._sex

    @property
    def x_position(self):
        return self._x_position

    @property
    def y_position(self):
        return self._y_position

    @x_position.setter
    def x_position(self, x_pos):
        self._x_position = x_pos

    @y_position.setter
    def y_position(self, y_pos):
        self._y_position = y_pos

    @abstractmethod
    def make_decision(self):
        pass

    def eat(self, creatures_around, prey):
        for creature in creatures_around:
            if creature.type == prey:
                print(creature)
                victim_place_x, victim_place_y = creature.x_position, creature.y_position
                self._field.environment[victim_place_x][victim_place_y] = self
                self._field.environment[self.x_position][self.y_position] = None
                self.x_position = victim_place_x
                self.y_position = victim_place_y
                self._hunger -= 2
                self._health += 40
                break

    def look_around(self):
        creatures_around = []
        if self._field.are_coords_valid(self.x_position - 1, self.y_position - 1):
            creatures_around.append(self._field.environment[self.x_position - 1][self.y_position - 1])
        if self._field.are_coords_valid(self.x_position - 1, self.y_position):
            creatures_around.append(self._field.environment[self.x_position - 1][self.y_position])
        if self._field.are_coords_valid(self.x_position - 1, self.y_position + 1):
            creatures_around.append(self._field.environment[self.x_position - 1][self.y_position + 1])
        if self._field.are_coords_valid(self.x_position, self.y_position - 1):
            creatures_around.append(self._field.environment[self.x_position][self.y_position - 1])
        if self._field.are_coords_valid(self.x_position, self.y_position + 1):
            creatures_around.append(self._field.environment[self.x_position][self.y_position + 1])
        if self._field.are_coords_valid(self.x_position + 1, self.y_position - 1):
            creatures_around.append(self._field.environment[self.x_position + 1][self.y_position - 1])
        if self._field.are_coords_valid(self.x_position + 1, self.y_position):
            creatures_around.append(self._field.environment[self.x_position + 1][self.y_position])
        if self._field.are_coords_valid(self.x_position + 1, self.y_position + 1):
            creatures_around.append(self._field.environment[self.x_position + 1][self.y_position + 1])
        creatures_around = list(filter(lambda x: x is not None, creatures_around))
        return creatures_around

    def move(self):
        direction = DIRECTIONS[randint(0, 3)]
        match direction:
            case "up":
                if self._field.are_coords_valid(self.x_position - self._step, self.y_position):
                    if self._field.is_place_empty(self.x_position - self._step, self.y_position):
                        self._field.environment[self.x_position][self.y_position] = None
                        self._field.environment[self.x_position - self._step][self.y_position] = self
                        self.x_position = self.x_position - self._step
            case "down":
                if self._field.are_coords_valid(self.x_position + self._step, self.y_position):
                    if self._field.is_place_empty(self.x_position + self._step, self.y_position):
                        self._field.environment[self.x_position][self.y_position] = None
                        self._field.environment[self.x_position + self._step][self.y_position] = self
                        self.x_position = self.x_position + self._step
            case "left":
                if self._field.are_coords_valid(self.x_position, self.y_position - self._step):
                    if self._field.is_place_empty(self.x_position, self.y_position - self._step):
                        self._field.environment[self.x_position][self.y_position] = None
                        self._field.environment[self.x_position][self.y_position - self._step] = self
                        self.y_position = self.y_position - self._step
            case "right":
                if self._field.are_coords_valid(self.x_position, self.y_position + self._step):
                    if self._field.is_place_empty(self.x_position, self.y_position + self._step):
                        self._field.environment[self.x_position][self.y_position] = None
                        self._field.environment[self.x_position][self.y_position + self._step] = self
                        self.y_position = self.y_position + self._step

    @abstractmethod
    def reproduce(self):
        pass

    def is_alive(self):
        return self._health > 0

    def dying(self):
        self._field.environment[self.x_position][self.y_position] = None
        del self


class Brontosaurus(Dinosaur):

    def make_decision(self):
        if self.is_alive():
            creatures_around = self.look_around()
            if self._hunger > 3:
                if "plant" in [creature.type for creature in creatures_around]:
                    self.eat(creatures_around, "plant")
            elif randint(1, 100) <= REPRODUCE_CHANCE:
                for creature in creatures_around:
                    if creature.type == "brontosaurus":
                        sex = "male" if self._sex == "female" else "female"
                        if creature.sex == sex:
                            self.reproduce()
            if randint(1, 100) <= CHANCE_TO_GO_AWAY:
                self.move()
                self._hunger += 1
            self._life_cycle = True
            self._health -= 2
            print(self._health)
        else:
            self.dying()

    def reproduce(self):
        empty_place = self._field.get_empty_place_near(
            self.x_position, self.y_position
        )
        if empty_place:
            self._field.append_creature(
                "brontosaurus",
                empty_place["x_pos"],
                empty_place["y_pos"],
            )

    def __str__(self):
        return '#'


class Stegosaurus(Dinosaur):

    def make_decision(self):
        if self.is_alive():
            creatures_around = self.look_around()
            if self._hunger > 3:
                if "plant" in [creature.type for creature in creatures_around]:
                    self.eat(creatures_around, "plant")
            elif randint(1, 100) <= REPRODUCE_CHANCE:
                for creature in creatures_around:
                    if creature.type == "stegosaurus":
                        sex = "male" if self._sex == "female" else "female"
                        if creature.sex == sex:
                            self.reproduce()
            if randint(1, 100) <= CHANCE_TO_GO_AWAY:
                self.move()
                self._hunger += 1
            self._life_cycle = True
            self._health -= 2
            print(self._health)
        else:
            self.dying()

    def reproduce(self):
        empty_place = self._field.get_empty_place_near(
            self.x_position, self.y_position
        )
        if empty_place:
            self._field.append_creature(
                "stegosaurus",
                empty_place["x_pos"],
                empty_place["y_pos"],
            )

    def __str__(self):
        return '$'


class Trex(Dinosaur):

    def make_decision(self):
        if self.is_alive():
            creatures_around = self.look_around()
            if self._hunger > 5:
                if "stegosaurus" in [creature.type for creature in creatures_around]:
                    self.eat(creatures_around, "stegosaurus")
                elif "brontosaurus" in [creature.type for creature in creatures_around]:
                    self.eat(creatures_around, "brontosaurus")
            elif randint(1, 100) <= REPRODUCE_CHANCE:
                for creature in creatures_around:
                    if creature.type == "trex":
                        sex = "male" if self._sex == "female" else "female"
                        if creature.sex == sex:
                            self.reproduce()
            if randint(1, 100) <= CHANCE_TO_GO_AWAY:
                self.move()
                self._hunger += 1
            self._life_cycle = True
            self._health -= 2
            print(self._health)
        else:
            self.dying()

    def reproduce(self):
        empty_place = self._field.get_empty_place_near(
            self.x_position, self.y_position
        )
        if empty_place:
            self._field.append_creature(
                "trex",
                empty_place["x_pos"],
                empty_place["y_pos"],
            )

    def __str__(self):
        return '%'
