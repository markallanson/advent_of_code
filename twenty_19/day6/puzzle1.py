from twenty_19.day6 import input
from twenty_19.day6 import orbit_tools

tree = orbit_tools.build_orbit_tree(input.orbits)
print(orbit_tools.count(tree))