from twenty_19.day8 import input
from twenty_19.day8 import get_layers, merge, print_image

layers = list(get_layers(input.image, 25, 6))
final_image = merge(layers, 25, 6)
print(final_image)
print_image(final_image, 25, 6)
