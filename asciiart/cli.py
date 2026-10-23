from asciiart.converter import (
    get_brightness_matrix, 
    get_ascii_matrix,
    ascii_matrix_to_text,
)
from asciiart.images import load_image, get_pixel_matrix, resize_image

WIDTH = 80
STRETCH = 2


def main():
    image = load_image("images/ascii-pineapple.jpg")
    image = resize_image(image, WIDTH)
    pixels = get_pixel_matrix(image)
    brightness = get_brightness_matrix(pixels)
    ascii_matrix = get_ascii_matrix(brightness)
    print(ascii_matrix_to_text(ascii_matrix, STRETCH))


    # width, height = image.size
    # print("Successfully loaded image!")
    # print(f"Image size: {width} * {height}")
    # print(f"Color mode: {image.mode}")

    # matrix = get_pixel_matrix(image)
    # print("Successfully constructed pixel matrix!")
    # print(f"Pixel matrix size: {len(matrix[0])} * {len(matrix)}")
    # print(f"Top-left pixel: {matrix[0][0]}")
    # print(f"Bottom-right pixel: {matrix[-1][-1]}")

    # brightness = get_brightness_matrix(matrix)
    # print("Successfully constructed brightness matrix!")
    # print(f"Brightness matrix size: {len(brightness[0])} * {len(brightness)}")
    # print(f"Top-left brightness: {brightness[0][0]}")
    # print(f"Bottom-right brightness: {brightness[-1][-1]}")

    # ascii_matrix = get_ascii_matrix(brightness)
    # print("Successfully constructed ASCII matrix!")
    # print(f"ASCII matrix size: {len(ascii_matrix[0])} x {len(ascii_matrix)}")
    # print("First 20 characters of row 0:", "".join(ascii_matrix[0][:20]))

if __name__ == "__main__":
    main()