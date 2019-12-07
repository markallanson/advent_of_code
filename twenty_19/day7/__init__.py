from queue import Queue
from twenty_19.util import IntCodeComputer
from twenty_19.day7.input import amp_program

class IOBuffer:
    """ Simple queued IO buffer for reading inputs and writing outputs"""
    def __init__(self, name):
        self.name = name
        self.buffer = Queue()

    def get_from_buffer(self):
        # print("{}RWAIT".format(self.name))
        val = self.buffer.get(True)
        # print("{}R{}".format(self.name, val))
        return val

    def write_to_buffer(self, val):
        # print("{}W{}".format(self.name, val))
        self.buffer.put(val)

class Amplifier:
    def __init__(self, input, input_buffer, output_buffer):
        self.input_buffer = input_buffer
        self.input_buffer.write_to_buffer(input)

        self.computer = IntCodeComputer(
            amp_program,
            # [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0],
            input_buffer.get_from_buffer,
            output_buffer.write_to_buffer
        )

    def amplify(self, initial_input=None):
        if initial_input is not None:
            self.input_buffer.write_to_buffer(initial_input)
        self.computer.compute()

