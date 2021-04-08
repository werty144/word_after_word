import time

from image_processing.Image_crop import grab_field, crop_field
from screen_utils.screen_utils import drag_through_word
from word_processing.dictionaring import make_trie, get_words_coord
from image_processing.Textify import get_letters
from word_processing.graph_utils import Graph
from image_processing.Constants import board_size


def main():
    time.sleep(1)
    trie = make_trie()
    field_image = grab_field()
    field_squares = crop_field(field_image)
    letters = get_letters(field_squares)
    graph = Graph(letters)
    used = {}
    for i in range(board_size):
        for j in range(board_size):
            pre_words = graph.gen_strings(9, i, j)
            words, word_coords = get_words_coord(pre_words, trie)
            for word, coords in zip(words, word_coords):
                if word not in used.keys():
                    used[word] = True
                    drag_through_word(coords)


if __name__ == '__main__':
    main()
