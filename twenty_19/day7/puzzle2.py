from twenty_19.day7 import Amplifier
from twenty_19.util.devices import IOBuffer

amplifications = []


def amplify(phases, input):
    io_buffers = [IOBuffer("IO" + str(phase)) for phase in phases]
    amplifiers = []
    for i in range(0, len(phases)):
        phase = phases[i]
        in_buf = io_buffers[i]
        if i == len(phases) - 1:
            # loop the output buffer of the phase amplifier to the input buffer of the first
            out_buf = io_buffers[0]
        else:
            out_buf = io_buffers[i + 1]
        amp = Amplifier(
            phase,
            in_buf,
            out_buf,
            lambda x: final_value(io_buffers[0].read()) if i == len(phases) - 1 else None)
        amplifiers.append(amp)

    # kick off processing by applying the input.
    io_buffers[0].write(input)


def final_value(value):
    amplifications.append(value)
    print(max(amplifications))

for a in range(5, 10):
    for b in [_ for _ in range(5, 10) if _ != a]:
        for c in [_ for _ in range(5, 10) if _ != a and _ != b]:
            for d in [_ for _ in range(5, 10) if _ != a and _ != b and _ != c]:
                for e in [_ for _ in range(5, 10) if _ != a and _ != b and _ != c and _ != d]:
                    amplify([a,b,c,d,e], 0)

# amplify([9,7,8,5,6], 0)

