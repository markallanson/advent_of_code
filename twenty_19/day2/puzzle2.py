from twenty_19.day2.input import memory
from twenty_19.util import IntCodeComputer

for noun in range(0, 99):
    for verb in range(0, 99):
        program = list(memory)
        program[1] = noun
        program[2] = verb
        if IntCodeComputer(program).compute() == 19690720:
            print((100 * noun) + verb)
            break