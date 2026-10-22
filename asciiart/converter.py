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