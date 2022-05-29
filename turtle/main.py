import turtle
import random as r
X = -200
Y = -200
SIZE = 400

def night(t, n, setup=(400, 400)):
    t.up()
    t.goto(X, Y)
    t.fillcolor('black')
    t.begin_fill()
    for _ in range(4):
        t.forward(400)
        t.lt(90)
    t.end_fill()
    for _ in range(n):
          x, y = r.randint(-200, 200), r.randint(-200, 200)
          t.goto(x, y)
          t.dot(r.randint(1,3), 'yellow')
          
def townshadow(t, build_dict, color_fill='darkblue'):
    t.up()
    t.seth(0)
    t.goto(X, Y)
    t.down()
    t.fillcolor(color_fill)
    t.begin_fill()
    for i, (w, h) in build_dict.items():
        t.goto(X+i*w,Y+h)
        t.forward(w)
    t.goto(X+SIZE, Y)
    t.end_fill()

def lightwindow(t, build_dict, nwindow, color_fill='yellow'):
    t.up(); t.seth(0); t.goto(X, Y)
    t.fillcolor(color_fill)
    
    padding_w = build_dict[0][0] * 0.1
    size_w = build_dict[0][0] * 0.2
    
    for _ in range(nwindow):
        key = r.choice(build_dict.keys())
        w, h = build_dict[key]
        nfloor = (h-padding_w)//(size_w+padding_w)
        nwin = 3
        posx = key*w + padding_w + r.randrange(nwin)*(size_w+padding_w)
        posy = r.randrange(nfloor)*(size_w+padding_w) + padding_w
        t.goto(X+posx, Y+posy)
        t.begin_fill()
        t.down()
        for _ in range(4):
            t.forward(size_w)
            t.lt(90)
        t.up()
        t.end_fill()
    t.goto(X,Y)
t = turtle.Turtle()
t.speed(10)
t._tracer(4, 0)
t.hideturtle()
bild_num = r.randint(5, 9)
# buildings = {num: (width, heigth)}
buildings = {i: (SIZE/bild_num, r.randint(SIZE*0.2, SIZE*0.8))  
             for i in range(bild_num)}
             
night(t, 100)
townshadow(t, buildings)
lightwindow(t, buildings, 20)