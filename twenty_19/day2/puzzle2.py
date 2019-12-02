from twenty_19.day2.input import memory
from twenty_19.util import intcode_computer

for noun in range(0, 99):
    for verb in range(0, 99):
        program = list(memory)
        program[1] = noun
        program[2] = verb
        if intcode_computer.compute(program) == 19690720:
            print((100 * noun) + verb)
            break;