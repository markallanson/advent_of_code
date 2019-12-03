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
    co_ords = [(0, 0)]
    for move in moves:
        co_ords.extend(calc_co_ord(co_ords[-1], move))
    return co_ords[1:]

def get_crossovers(wire1, wire2):
    """ gets the crossover points for 2 wires """
    w1_co_ords = to_co_ords(wire1)
    w2_co_ords = to_co_ords(wire2)
    w2_set = set(w2_co_ords)
    return [co_ord for co_ord in set(w1_co_ords) if co_ord in w2_set]