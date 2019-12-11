from twenty_19.day8 import input

def get_layers(image_data, width, height):
    pixels_per_layer = width * height
    for i in range(0, len(image_data), pixels_per_layer):
        yield image_data[i:i + pixels_per_layer]


def merge(layers, width, height):
    merged_image = [0] * (width * height)
    #iterate layers in reverse, only take the pixel in each layer if its not transparent
    for layer in reversed(layers):
        for pixel_index in range(0, len(layer)):
            if layer[pixel_index] != 2:
                merged_image[pixel_index] = layer[pixel_index]
    return merged_image

def print_image(image, width, height):
    for y in range(0, height):
        scan_line = []
        for x in range(0, width):
            pixel_index = (y * width) + x
            pixel = image[pixel_index]
            if pixel == 1:
                scan_line.append("█")
            else:
                scan_line.append(" ")
        print("".join(scan_line))
