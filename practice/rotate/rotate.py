"""Opens an image, rotates it, and outputs an image"""

from PIL import Image
import sys


def input_image():
    """Imports image to be modified into application."""
    return Image.open(sys.argv[1])


def rotate(image):
    """Rotates image 45 degrees"""
    return image.rotate(45)gi


def save(image):
    """Saves image into a file."""
    image.save(sys.argv[2])


def main():
    """Main."""
    image = input_image()
    rotated_image = rotate(image)
    save(rotated_image)


if __name__ == '__main__':
    main()
