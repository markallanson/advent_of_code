from twenty_19.day3 import input
from twenty_19.day3 import distance

def distance_to_co_ord(co_ords, crossover):
    distance = 0
    for co_ord in co_ords:
        distance += 1
        if co_ord == crossover:
            return distance

w1_co_ords = distance.to_co_ords(input.wire1)
w2_co_ords = distance.to_co_ords(input.wire2)

crossovers = distance.get_crossovers(input.wire1, input.wire2)
wire_distances = [distance_to_co_ord(w1_co_ords, crossover) + distance_to_co_ord(w2_co_ords, crossover) for crossover in crossovers]
print(min(wire_distances))