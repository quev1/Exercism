def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return all(letter in sentence.lower() for letter in alphabet)
