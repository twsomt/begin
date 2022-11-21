text, n = input(), 8
matrix = [['.' for i in range(8)] for i in range(8)]
field = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

x = n - int(text[-1])
y = field[text[0]] - 1
matrix[x][y] = 'N'

for i in range(n):
    for j in range(n):
        if (i - x) ** 2 + (j - y) ** 2 == 5:
            matrix[i][j] = '*'
[print(*i) for i in matrix]