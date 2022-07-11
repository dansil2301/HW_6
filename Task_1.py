from time import sleep


class TrafficLight:
    __color = 'Красный'

    def running(self):
        print(TrafficLight.__color)
        sleep(7)
        TrafficLight.__color = 'Желтый'
        print(TrafficLight.__color)
        sleep(2)
        TrafficLight.__color = 'Зеленый'
        print(TrafficLight.__color)
        sleep(5)
        TrafficLight.__color = 'Красный'


if __name__ == "__main__":
    traffic = TrafficLight()

    traffic.running()
