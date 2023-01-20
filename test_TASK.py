import random
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

        fract_ok = False
        fract_ok_1 = False

        if (get_all_divisors_arithmetic_4(b, c) and get_all_divisors_arithmetic_4(f, g)):
            fract_ok = True

        if(b != 1 and c % b == 0) or (f != 1 and g % f == 0):
            fract_ok_1 = True

        if ((res - int(res * 100) / 100) == 0) and (b < c) and (f < g) and (fract_ok == True) and (fract_ok_1 == False):
            bool = False
            return a, b, c, e, d, f, g, res

def get_all_divisors_arithmetic_4(n1, n2):
    flag = True
    for i in range(2, int(n1 / 2) + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            flag = False
    return flag

i = 0
while i < 50:
    a, b, c, e, d, f, g, res = arithmetic_4()

    print ( f' ( {a} {b}/{c} - {d} ) *{e} {f}/{g} = {res}')
    i += 1
