class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if any(type(i) not in (int, float) or i == 0 for i in (self.a, self.b, self.c)):
            return 1
        elif (self.a + self.b < self.c) or (self.b + self.c < self.a) or (self.c + self.a < self.b):
            return 2
        else:
            return 3

a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())