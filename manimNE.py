from manim import *

s1 = Text("МАТЕМАТИКА", font="montserrat", weight=HEAVY).scale(0.4).to_corner(DR, buff=1).shift(0.6 * DOWN).set_color(BLUE_A)
s2 = Text("с Никитой Евгеньевичем", font="montserrat", weight=THIN).scale(0.3).next_to(s1, DOWN, buff=0.05, aligned_edge=LEFT).set_color(BLUE_A)
s = VGroup(s1,s2).shift(2*UP)
s3 = Text("Найдите значение выражения", font="montserrat", weight=HEAVY).scale(0.7).to_corner(UL, buff=1).shift(1.4*DOWN).shift(0.4*LEFT)