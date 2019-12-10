def to_grid(map):
    map_grid = []
    for line in map:
        map_grid.append([c for c in line])
    return map_grid

def render(map):
    for x in map:
        print("".join(x))
