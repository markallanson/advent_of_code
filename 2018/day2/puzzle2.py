import input
#some o(n2) love
for check_code in input.codes:
    for match_code in input.codes:
        d = list(zip(check_code, match_code))
        diffs = sum([0 if key == value else 1 for key, value in d])
        if diffs == 1:
            print("".join([key for key, value in d if key == value]))
            exit()
