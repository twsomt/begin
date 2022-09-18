class Cell:
    def __init__(self, around_mines, mine):   # параметры клетки
        self.around_mines = 0
        self.mine = mine
        self.fl_open = False


class GamePole:  # параметры поля
    def __init__(self, N, M):
        self.N = N
        self.M = M

        self.field = [['#' for i in range(N)] for j in range(N)]
        


x = GamePole(5, 3)
[print(*i) for i in x.field]



