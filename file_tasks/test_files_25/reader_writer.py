
with open('goats.txt', 'r', encoding='utf-8') as read_file, open('answer.txt', 'w', encoding='utf-8') as out_file:
    lines = list(map(lambda x: x.strip(), read_file.readlines()))
    colours = lines[1:lines.index('GOATS')]
    goats = lines[lines.index('GOATS')+1:]

    for color in colours:
        if goats.count(color) / len(goats) > 0.07:
            print(color, file=out_file)
    

