import random


def generate_problems(numbers_of_signs, sin):
    sign = sin
    res1 = 0
    res2 = 0
    str = ""
    numbers_of_signs = numbers_of_signs - 1
    numbers_of_signs1 = numbers_of_signs
    while numbers_of_signs >= 0:
        numb = random.randint(1,9)
        st = numb * 10**numbers_of_signs
        numbers_of_signs = numbers_of_signs -1
        res1 = res1 + st

    while numbers_of_signs1 >= 0:
        numb = random.randint(1,9)
        st = numb * 10**numbers_of_signs1
        numbers_of_signs1 = numbers_of_signs1 -1
        res2 = res2 + st

    if sign == "+":
        ans = res1 + res2
    if sign == "-":
        ans = res1 - res2

    if res1 > res2:
        return res1, res2, abs(ans), sign
    if res1 < res2:
        return res2, res1, abs(ans), sign


