from PIL import Image


def load_image(path):
    return Image.open(path)

def get_pixel_matrix(image):
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(pixels[x, y])
        matrix.append(row)
    return matrix

def resize_image(image, new_width):
    width, height = image.size
    new_height = max(1, round(height * new_width / width))
    return image.resize((new_width, new_height))