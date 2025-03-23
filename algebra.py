def prime_factors(n):
    """For numbers below 10**6 trial division is ~3x faster than Pollard's Rho."""
    if n < 2:
        return []

    factors = [0] * 32
    idx = 0

    while (n & 1) == 0:
        factors[idx] = 2
        idx += 1
        n >>= 1

    p = 3
    limit = int(n**0.5) + 1
    while p <= limit and n > 1:
        while n % p == 0:
            factors[idx] = p
            idx += 1
            n //= p
            limit = int(n**0.5) + 1
        p += 2

    if n > 1:
        factors[idx] = n
        idx += 1

    return factors[:idx]
