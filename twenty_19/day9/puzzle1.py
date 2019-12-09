from twenty_19.day9 import input
from twenty_19.util import IntCodeComputer
from twenty_19.util import IOBuffer

io = IOBuffer("io1")
io.write(1)
IntCodeComputer(input.boost_program, input_func=io.read).compute()