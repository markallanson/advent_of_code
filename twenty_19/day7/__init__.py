from queue import Queue
from threading import Thread
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
    def __init__(self, input, input_buffer, output_buffer, term_func=None):
        self.input_buffer = input_buffer
        self.input_buffer.write_to_buffer(input)
        self.term_func = term_func
        self.computer = IntCodeComputer(
            amp_program,
            input_buffer.get_from_buffer,
            output_buffer.write_to_buffer
        )
        Thread(target=self.run).start()

    def run(self):
        out = self.computer.compute()
        if self.term_func:
            self.term_func(out)

