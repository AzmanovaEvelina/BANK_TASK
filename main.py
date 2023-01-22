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

        fract_ok = False
        fract_ok_1 = False

        if (get_all_divisors(b, c) and get_all_divisors(d, e)):
            fract_ok = True

        if (b != 1 and c % b == 0) or (d != 1 and e % d == 0):
            fract_ok_1 = True

        if ((res - int(res * 100) / 100) == 0) and (b < c) and (d < e) and (fract_ok == True) and (fract_ok_1 == False):
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

def arithmetic_3_1():
    bool = True
    while bool:
        number_1 = random.randint(101, 888)
        number_2 = random.randint(101, 888)
        if (number_1 % 10 != 0 and number_2 % 10 != 0):
            bool = False
    a, c = arithmetic_3_2(number_1)
    b, d = arithmetic_3_2(number_2)

    res = round((round((a*b),6)/ round((c*d),6)), 4)

    if (res - int(res)) == 0:
        res = round(res)

    return a, b, c, d, res
def arithmetic_3_2(number):
    rnd = 0
    rnd_1 = 0
    while (rnd == rnd_1):
        rnd = random.choice([10, 100, 1000])
        rnd_1 = random.choice([10, 100, 1000])

    number_1 = number / rnd
    number_2 = number / rnd_1
    return number_1, number_2

class id0401003(Scene):

    def construct(self):

        self.camera.background_color = DARKER_GRAY

        f = open('answer_4_3.txt','w')

        i = 0
        while i < 10:
            a, b, c, d, res = arithmetic_3_1()

            t = MathTex("{", a, " \\cdot ", b, "\\over", c, " \\cdot ", d, "}", " = ", font_size=60)

            f.write(f'{res}\n')
            self.add(t, s, s3)
            self.wait(1 / 60)
            self.clear()
            i += 1

        f.close()

def arithmetic_4():
    bool = True
    while bool:
        a = random.randint(1, 6)
        b = random.randint(1, 9)
        c = random.randint(1, 9)

        d = random.randint(1, 40) / 10

        e = random.randint(1, 6)
        f = random.randint(1, 9)
        g = random.randint(1, 9)

        res = ((a * c + b) / c - d) * ((e*g+f)/g)

        if (d - int(d)) == 0:
            d = round(d)

        fract_ok = False
        fract_ok_1 = False

        if (get_all_divisors(b, c) and get_all_divisors(f, g)):
            fract_ok = True

        if (b != 1 and c % b == 0) or (f != 1 and g % f == 0):
            fract_ok_1 = True

        if ((res - int(res * 100) / 100) == 0) and (b < c) and (f < g) and (fract_ok == True) and (fract_ok_1 == False):
            bool = False
            return a, b, c, e, d, f, g, res

def get_all_divisors(n1, n2):
    flag = True
    for i in range(2, int(n1 / 2) + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            flag = False
    return flag

class id0401004(Scene):
    def construct(self):

        self.camera.background_color = DARKER_GRAY

        f = open('answer_4_4.txt','w')

        i = 0
        while i < 10:
            a, b, c, e, d, f1, g, res = arithmetic_4()

            t = MathTex("\\left(", a, "{", b, "\\over", c, "}", "-", d, "\\right)", " \\cdot ", e, "{", f1, "\\over", g, "}"," = ", font_size=60)

            if (res - int(res)) == 0:
                res = round(res)

            f.write(f'{res}\n')

            self.add(t, s, s3)
            self.wait(1 / 60)
            self.clear()
            i += 1

        f.close()

def arithmetic_5():
    bool = True
    while bool:
        a = random.randint(1, 6)
        b = random.randint(1, 9)
        c = random.randint(1, 9)

        d = random.randint(1, 40) / 10

        f = random.randint(1, 9)
        g = random.randint(1, 70)

        res = ((a * c + b) / c - d) / (f / g)

        if (d - int(d)) == 0:
            d = round(d)

        fract_ok = False
        fract_ok_1 = False

        if (get_all_divisors(b, c) and get_all_divisors(f, g)):
            fract_ok = True

        if (b != 1 and c % b == 0) or (f != 1 and g % f == 0):
            fract_ok_1 = True

        if ((res - int(res * 100) / 100) == 0) and (b < c) and (f < g) and (fract_ok == True) and (fract_ok_1 == False):
            bool = False
            return a, b, c, d, f, g, res


class id0401005(Scene):
    def construct(self):

        self.camera.background_color = DARKER_GRAY

        f = open('answer_4_5.txt','w')

        i = 0
        while i < 10:
            a, b, c, d, f1, g, res = arithmetic_5()

            t = MathTex("\\left(", a, "{", b, "\\over", c, "}", "-", d, "\\right)", ":", "{", f1, "\\over", g, "}"," = ", font_size=60)

            if (res - int(res)) == 0:
                res = round(res)

            f.write(f'{res}\n')

            self.add(t, s, s3)
            self.wait(1 / 60)
            self.clear()
            i += 1

        f.close()

def arithmetic_6():
    bool = True
    while bool:
        a = random.randint(1, 6) * random.choice([-1, 1])
        b = random.randint(1, 9)
        c = random.randint(1, 9)

        d = random.randint(1, 9) * random.choice([-1, 1])
        e = random.randint(1, 9)

        f = random.randint(1, 250) / random.choice([1, 10, 100])

        if(d < 0):
            d1 = d * -1
        else:
            d1 = d

        if (a > 0):
            res = (((a * c + b) / c) + (d / e)) * f
        else:
            a1 = a * -1
            res = ((-(a1 * c + b) / c) + (d / e)) * f

        if (f - int(f)) == 0:
            f = round(f)

        fract_not_ok = False
        fract_not_ok_1 = False

        if (get_all_divisors(b, c) and get_all_divisors(d, e)):
            fract_not_ok = True

        if (b != 1 and c % b == 0) or (d != 1 and e % d == 0):
            fract_not_ok_1 = True

        if ((res - int(res * 100) / 100) == 0) and (b < c) and (d1 < e) and (fract_not_ok == True) and ( fract_not_ok_1 == False):
            bool = False
            return a, b, c, d, e, f, res

class id0401006(Scene):
    def construct(self):

        self.camera.background_color = DARKER_GRAY

        f = open('answer_4_6.txt','w')

        i = 0
        while i < 10:
            a, b, c, d, e, f1, res = arithmetic_6()

            if (d < 0):

                d = d * -1
                t = MathTex("\\left(", a, "{", b, "\\over", c, "}", " - ",  "{", d, "\\over", e, "}", "\\right)", " \\cdot ", f1, " = ", font_size=60)
            else:
                t = MathTex("\\left(", a, "{", b, "\\over", c, "}", " + ",  "{", d, "\\over", e, "}", "\\right)", " \\cdot ", f1, " = ", font_size=60)

            if (res - int(res)) == 0:
                res = round(res)

            f.write(f'{res}\n')

            self.add(t, s, s3)
            self.wait(1 / 60)
            self.clear()
            i += 1

        f.close()