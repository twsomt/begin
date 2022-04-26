a = [
    [1, 1, 1], 
    [2, 2, 2], 
    [3, 3, 3]
]

b = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
def multi_matrix(a, b):

    m, n = len(a), len(b)
    matrix = [['.' for i in range(n)] for i in range(m)]

    for x in range(m):
        for col in range(m):
            summ =0
            for row in range(m):
                summ += a[col][x] * b[row][x]
            matrix[x][col] = str(summ)

    for i in range(m):
        for j in range(n):
            print(matrix[j][i].ljust(3), end='')
        print()

multi_matrix(a, b)
