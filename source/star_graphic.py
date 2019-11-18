from graphics import *
import conf

_WINDOW_NAME = conf.get_str('WINDOW', 'NAME')
_WINDOW_HEIGHT = conf.get_intvalue('WINDOW', 'HEIGHT')
_WINDOW_WIDTH = conf.get_intvalue('WINDOW', 'WIDTH')
_RAD_PIX = conf.get_fvalue('GRAPHIC', 'SOLAR_RADIUS_IN_PIXELS')
LAB_X = conf.get_fvalue('WINDOW', 'LAB_X')
LAB_Y = conf.get_fvalue('WINDOW', 'LAB_Y')

CENTRE = Point(_WINDOW_WIDTH / 2, _WINDOW_HEIGHT / 2)

COLORS = {
    'Black': color_rgb(0, 0, 0),
    'Dark_red': color_rgb(139, 0, 0),
    'Red': color_rgb(100, 0, 0),
    'Yellow': color_rgb(255, 255, 0),
    'White': color_rgb(255, 255, 255),
    'Bluish_white': color_rgb(166, 202, 240),
    'Blue': color_rgb(0, 0, 255),
}

graph_window = GraphWin(_WINDOW_NAME, _WINDOW_WIDTH, _WINDOW_HEIGHT)
graph_window.setBackground('Black')


class GraphStar:
    star = None
    circle = None
    pos = CENTRE

    def __init__(self, star):
        self.star = star
        self.circle = Circle(self.pos, self.star.rad * _RAD_PIX)
        self.circle.setOutline('White')
        self.circle.setFill('White')

    def draw(self, win):
        self.circle.draw(win)

    def update(self, win):
        self.circle.undraw()
        self.circle = Circle(self.pos, self.star.rad * _RAD_PIX)
        self.circle.setFill(COLORS[self.star.color])
        self.draw(win)


class GraphStarInfo:
    star = None
    lab = None

    def __init__(self, star):
        self.star = star
        self.lab = Text(Point(LAB_X, LAB_Y), self.star.__str__())
        self.lab.setFill('White')

    def draw(self, win):
        self.lab.draw(win)

    def update(self, win):
        self.lab.setText(self.star.__str__())


