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

    def dump_memory(self):
        return self.memory


class Joystick(IODevice):
    """ You can use this to manually play the game for day13 if you like, but it's tedious """
    def read(self):
        while (True):
            direction = input("Dir: ")
            if direction == "a":
                return -1
            if direction == "d":
                return 1
            if direction == "w":
                return 0
