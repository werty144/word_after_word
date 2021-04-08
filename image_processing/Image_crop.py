import pyscreenshot as ImageGrab
from image_processing.Constants import *


def grab_field():
    return ImageGrab.grab((top_left_corner_x, top_left_corner_y, bottom_right_corner_x, bottom_right_corner_y))


def crop_field(im):
    squares = []
    for i in range(5):
        squares.append([])
        for j in range(5):
            squares[i].append(im.crop(
                (j * (square_size + gap), i * (square_size + gap),
                 j * (square_size + gap) + square_size, i * (square_size + gap) + square_size))
            )
    squares = [[crop_square(sq) for sq in row] for row in squares]
    return squares


def crop_square(im):
    return im.crop((character_margin_left, character_margin_top,
                    square_size - character_margin_right, square_size - character_margin_bottom))
