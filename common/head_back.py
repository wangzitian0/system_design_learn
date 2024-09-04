from manim import *
import os
import numpy as np

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

class LogoTunnelScene(Scene):
    def construct(self):
        # 设置背景颜色
        self.camera.background_color = "#E5DCBE"

        # 读取指定目录中的所有 SVG 文件
        logo_directory = "assets/head/brands"
        logo_files = [os.path.join(logo_directory, f) for f in os.listdir(logo_directory) if f.endswith(".svg")]

        # 隧道的半径和Logo数量
        tunnel_radius = 3
        num_logos = len(logo_files)

        # 创建一个 Logo 组用于整体移动
        logo_group = VGroup()

        # 将每个 Logo 均匀地贴在隧道内部，从近到远排列
        for i, logo_file in enumerate(logo_files):
            logo = SVGMobject(logo_file).set_color("#82A4BC")
            logo.scale(0.5)

            # 计算 Logo 在隧道中的初始位置
            angle = 2 * np.pi * (i % num_logos) / num_logos  # 环绕隧道的角度
            distance_along_tunnel = i * 1.5  # 沿隧道方向的距离，每个 logo 相隔一定距离

            x = tunnel_radius * np.cos(angle)
            y = tunnel_radius * np.sin(angle)
            z = -distance_along_tunnel  # 在隧道中从近到远排列

            logo.move_to([x, y, z])

            # 使 Logo 朝向隧道中心
            logo.rotate(angle, axis=OUT)

            # 将 Logo 添加到组中
            logo_group.add(logo)

        # 将 Logo 组添加到场景
        self.add(logo_group)

        # 动画：使 Logo 组随着隧道一起往远处移动，并逐渐缩小
        self.play(
            logo_group.animate.shift(10 * OUT).scale(0.1),  # 向 Z 轴正方向移动并缩小
            run_time=5,
            rate_func=smooth
        )

        self.wait(1)  # 停留一段时间