class Road:
    def __init__(self, width, length):
        self._length = length
        self._width = width

    def weight(self, weight_square_meter, thickness):
        return self._width * self._length * weight_square_meter * thickness


if __name__ == "__main__":
    road = Road(20, 5000)

    print(road.weight(25, 5))
