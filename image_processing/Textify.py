import pytesseract

im_dir = '/home/user/PycharmProjects/word_after_word/images/'
rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'


def get_raw_letters(squares):
    letters = []
    for row in squares:
        letters.append([])
        for im in row:
            c = pytesseract.image_to_string(im, lang='rus', config=' --psm 10')
            letters[-1].append(c)
    return letters


def clean_letter(letter):
    if '5' in letter:
        return 'б'
    if '3' in letter:
        return 'з'
    return list(filter(lambda c: c in rus_alphabet, letter))[0].lower()


def get_letters(squares):
    raw_letters = get_raw_letters(squares)
    letters = [[clean_letter(letter) for letter in row] for row in raw_letters]
    return letters
