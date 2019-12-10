import itertools
import math
from math import floor

from twenty_19.day10 import input
from twenty_19.day10 import *

# https://math.stackexchange.com/a/1596518
def calculate_angle_between_co_ords(co_ord, terminal_co_ord):
    t = math.atan2(terminal_co_ord[0] - co_ord[0], co_ord[1] - terminal_co_ord[1])
    if t < 0:
        t = t + (2 * math.pi)
    return t

# determine the unique set of angles between the source co-ordinate and
# all other asteroid co-ordinates
def count_visible(map, co_ord):
    angles = set()
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == "#" and co_ord != (x, y):
                angles.add(calculate_angle_between_co_ords(co_ord, (x, y)))
    return len(angles)

# returns the co-ordinate of the most suitable for the new base
def get_most_suitable_asteroid(map):
    counts = {}
    for yi in range(0, len(map)):
        y = map[yi]
        for xi in range(0, len(y)):
            x = y[xi]
            if x == "#":
                counts[count_visible(map, (xi, yi))] = (xi, yi)

    return (counts[max(counts.keys())], max(counts.keys()))

map_grid = to_grid(input.asteroid_map)
render(map_grid)

best_asteroid = get_most_suitable_asteroid(map_grid)
print(best_asteroid)











