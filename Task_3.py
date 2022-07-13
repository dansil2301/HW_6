class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    #def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
    #    super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == "__main__":
    config = {'name': '', 'surname': '', 'position': '', 'wage': 0, 'bonus': 0}
    for field in config:
        phrase = f'Введите занчение поля {field}: '
        config[field] = input(phrase) if field != 'wage' and field != 'bonus' else float(input(phrase))

    pos = Position(config['name'], config['surname'], config['position'], config['wage'], config['bonus'])

    print(pos.get_full_name())
    print(pos.get_total_income())
