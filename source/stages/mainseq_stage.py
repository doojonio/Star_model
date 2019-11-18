import copy
import conf

_RAD_INCR = conf.get_fvalue('MAINSEQ', 'RAD_INCR')
_LUM_INCR = conf.get_fvalue('MAINSEQ', 'LUM_INCR')
_TEMP_INCR = conf.get_fvalue('MAINSEQ', 'TEMP_INCR')
_MASS_INCR = conf.get_fvalue('MAINSEQ', 'MASS_INCR')


class Mainseq:
    star = None
    name = 'mainseq'

    def __init__(self, star):
        self.star = star

    def calc_duration(self):
        if self.star.mass > 1:
            return (10 ** 10) / (100 * self.star.mass)
        elif self.star.mass == 1:
            return 10 ** 10
        else:
            return (10 ** 10) * 100 / self.star.mass

    def calc_aspiration_state(self):
        asp_state = copy.copy(self.star)

        asp_state.mass *= _MASS_INCR
        asp_state.rad = (asp_state.mass ** 0.75) * _RAD_INCR
        asp_state.lum = (asp_state.mass ** 3.9) * _LUM_INCR
        asp_state.temp *= _TEMP_INCR

        return asp_state
