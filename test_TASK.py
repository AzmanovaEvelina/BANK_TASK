import random
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
        rnd = random.choice([1, 2, 3])
        rnd_1 = random.choice([1, 2, 3])

    if rnd == 1:
        number_1 = number / 10
        if rnd_1 == 2:
            number_2 = number / 100
        else:
            number_2 = number / 1000
    if rnd == 2:
        number_1 = number / 100
        if rnd_1 == 1:
            number_2 = number / 10
        else:
            number_2 = number / 1000
    if rnd == 3:
        number_1 = number / 1000
        if rnd_1 == 2:
            number_2 = number / 100
        else:
            number_2 = number / 10
    return number_1, number_2

i = 0
while i < 100:
    a, b, c, d, res = arithmetic_3_1()
    print (a, b, c, d, res)
    i += 1
