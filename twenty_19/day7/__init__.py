from threading import Thread
from twenty_19.util import IntCodeComputer
from twenty_19.day7.input import amp_program

class Amplifier:
    def __init__(self, input, input_buffer, output_buffer, term_func=None):
        self.input_buffer = input_buffer
        self.input_buffer.write(input)
        self.term_func = term_func
        self.computer = IntCodeComputer(
            amp_program,
            input_buffer.read,
            output_buffer.write
        )
        Thread(target=self.run).start()

    def run(self):
        out = self.computer.compute()
        if self.term_func:
            self.term_func(out)

