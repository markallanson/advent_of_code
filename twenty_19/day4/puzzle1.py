def test_value(value):
    chars = str(value)
    has_doubles = False
    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            has_doubles = True
        if chars[i] < chars[i-1]:
            return False
    return has_doubles

possible_passwords = [value for value in range(240920, 789857) if test_value(value)]
print(len(possible_passwords))