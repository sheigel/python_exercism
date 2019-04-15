from string import ascii_lowercase


def is_pangram(sentence: str):
    alphabet = set(ascii_lowercase)
    return alphabet.issubset(sentence.lower())
