class FieldInterface:

    def __init__(self, field) -> None:
        self._field = field

    def show_field(self) -> None:
        creatures = self._field.environment
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