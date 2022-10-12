import string
alphabet = list(string.ascii_lowercase)


def is_pangram(s):
    return all(s.lower().count(i) > 0 for i in alphabet)




print(is_pangram("Cwm fjord bank glyphs vext quiz"))