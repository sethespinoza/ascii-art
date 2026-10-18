from asciiart.images import load_image


def main():
    image = load_image("images/ascii-pineapple.jpg")
    width, height = image.size
    print("Successfully loaded image!")
    print(f"Image size: {width} * {height}")
    print(f"Color mode: {image.mode}")


if __name__ == "__main__":
    main()