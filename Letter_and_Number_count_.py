def count_letters_and_numbers(s):
    letters = [c for c in s if c.isalpha()]
    numbers = [n for n in s if n.isdigit()]
    l_count = len(letters)
    n_count = len(numbers)
    letter_str = str(l_count) + (" letters" if l_count != 1 else " letter")
    number_str = str(n_count) + (" numbers" if n_count != 1 else " number")
    return f"The string has {letter_str} and {number_str}."
