import random

def irrational_1():
    bool = True
    while bool:
        a = random.randint(1, 10) * random.choice([-1, 1])
        b = random.randint(1, 15) * random.choice([-1, 1])
        c = random.randint(1, 30)

        d = random.randint(1, 15) * random.choice([-1, 1])
        e = c * random.choice([1, 5])

        res = ((a*c+b)/c)*(e/d)

        if (res - int(res * 100) / 100) == 0:
            bool = False
            return a, b, c, e, d, res


i = 0
while i < 11:
    a, b, c, e, d, res = irrational_1()
    print(f'{a} {b}/{c} : {d}/{e} = {res}')
    i += 1
