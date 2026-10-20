from asciiart.images import load_image, get_pixel_matrix


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



if __name__ == "__main__":
    main()