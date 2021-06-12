#!/usr/bin/env python3

def square(number: int) -> int:
    if not 1 <= number <= 64:
        raise ValueError('Square number must be between 1 and 64')
    # double for each square
    return 2**(number - 1)


def total() -> int:
    # geometric sum: a = 1, r = 2, n = 64
    return 2**64 - 1
