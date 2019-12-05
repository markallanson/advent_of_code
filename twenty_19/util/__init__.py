import sys
from enum import Enum

debug = sys.settrace is not None

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


class Add(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        a = self.read(memory, memory[instruction_pointer + 1], op_meta.pmodes[0])
        b = self.read(memory, memory[instruction_pointer + 2], op_meta.pmodes[1])
        result = a + b
        if debug:
            print("Add {} + {} = {}".format(a, b, result))
        self.write(memory, memory[instruction_pointer + 3], result)
        return instruction_pointer + 4


class Multiply(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        a = self.read(memory, memory[instruction_pointer + 1], op_meta.pmodes[0])
        b = self.read(memory, memory[instruction_pointer + 2], op_meta.pmodes[1])
        result = a * b
        if debug:
            print("Mul {} * {} = {}".format(a, b, result))
        self.write(memory, memory[instruction_pointer + 3], result)
        return instruction_pointer + 4


class Input(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        val = int(input("Input: "))
        self.write(memory, memory[instruction_pointer + 1], val)
        return instruction_pointer + 2


class Output(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        val = self.read(memory, memory[instruction_pointer + 1], op_meta.pmodes[0])
        print("Output: ", val)
        return instruction_pointer + 2


class Term(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        if debug:
            print("TERM")
        return -1

class JumpIfTrue(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        a = self.read(memory, memory[instruction_pointer + 1], op_meta.pmodes[0])
        b = self.read(memory, memory[instruction_pointer + 2], op_meta.pmodes[1])
        is_true = a != 0
        if debug:
            print("Is True? {} != 0 == {}".format(a, is_true))
        if is_true:
            return b
        return instruction_pointer + 3

class JumpIfFalse(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        a = self.read(memory, memory[instruction_pointer + 1], op_meta.pmodes[0])
        b = self.read(memory, memory[instruction_pointer + 2], op_meta.pmodes[1])
        is_false = a == 0
        if debug:
            print("Is False? {} == 0 == {}".format(a, is_false))
        if is_false:
            return b
        return instruction_pointer + 3


class Equals(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        a = self.read(memory, memory[instruction_pointer + 1], op_meta.pmodes[0])
        b = self.read(memory, memory[instruction_pointer + 2], op_meta.pmodes[1])
        are_equal = a == b
        if debug:
            print("Are Equal? {} == {} == {}".format(a, b, are_equal))
        self.write(memory, memory[instruction_pointer + 3], 1 if are_equal else 0)
        return instruction_pointer + 4


class LessThan(Instruction):
    def execute(self, memory, op_meta, instruction_pointer):
        a = self.read(memory, memory[instruction_pointer + 1], op_meta.pmodes[0])
        b = self.read(memory, memory[instruction_pointer + 2], op_meta.pmodes[1])
        less_than = a < b
        if debug:
            print("Less Than? {} < {} == {}".format(a, b, less_than))
        self.write(memory, memory[instruction_pointer + 3], 1 if less_than else 0)
        return instruction_pointer + 4


class IntCodeComputer:
    def __init__(self, memory):
        self.memory = list(memory)

        self.instructions = {
            Instructions.ADD: Add(),
            Instructions.MUL: Multiply(),
            Instructions.INPUT: Input(),
            Instructions.OUTPUT: Output(),
            Instructions.JMP_TRUE: JumpIfTrue(),
            Instructions.JMP_FALSE: JumpIfFalse(),
            Instructions.LESS_THAN: LessThan(),
            Instructions.EQUALS: Equals(),
            Instructions.TERM: Term()
        }

    def compute(self, input=None):
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