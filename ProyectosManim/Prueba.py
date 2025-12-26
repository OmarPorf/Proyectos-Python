from manim import *

class CuadradoACirculo(Scene):
    def construct(self):
        circle = Circle()  # Crear un círculo
        square = Square()  # Crear un cuadrado
        square.flip(RIGHT) # Voltear el cuadrado
        square.rotate(-3 * TAU / 8) # Rotarlo un poco

        # La animación: Transformar cuadrado en círculo
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))