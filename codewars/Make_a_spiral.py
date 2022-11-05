
def spiralize(size):
    ma = [[0] * size for _ in range(size)]
    print
    mi = list(map(lambda x: list(map(lambda y: 1 if (int(size + 1) / 2) % 2 == 1 else 0, range(0, size))), range(0, size)))
    cnt = 1
    for i in range(0, int(size / 2)):
        for j in range(0, size - i * 2):
            ma[i][j+i] = cnt
            ma[j+i][i] = cnt
            ma[size - i - 1][j+i] = cnt
            ma[j+i][size - i - 1] = cnt
            
            if size % 4 == 0:
                if i != int(size / 2) - 1:
                    ma[i+1][i] = 1 - cnt
            else:
                ma[i+1][i] = 1 - cnt

        cnt = 1 - cnt
    return ma









    
[print(i) for i in spiralize(5)]