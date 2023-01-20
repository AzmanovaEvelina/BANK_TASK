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
        rnd = random.choice([10, 100, 1000])
        rnd_1 = random.choice([10, 100, 1000])
    #number_2 = number
    number_1 = number / rnd
    number_2 =  number/rnd_1
    return number_1, number_2
i = 0
while i < 50:
    a, b, c, d, res = arithmetic_3_1()
    print (a, b, c, d, res)
    i += 1
