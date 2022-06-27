def more_than_65(line):
    return all(x >= 65 for x in map(int, line.strip().split()[1:]))

result = []

with open('grades.txt', 'r', encoding='utf-8') as read_file:
    lines = read_file.readlines()
    for line in lines:
        if more_than_65(line):
            result.append('1')

print(len(result))