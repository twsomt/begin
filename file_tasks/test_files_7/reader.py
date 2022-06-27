from random import sample
file = open('lines.txt', 'r', encoding='UTF-8')
lines = file.readlines()

print(*sample(list(map(lambda x: x.strip(), lines)), 1))

file.close()
