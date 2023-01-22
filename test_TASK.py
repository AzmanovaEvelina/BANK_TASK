import random
def arithmetic_7():
    bool = True
    while bool:
        a = random.randint(1, 10)
        b = random.randint(1, 9)
        c = random.randint(1, 12)

        res = (a + b) / c
        if (res - int(res * 100) / 100) == 0:
            bool = False
            return a, b, c, res


i = 0
while i < 50:
    a, b, c, res = arithmetic_7()

    print ( f' ( {a} + {b} ) : {c} = {res}')
    i += 1
