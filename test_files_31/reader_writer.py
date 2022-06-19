import re

with open('data.txt', 'r', encoding='utf-8') as file, open('forbidden_words.txt', 'r', encoding='utf-8') as words:
    content = file.read()
    for word in words.read().split():
        content = re.sub('(?i)' + word, '*' * len(word), content)
    print(content)