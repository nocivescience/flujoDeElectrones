from manim import *
class Electron(Dot):
    def __init__(self, **kwargs):
        kwargs['radius'] = .5
        super().__init__(**kwargs)
        self.set_color(YELLOW)
        self.direction = 1
        self.vertical_direction = 1
        self.randomH=np.random.random()
        self.randomV=np.random.random()
        self.acumulated_time = 0
        self.center = np.array([np.random.uniform(-config['frame_width']/2,config['frame_width']/2),np.random.uniform(-config['frame_height']/4,config['frame_height']/4),0])
        self.velocity = 1
        self.add_updater(self.update_color)
    def update_color(self, mob, dt):
        mob.acumulated_time += dt*mob.direction
        if mob.acumulated_time >= 1:
            mob.direction = -1
        elif mob.acumulated_time <= 0:
            mob.direction = 1
        mob.set_color(interpolate_color(YELLOW, BLUE, mob.acumulated_time))
        mob.center += np.array([dt*mob.velocity+mob.randomH, 0.2*mob.vertical_direction+mob.randomV,0])
        if mob.center[0]+mob.radius > config['frame_width']/2:
            mob.center[0] = -config['frame_width']/2
        if mob.center[1]+mob.radius > config['frame_height']/2:
            mob.vertical_direction = -1
        elif mob.center[1]-mob.radius < -config['frame_height']/2:
            mob.vertical_direction = 1
        mob.move_to(mob.center)
class Electrones(Scene):
    def construct(self):
        for _ in range(30):
            electron = Electron()
            self.add(electron)
        self.wait(10)