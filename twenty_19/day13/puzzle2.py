from twenty_19.day13 import input
from twenty_19.util import IntCodeComputer
from twenty_19.day13 import GamePlayerDevice

player_device = GamePlayerDevice(40, 24)
computer = IntCodeComputer(input.game_program, input_func=player_device.read, out_func=player_device.write)
computer.memory.heap[0] = 2
computer.compute()
print(player_device.memory)
print("Final Score:", player_device.score)