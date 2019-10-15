from setup import *

# Increasing age of the star
class Maturity:
    star = None
    next_star = None
    n_iter = 0
    stage = INIT_STAGE_NAME
    initStageDuration = 0

    def __init__(self, star):
        self.star = star
        self.calcInitStageDuration()
        self.calcStage()

    def calcStage(self):
        self.stage = {
            self.star.age < self.initStageDuration: INIT_STAGE_NAME
        }[1]

    def calcNextStar(self, radCoef = 1, tempCoef = 1, lumCoef = 1, massCoef = 1):
        self.next_star = self.star

        self.next_star.rad *= radCoef
        self.next_star.temp *= tempCoef
        self.next_star.lum *= lumCoef
        self.next_star.mass *= massCoef

    def calcInitStageDuration(self):
        if self.star.mass > 1:
            self.initStageDuration = INIT_STAGE_STAND_DUR / (self.star.mass * INIT_STAGE_DUR_COEF)
        elif self.star.mass < 1:
            self.initStageDuration = (INIT_STAGE_DUR_COEF / self.star.mass) * INIT_STAGE_STAND_DUR
        else:
            self.initStageDuration = INIT_STAGE_STAND_DUR
        self.n_iter = int(self.initStageDuration / TIME_STEP)
        self.calcNextStar(STAR_RADIUS_DECREASE, STAR_TEMP_INCREASE, STAR_LUM_DECREASE)

    def growStar(self):
        self.star.age += TIME_STEP

        self.star.rad += (self.star.rad - self.next_star.rad)/self.n_iter
        self.star.temp += (self.star.temp - self.next_star.temp)/self.n_iter
        self.star.lum += (self.star.lum - self.next_star.lum)/self.n_iter
        self.star.mass += (self.star.mass - self.next_star.mass)/self.n_iter

