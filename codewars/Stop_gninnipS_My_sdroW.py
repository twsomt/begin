def spin_words(sentence):
    return ' '.join(map(lambda x: x[::-1] if len(x) >= 5 else x, sentence.split()))

x = 'Hey fellow warriors'

print(spin_words(x))

