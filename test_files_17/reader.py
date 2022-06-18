from random import sample

with open('first_names.txt') as name, open('last_names.txt') as surname:
    first_names = map(lambda x: x.strip(), name.readlines())
    last_names = map(lambda x: x.strip(), surname.readlines())

[print(*i) for i in sample(list(zip(first_names, last_names)), 3)]