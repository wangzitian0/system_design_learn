from manim import *

class HelloWorld(Scene):
    def construct(self):
        self.camera.background_color = "#A9A9A9"
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(1)
