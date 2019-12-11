from twenty_19.day11 import input, Canvas
from twenty_19.util import IntCodeComputer

canvas = Canvas()
IntCodeComputer(input.painter_program, input_func=canvas.read, out_func=canvas.write).compute()
canvas.print()
print(len(canvas.painted))