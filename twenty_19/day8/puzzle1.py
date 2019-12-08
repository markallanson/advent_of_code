from twenty_19.day8 import input
from twenty_19.day8 import get_layers

layers = get_layers(input.image, 25, 6)
print(layers)

a = [(layer,
  len([p for p in layer if p == 0]),
  len([p for p in layer if p == 1]) * len([p for p in layer if p == 2]))
 for layer in layers]

for b in a:
    print(b[1], b[2])
