import copy
import conf
import random

_RAD_DECR = conf.get_fvalue('DYING', 'RAD_DECR')
_LUM_INCR = conf.get_fvalue('DYING', 'LUM_INCR')
_TEMP_INCR = conf.get_fvalue('DYING', 'TEMP_INCR')
_MASS_DECR = conf.get_fvalue('DYING', 'MASS_DECR')
_MASS_DECR_WHITE_DWARF = conf.get_fvalue('DYING', 'MASS_DECR_WHITE_DWARF')
random.seed()


class Dying:
    star = None
    name = 'dying'

    def __init__(self, star):
        self.star = star

    def calc_duration(self):
        if self.star.mass > 8:
            return 0.000019
        else:
            return 1

    def calc_aspiration_state(self):
        asp_state = copy.copy(self.star)
        if asp_state.mass > 8:
            asp_state.mass = random.randrange(138, 300) / 100
            if asp_state.mass > 2.5:
                asp_state.rad = _RAD_DECR * 1 / (2.95 * asp_state.mass)
                asp_state.lum = _LUM_INCR * -999
                asp_state.temp = _TEMP_INCR * -999
            else:
                asp_state.rad = _RAD_DECR * 1 / random.randrange(34000, 35000)
                asp_state.temp = _TEMP_INCR * random.randrange(25000, 35000)
        else:
            asp_state.mass *= _MASS_DECR_WHITE_DWARF
            asp_state.rad = _RAD_DECR * random.randrange(9, 11) / 1000
            asp_state.temp = random.randrange(10000, 25000) * _TEMP_INCR
            asp_state.lum *= _LUM_INCR
        return asp_state
