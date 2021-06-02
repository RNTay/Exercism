#!/usr/bin/env python3

def classify(number):
    if number < 1:
        raise ValueError('Input must be greater than or equal to 2.')
    if int(number) != number:
        raise ValueError('Input should be an integer.')

    aliquot_sum = 0
    for d in range(1, number):
        if number % d == 0:
            aliquot_sum += d
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'deficient'
