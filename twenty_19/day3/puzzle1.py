from twenty_19.day3 import input

def calc_co_ord(co_ord, move):
    """ converts a move into new co-ordinates using the supplied co-ordinate as a base reference """
    move_co_ords = [co_ord]
    for i in range(1, int(move[1:]) + 1):
        if move[:1] == 'U':
            move_co_ords.append((co_ord[0], move_co_ords[-1][1] - 1))
        if move[:1] == 'D':
            move_co_ords.append((co_ord[0], move_co_ords[-1][1] + 1))
        if move[:1] == 'L':
            move_co_ords.append((move_co_ords[-1][0] - 1, co_ord[1]))
        if move[:1] == 'R':
            move_co_ords.append((move_co_ords[-1][0] + 1, co_ord[1]))
    return move_co_ords[1:]

def to_co_ords(moves):
    """ converts a list of moves from the central port into a list of co-ordinates using central port as a reference """
    co_ords = set()
    last_co_ord = (0, 0)
    for move in moves:
        new_co_ords = calc_co_ord(last_co_ord, move)
        last_co_ord = new_co_ords[-1]
        co_ords.update(new_co_ords)
    return co_ords


w1_co_ords = to_co_ords(input.wire1)
w2_co_ords = to_co_ords(input.wire2)
crossovers = [co_ord for co_ord in w1_co_ords if co_ord in w2_co_ords]
distances = [abs(crossover[0]) + abs(crossover[1]) for crossover in crossovers]
print(min(distances))