class Cycle:
    def __init__(self, field) -> None:
        self._field = field

    def life(self):
        creatures = self._field.environment
        for line in creatures:
            for creature in line:
                if creature:
                    if not creature.life_cycle:
                        creature.make_decision()
        for line in creatures:
            for creature in line:
                if creature:
                    creature.life_cycle = False
