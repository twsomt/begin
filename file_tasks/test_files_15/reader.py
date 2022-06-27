with open('nums.txt', encoding='utf-8') as file:
    res = 0
    for line in file.readlines():
        res += sum(map(int, ''.join(list(map(lambda x: ' ' if not x.isnumeric() else x, line.strip()))).split()))

    print(res)