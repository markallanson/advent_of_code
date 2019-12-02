import input
from math import floor

def calc_fuel(mass):
    fuel_mass = floor(mass / 3) - 2
    if fuel_mass > 0:
        return fuel_mass + calc_fuel(fuel_mass)
    return 0


print(sum([calc_fuel(mass) for mass in input.module_masses]))