import random
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

def get_all_divisors(n1, n2):
    flag = True
    for i in range(2, int(n1 / 2) + 1):   # for i in range(2, int(n1 / 2) + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            flag = False
    return flag

i = 0
while i < 50:
    a, b, c, d, e, f, res = arithmetic_6()

    print ( f' ( {a} {b}/{c} - {d}/{e} ) * {f} = {res}')
    i += 1
