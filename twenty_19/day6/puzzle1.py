from twenty_19.day6 import input

class Orbit:
    def __init__(self, name):
        self.name = name
        self.orbitors = []
        self.parent = None

    def __str__(self):
        return "{}({})->{}".format(self.name, len(self.orbitors), self.parent.name if self.parent else '')

    def __repr__(self):
        return str(self)


def find(orbit_tree, orbit_name):
    if orbit_tree.name == orbit_name:
        return orbit_tree
    for orbit in orbit_tree.orbitors:
        found_orbit = find(orbit, orbit_name)
        if found_orbit:
            return found_orbit


def count_parents(orbit):
    print(print_parents(orbit))
    num = 0
    parent = orbit.parent
    while parent is not None:
        num += 1
        parent = parent.parent
    return num


def count(orbit):
    num = count_parents(orbit)
    for orbitor in orbit.orbitors:
        num += count(orbitor)
    return num


def print_parents(orbit):
    if orbit.parent is not None:
        return "{} -> {}".format(orbit.name, print_parents(orbit.parent))
    return orbit.name


def build_orbit_tree(orbit_tokens):
    """Builds out all the orbits in a tree structure and returns the COM orbit"""
    orbit_map = {}
    for orbit_token in orbit_tokens:
        split_orbit = orbit_token.split(")")
        orbit_name = split_orbit[0]
        orbitor_name = split_orbit[1]

        # if no orbit exists, create it
        if orbit_name not in orbit_map:
            orbit_map[orbit_name] = Orbit(orbit_name)

        # if no orbitor exits, create it
        if orbitor_name not in orbit_map:
            orbit_map[orbitor_name] = Orbit(orbitor_name)

        # parent the orbitor to the orbit
        orbit_map[orbitor_name].parent = orbit_map[orbit_name]

        # add the orbitor to the orbits list of orbitors
        orbit_map[orbit_name].orbitors.append(orbit_map[orbitor_name])

    return orbit_map["COM"]

tree = build_orbit_tree(input.orbits)
print(count(tree))