from twenty_19.day9 import input
from twenty_19.util import IntCodeComputer
from twenty_19.util.devices import IOBuffer

io = IOBuffer("io1")
io.write(2)
IntCodeComputer(input.boost_program, input_func=io.read).compute()