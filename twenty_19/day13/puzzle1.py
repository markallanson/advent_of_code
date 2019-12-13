from twenty_19.day13 import input
from twenty_19.util import IntCodeComputer
from twenty_19.util.devices import FrameBuffer, GridScreen

framebuffer = GridScreen(100, 100)
IntCodeComputer(input.game_program, input_func=framebuffer.read, out_func=framebuffer.write).compute()
print(framebuffer.memory)