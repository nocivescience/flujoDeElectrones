from manim import *
class Electron(Dot):
    def __init__(self, **kwargs):
        kwargs['radius'] = .5
        super().__init__(**kwargs)
        self.set_color(YELLOW)
        self.direction = 1
        self.acumulated_time = 0
        self.add_updater(self.update_color)
    def update_color(self, mob, dt):
        mob.acumulated_time += dt*mob.direction
        if mob.acumulated_time >= 1:
            mob.direction = -1
        elif mob.acumulated_time <= 0:
            mob.direction = 1
        mob.set_color(interpolate_color(YELLOW, BLUE, mob.acumulated_time))
class Electrones(Scene):
    def construct(self):
        electron = Electron()
        self.add(electron)
        self.wait(10)