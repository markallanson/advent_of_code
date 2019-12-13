from enum import Enum
from queue import Queue


class IODevice:
    def read(self):
        return None

    def write(self):
        pass


class IOBuffer(IODevice):
    """ Simple queued IO buffer for reading inputs and writing outputs"""
    def __init__(self, name):
        self.name = name
        self.buffer = Queue()

    def read(self):
        # print("{}RWAIT".format(self.name))
        val = self.buffer.get(True)
        # print("{}R{}".format(self.name, val))
        return val

    def write(self, val):
        # print("{}W{}".format(self.name, val))
        self.buffer.put(val)


class UserUI(IODevice):
    def read(self):
        return input("Input: ")

    def write(self, value):
        print("Output: ", value)


class FrameBuffer(IODevice):
    def __init__(self, size):
        self.memory = [0] * size

    def read(self):
        return 0

    def write(self, position, value):
        self.memory = self.memory[:position] + value + self.memory[position + len(value):]

class GridScreen(FrameBuffer):
    class Sprite:
        def __init__(self, repr):
            self.repr = repr

    def __init__(self, width, height):
        super().__init__(width * height)
        self.width = width
        self.height = height
        self.y = None
        self.x = None
        self.block_count = 0

        self.sprites = {
            0: self.Sprite([]),
            1: self.Sprite([1]),
            2: self.Sprite([1]),
            3: self.Sprite([1, 1]),
            4: self.Sprite([1])
        }

    def write(self, value):
        if self.x == None:
            self.x = value
        elif self.y == None:
            self.y = value
        else:
            print("{}x{}={}".format(self.x, self.y, value))
            if value == 2:
                self.block_count += 1
                print("Block Count: ", self.block_count)
            super().write((self.y * self.width) + self.x, self.sprites[value].repr)
            self.y = None
            self.x = None
