import math
import random

from scipy import special, integrate

def fi_integral(x1, x2):
    return integrate.quad(lambda x: math.e ** (-x**2/2), x1, x2)[0] / math.sqrt(2 * math.pi)


def get_probability(p, n, am):
    return math.pow(p, am) * special.binom(n, am) * math.pow(1 - p, n - am)

def get_error_rate(p, n):
    return (p ** 2 + (1 - p) ** 2) / math.sqrt(n * p * (1 - p))

def func(k, n, p):
    return (k - n * p) / math.sqrt(n * p * (1 - p))

def simulate(n, p, am):
    count = 0
    q = 1 - p
    for _ in range(am):
        kol = 0
        for i in range(n):
            u = random.uniform(0, 1)
            if u <= p:
                kol += 1
        if n / 2 - math.sqrt(n * p * q) <= kol <= n / 2 + math.sqrt(n * p * q):
            count += 1
    return count / am


def test(n, p):
    print("Test case:", n, p)
    q = 1 - p
    l = n / 2 - math.sqrt(n * p * q)
    r = n / 2 + math.sqrt(n * p * q)

    F = fi_integral(func(math.ceil(l), n, p), func(math.floor(r), n, p))
    err = get_error_rate(p, n)

    lb = max(F - err, 0)
    rb = min(F + err, 1)

    T = (n <= 1000)

    print("  expected bounds: ", lb, " : ", rb)
    print("  approximate: ", F)
    S = simulate(n, p, 10000000 // n)
    print("  simulated: ", S)
    print("  deviation: ", abs(F - S))
    prob = 0
    if T:
        for i in range(math.ceil(l), math.floor(r) + 1):
            prob += get_probability(p, n, i)
        print("  found: ", prob)
        print("  deviation from approximate: ", abs(F - prob))
        print("  deviation from simulated: ", abs(F - prob))


ns = [10, 100, 1000, 10000]
ps = [0.001, 0.01, 0.1, 0.25, 0.5]

if __name__ == "__main__":
    for n in ns:
        for p in ps:
            test(n, p)
