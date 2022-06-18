with open('input.txt', 'r', encoding='utf-8') as read_file, open('output.txt', 'w', encoding='utf-8') as out_file:
    for i, row in enumerate(read_file.readlines(), 1):
        print(f'{i}) {row.strip()}', file=out_file)
