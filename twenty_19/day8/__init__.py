from twenty_19.day8 import input

def get_layers(image_data, width, height):
    pixels_per_layer = width * height
    layer_count = int(len(image_data) / pixels_per_layer)
    layers = [[] for layer in range(0, layer_count)]
    for l in range(0, layer_count):
        for p in range(0, width * height):
            layers[l].append(image_data[(l * pixels_per_layer) + p])
    return layers


