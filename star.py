import math


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

    # create star based on temperature(temp) and mass(mass)
    def __init__(self, temp, mass):
        self.temp = temp
        self.color = Formula.calcColor(temp)
        self.mass = mass
        self.rad = Formula.calcRad(mass)
        self.lum = Formula.calcLum(mass)

    def printStar(self):
        print("Star: {}".format(self.name))
        print("Temperature: {}\nColor: {}\nLuminosity: {}\nMass: {}\n".format(self.temp,
                                                                              self.color,
                                                                              self.lum,
                                                                              self.mass))


class Formula:
    # Stefan–Boltzmann constant
    sigma = 5.67 * (10 ** (-8))
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
            temp < 3500: "Isn't star's color",
            3500 <= temp < 4500: 'Dark-red',
            4500 <= temp < 6000: 'Red',
            6000 <= temp < 10000: 'Yellow',
            10000 <= temp < 25000: 'White',
            25000 <= temp < 30000: 'Bluish white',
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

star = Star(9940, 2.3)
stop = 1
