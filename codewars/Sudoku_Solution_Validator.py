def sudoku(x):
    solution = Sudoku(x)
    solution.solve()
    return solution.field

class Sudoku(object):

    def __init__(self, field):
        self.field = field
        self.varianti = [[[]]*9]*9

    def new_varianti(self, r, c):
        row = self.get_row(r)
        print(row)
        col = self.get_col(c)
        cub = self.get_cub(r, c)
        p = set(range(1,10))
        g = set(row + col + cub)
        new_var = list(p - g)
        self.varianti[r][c] = new_var

    def solve(self):
        while not self.if_possible_complete:
            for row in range(9):
                for col in range(9):
                    if self.field[row][col] == 0: self.new_varianti(row, col)
                    if len(self.varianti[row][col]) == 1: self.field[row][col] = self.varianti[row][col].pop()

    @property
    def if_possible_complete(self):
        for row in self.field:
            if 0 in row:
                return False
        return True

    def get_row(self, r):
        return [n for n in self.field[r] if n != 0]

    def get_col(self, c):
        return [row[c] for row in self.field if row[c] != 0]

    def get_cub(self, r, c):
        sq = []
        i = int(r/3) 
        j = int(c/3)
        ri = range(i*3, (i*3)+3)
        rj = range(j*3, (j*3)+3)
        for ni in ri:
            for nj in rj:
                n = self.field[ni][nj]
                if n != 0:
                    sq.append(n)
        return sq

x = [[0,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]]

print(sudoku(x))

# 0  1  2  3  4  5  6  7  8 
# 9  10 11 12 13 14 15 16 17
# 18 29 20 21 22 23 24 25 26

# 27 28 29 30 31 32 33 34 35
# 36 37 38 39 40 41 42 43 44
# 45 46 47 48 49 50 51 52 53

# 54 55 56 57 58 59 60 61 62
# 63 64 65 66 67 68 69 70 71
# 72 73 74 75 76 77 78 79 80


