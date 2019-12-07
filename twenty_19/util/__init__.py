import sys
import abc
from enum import Enum

#debug = sys.settrace is not None
debug = False


class Instructions(Enum):
    ADD = 1
    MUL = 2
    INPUT = 3
    OUTPUT = 4
    JMP_TRUE = 5
    JMP_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    TERM = 99

    def __str__(self):
        return self.name


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1

    def __repr__(self):
        return self.name


class OpMeta:
    def __init__(self, instruction):
        str_instruction = "{:05}".format(instruction)
        self.opcode = Instructions(int(str_instruction[-2:]))
        self.pmodes = [
            ParameterMode(int(str_instruction[2])),
            ParameterMode(int(str_instruction[1])),
            ParameterMode(int(str_instruction[0])),
        ]
        if (debug):
            print("OpMeta: ", str(self))

    def __str__(self):
        return "OpCode: {}, PMode: {}".format(self.opcode, self.pmodes)

class Instruction:
    """ Base class for all instruction implementation. Contains common instruction functionality """
    def __init__(self, param_count=0):
        self.param_count = param_count

    def read_params(self, memory, instruction_pointer, op_meta):
        return [
            self.read(memory, memory[instruction_pointer + param_num], op_meta.pmodes[param_num - 1])
            for param_num
            in range(1, self.param_count + 1)
        ]

    def write(self, memory, address, value):
        existing = memory[address]
        if debug:
            print("Write: &{}, '{} -> {}'".format(address, existing, value))
        memory[address] = value

    def read(self, memory, address, pmode):
        if pmode == ParameterMode.POSITION:
            value = memory[address]
        elif pmode == ParameterMode.IMMEDIATE:
            value = address
        else:
            raise ValueError("Parameter Mode {} is not supported".format(pmode))
        if debug:
            print("Read: &{} = {}".format(address, value))
        return value


class ReadWriteInstruction(Instruction, metaclass=abc.ABCMeta):
    """
    A common base method for simple instructions that read and write values from memory without fiddling with
    the instruction pointer.
    """
    def __init__(self, param_count=0):
        super().__init__(param_count)

    def execute(self, memory, op_meta, instruction_pointer):
        params = self.read_params(memory, instruction_pointer, op_meta)
        result = self.calculate(params)
        if result is not None:
            self.write(memory, memory[instruction_pointer + self.param_count + 1], result)
            return instruction_pointer + self.param_count + 2
        return instruction_pointer + self.param_count + 1

    @abc.abstractmethod
    def calculate(self, params):
        """calculate the value and return the result. Return none if no result"""


class Add(ReadWriteInstruction):
    def __init__(self):
        super().__init__(2)

    def calculate(self, params):
        result = params[0] + params[1]
        if debug:
            print("Add {} + {} = {}".format(params[0], params[1], result))
        return result

class Multiply(ReadWriteInstruction):
    def __init__(self):
        super().__init__(2)

    def calculate(self, params):
        result = params[0] * params[1]
        if debug:
            print("Mul {} * {} = {}".format(params[0], params[1], result))
        return result


class Input(ReadWriteInstruction):
    def __init__(self, input_func):
        super().__init__()
        self.input_func = input_func

    def calculate(self, params):
        return int(self.input_func())


class Output(ReadWriteInstruction):
    def __init__(self, out_func):
        super().__init__(1)
        self.out_func = out_func

    def calculate(self, params):
        self.out_func(params[0])


class Term(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        if debug:
            print("TERM")
        return -1


class JumpIfTrue(Instruction):
    def __init__(self):
        super().__init__(2)

    def execute(self, memory, op_meta, instruction_pointer):
        input = self.read_params(memory, instruction_pointer, op_meta)
        is_true = input[0] != 0
        if debug:
            print("Is True? {} != 0 == {}".format(input[0], is_true))
        if is_true:
            return input[1]
        return instruction_pointer + 3


class JumpIfFalse(Instruction):
    def __init__(self):
        super().__init__(2)

    def execute(self, memory, op_meta, instruction_pointer):
        input = self.read_params(memory, instruction_pointer, op_meta)
        is_false = input[0] == 0
        if debug:
            print("Is False? {} == 0 == {}".format(input[0], is_false))
        if is_false:
            return input[1]
        return instruction_pointer + 3


class Equals(ReadWriteInstruction):
    def __init__(self):
        super().__init__(2)

    def calculate(self, params):
        are_equal = params[0] == params[1]
        if debug:
            print("Are Equal? {} == {} == {}".format(params[0], params[1], are_equal))
        return 1 if are_equal else 0


class LessThan(ReadWriteInstruction):
    def __init__(self):
        super().__init__(2)

    def calculate(self, params):
        less_than = params[0] < params[1]
        if debug:
            print("Less Than? {} < {} == {}".format(params[0], params[1], less_than))
        return 1 if less_than else 0


def print_output(output):
    print("Output: ", output)

def console_input():
    return input("Input: ")

class IntCodeComputer:
    def __init__(self, memory, input_func=console_input, out_func=print_output):
        self.memory = list(memory)

        self.instructions = {
            Instructions.ADD: Add(),
            Instructions.MUL: Multiply(),
            Instructions.INPUT: Input(input_func),
            Instructions.OUTPUT: Output(out_func),
            Instructions.JMP_TRUE: JumpIfTrue(),
            Instructions.JMP_FALSE: JumpIfFalse(),
            Instructions.LESS_THAN: LessThan(),
            Instructions.EQUALS: Equals(),
            Instructions.TERM: Term()
        }


    def compute(self):
        """ Computes and intprogram """
        instruction_pointer = 0
        while True:
            if debug:
                print(self.memory)
            op_meta = OpMeta(self.memory[instruction_pointer])
            if op_meta.opcode not in self.instructions.keys():
                raise AssertionError("Unknown Instruction '{}'".format(op_meta))
            instr_func = self.instructions[op_meta.opcode]
            instruction_pointer = instr_func.execute(self.memory, op_meta, instruction_pointer)
            if instruction_pointer == -1:
                return self.memory[0]