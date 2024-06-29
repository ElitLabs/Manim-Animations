from manim import (
    Scene,
    Code,
    Transform,
    ImageMobject,
    RIGHT,
    LEFT,
    ReplacementTransform,
    UP,
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
		<div><h2>World</h2></div>
	</body>
</html>
"""


class Render(Scene):
    def render_imgs(self):
        for i in range(1, 10):
            imgkit.from_string(
                html.replace("PLACEHOLDER", str(i)),
                f"cssheirarchy/imgs/{i}.jpg",
                options=options,
                css=f"cssheirarchy/{i}.css",
            )

    def construct(self):
        self.render_imgs()
        code = []
        imgs = []

        for i in range(1, 10):
            code.append(
                Code(
                    f"cssheirarchy/{i}.css",
                    style="one-dark",
                    font_size=16,
                    line_spacing=0.5,
                    corner_radius=0.1,
                ).to_edge(LEFT)
            )

            imgs.append(ImageMobject(f"cssheirarchy/imgs/{i}.jpg").to_edge(RIGHT))

        mob_html = Code(
            code="""
<!DOCTYPE html>
<html lang="en">
	<head>
		<!-- ... -->
	</head>
	<body>
		<h1>Hello</h1>
		<div>
            <h2>World</h2>
        </div>
	</body>
</html>
""",
            language="html",
            style="one-dark",
            font_size=18,
            line_spacing=0.5,
            corner_radius=0.1,
        )

        self.add(mob_html)
        self.wait(3)
        self.play(ReplacementTransform(mob_html, code[0], run_time=2))
        self.add(code[0])
        self.add(imgs[0])
        for i in range(1, 6):
            print(i)
            self.wait(1)
            self.play(
                Transform(code[0], code[i], run_time=2),
                Transform(imgs[0], imgs[i], run_time=2),
            )
