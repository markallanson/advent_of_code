import input

position = 0
while True:
    op = input.ops[position]
    if op == 99:
        break

    a_pos = input.ops[position+1]
    b_pos = input.ops[position+2]
    result_pos = input.ops[position + 3]
    if op == 1:
        input.ops[result_pos] = input.ops[a_pos] + input.ops[b_pos]
    elif op == 2:
        input.ops[result_pos] = input.ops[a_pos] * input.ops[b_pos]
    position += 4


print(input.ops[0])
