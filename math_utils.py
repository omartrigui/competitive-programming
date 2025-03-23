import math
from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def prime_factors(n):
    factors = []
    
    for p in [2, 3, 5]:
        while n % p == 0:
            factors.append(p)
            n //= p
    
    increments = [4, 2, 4, 2, 4, 6, 2, 6]
    i = 0
    d = 7
    
    while d*d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += increments[i]
        i = (i + 1) % 8
        
    if n > 1:
        factors.append(n)
    return factors


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
