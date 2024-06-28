from manim import Scene, Code, Create, Transform


class Render(Scene):
    def construct(self):
        one = Code("css/one.css", tab_width=4, style="one-dark", language="css")
        two = Code("css/two.css", tab_width=4, style="one-dark", language="css")
        self.play(Create(one))
        self.play(Transform(one, two))
