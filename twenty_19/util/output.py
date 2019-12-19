default_display = {
    1: "█",
    2: "*"
}

class ImagePrinter:
    def __init__(self, width, height, value_display_dict=default_display, default_char=" "):
        self.width = width
        self.height = height
        self.value_display_dict = value_display_dict
        self.default_char = default_char

    def print(self, image):
        for y in range(0, self.height):
            scan_line = []
            for x in range(0, self.width):
                pixel_index = (y * self.width) + x
                pixel = image[pixel_index]
                display_char = self.default_char
                if pixel in self.value_display_dict:
                    display_char = self.value_display_dict[pixel]
                scan_line.append(display_char)
            print("".join(scan_line))
