from maturity import *
from star_graphics import *
import time


class Star:
    # Luminosity in solar units(solar luminosity)
    lum = .0
    # Effective temperature in kelvins
    temp = .0
    # Color
    color = "Black"
    # Mass in solar units(solar mass)
    mass = .0
    # Radius in solar units(solar radius)
    rad = .0
    # Name
    name = 'star'
    # Age in millions years
    age = 0
    # Object for maturity
    mat = None
    # Object for graphic
    gshell = None

    # create star based on temperature(temp) and mass(mass)
    def __init__(self, temp, mass):
        self.temp = temp
        self.color = Formula.calcColor(temp)
        self.mass = mass
        self.rad = Formula.calcRad(mass)
        self.lum = Formula.calcLum(mass)
        self.mat = Maturity(self)
        self.gshell = Gshell(self)

    def __str__(self):
        return (
            f"Star: '{self.name}' \n"
            f"Temperature: {self.temp} \n"
            f"Color: {self.color} \n"
            f"Luminosity: {self.lum} \n"
            f"Radius: {self.rad} \n"
            f"Mass: {self.mass} \n"
        )

    def growUp(self):
        self.mat.growStar()
        self.gshell.update()


class Formula:
    # Minimal temperature
    min_temp = 3500
    # Minimal star radius in solar units(solar radius)
    min_rad = 0.01
    # Maximum star radius in solar units(solar radius)
    max_rad = 3 * (10 ** 3)
    # Minimal star luminosity in solar units(solar luminosity)
    min_lum = 10 ** (-4)
    # Maximum star luminosity in solar units(solar luminosity)
    max_lum = 10 ** 4

    # Calculate color(color) based on temperature(temp)
    @staticmethod
    def calcColor(temp):
        return {
            temp < 3500: "Black",
            3500 <= temp < 4500: 'Dark_red',
            4500 <= temp < 6000: 'Red',
            6000 <= temp < 10000: 'Yellow',
            10000 <= temp < 25000: 'White',
            25000 <= temp < 30000: 'Bluish_white',
            temp >= 30000: 'Blue'
        }[1]

    # Calculate luminosity(lum) based on mass(mass)
    @staticmethod
    def calcLum(mass):
        return mass ** 3.9

    # Calculate radius(rad) based on mass(mass)
    @staticmethod
    def calcRad(mass):
        return mass ** 0.75


star = Star(5000., 2.3)
for i in range(star.mat.n_iter):
    print(star)
    star.growUp()
