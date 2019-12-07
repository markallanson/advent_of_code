from twenty_19.day7 import Amplifier, IOBuffer

def input_from_output(output_func):
    return output_func()

def amplify(phases, input):
    io_buffers = []
    amplifiers = []
    bufNum = 0
    for phase in phases:
        if len(io_buffers) == 0:
            input_buffer = IOBuffer("IO" + str(bufNum))
            io_buffers.append(input_buffer)
        bufNum += 1
        output_buffer = IOBuffer("IO" + str(bufNum))
        io_buffers.append(output_buffer)

        amp = Amplifier(phase, io_buffers[bufNum - 1], io_buffers[bufNum])
        amplifiers.append(amp)

    ampNum = 0
    for amplifier in amplifiers:
        if ampNum == 0: amplifier.amplify(input)
        else: amplifier.amplify()
        ampNum += 1

    return io_buffers[-1].get_from_buffer()

amplifications = []
for a in range(0,5):
    for b in [_ for _ in range(0, 5) if _ != a]:
        for c in [_ for _ in range(0, 5) if _ != a and _ != b]:
            for d in [_ for _ in range(0, 5) if _ != a and _ != b and _ != c]:
                for e in [_ for _ in range(0, 5) if _ != a and _ != b and _ != c and _ != d]:
                    print("Amplifying ", a, b, c, d, e)
                    amplifications.append(amplify([a,b,c,d,e], 0))

print(max(amplifications))
