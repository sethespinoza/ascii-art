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