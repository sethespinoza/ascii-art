from asciiart.images import load_image, get_pixel_matrix
from asciiart.converter import get_brightness_matrix


def main():
    image = load_image("images/ascii-pineapple.jpg")
    width, height = image.size
    print("Successfully loaded image!")
    print(f"Image size: {width} * {height}")
    print(f"Color mode: {image.mode}")

    matrix = get_pixel_matrix(image)
    print("Successfully constructed pixel matrix!")
    print(f"Pixel matrix size: {len(matrix[0])} * {len(matrix)}")
    print(f"Top-left pixel: {matrix[0][0]}")
    print(f"Bottom-right pixel: {matrix[-1][-1]}")

    brightness = get_brightness_matrix(matrix)
    print("Successfully constructed brightness matrix!")
    print(f"Brightness matrix size: {len(brightness[0])} * {len(brightness)}")
    print(f"Top-left brightness: {brightness[0][0]}")
    print(f"Bottom-right brightness: {brightness[-1][-1]}")


if __name__ == "__main__":
    main()