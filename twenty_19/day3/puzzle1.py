from twenty_19.day3 import input
from twenty_19.day3 import distance

crossovers = distance.get_crossovers(input.wire1, input.wire2)
distances = [abs(crossover[0]) + abs(crossover[1]) for crossover in crossovers]
print(min(distances))