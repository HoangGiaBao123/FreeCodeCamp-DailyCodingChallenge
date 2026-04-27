def get_word_score(word):
    letters_in_alphabet = list('abcdefghijklmnopqrstuvwxyz')
    letters_in_word = list(word.lower())
    letters_index = [letters_in_alphabet.index(c) + 1 for c in letters_in_word]
    return sum(letters_index)
