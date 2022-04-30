from random import randint

import Field


REPRODUCE_CHANCE = 25


class Plant:

    def __init__(self, field: Field, pos_x: int, pos_y: int):
        self._type = 'plant'
        self._health: int = 50
        self._life_cycle: bool = False
        self._field: Field = field
        self._x_position: int = pos_x
        self._y_position: int = pos_y

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

    def is_alive(self):
        return self._health > 0

    def dying(self):
        self._field.environment[self.x_position][self.y_position] = None
        del self

    def make_decision(self):
        if self.is_alive():
            if randint(1, 100) <= REPRODUCE_CHANCE:
                self.reproduce()
            self._life_cycle = True
            self._health -= 5
            print(self._health)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        else:
            self.dying()

    def reproduce(self):
        empty_place = self._field.get_empty_place_near(
            self.x_position, self.y_position
        )
        if empty_place:
            self._field.append_creature(
                "plant",
                empty_place["x_pos"],
                empty_place["y_pos"],
            )

    def __str__(self) -> str:
        return '!'
