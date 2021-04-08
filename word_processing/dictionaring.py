import os
from word_processing.graph_utils import Trie


def get_words_coord(pre_words_with_coords, trie):
    ans_coords = []
    ans_words = []
    for word, coords in pre_words_with_coords:
        if trie.contains(word):
            ans_coords.append(coords)
            ans_words.append(word)
    return ans_words, ans_coords


def make_trie():
    dict_path = os.getcwd() + '/dictionary/russian_filtered.txt'
    dict_file = open(dict_path, 'r')
    words = dict_file.read().splitlines()
    trie = Trie()
    for word in words:
        trie.add_word(word)
    return trie
