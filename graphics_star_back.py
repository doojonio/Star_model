from graphics import *
from setup import *
import random
import time

win = GraphWin('shit', WINDOW_LENGHT, WINDOW_WIDTH)
win.setBackground('black')
moon_c = Point(3/4*WINDOW_LENGHT, 1/4 * WINDOW_WIDTH)
luna = Circle(moon_c, 100)
luna.setFill('white')
black_shit = []
for _ in range(10):
    shit = Circle(Point(moon_c.x + random.randrange(-80, 80, 1), moon_c.y + random.randrange(-80, 80, 1)),random.randrange(5, 30, 1))
    shit.setFill('grey')
    black_shit.append(shit)
centre = Point(WINDOW_LENGHT/2, WINDOW_WIDTH/2)
atoms = []
MOVE_STEP = 10
for i in range(500):
    atoms.append(Point(random.randrange(0, WINDOW_LENGHT, 1), random.randrange(0, WINDOW_WIDTH, 1)))
    atoms[i].setFill('white')
    atoms[i].draw(win)


class Line:
    def __init__(self, cur_coord, k, b):
        self.cur_coord = cur_coord
        self.k = k
        self.b = b

    cur_coord = None
    k = None
    b = None


moving_atoms = atoms[0:500:1]
traces = []
for at in moving_atoms:
    if at.y - centre.y != 0:
        k = (at.x - centre.x) / (at.y - centre.y)
    else:
        k = 0
    b = at.x - k * at.y
    traces.append(Line(at, k, b))

flag = 1

luna.draw(win)
for shit in black_shit:
    shit.draw(win)
while (flag):
    time.sleep(TIME_SLEEP)
    for trace in traces:
        index = traces.index(trace)
        if trace.cur_coord.y > centre.y:
            dy = -MOVE_STEP
            dx = trace.k * (trace.cur_coord.y + dy) + trace.b - trace.cur_coord.x
        elif trace.cur_coord.y < centre.y:
            dy = MOVE_STEP
            dx = trace.k * (trace.cur_coord.y + dy) + trace.b - trace.cur_coord.x
        else:
            dy = 0
            if trace.cur_coord.x > centre.x:
                dx = -MOVE_STEP
            else:
                dx = MOVE_STEP
        moving_atoms[index].move(dx, dy)
