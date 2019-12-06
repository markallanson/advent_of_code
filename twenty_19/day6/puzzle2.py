from twenty_19.day6 import input
from twenty_19.day6 import orbit_tools

def find(orbit, orbit_name):
    if orbit.name == orbit_name:
        return orbit
    for orbitor in orbit.orbitors:
        found_orbit = find(orbitor, orbit_name)
        if found_orbit is not None:
            return found_orbit
    return None


def has_parent_orbit(orbit, parent_name):
    parent = orbit.parent
    while parent is not None:
        if parent.name == parent_name:
            return True
        parent = parent.parent
    return False

def hops_to_common_root(orbit_a, orbit_b):
    hop_num = 0
    parent = orbit_a.parent
    while parent is not None:
        hop_num += 1
        if has_parent_orbit(orbit_b, parent.name):
            break
        parent = parent.parent
    return hop_num

com_orbit = orbit_tools.build_orbit_tree(input.orbits)

san_orbit = find(com_orbit, "SAN")
you_orbit = find(com_orbit, "YOU")
print(hops_to_common_root(san_orbit, you_orbit) + hops_to_common_root(you_orbit, san_orbit) - 2)
