from twenty_19.day15 import input
from twenty_19.util import IntCodeComputer
from twenty_19.day15 import Navigator

navigator = Navigator(50, 50)
IntCodeComputer(input.game_program, input_func=navigator.read, out_func=navigator.write).compute()
