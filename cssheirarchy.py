from manim import Scene, Code, ReplacementTransform, ImageMobject, RIGHT, LEFT
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
            html.replace("PLACEHOLDER", "one"),
            "one.jpg",
            options=options,
            css="cssheirarchy/one.css",
        )
        imgkit.from_string(
            html.replace("PLACEHOLDER", "two"),
            "two.jpg",
            options=options,
            css="cssheirarchy/two.css",
        )
        imgkit.from_string(
            html.replace("PLACEHOLDER", "three"),
            "three.jpg",
            options=options,
            css="cssheirarchy/three.css",
        )

    def construct(self):
        self.render_imgs()
        one = Code(
            "cssheirarchy/one.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        two = Code(
            "cssheirarchy/two.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)
        three = Code(
            "cssheirarchy/three.css",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
        ).to_edge(LEFT)

        one_img = ImageMobject("one.jpg").to_edge(RIGHT)
        two_img = ImageMobject("two.jpg").to_edge(RIGHT)
        three_img = ImageMobject("three.jpg").to_edge(RIGHT)

        self.add(one_img)
        self.add(one)
        self.wait(1)
        self.play(
            ReplacementTransform(one, two, run_time=2),
            ReplacementTransform(one_img, two_img, run_time=2),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(two, three, run_time=2),
            ReplacementTransform(two_img, three_img, run_time=2),
        )
