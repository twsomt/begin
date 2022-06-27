with open('lines.txt', 'r', encoding='utf-8') as read_file:
    lines = list(map(lambda x: x.strip(), read_file.readlines()))
    if len(lines) >= 10:
        [print(i) for i in lines[-10:]]
    else:
        [print(i) for i in lines]
