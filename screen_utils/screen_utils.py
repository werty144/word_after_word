from image_processing.Constants import *
import pyautogui


def get_square_mid_coords(i, j):
    lucornerx = top_left_corner_x + j * (square_size + gap)
    lucornery = top_left_corner_y + i * (square_size + gap)
    rbcornerx = top_left_corner_x + (j + 1) * (square_size + gap)
    rbcornery = top_left_corner_y + (i + 1) * (square_size + gap)
    return (lucornerx + rbcornerx) // 2, (lucornery + rbcornery) // 2


def drag_through_word(word_coords):
    if len(word_coords) == 1:
        return
    pixel_coords = [get_square_mid_coords(y, x) for y, x in word_coords]
    # pyautogui.MINIMUM_SLEEP = 0
    # pyautogui.PAUSE = 0.03
    # pyautogui.MINIMUM_DURATION = 0
    pyautogui.moveTo(pixel_coords[0])
    pyautogui.mouseDown()
    for x, y in pixel_coords[1:]:
        pyautogui.dragTo(x, y, mouseDownUp=False)
    pyautogui.mouseUp()
