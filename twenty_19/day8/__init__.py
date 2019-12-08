from twenty_19.day8 import input

def get_layers(image_data, width, height):
    pixels_per_layer = width * height
    for i in range(0, len(image_data), pixels_per_layer):
        yield image_data[i:i + pixels_per_layer]
