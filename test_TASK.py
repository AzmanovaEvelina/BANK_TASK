import random
def arithmetic_9():
    bool = True
    while bool:
        a = random.randint(1, 9)
        b = random.randint(1, 9) * random.choice([-1, 1])

        if (b > 0):
            res = - b
        else:
            res = b * -1

        if (res - int(res * 100) / 100) == 0:
            bool = False
            return a, b, res

i = 0
while i < 15:
    a, b, res = arithmetic_9()

    print ( f' ( {a} {b} )= {res}')
    i += 1
