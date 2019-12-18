""" Determine if a sentence is a pangram, i.e., a sentence that uses each letter of the alphabet at least once.
Examples: "The quick brown fox jumps over the lazy dog."
Comparison should be case insensitive. """
from string import ascii_lowercase

def is_pangram(sentence):
    alphabet = set(ascii_lowercase)

    return alphabet.issubset(sentence.lower())
