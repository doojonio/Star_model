from maturity import Maturity
import conf

N_DEC = conf.get_intvalue('WINDOW', 'N_DEC')


def calc_color(temp):
    return {
        temp < 3500: "Black",
        3500 <= temp < 4500: 'Dark_red',
        4500 <= temp < 6000: 'Red',
        6000 <= temp < 10000: 'Yellow',
        10000 <= temp < 25000: 'White',
        25000 <= temp < 30000: 'Bluish_white',
        temp >= 30000: 'Blue'
    }[1]


class Star:
    lum = 0
    rad = 0
    temp = 0
    mass = 0
    age = 0
    color = None
    maturity = None

    def __init__(self, lum, rad, temp, mass):
        (self.lum, self.rad, self.temp, self.mass) = (lum, rad, temp, mass)
        self.maturity = Maturity(self)
        self.color = calc_color(self.temp)

    def __str__(self):
        return (
            f"luminosity: {round(self.lum, N_DEC)}\n"
            f"radius: {round(self.rad, N_DEC)}\n"
            f"temp: {round(self.temp, N_DEC)}\n"
            f"age: {round(self.age, N_DEC)}\n"
            f"mass: {round(self.mass, N_DEC)}\n"
            f"stage: {self.maturity.__str__()}\n"
        )

    def grow_up(self):
        self.maturity.grow_star()
        self.color = calc_color(self.temp)
