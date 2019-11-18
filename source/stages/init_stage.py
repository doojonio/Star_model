import conf
import copy

_RAD_DECR = conf.get_fvalue('INIT', 'RAD_DECR')
_LUM_DECR = conf.get_fvalue('INIT', 'LUM_DECR')
_TEMP_INCR = conf.get_fvalue('INIT', 'TEMP_INCR')
_MASS_INCR = conf.get_fvalue('INIT', 'MASS_INCR')


class Init:
    star = None
    name = 'init'

    def __init__(self, star):
        self.star = star

    def calc_duration(self):
        if self.star.mass > 1:
            return (10**6) / (self.star.mass * 100)
        elif self.star.mass == 1:
            return 10**6
        else:
            return (100 / self.star.mass) * (10**6)

    def calc_aspiration_state(self):
        asp_state = copy.copy(self.star)
        asp_state.mass *= _MASS_INCR
        asp_state.rad = (asp_state.mass ** 0.75) * _RAD_DECR
        asp_state.lum = (asp_state.mass ** 3.9) * _LUM_DECR
        asp_state.temp *= _TEMP_INCR
        return asp_state
