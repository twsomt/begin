def get_count(sentence):
    wowel_letters = ('a', 'e', 'i', 'o', 'u')
    return len([i for i in sentence if i in wowel_letters])


print(get_count(sentence))