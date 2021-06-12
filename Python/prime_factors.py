#!/usr/bin/env python3

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimisation."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def factors(n: int) -> list:
    prime_factors = []
    if n < 2:
        return []
    if n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
        while n % 2 == 0:
            prime_factors.append(2)
            n = n // 2
    if n % 3 == 0:
        prime_factors.append(3)
        n = n // 3
        while n % 3 == 0:
            prime_factors.append(3)
            n = n // 3
    p = 6
    while n != 1:
        if is_prime(p - 1):
            if n % (p - 1) == 0:
                prime_factors.append(p - 1)
                n = n // (p - 1)
                while n % (p - 1) == 0:
                    prime_factors.append(p - 1)
                    n = n // (p - 1)
        if is_prime(p + 1):
            if n % (p + 1) == 0:
                prime_factors.append(p + 1)
                n = n // (p + 1)
                while n % (p + 1) == 0:
                    prime_factors.append(p + 1)
                    n = n // (p + 1)
        p += 6
    return prime_factors
