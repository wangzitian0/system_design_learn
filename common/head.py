from manim import *

class DisplayMultipleSVGs(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#E5DCBE"

        # 加载 SVG 文件
        svg_files = [
            "assets/head/Hand Luck.svg",
            "assets/head/Victory finger.svg",
            "assets/head/Tap Finger.svg",
            "assets/head/Thumbs Up.svg",
        ]

        # 设置每个 SVG 的颜色，并调整大小
        svgs = [SVGMobject(svg_file).set(height=1).set_color("#82A4BC") for svg_file in svg_files]

        # 将第一个 SVG 图像添加到场景中
        current_svg = svgs[0]
        self.play(FadeIn(current_svg), run_time=0.2)

        # 依次平滑切换到下一个 SVG，并在每次切换前变大 15%
        for i in range(1, len(svgs) - 1):
            next_svg = svgs[i].copy()
            next_svg.match_width(current_svg)  # 先将下一个 SVG 的大小设置为和当前 SVG 一致
            next_svg.scale(1.15)  # 然后将其放大 15%
            self.play(ReplacementTransform(current_svg, next_svg, run_time=1, rate_func=smooth))
            current_svg = next_svg
            self.wait(0.3)

        # 对最后一个 SVG 执行特殊操作
        final_svg = svgs[-1].copy()
        final_svg.match_width(current_svg)  # 匹配当前 SVG 的宽度
        final_svg.scale(1.3)  # 先放大 30%
        self.play(ReplacementTransform(current_svg, final_svg, run_time=1, rate_func=smooth))

        # 缩小 40% 并向上移动 1 单位
        self.play(final_svg.animate.scale(0.6).shift(UP), run_time=1)

        # 保持最后一个 SVG 显示 1 秒
        self.wait(1)