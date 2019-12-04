import itertools

def test_value(value):
    chars = str(value)
    grouped = itertools.groupby(chars, lambda c: c)
    has_double = len([k for (k,v) in grouped if len(list(v)) == 2]) > 0
    has_triple = len([k for (k,v) in grouped if len(list(v)) == 3]) > 0
    ever_increasing = True
    for i in range(1, len(chars)):
        if chars[i] < chars[i-1]:
            ever_increasing = False
            break
    return ever_increasing and has_double and not has_triple


possible_passwords = [value for value in range(240920, 789857) if test_value(value)]
print(len(possible_passwords))