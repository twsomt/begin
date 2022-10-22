def valid_solution(board):
    if not len(board) == 9 and not all(len(i) == 9 for i in board):
        return False

    x = [1,2,3,4,5,6,7,8,9]

    row = all(all(f in i for f in x) for i in board) # row
    d = [[board[j][i] for j in range(9)] for i in range(9)]
    col = all(all(f in i for f in x) for i in d) # column

    c = [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for j in range(9):
            if 0 <= i <= 2 and 0 <= j <= 2:
                c[0].append(board[i][j])
            elif  0 <= i <= 2 and 3 <= j <= 5:
                c[1].append(board[i][j])
            elif  0 <= i <= 2 and 6 <= j <= 8:
                c[2].append(board[i][j])
            elif 3 <= i <= 5 and 0 <= j <= 2:
                c[3].append(board[i][j])
            elif  3 <= i <= 5 and 3 <= j <= 5:
                c[4].append(board[i][j])
            elif  3 <= i <= 5 and 6 <= j <= 8:
                c[5].append(board[i][j])
            elif 6 <= i <= 8 and 0 <= j <= 2:
                c[6].append(board[i][j])
            elif  6 <= i <= 8 and 3 <= j <= 5:
                c[7].append(board[i][j])
            elif  6 <= i <= 8 and 6 <= j <= 8:
                c[8].append(board[i][j])

    cub = all(all(f in i for f in x) for i in c)
    return all(i for i in (row, col, cub))


x = [
[5, 3, 4, 6, 7, 8, 9, 1, 2], 
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]
]

print(valid_solution(x))  # True

x = [
[5, 3, 4, 6, 7, 8, 9, 1, 2], 
[6, 7, 2, 1, 9, 0, 3, 4, 9],
[1, 0, 0, 3, 4, 2, 5, 6, 0],
[8, 5, 9, 7, 6, 1, 0, 2, 0],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 0, 1, 5, 3, 7, 2, 1, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 0, 0, 4, 8, 1, 1, 7, 9]

]
print(valid_solution(x))  # False