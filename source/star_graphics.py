from graphics import *
from setup import *

window = GraphWin(WINDOW_NAME, WINDOW_LENGTH, WINDOW_WIDTH)


class Gshell:
    star = None
    circle = None
    glabels = None
    win = window
    star_rad = 0  # pixel in solar radius

    def __init__(self, star):
        self.star = star
        self.circle = Circle(WINDOW_CENTRE, self.star.rad * SUN_RAD_IN_PIX)
        self.circle.setFill(COLORS[self.star.color])
        self.glabels = GstarLabel(star)
        self.glabels.draw(self.win)
        self.draw()

    def update(self):
        time.sleep(TIME_SLEEP)
        self.circle.undraw()
        del self.circle
        self.circle = Circle(WINDOW_CENTRE, self.star.rad * SUN_RAD_IN_PIX)
        self.circle.setFill(COLORS[self.star.color])
        self.draw()
        self.glabels.update()

    def draw(self):
        self.circle.draw(self.win)

class GstarLabel:
    star = None
    rad = None
    lum = None
    mass = None
    temp = None

    def __init__(self, star):
        self.star = star
        self.rad = Text(LAB_RAD_POS, f"RADIUS: {round(self.star.rad, N_DEC)} su")
        self.lum = Text(LAB_LUM_POS, f"LUMINOS: {round(self.star.lum, N_DEC)} su")
        self.temp = Text(LAB_TEMP_POS, f"TEMP: {round(self.star.temp, N_DEC)} su")
        self.mass = Text(LAB_MASS_POS, f"MASS: {round(self.star.mass, N_DEC)} su")

    def draw(self, win):
        self.rad.draw(win)
        self.lum.draw(win)
        self.temp.draw(win)
        self.mass.draw(win)

    def update(self):
        self.rad.setText(f"RADIUS: {round(self.star.rad, N_DEC)} su")
        self.lum.setText(f"LUMINOS: {round(self.star.lum, N_DEC)} su")
        self.temp.setText(f"TEMP: {round(self.star.temp, N_DEC)} su")
        self.mass.setText(f"MASS: {round(self.star.mass, N_DEC)} su")

