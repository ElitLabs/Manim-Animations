from manim import Scene, Code, Transform, ImageMobject, RIGHT, LEFT, DOWN, UP
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
        for i in range(1, 7):
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

        for i in range(1, 7):
            code.append(
                Code(
                    f"cssheirarchy/{i}.css",
                    style="one-dark",
                    font_size=16,
                    line_spacing=0.5,
                    corner_radius=0.1,
                    margin=0.2,
                )
                .to_edge(LEFT)
                .align_on_border(UP)
            )

            imgs.append(ImageMobject(f"cssheirarchy/imgs/{i}.jpg").to_edge(RIGHT))

        mob_html = (
            Code(
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
                font_size=12,
                line_spacing=0.5,
                corner_radius=0.1,
                margin=0.2,
            )
            .align_on_border(DOWN)
            .to_edge(LEFT)
        )

        self.add(code[0])
        self.add(mob_html)
        self.add(imgs[0])
        for i in range(1, 6):
            print(i)
            self.wait(1)
            self.play(
                Transform(code[0], code[i], run_time=2),
                Transform(imgs[0], imgs[i], run_time=2),
            )
