from manim import *
import random
from manimNE import s,s3

def arithmetic_1():
    bool = True
    while bool:
        a = random.randint(1, 10) * random.choice([-1, 1])
        b = random.randint(1, 15)
        c = random.randint(1, 30)

        d = random.randint(1, 15) * random.choice([-1, 1])
        e = c * random.choice([1, 5])
        if(a > 0):
            res = ((a * c + b) / c) * (e / d)
        else:
            a1 = a * -1
            res = (-(a1 * c + b) / c) * (e / d)

        if ((res - int(res * 100) / 100) == 0) and (b < c) and (d < e):
            bool = False
            return a, b, c, e, d, res


class id0401001(Scene):

    def construct(self):

        self.camera.background_color = DARKER_GRAY

        f = open('answer_4_1.txt','w')

        i = 0
        while i < 10:
            a, b, c, e, d, res = arithmetic_1()
            if(d < 0):
                d = d * -1
                t = MathTex(a, "{", b, "\\over", c, "}", " : ", "\\left(","-","{", d, "\\over", e, "}","\\right)", " = ", font_size = 60)
            else:
                t = MathTex( a, "{", b, "\\over", c, "}", " : ", "{", d, "\\over", e, "}", " = ", font_size = 60)

            if (res - int(res)) == 0:
                res = round(res)
            f.write(f'{res}\n')
            self.add(t, s, s3)
            self.wait(1 / 60)
            self.clear()
            i += 1

        f.close()


def arithmetic_2():
    bool = True
    while bool:
        a = random.randint(1, 400)
        b = random.randint(1, 100)
        cc = random.choice([-1, 1])
        if (cc == 1):
            c = a + b
            res = a-b
        else:
            c = a - b
            res = a + b

        if (a > b):
            bool = False
            return a, b, c, res

class id0401002(Scene):

    def construct(self):

        self.camera.background_color = DARKER_GRAY

        f = open('answer_4_2.txt','w')

        i = 0
        while i < 10:
            a, b, c, res = arithmetic_2()

            t = MathTex("\\left(",a,"^2","-",b,"^2", "\\right)", " : ", c, " = ",font_size=60)

            f.write(f'{res}\n')
            self.add(t, s, s3)
            self.wait(1 / 60)
            self.clear()
            i += 1

        f.close()