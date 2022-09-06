from random import sample, choice

class Figure:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Line(Figure):
    pass
    
class Rect(Figure):
    pass
    
class Ellipse(Figure):
    pass

elements = [choice([Line, Rect, Ellipse])(*sample(range(10), 4)) for _ in range(217)]
elements = [i if not isinstance(i, Line) else Line(0, 0, 0, 0) for i in elements]