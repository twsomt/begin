with open('numbers.txt') as file:
    for line in file.readlines():
        print(sum(map(int, line.split())))