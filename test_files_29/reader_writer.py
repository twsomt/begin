with open('words.txt', 'r', encoding='utf-8') as read_file:
    lines = ' '.join(read_file.readlines()).split()
    result = list(filter(lambda x: len(x) == max(map(len, lines)) ,lines))

    for i in result:
        print(i)
