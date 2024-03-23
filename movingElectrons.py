from manim import *
class Electron(Dot):
    def __init__(self, **kwargs):
        kwargs['radius'] = .5
        super().__init__(**kwargs)
        self.set_color(YELLOW)
        self.direction = 1
        self.acumulated_time = 0
        def update_color(mob, dt):
            mob.acumulated_time += dt*mob.direction
            if mob.acumulated_time >= 1:
                mob.direction = -1
            elif mob.acumulated_time <= 0:
                mob.direction = 1
            mob.set_color(interpolate_color(YELLOW, GREEN, mob.acumulated_time))
        self.add_updater(update_color)
class Electrones(Scene):
    def construct(self):
        electron = Electron()
        self.add(electron)
        self.wait(10)