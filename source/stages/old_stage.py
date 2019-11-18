import conf
import copy
import random

_RAD_INCR = conf.get_fvalue('OLD', 'RAD_INCR')
_LUM_INCR = conf.get_fvalue('OLD', 'LUM_INCR')
_TEMP_INCR = conf.get_fvalue('OLD', 'TEMP_INCR')
_MASS_INCR = conf.get_fvalue('OLD', 'MASS_INCR')
random.seed()


class Old:
    star = None
    name = 'old'

    def __init__(self, star):
        self.star = star

    def calc_duration(self):
        if self.star.mass > 2:
            return 10 ** 6
        else:
            return 10 ** 6

    def calc_aspiration_state(self):
        asp_state = copy.copy(self.star)

        asp_state.temp = random.randrange(4500, 5999) * _TEMP_INCR
        asp_state.rad *= _RAD_INCR
        asp_state.lum *= _LUM_INCR
        asp_state.mass *= _MASS_INCR

        return asp_state
