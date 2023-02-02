import random
def arithmetic_10():
    bool = True
    while bool:
        a = random.randint(1, 9)
        b = random.randint(1, 9) * random.choice([-1, 1])
        c = random.randint(1, 15) * random.choice([-1, 1])

        if (b > 0):
            res = (2 * a * b)/ c
        else:
            res = -2 * a * b)/ c

        if (res - int(res * 100) / 100) == 0:
            bool = False
            return a, b, c, res

i = 0
while i < 15:
    a, b, c, res = arithmetic_10()

    print ( f' {a} {b} {c}={res}')
    i += 1
