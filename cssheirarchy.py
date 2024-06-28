from manim import Scene, Code, Create, Transform, ImageMobject, RIGHT, LEFT

# from html2image import Html2Image
import imgkit

# hti = Html2Image(size=(500, 200))

options = {"enable-local-file-access": "", "width": 960}


class Render(Scene):
    def render_imgs(self):
        imgkit.from_file("cssheirarchy/one.html", "one.jpg", options=options)
        imgkit.from_file("cssheirarchy/two.html", "two.jpg", options=options)

    def construct(self):
        self.render_imgs()
        one = Code(
            "cssheirarchy/one.css",
            tab_width=4,
            style="one-dark",
            language="css",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        two = Code(
            "cssheirarchy/two.css",
            tab_width=4,
            style="one-dark",
            language="css",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        one_img = ImageMobject("one.jpg").to_edge(RIGHT)
        two_img = ImageMobject("two.jpg").to_edge(RIGHT)
        self.add(one_img)
        self.add(one)
        self.wait(1)
        self.play(
            Transform(one, two, run_time=2), Transform(one_img, two_img, run_time=2)
        )
