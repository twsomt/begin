from random import randint as rnd


class Cell:
    def __init__(self, around_mines, mine):   # параметры клетки
        self.around_mines = 50
        self.mine = mine
        self.fl_open = False


class Gamefield:  # параметры поля
    def __init__(self, N, M):
        self.N = N
        self.M = M

        self.field = [[Cell(0, False) for i in range(N)] for j in range(N)]

        cnt = 0
        while cnt != self.M:
            x = rnd(0, self.N-1)
            y = rnd(0, self.N-1)
            if self.field[x][y].mine:
                continue
            else:
                self.field[x][y] = Cell(0, True)
                cnt += 1

        for i in range(N):
            for j in range(N):
                if i == 0:
                    if j == 0:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i][j+1].mine, self.field[i+1][j+1].mine, self.field[i+1][j].mine)))
                    elif j == N-1:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i][j-1].mine, self.field[i+1][j-1].mine, self.field[i+1][j].mine)))
                    else:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i][j-1].mine, self.field[i+1][j-1].mine, self.field[i+1][j].mine, self.field[i+1][j+1].mine, self.field[i][j+1].mine)))
                elif i == N-1:
                    if j == 0:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i-1][j].mine, self.field[i-1][j+1].mine, self.field[i][j+1].mine)))
                    elif j == N-1:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i-1][j].mine, self.field[i-1][j-1].mine, self.field[i][j-1].mine)))
                    else:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i][j-1].mine, self.field[i-1][j-1].mine, self.field[i-1][j].mine, self.field[i-1][j+1].mine, self.field[i][j+1].mine)))
                else:
                    if j == 0:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i-1][j].mine, self.field[i-1][j+1].mine, self.field[i][j+1].mine, self.field[i+1][j+1].mine, self.field[i+1][j].mine)))
                    elif j == N-1:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i-1][j].mine, self.field[i-1][j-1].mine, self.field[i][j-1].mine, self.field[i+1][j-1].mine, self.field[i+1][j].mine)))
                    else:
                        self.field[i][j].around_mines = sum(map(lambda x: 1 if x else 0, (self.field[i-1][j-1].mine, self.field[i-1][j].mine, self.field[i-1][j+1].mine, self.field[i][j+1].mine, self.field[i+1][j+1].mine, self.field[i+1][j].mine, self.field[i+1][j-1].mine, self.field[i][j-1].mine)))
    def show(self):
        for i in self.field:
            for j in i:
                if j.fl_open:
                    print(j.around_mines, end=' ')
                else:
                    print('#', end=' ')
            print()

    def init(self):
        # костыль
        pass

field_game  = Gamefield(10, 12)
field_game.show()

print(hasattr(Gamefield, 'show'))
print(hasattr(Gamefield, '__init__'))
print(isinstance(field_game, Gamefield))





