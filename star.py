import numpy
import math

class Star:
    # Luminosity
    lum = 0
    # Effective temperature
    temp = 0
    # Color
    color = "Black"
    # Mass
    mass = 0
    # Name
    name = 'star'

    def __init__(self, temp):
        self.temp = temp
        self.color = Formules.calcColor(temp)

    def printStar(self):
        print("Star: {}".format(self.name))
        print("Temperature: {}\nColor: {}\nLuminosity: {}\nMass: {}\n".format(self.temp,
                                                                              self.color,
                                                                              self.lum,
                                                                              self.mass))


class Formules:
    # Stefan–Boltzmann constant
    sigma = 5.67 * 10 ** (-8)

    # Calculate luminosity(L) based on light(E) and distance(R)
    @staticmethod
    def calcLum(E, R):
        return E * math.pow(R, 2) * 4 * math.pi

    # Calculate color(Color) based on temperature(Temp)
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

