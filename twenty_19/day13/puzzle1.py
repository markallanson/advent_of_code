from twenty_19.day13 import input
from twenty_19.util import IntCodeComputer
from twenty_19.day13 import GamePlayerDevice

player = GamePlayerDevice(100, 100)
IntCodeComputer(input.game_program, input_func=player.read, out_func=player.write).compute()
print(player.memory)