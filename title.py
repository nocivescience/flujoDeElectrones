from manim import *
class TitleScene(Scene):
    configuracion={
        'count':0,
        'direction': 1,
    }
    def construct(self):
        texto= MarkupText(
            'Flujo de Electrones',
            font_size=96,
            font='Arial'
        )
        texto.set_stroke(width=1,color=WHITE)
        def update_color(mob, dt):
            self.configuracion['count']+=dt*self.configuracion['direction']
            if self.configuracion['count']>=1:
                self.configuracion['direction']=-1
            elif self.configuracion['count']<=0:
                self.configuracion['direction']=1
            mob.set_color(interpolate_color(YELLOW, GREEN, self.configuracion['count']))
        texto.add_updater(update_color)
        self.add(texto)
        self.wait(10)