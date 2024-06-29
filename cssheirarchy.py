from manim import (
    Scene,
    Code,
    Transform,
    ReplacementTransform,
    ImageMobject,
    RIGHT,
    LEFT,
)
import imgkit


options = {"enable-local-file-access": "", "width": 960}

html = """
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Info</title>
		<link rel="stylesheet" href="cssheirarchy/PLACEHOLDER.css" />
	</head>
	<body style="height: 100dvh; min-height: 540px">
		<h1>Hello</h1>
		<div><p>World</p></div>
	</body>
</html>
"""


class Render(Scene):
    def render_imgs(self):
        imgkit.from_string(
            html.replace("PLACEHOLDER", "1"),
            "1.jpg",
            options=options,
            css="cssheirarchy/1.css",
        )
        imgkit.from_string(
            html.replace("PLACEHOLDER", "2"),
            "2.jpg",
            options=options,
            css="cssheirarchy/2.css",
        )
        imgkit.from_string(
            html.replace("PLACEHOLDER", "3"),
            "3.jpg",
            options=options,
            css="cssheirarchy/3.css",
        )
        imgkit.from_string(
            html.replace("PLACEHOLDER", "4"),
            "4.jpg",
            options=options,
            css="cssheirarchy/4.css",
        )
        imgkit.from_string(
            html.replace("PLACEHOLDER", "5"),
            "5.jpg",
            options=options,
            css="cssheirarchy/5.css",
        )
        imgkit.from_string(
            html.replace("PLACEHOLDER", "6"),
            "6.jpg",
            options=options,
            css="cssheirarchy/6.css",
        )

    def construct(self):
        self.render_imgs()
        one = Code(
            "cssheirarchy/1.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        two = Code(
            "cssheirarchy/2.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        three = Code(
            "cssheirarchy/3.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        four = Code(
            "cssheirarchy/4.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        five = Code(
            "cssheirarchy/5.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        six = Code(
            "cssheirarchy/6.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)

        one_img = ImageMobject("1.jpg").to_edge(RIGHT)
        two_img = ImageMobject("2.jpg").to_edge(RIGHT)
        three_img = ImageMobject("3.jpg").to_edge(RIGHT)
        four_img = ImageMobject("4.jpg").to_edge(RIGHT)
        five_img = ImageMobject("5.jpg").to_edge(RIGHT)
        six_img = ImageMobject("6.jpg").to_edge(RIGHT)

        self.add(one_img)
        self.add(one)
        self.wait(1)
        self.play(
            Transform(one, two, run_time=2),
            Transform(one_img, two_img, run_time=2),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(one, three, run_time=2),
            ReplacementTransform(one_img, three_img, run_time=2),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(three, four, run_time=2),
            ReplacementTransform(three_img, four_img, run_time=2),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(four, five, run_time=2),
            ReplacementTransform(four_img, five_img, run_time=2),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(five, six, run_time=2),
            ReplacementTransform(five_img, six_img, run_time=2),
        )
        self.wait(1)
