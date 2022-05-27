from Field.field import Field


class FieldInterface:

    def __init__(self, field: Field) -> None:
        self._field = field

    def show_field(self) -> None:
        creatures = self._field._environment
        print('_' * 35, end='\n\n')
        for line in creatures:
            print('|', end='  ')
            for creature in line:
                if creature:
                    print(creature, end=' ')
                else:
                    print(' ', end=' ')
            print(' |')
        print('_' * 35)
