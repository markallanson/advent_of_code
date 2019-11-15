import input

two_sum = 0
three_sum = 0
for code in input.codes:
    char_counts = {code.count(char): 1 for char in code}
    two_sum += 1 if 2 in char_counts else 0
    three_sum += 1 if 3 in char_counts else 0

print(three_sum * two_sum)