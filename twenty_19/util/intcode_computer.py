def _add(memory, instruction_pointer):
    a_pos = memory[instruction_pointer + 1]
    b_pos = memory[instruction_pointer + 2]
    result_pos = memory[instruction_pointer + 3]
    memory[result_pos] = memory[a_pos] + memory[b_pos]
    return instruction_pointer + 4

def _mul(memory, instruction_pointer):
    a_pos = memory[instruction_pointer + 1]
    b_pos = memory[instruction_pointer + 2]
    result_pos = memory[instruction_pointer + 3]
    memory[result_pos] = memory[a_pos] * memory[b_pos]
    return instruction_pointer + 4

def _term(memory, address):
    pass

instructions = {
    1: _add,
    2: _mul,
    99: _term
}

def compute(initial_memory):
    """ Computes and intprogram """
    memory = list(initial_memory)
    instruction_pointer = 0
    while True:
        instruction = memory[instruction_pointer]
        instr_func = instructions[instruction]
        if not instr_func:
            raise AssertionError("Unknown Instruction '{}'".format(instruction))
        if instr_func == _term:
            return memory[0]
        instruction_pointer = instr_func(memory, instruction_pointer)
