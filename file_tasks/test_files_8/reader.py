file = open('numbers.txt')
print(sum(list(map(lambda x: int(x.strip()),file.readlines()))))