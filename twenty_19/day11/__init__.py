import itertools
from enum import IntEnum
from math import floor
from twenty_19.day8 import print_image


class Mode(IntEnum):
    PAINT = 0
    MOVE = 1


class Compass(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def cw(self):
        return Compass(int(self.value) + 1) if int(self) < int(Compass.WEST) else Compass.NORTH

    def ccw(self):
        return Compass(int(self.value) - 1) if int(self) > int(Compass.NORTH) else Compass.WEST


class Canvas:
    def __init__(self, size):
        self.canvas_size = size
        self.direction = Compass.NORTH
        self.curr = (floor(size/2), floor(size/2))
        self.canvas = [[0] * size for i in range(0, size)]
        self.mode = Mode.PAINT
        self.painted = set()

    def write(self, value):
        if self.mode == Mode.PAINT:
            self.painted.add(self.curr)
            self.paint(value)
            self.mode = Mode.MOVE
        elif self.mode == Mode.MOVE:
            self.move(value)
            self.mode = Mode.PAINT

    def paint(self, value):
        print("Paint: {} @ {}".format(value, self.curr))
        self.canvas[self.curr[1]][self.curr[0]] = value

    def move(self, value):
        self.direction = self.new_direction(value)
        old_pos = self.curr
        if self.direction == Compass.NORTH:
            self.curr = (self.curr[0], self.curr[1] - 1)
        elif self.direction == Compass.WEST:
            self.curr = (self.curr[0] - 1, self.curr[1])
        elif self.direction == Compass.SOUTH:
            self.curr = (self.curr[0], self.curr[1] + 1)
        elif self.direction == Compass.EAST:
            self.curr = (self.curr[0] + 1, self.curr[1])
        else:
            raise ValueError("Unknown Move Direction")
        print("Move {} from {} to {}".format(self.direction.name, old_pos, self.curr))

    def new_direction(self, value):
        if value == 0:
            return self.direction.ccw()
        elif value == 1:
            return self.direction.cw()
        raise ValueError("Don't know what way to turn for value {}".format(value))

    def read(self):
        return self.canvas[self.curr[1]][self.curr[0]]

    def print(self):
        print_image(list(itertools.chain.from_iterable(self.canvas)), self.canvas_size, self.canvas_size)

