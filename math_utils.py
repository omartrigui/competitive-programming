import math
from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def prime_factors(n):
    ans = list()
    while n % 2 == 0:
        ans.append(2),
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            ans.append(i),
            n = n / i

    if n > 2:
        ans.append(n)

    return ans


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n // i])
    divs.extend([n])
    return list(set(divs))


def isPrime(n):  # Check Prime Number or not
    if (n <= 1): return False
    if (n <= 3): return True
    if (n % 2 == 0 or n % 3 == 0): return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True
