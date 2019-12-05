class Instruction:
    def __init__(self):
        pass


class Add(Instruction):
    def execute(self, memory, instruction_pointer):
        a_pos = memory[instruction_pointer + 1]
        b_pos = memory[instruction_pointer + 2]
        result_pos = memory[instruction_pointer + 3]
        memory[result_pos] = memory[a_pos] + memory[b_pos]
        return instruction_pointer + 4


class Multiply(Instruction):
    def execute(self, memory, instruction_pointer):
        a_pos = memory[instruction_pointer + 1]
        b_pos = memory[instruction_pointer + 2]
        result_pos = memory[instruction_pointer + 3]
        memory[result_pos] = memory[a_pos] * memory[b_pos]
        return instruction_pointer + 4


class Term(Instruction):
    def execute(self, memory, instruction_pointer):
        return -1

class IntCodeComputer:
    def __init__(self, memory):
        self.memory = list(memory)

        self.instructions = {
            1: Add(),
            2: Multiply(),
            99: Term()
        }

    def compute(self, input=None):
        """ Computes and intprogram """
        instruction_pointer = 0
        while True:
            instruction = self.memory[instruction_pointer]
            instr_func = self.instructions[instruction]
            if not instr_func:
                raise AssertionError("Unknown Instruction '{}'".format(instruction))
            instruction_pointer = instr_func.execute(self.memory, instruction_pointer)
            if instruction_pointer == -1:
                return self.memory[0]