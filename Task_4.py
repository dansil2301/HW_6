class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = bool(is_police)

    def go(self, g: bool):
        print('Машина поехала' if g else 'Машина стоит')

    def stop(self, s: bool):
        print('Машина стоит' if s else 'Машина едет')

    def turn(self, side: str):
        print(f'Машина повернула {side}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed if self.speed <= 60 else 'Скорость превышена')


class SportCar(Car):
    #def __init__(self, speed, color, name, is_police):
    #    super().__init__(speed, color, name, is_police)
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.speed if self.speed <= 40 else 'Скорость превышена')


class PoliceCar(Car):
    #def __init__(self, speed, color, name, is_police):
    #    super().__init__(speed, color, name, is_police)
    pass


if __name__ == "__main__":
    config = {'speed': 0, 'color': '', 'name': '', 'is_police': True}
    for field in config:
        config[field] = input(f'Введите занчение поля {field}: ')

    car1 = TownCar(config['speed'], config['color'], config['name'], config['is_police'])

    car1.show_speed()
    car1.go(bool(input('Машина едет или нет? (True, False): ')))
    car1.stop(bool(input('Машина стоит или нет? (True, False): ')))
    car1.turn(input('Куда машина поворачивает?: '))

    car2 = WorkCar(config['speed'], config['color'], config['name'], config['is_police'])

    car2.show_speed()
    car2.go(bool(input('Машина едет или нет? (True, False): ')))
    car2.stop(bool(input('Машина стоит или нет? (True, False): ')))
    car2.turn(input('Куда машина поворачивает?: '))

    car3 = SportCar(config['speed'], config['color'], config['name'], config['is_police'])
    car2.go(bool(input('Машина едет или нет? (True, False): ')))
    car2.stop(bool(input('Машина стоит или нет? (True, False): ')))
    car2.turn(input('Куда машина поворачивает?: '))
