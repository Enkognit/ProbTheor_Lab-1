import math
import random

def get_graphic_length(x):
    q = math.sqrt(4 * x ** 2 + 1)
    return q * x / 2 + math.log(q + 2 * x) / 4


def get_x_from_length(len):
    l = 0
    r = 2
    while r - l > 1e-10:
        w = (l + r) / 2
        if get_graphic_length(w) < len:
            l = w
        else:
            r = w
    return l


expected = get_graphic_length(math.sqrt(3)) / get_graphic_length(2)


def test(tests_amount):
    good = 0
    len = get_graphic_length(2)
    random.seed(228)
    for i in range(tests_amount):
        if get_x_from_length(random.uniform(0, len)) < math.sqrt(3):
            good += 1

    found = good / tests_amount
    print(f'Expected: {expected}, found: {found}, subtraction: {abs(expected - found)}')


if __name__ == "__main__":
    test(100000)
