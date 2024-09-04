from manim import *
import os
import math

class LogoScrollScene(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#E5DCBE"

        # 读取指定目录中的所有 SVG 文件
        logo_directory = "assets/head/brands"
        logo_files = [os.path.join(logo_directory, f) for f in os.listdir(logo_directory) if f.endswith(".svg")]

        # 创建一个容器来存放所有的 Logo
        logo_group = VGroup()

        # 目标对角线长度
        target_diagonal = 0.6  # 可以根据需求调整这个值
        edge_margin = 0.3  # 保留 0.1 的边距

        # 获取画布的宽度和高度
        screen_width = config.frame_width
        screen_height = config.frame_height

        # 计算左边和右边的 x 位置
        left_x_positions = [-screen_width / 2 + edge_margin, -screen_width / 2 + edge_margin + target_diagonal]
        right_x_positions = [screen_width / 2 - edge_margin - target_diagonal, screen_width / 2 - edge_margin]

        # 平铺 Logo，部分在视野外
        for i, logo_file in enumerate(logo_files):
            logo = SVGMobject(logo_file).set_color("#82A4BC")

            # 获取 Logo 的宽度和高度
            logo_width = logo.get_width()
            logo_height = logo.get_height()

            # 计算对角线长度
            diagonal_length = math.sqrt(logo_width**2 + logo_height**2)

            # 计算缩放因子，使对角线长度等于目标值
            scale_factor = target_diagonal / diagonal_length
            logo.scale(scale_factor)

            # 计算 Logo 的位置
            if (i // 2) % 2 == 0:  # 偶数行在左边
                x_pos = left_x_positions[i % 2]
            else:  # 奇数行在右边
                x_pos = right_x_positions[i % 2]

            y_pos = -(i // 4) * (target_diagonal + edge_margin)  # 按行排列 Logo，每行 4 个（2 左 2 右）

            logo.move_to([x_pos, y_pos, 0])
            logo_group.add(logo)

        # 将 Logo 组添加到场景
        self.add(logo_group)

        # 创建向上滚动的动画
        scroll_animation = logo_group.animate.shift(UP * (logo_group.get_height() + screen_height))  # 向上滚动

        # 播放动画，滚动时间为 10 秒
        self.play(scroll_animation, run_time=10, rate_func=linear)

        # 保持场景显示
        self.wait(1)


class CentralCountDown(Scene):
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
