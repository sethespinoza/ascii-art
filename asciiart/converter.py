CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def average_brightness(pixel):
    r, g, b = pixel
    return (r + g + b) // 3

    
def get_brightness_matrix(pixel_matrix):
    result = []
    for row in pixel_matrix:
        new_row = []
        for pixel in row:
            new_row.append(average_brightness(pixel))
        result.append(new_row)
    return result

def brightness_to_char(brightness):
    index = brightness * len(CHARS) // 256
    return CHARS[index]

def get_ascii_matrix(brightness_matrix):
    result = []
    for row in brightness_matrix:
        char_row = []
        for b in row:
            char_row.append(brightness_to_char(b))
        result.append(char_row)
    return result

        