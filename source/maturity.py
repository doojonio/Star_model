from stages.init_stage import Init
from stages.mainseq_stage import Mainseq
from stages.old_stage import Old
from stages.dying_stage import Dying
import conf

STAGE_ITERATIONS = conf.get_fvalue('SPEED', 'STAGE_ITERATIONS')


class Maturity:
    star = None
    asp_state = None
    stage = None
    cur_stage_dur = 0
    step_years = 0
    stage_threshold = 0
    change_for_step = {
        'lum': 0,
        'rad': 0,
        'temp': 0,
        'mass': 0
    }

    def __init__(self, star):
        self.star = star
        self.stage = Init(self.star)
        self._update_values()

    def __str__(self):
        return self.stage.name

    def _update_values(self):
        self.cur_stage_dur = self.stage.calc_duration()
        self.asp_state = self.stage.calc_aspiration_state()
        self.step_years = self.cur_stage_dur / STAGE_ITERATIONS
        self.stage_threshold = self.star.age + self.cur_stage_dur

        self.change_for_step['lum'] = (self.asp_state.lum - self.star.lum) / STAGE_ITERATIONS
        self.change_for_step['rad'] = (self.asp_state.rad - self.star.rad) / STAGE_ITERATIONS
        self.change_for_step['temp'] = (self.asp_state.temp - self.star.temp) / STAGE_ITERATIONS
        self.change_for_step['mass'] = (self.asp_state.mass - self.star.mass) / STAGE_ITERATIONS

    def _update_star_values(self):
        self.star.lum += self.change_for_step['lum']
        self.star.rad += self.change_for_step['rad']
        self.star.temp += self.change_for_step['temp']
        self.star.mass += self.change_for_step['mass']
        self.star.age += self.step_years

    def _set_stage(self):
        self.stage = {
            self.stage.name == 'init'   : Mainseq(self.star),
            self.stage.name == 'mainseq': Old(self.star),
            self.stage.name == 'old'    : Dying(self.star)
        }[1]

    def grow_star(self):
        if self.star.age >= self.stage_threshold:
            self._set_stage()
            self._update_values()
        self._update_star_values()

