with open('ledger.txt', 'r', encoding='utf-8') as read_file:
    lines = list(map(lambda x: int(x.strip('$')), read_file.readlines()))
    print(f'${sum(lines)}')